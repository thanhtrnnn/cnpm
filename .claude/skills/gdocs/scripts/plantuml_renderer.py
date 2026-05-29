"""PlantUML code to PNG renderer."""

import os
import hashlib
import zlib
import base64
import urllib.request
import tempfile


def render_plantuml_to_png(plantuml_code: str, output_path: str = None,
                            cache_dir: str = 'output/diagrams') -> str:
    """Render PlantUML code to PNG file.

    Args:
        plantuml_code: PlantUML source code (without @startuml/@enduml if missing)
        output_path: Where to save PNG. Auto-generated if None.
        cache_dir: Directory to cache rendered PNGs.

    Returns:
        Path to the rendered PNG file.
    """
    # Ensure @startuml/@enduml markers
    code = plantuml_code.strip()
    if not code.startswith('@startuml'):
        code = '@startuml\n' + code
    if not code.endswith('@enduml'):
        code = code + '\n@enduml'

    # Generate hash for caching
    code_hash = hashlib.md5(code.encode()).hexdigest()[:12]

    if output_path is None:
        os.makedirs(cache_dir, exist_ok=True)
        output_path = os.path.join(cache_dir, f'plantuml_{code_hash}.png')

    # Return cached version if exists
    if os.path.exists(output_path):
        return output_path

    # Render via PlantUML public server (try HTTPS first, then HTTP)
    encoded = _encode_plantuml(code)

    for base_url in ['https://www.plantuml.com/plantuml/png', 'http://www.plantuml.com/plantuml/png']:
        url = f'{base_url}/{encoded}'
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as response:
                with open(output_path, 'wb') as f:
                    f.write(response.read())
            return output_path
        except Exception:
            continue

    raise RuntimeError("Failed to render PlantUML: Public server unavailable. Use MCP plantuml tool instead.")


def _encode_plantuml(code: str) -> str:
    """Encode PlantUML text for URL usage.

    PlantUML uses a custom encoding: UTF-8 -> deflate -> custom base64.
    """
    # PlantUML custom base64 alphabet
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'

    # Deflate the code
    compressed = zlib.compress(code.encode('utf-8'))[2:-4]

    # Convert to PlantUML base64
    result = _encode64(len(compressed), 3, alphabet)
    for i in range(0, len(compressed), 3):
        if i + 2 < len(compressed):
            b1 = compressed[i]
            b2 = compressed[i + 1]
            b3 = compressed[i + 2]
            result += _encode64((b1 << 16) + (b2 << 8) + b3, 4, alphabet)
        elif i + 1 < len(compressed):
            b1 = compressed[i]
            b2 = compressed[i + 1]
            result += _encode64((b1 << 16) + (b2 << 8), 4, alphabet)
        else:
            b1 = compressed[i]
            result += _encode64(b1 << 16, 4, alphabet)

    return result


def _encode64(value: int, count: int, alphabet: str) -> str:
    """Encode a value using the given alphabet and number of characters."""
    result = ''
    for i in range(count - 1, -1, -1):
        index = (value >> (i * 6)) & 0x3F
        result += alphabet[index]
    return result


def render_multiple(plantuml_blocks: list, cache_dir: str = 'output/diagrams') -> list:
    """Render multiple PlantUML blocks to PNG files.

    Args:
        plantuml_blocks: List of PlantUML code strings.
        cache_dir: Directory to cache rendered PNGs.

    Returns:
        List of paths to rendered PNG files.
    """
    paths = []
    for i, block in enumerate(plantuml_blocks):
        output_path = os.path.join(cache_dir, f'plantuml_{i:03d}.png')
        path = render_plantuml_to_png(block, output_path, cache_dir)
        paths.append(path)
    return paths


if __name__ == '__main__':
    # Test rendering
    test_code = """
@startuml
actor User
User -> System : Login
System --> User : Success
@enduml
"""
    path = render_plantuml_to_png(test_code, 'test_output.png')
    print(f"Rendered to: {path}")
