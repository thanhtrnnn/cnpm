"""
Fix UC diagrams in Google Docs:
1. Upload new PlantUML-rendered PNG images to Google Drive
2. Find existing image object IDs in document
3. Replace images using replaceImage API
4. Update text tables with corrected UC structure
"""

import sys
import os
import io
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs', 'scripts'))

from auth import get_service, get_drive_service
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tab IDs
TAB_ACCOUNT = 't.e7vhkfc8t70g'
TAB_CORE = 't.pl02ohyiavub'

# PlantUML server URLs (generated from MCP tool)
PLANTUML_URLS = {
    'uc_account_main': 'https://www.plantuml.com/plantuml/png/XPHFQnD16CRlyobUSl3MKajEKa8n1GjBej8aU0YKsTbnPyXcDkpEYaK4fGVnPYazU10QFOY5Wg8Ni_IqmU-nVXBVtIQRtUqaNlRVytlVUTwP9zaFDGrqDFQ8nvzhq3u4qXKQ71bmfgMlI3YIQa83EWPFAgvF9XpyG0k_94me6r6N7-aJZqDMHvNhSQAbnlU7CerF8vYVfV4vz4CEROgNls_EeUCx4GAzv5A29VnqzaN1FUY9v5896CZaIX52cVO3Q5WYcJ81cUGsW8PW7IwbhaW-AtYHuRdI7IoLjaZZh-3u5DifLw2FTvCSQHzq2IbyGiDWf06l240KSfQvRJp3vK5Zlnzig9JxvtiQVvBW9ByNTlhjdVjblYlIsVK4Av9VoWKjrL3Dp-Qd-AnofIYYvQgd4Gu1OmGqZ93x5XMSNURc7_9Me-Icq8yFh2g1qxvL9WErAhfcJ7ZSUrBcAWOUfV6r12-TJMMTOrKRQNmXpHCTTwp_xjZ6wjhMvV7nafjA2vPCSSSn8Cl2Phae2yXx34U8uz2XMXKMT7Lt-1ZGnLIvGpp5-ACifIw3RRCX34mjeltsxawPnSXVZS54LTO_ocmQCRjwY3_D52El2R4EOMkhTHlOrNEJT0Uhx_ZxCBsWQP9zWktjMut20zZRaufvaSDRhLoq2pKN-KlDbRFGC1wRrCuwzKvnbbl3sZN4DYEip9WMAld8ObRhGl9SB8dcdJcQzXgDv0Uw47TtweLuYXiqjaRRnnl-U_y3',
    'uc_account_uc01': 'https://www.plantuml.com/plantuml/png/ZPF1IiD048Rl-nH3xorwbL8ABLW8ZOfQF0XbkrcJ9Uac91knYA3u0efu5AmNKIWeUB71Kuhl4P_4JMhJDAIjjvtytp_xpoIfUmAxmkzRoA8d0eGDBjCD0HfpAH7CviWp6NUmY_jWCKx5mA5WkyAmCuA3YObrkYy65eNOXxbkKIIOaFLXOsCJVYxlu2WS4X165BmJuFhtMnGyCD32JwuZX8cmNIWfXcGCCC97hfS0Uw2qPf9gX4ySJbduoXD5xSoKXcpv34qrUTnegWYb4Q2q_D8Id2C0twC4Usj0sJUU8ekhHZGUET8GVd0T1EF7V78xkPPddYYf2MTTUxwC3tq9230bz-AdN2_BJMwILcRubUhTfh98i2YuuaK1SYwyRCgTWzqijn1WEmf63AneF6HvZYp6Y89xLZnHjwsitTXADqON22ajA9Thq_shdVbPlkXvWPAFh5APbXYse5fbd5Y-HckrHEobQYBICq6vzgV9eLQfRUMVtdZP1LVda5unGhBCwXJnQd9DwfAKF_4l',
    'uc_account_uc04': 'https://www.plantuml.com/plantuml/png/XP4nImD148Nx_HMFwnCih2GSWJI1gqG42vlDPhrTiZSNTkV488AjjPMTfvrWPvLWjR_a_2Lk4eZN1AlXyRxtPc36WQNdfdB2wHi6r_2sD8ovzLgnhKc4XQMbzBA2iwHvjTIeFPkwPoobMiXIN_3AQMnpaagd1LjE-d9oSegVnsUSDztwdU3YDzZ4Boh1bg1Y2pBnZOIGYckFh32nLGOclbAPGGOKKo4EhSZ-wSbmBu0cQ2N3CVgQUdZQiBsn7vgORlD41g7RVCfUxW3BFdsbAvXktIOcvLuiRcty-6Ddua68Oeh18DylsXLWEDnBd64qqdUiQPxdEszsn1kdaJxr2m00',
    'uc_account_uc20': 'https://www.plantuml.com/plantuml/png/VP71IiD048Rl-nG_kRU8HocX4C-2LC7hTBDcbsvdmsOY5X6y-G2-WHw4WYTl1azvalWafYr83h6dOVY_-USVPbu9HQdNNdbpAv20w0eho5qqMbnWLQqSbnHf3U_OoAOq255i60WbwHKLPY4RRx2R8owyKUAaxw-pqnFyFBtWikw-tXY-_GRRzfLnvzejAqLQGaIIsQvvHnw8BRYmhckUomHK8Jk_KEhF5ScuJu871TILqLGTWNg_NQ0XUcNRxNgKeY6sw9eF6iMMG-oc_Hodj7fKghy5aqbwoB1VWUdqqE8Civcv5yDvckwrvH5D_wFD-z9_ynS0',
    'uc_core_uc18': 'https://www.plantuml.com/plantuml/png/ZL9FIyCm5B_dKpnwtw0taJ46yop8zDPBciOcj7qjRIeE5Rnv7kB1csE88FFcgKKyn2yIFubPzuSED_4Ktk_FUx-yP50ecgioYKdCpnMe578P2WM1p3bJCaLIH18pcjC4OebSZJCEQQv4sY8ooY8Qyf4QnnmMFefXp8cIojPdG_S0lc_luQGqrGmXrXyWJ3N5q1xreuGBgL-H4CfKceCpjE0B12b50HWAQUgxp05QmF3ec91DSt3-REV05G4e2yveiQNrS9VOjb_4R5j6fdwZm4prN8BGSvjcQTo8QLjzAkWOlYQcVf0hdOUgkGdJxosJlsNIymGYQQhFnCD8w2cpG_HJM-x-qYl1Kr3jrBvBTweyB4mziQaMEqGBfJQORDdyFRP4ps1F74Pk2B4l0PrEVxcoPXNGxIvBE8HUZrygZa6_tt3-lpZVRLY9B2u3lgPTQkTShnKhpD-1iIriO2VO7_q3',
    'uc_core_uc19': 'https://www.plantuml.com/plantuml/png/ZPAnIiH048RxVOgVz7TWgHpX8DQ2g61XixTPiyjjPaCo0GyHx7m0dq141C56hIvOvKdYaxYvWoE84QjX-Fz_ljbbvXNBaklS2QSl6UnHsimmKbjgnTQJg9QM2bdA7CwIvbMXuKisVY0KKYrbfazuvJJwdAJCQS6MGt-MxEtZw_OUntMtVYIuzXEf98EyQvuKdE_M3nQ5QTye4q8gzYMYn7JDCrBV-oWpjclkYWYoGd9u9CGEWUWVGoDS2w2kj9BLMEA2VaG2gbzy63mrxKkEttroQ4owzMi1Cg647pNj1sLWIsECnJ1xthxB4OOIDqA4zsCoYRVBRSYOJhSj3Z2RwIlMbCRnHblyeQaHRHvAE8Tl',
}


def upload_image_to_drive(drive_service, png_path: str, filename: str) -> str:
    """Upload PNG to Drive and return shareable URL."""
    file_metadata = {
        'name': filename,
        'mimeType': 'image/png',
    }
    media = MediaFileUpload(png_path, mimetype='image/png', resumable=False)
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    file_id = file.get('id')

    # Make publicly readable
    drive_service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'},
    ).execute()

    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    print(f'  Uploaded {filename} → {url}')
    return url


def find_inline_images(doc_service, doc_id: str, tab_id: str) -> dict:
    """Find all inline images in a tab and return {objectId: index}."""
    doc = doc_service.documents().get(
        documentId=doc_id,
        includeTabsContent=True
    ).execute()

    images = {}
    idx = 0
    for tab in _iter_tabs(doc.get('tabs', [])):
        if tab.get('tabProperties', {}).get('tabId') != tab_id:
            continue
        content = tab.get('documentTab', {}).get('body', {}).get('content', [])
        for element in content:
            para = element.get('paragraph', {})
            for el in para.get('elements', []):
                inline = el.get('inlineObjectElement', {})
                obj_id = inline.get('inlineObjectId')
                if obj_id:
                    idx += 1
                    images[f'image_{idx:02d}'] = obj_id
                    print(f'  Found image_{idx:02d} → objectId={obj_id}')
    return images


def _iter_tabs(tabs):
    for tab in tabs:
        yield tab
        for child in tab.get('childTabs', []):
            yield from _iter_tabs([child])


def replace_image_in_doc(doc_service, doc_id: str, tab_id: str, object_id: str, image_url: str):
    """Replace an inline image using replaceImage API."""
    requests = [{
        'replaceImage': {
            'imageObjectId': object_id,
            'uri': image_url,
            'imageReplaceMethod': 'CENTER_CROP',
            'tabsCriteria': {'tabIds': [tab_id]},
        }
    }]
    try:
        result = doc_service.documents().batchUpdate(
            documentId=doc_id,
            body={'requests': requests}
        ).execute()
        print(f'  ✅ Replaced image objectId={object_id}')
        return result
    except Exception as e:
        print(f'  ❌ Failed objectId={object_id}: {e}')
        return None


def update_text_in_doc(doc_service, doc_id: str, tab_id: str, old_text: str, new_text: str) -> bool:
    """Replace exact text string in document tab."""
    requests = [{
        'replaceAllText': {
            'containsText': {
                'text': old_text,
                'matchCase': True,
            },
            'replaceText': new_text,
            'tabsCriteria': {
                'tabIds': [tab_id]
            }
        }
    }]
    result = doc_service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': requests}
    ).execute()
    replacements = result.get('replies', [{}])[0].get('replaceAllText', {}).get('occurrencesChanged', 0)
    print(f'  Text replace "{old_text[:40]}" → "{new_text[:40]}" ({replacements} occurrences)')
    return replacements > 0


def main():
    print('=== Fixing UC Diagrams in Google Docs ===\n')

    docs_service = get_service()

    # ───────────────────────────────────────────────
    # STEP 1: Find image object IDs in Account tab
    # ───────────────────────────────────────────────
    print('STEP 1: Finding image positions in Tài khoản tab...')
    account_images = find_inline_images(docs_service, DOC_ID, TAB_ACCOUNT)

    # ───────────────────────────────────────────────
    # STEP 2: Replace images in Account tab using PlantUML URLs
    # ───────────────────────────────────────────────
    print('\nSTEP 2: Replacing UC images in Tài khoản tab...')
    # Map: image_XX key → plantuml URL key
    account_replacement_map = {
        'image_02': 'uc_account_main',   # UC tổng quan
        'image_03': 'uc_account_uc01',   # UC01 Xác thực người dùng
        'image_06': 'uc_account_uc04',   # UC04 Quản lý TTCN
        'image_07': 'uc_account_uc20',   # UC20 Quản lý nhân viên
    }
    for img_key, url_key in account_replacement_map.items():
        if img_key in account_images and url_key in PLANTUML_URLS:
            replace_image_in_doc(
                docs_service, DOC_ID, TAB_ACCOUNT,
                account_images[img_key], PLANTUML_URLS[url_key]
            )
            time.sleep(1.5)
        else:
            print(f'  SKIP: {img_key} (found={img_key in account_images})')

    # ───────────────────────────────────────────────
    # STEP 3: Update text – Account tab
    # ───────────────────────────────────────────────
    print('\nSTEP 3: Updating text content in Tài khoản tab...')

    text_replacements = [
        # UC01 name change
        ('UC01\tĐăng nhập', 'UC01\tXác thực người dùng'),
        ('UC01 | Đăng nhập', 'UC01 | Xác thực người dùng'),
        ('UC01 – Đăng nhập', 'UC01 – Xác thực người dùng'),
        ('| UC01 | Đăng nhập |', '| UC01 | Xác thực người dùng |'),

        # Remove system-internal UC cons from relationship table
        ('Xác thực tài khoản | include | Bắt buộc – hệ thống kiểm tra sau khi nhập',
         'Đăng ký | extend | Khi người dùng chưa có tài khoản, nhấn Đăng ký'),

        ('Xác minh mật khẩu cũ | include | Bắt buộc – phải xác minh MK hiện tại trước khi đổi',
         'Đổi mật khẩu | extend | Khi người dùng muốn thay đổi mật khẩu'),

        ('Xem hồ sơ cá nhân | include | Bắt buộc – hiển thị hồ sơ khi vào trang',
         'Chỉnh sửa thông tin | extend | Khi người dùng chọn chỉnh sửa'),

        ('Xem danh sách nhân viên | include | Bắt buộc – hiển thị danh sách trước khi thao tác',
         'Thêm nhân viên | extend | Khi Admin chọn thêm mới'),

        # Section headings for individual UCs
        ('UC01 – Đăng nhập\n', 'UC01 – Xác thực người dùng\n'),
    ]

    for old, new in text_replacements:
        update_text_in_doc(docs_service, DOC_ID, TAB_ACCOUNT, old, new)
        time.sleep(0.3)

    # ───────────────────────────────────────────────
    # STEP 4: Find + replace images in Core tab
    # ───────────────────────────────────────────────
    print('\nSTEP 4: Finding image positions in Quản trị cốt lõi tab...')
    core_images = find_inline_images(docs_service, DOC_ID, TAB_CORE)

    print('\nSTEP 5: Replacing UC18 and UC19 images in Core tab...')
    core_replacement_map = {
        'image_04': 'uc_core_uc18',
        'image_05': 'uc_core_uc19',
    }
    for img_key, url_key in core_replacement_map.items():
        if img_key in core_images and url_key in PLANTUML_URLS:
            replace_image_in_doc(
                docs_service, DOC_ID, TAB_CORE,
                core_images[img_key], PLANTUML_URLS[url_key]
            )
            time.sleep(1.5)
        else:
            print(f'  SKIP: {img_key} (found={img_key in core_images})')

    print('\n✅ Done! Review changes at:')
    print(f'https://docs.google.com/document/d/{DOC_ID}/edit')


if __name__ == '__main__':
    main()
