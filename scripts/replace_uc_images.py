"""
Replace UC diagram images in Google Docs tabs using insertInlineImage + deleteContentRange.
Process: delete old image → insert new image at same index.
Process in REVERSE order to avoid index shifting.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs', 'scripts'))
from auth import get_service

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_ACCOUNT = 't.e7vhkfc8t70g'
TAB_CORE    = 't.pl02ohyiavub'

# image_XX (1-indexed) → PlantUML URL
ACCOUNT_REPLACEMENTS = {
    2: 'https://www.plantuml.com/plantuml/png/XPHFQnD16CRlyobUSl3MKajEKa8n1GjBej8aU0YKsTbnPyXcDkpEYaK4fGVnPYazU10QFOY5Wg8Ni_IqmU-nVXBVtIQRtUqaNlRVytlVUTwP9zaFDGrqDFQ8nvzhq3u4qXKQ71bmfgMlI3YIQa83EWPFAgvF9XpyG0k_94me6r6N7-aJZqDMHvNhSQAbnlU7CerF8vYVfV4vz4CEROgNls_EeUCx4GAzv5A29VnqzaN1FUY9v5896CZaIX52cVO3Q5WYcJ81cUGsW8PW7IwbhaW-AtYHuRdI7IoLjaZZh-3u5DifLw2FTvCSQHzq2IbyGiDWf06l240KSfQvRJp3vK5Zlnzig9JxvtiQVvBW9ByNTlhjdVjblYlIsVK4Av9VoWKjrL3Dp-Qd-AnofIYYvQgd4Gu1OmGqZ93x5XMSNURc7_9Me-Icq8yFh2g1qxvL9WErAhfcJ7ZSUrBcAWOUfV6r12-TJMMTOrKRQNmXpHCTTwp_xjZ6wjhMvV7nafjA2vPCSSSn8Cl2Phae2yXx34U8uz2XMXKMT7Lt-1ZGnLIvGpp5-ACifIw3RRCX34mjeltsxawPnSXVZS54LTO_ocmQCRjwY3_D52El2R4EOMkhTHlOrNEJT0Uhx_ZxCBsWQP9zWktjMut20zZRaufvaSDRhLoq2pKN-KlDbRFGC1wRrCuwzKvnbbl3sZN4DYEip9WMAld8ObRhGl9SB8dcdJcQzXgDv0Uw47TtweLuYXiqjaRRnnl-U_y3',  # UC tổng quan
    3: 'https://www.plantuml.com/plantuml/png/ZPF1IiD048Rl-nH3xorwbL8ABLW8ZOfQF0XbkrcJ9Uac91knYA3u0efu5AmNKIWeUB71Kuhl4P_4JMhJDAIjjvtytp_xpoIfUmAxmkzRoA8d0eGDBjCD0HfpAH7CviWp6NUmY_jWCKx5mA5WkyAmCuA3YObrkYy65eNOXxbkKIIOaFLXOsCJVYxlu2WS4X165BmJuFhtMnGyCD32JwuZX8cmNIWfXcGCCC97hfS0Uw2qPf9gX4ySJbduoXD5xSoKXcpv34qrUTnegWYb4Q2q_D8Id2C0twC4Usj0sJUU8ekhHZGUET8GVd0T1EF7V78xkPPddYYf2MTTUxwC3tq9230bz-AdN2_BJMwILcRubUhTfh98i2YuuaK1SYwyRCgTWzqijn1WEmf63AneF6HvZYp6Y89xLZnHjwsitTXADqON22ajA9Thq_shdVbPlkXvWPAFh5APbXYse5fbd5Y-HckrHEobQYBICq6vzgV9eLQfRUMVtdZP1LVda5unGhBCwXJnQd9DwfAKF_4l',  # UC01 Xác thực
    6: 'https://www.plantuml.com/plantuml/png/XP4nImD148Nx_HMFwnCih2GSWJI1gqG42vlDPhrTiZSNTkV488AjjPMTfvrWPvLWjR_a_2Lk4eZN1AlXyRxtPc36WQNdfdB2wHi6r_2sD8ovzLgnhKc4XQMbzBA2iwHvjTIeFPkwPoobMiXIN_3AQMnpaagd1LjE-d9oSegVnsUSDztwdU3YDzZ4Boh1bg1Y2pBnZOIGYckFh32nLGOclbAPGGOKKo4EhSZ-wSbmBu0cQ2N3CVgQUdZQiBsn7vgORlD41g7RVCfUxW3BFdsbAvXktIOcvLuiRcty-6Ddua68Oeh18DylsXLWEDnBd64qqdUiQPxdEszsn1kdaJxr2m00',  # UC04 Quản lý TTCN
    7: 'https://www.plantuml.com/plantuml/png/VP71IiD048Rl-nG_kRU8HocX4C-2LC7hTBDcbsvdmsOY5X6y-G2-WHw4WYTl1azvalWafYr83h6dOVY_-USVPbu9HQdNNdbpAv20w0eho5qqMbnWLQqSbnHf3U_OoAOq255i60WbwHKLPY4RRx2R8owyKUAaxw-pqnFyFBtWikw-tXY-_GRRzfLnvzejAqLQGaIIsQvvHnw8BRYmhckUomHK8Jk_KEhF5ScuJu871TILqLGTWNg_NQ0XUcNRxNgKeY6sw9eF6iMMG-oc_Hodj7fKghy5aqbwoB1VWUdqqE8Civcv5yDvckwrvH5D_wFD-z9_ynS0',  # UC20 Quản lý NV
}

CORE_REPLACEMENTS = {
    4: 'https://www.plantuml.com/plantuml/png/ZL9FIyCm5B_dKpnwtw0taJ46yop8zDPBciOcj7qjRIeE5Rnv7kB1csE88FFcgKKyn2yIFubPzuSED_4Ktk_FUx-yP50ecgioYKdCpnMe578P2WM1p3bJCaLIH18pcjC4OebSZJCEQQv4sY8ooY8Qyf4QnnmMFefXp8cIojPdG_S0lc_luQGqrGmXrXyWJ3N5q1xreuGBgL-H4CfKceCpjE0B12b50HWAQUgxp05QmF3ec91DSt3-REV05G4e2yveiQNrS9VOjb_4R5j6fdwZm4prN8BGSvjcQTo8QLjzAkWOlYQcVf0hdOUgkGdJxosJlsNIymGYQQhFnCD8w2cpG_HJM-x-qYl1Kr3jrBvBTweyB4mziQaMEqGBfJQORDdyFRP4ps1F74Pk2B4l0PrEVxcoPXNGxIvBE8HUZrygZa6_tt3-lpZVRLY9B2u3lgPTQkTShnKhpD-1iIriO2VO7_q3',  # UC18
    5: 'https://www.plantuml.com/plantuml/png/ZPAnIiH048RxVOgVz7TWgHpX8DQ2g61XixTPiyjjPaCo0GyHx7m0dq141C56hIvOvKdYaxYvWoE84QjX-Fz_ljbbvXNBaklS2QSl6UnHsimmKbjgnTQJg9QM2bdA7CwIvbMXuKisVY0KKYrbfazuvJJwdAJCQS6MGt-MxEtZw_OUntMtVYIuzXEf98EyQvuKdE_M3nQ5QTye4q8gzYMYn7JDCrBV-oWpjclkYWYoGd9u9CGEWUWVGoDS2w2kj9BLMEA2VaG2gbzy63mrxKkEttroQ4owzMi1Cg647pNj1sLWIsECnJ1xthxB4OOIDqA4zsCoYRVBRSYOJhSj3Z2RwIlMbCRnHblyeQaHRHvAE8Tl',  # UC19
}

IMG_W = {'magnitude': 500, 'unit': 'PT'}
IMG_H = {'magnitude': 350, 'unit': 'PT'}


def get_image_positions(docs, doc_id, tab_id):
    """Return list of (index, startIndex, endIndex, objectId) sorted by startIndex."""
    doc = docs.documents().get(documentId=doc_id, includeTabsContent=True).execute()
    result = []
    img_idx = 0
    for tab in _iter_tabs(doc.get('tabs', [])):
        if tab.get('tabProperties', {}).get('tabId') != tab_id:
            continue
        body = tab.get('documentTab', {}).get('body', {}).get('content', [])
        for el in body:
            for pe in el.get('paragraph', {}).get('elements', []):
                inline = pe.get('inlineObjectElement', {})
                if inline.get('inlineObjectId'):
                    img_idx += 1
                    result.append({
                        'idx': img_idx,
                        'start': pe['startIndex'],
                        'end': pe['endIndex'],
                        'obj_id': inline['inlineObjectId'],
                    })
    return result


def _iter_tabs(tabs):
    for t in tabs:
        yield t
        for c in t.get('childTabs', []):
            yield from _iter_tabs([c])


def replace_one_image(docs, doc_id, tab_id, start_idx, end_idx, new_url):
    """Delete old image and insert new image at same position (two separate requests)."""
    # Step 1: Delete old image character
    docs.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': [{
            'deleteContentRange': {
                'range': {
                    'startIndex': start_idx,
                    'endIndex': end_idx,
                    'tabId': tab_id,
                }
            }
        }]}
    ).execute()

    # Step 2: Insert new image at same position
    docs.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': [{
            'insertInlineImage': {
                'uri': new_url,
                'location': {'index': start_idx, 'tabId': tab_id},
                'objectSize': {'height': IMG_H, 'width': IMG_W},
            }
        }]}
    ).execute()


def process_tab(docs, doc_id, tab_id, replacements, tab_name):
    print(f'\n--- {tab_name} ---')
    positions = get_image_positions(docs, doc_id, tab_id)
    print(f'Found {len(positions)} images')

    # Filter to only images we want to replace
    to_replace = [(p, replacements[p['idx']]) for p in positions if p['idx'] in replacements]

    # Process in REVERSE order (highest startIndex first) to avoid index drift
    for pos, url in sorted(to_replace, key=lambda x: x[0]['start'], reverse=True):
        print(f"  Replacing image_{pos['idx']:02d} (start={pos['start']}, obj={pos['obj_id']})...", end='', flush=True)
        try:
            replace_one_image(docs, doc_id, tab_id, pos['start'], pos['end'], url)
            print(' ✅')
        except Exception as e:
            print(f' ❌ {e}')
        time.sleep(2)


def main():
    print('=== Replacing UC Diagrams via insertInlineImage ===')
    docs = get_service()

    process_tab(docs, DOC_ID, TAB_ACCOUNT, ACCOUNT_REPLACEMENTS, 'Tài khoản & Thành viên')
    process_tab(docs, DOC_ID, TAB_CORE, CORE_REPLACEMENTS, 'Quản trị cốt lõi')

    print(f'\n✅ Done — review at: https://docs.google.com/document/d/{DOC_ID}/edit')


if __name__ == '__main__':
    main()
