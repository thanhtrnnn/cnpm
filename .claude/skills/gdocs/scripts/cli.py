"""CLI entry point for Google Docs operations."""

import argparse
import json
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.auth import get_service, verify_token, setup_credentials, find_credentials
from scripts.client import GDocsClient
from scripts.converter import convert_markdown_to_requests, extract_plantuml_blocks
from scripts.plantuml_renderer import render_plantuml_to_png


def cmd_auth(args):
    """Handle auth subcommand."""
    if args.credentials:
        # Setup credentials from file
        if not os.path.exists(args.credentials):
            print(f"Error: File not found: {args.credentials}")
            sys.exit(1)
        path = setup_credentials(args.credentials)
        print(f"Credentials copied to: {path}")
        print("Run 'python cli.py auth --verify' to authenticate.")

    elif args.verify:
        # Verify token
        result = verify_token()
        if result['valid']:
            print(f"Token valid.")
        else:
            print(f"Token invalid: {result['error']}")
            print("Run with --credentials to re-authenticate.")
            sys.exit(1)

    else:
        # Default: authenticate (will open browser)
        try:
            service = get_service()
            print("Authentication successful!")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            sys.exit(1)


def cmd_read(args):
    """Handle read subcommand."""
    try:
        client = GDocsClient()

        if args.format == 'text':
            text = client.read_as_text(args.document_id)
            print(text)
        else:
            doc = client.read_document(args.document_id)
            print(json.dumps(doc, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"Error reading document: {e}")
        sys.exit(1)


def cmd_write(args):
    """Handle write subcommand."""
    try:
        # Read markdown file
        if args.file:
            with open(args.file, 'r', encoding='utf-8') as f:
                markdown_text = f.read()
        else:
            # Read from stdin
            markdown_text = sys.stdin.read()

        if not markdown_text.strip():
            print("Error: No content to write")
            sys.exit(1)

        client = GDocsClient()

        # Extract and render PlantUML blocks
        plantuml_blocks = extract_plantuml_blocks(markdown_text)
        rendered_images = {}

        if plantuml_blocks:
            print(f"Rendering {len(plantuml_blocks)} PlantUML diagrams...")
            for i, block in enumerate(plantuml_blocks):
                try:
                    path = render_plantuml_to_png(block)
                    rendered_images[i] = path
                    print(f"  Rendered diagram {i+1}: {path}")
                except Exception as e:
                    print(f"  Warning: Failed to render diagram {i+1}: {e}")

        # Convert markdown to requests
        def plantuml_renderer(code):
            # Find the rendered image for this code
            for i, block in enumerate(plantuml_blocks):
                if block.strip() == code.strip():
                    return rendered_images.get(i)
            return None

        requests = convert_markdown_to_requests(markdown_text, plantuml_renderer)

        if not requests:
            print("No content to write")
            sys.exit(1)

        # Execute batch update
        if args.section:
            # Update specific section
            result = client.clear_and_replace_section(
                args.document_id, args.section, markdown_text
            )
            print(f"Section '{args.section}' updated successfully")
        else:
            # Append to document
            result = client.batch_update(args.document_id, requests)
            print(f"Document updated successfully ({len(requests)} requests)")

    except Exception as e:
        print(f"Error writing to document: {e}")
        sys.exit(1)


def cmd_sections(args):
    """Handle sections subcommand."""
    try:
        client = GDocsClient()
        sections = client.get_document_sections(args.document_id)

        if not sections:
            print("No sections found in document")
            return

        print(f"Found {len(sections)} sections:")
        for section in sections:
            indent = "  " * (int(section['level'].replace('HEADING_', '')) - 1)
            print(f"{indent}{section['level']}: {section['text']}")

    except Exception as e:
        print(f"Error listing sections: {e}")
        sys.exit(1)


def cmd_render(args):
    """Handle render subcommand."""
    try:
        code = args.code
        if not code:
            # Read from file
            if args.file:
                with open(args.file, 'r', encoding='utf-8') as f:
                    code = f.read()
            else:
                print("Error: Provide PlantUML code via --code or --file")
                sys.exit(1)

        output_path = render_plantuml_to_png(code, args.output)
        print(f"Rendered to: {output_path}")

    except Exception as e:
        print(f"Error rendering PlantUML: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Google Docs API CLI for CNPM project'
    )
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Auth command
    auth_parser = subparsers.add_parser('auth', help='Authentication commands')
    auth_parser.add_argument('--credentials', help='Path to credentials.json')
    auth_parser.add_argument('--verify', action='store_true', help='Verify current token')

    # Read command
    read_parser = subparsers.add_parser('read', help='Read document content')
    read_parser.add_argument('document_id', help='Google Docs document ID')
    read_parser.add_argument('--format', choices=['json', 'text'], default='text',
                           help='Output format (default: text)')

    # Write command
    write_parser = subparsers.add_parser('write', help='Write content to document')
    write_parser.add_argument('document_id', help='Google Docs document ID')
    write_parser.add_argument('--file', help='Markdown file to write')
    write_parser.add_argument('--section', help='Section heading to update (instead of appending)')

    # Sections command
    sections_parser = subparsers.add_parser('sections', help='List document sections')
    sections_parser.add_argument('document_id', help='Google Docs document ID')

    # Render command
    render_parser = subparsers.add_parser('render', help='Render PlantUML to PNG')
    render_parser.add_argument('code', nargs='?', help='PlantUML code string')
    render_parser.add_argument('--file', help='File containing PlantUML code')
    render_parser.add_argument('--output', help='Output PNG path')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        'auth': cmd_auth,
        'read': cmd_read,
        'write': cmd_write,
        'sections': cmd_sections,
        'render': cmd_render,
    }

    commands[args.command](args)


if __name__ == '__main__':
    main()
