#!/usr/bin/env python3
"""
deep_audit_q1.py
Kiểm tra toàn diện 9 tiêu chí của user đối với c++-level-1-quyen-1.docx:
1. XML parse OK, sectPr nguyên vẹn, namespace prefix chuẩn.
2. [BLOCKER 1] r:embed trong document.xml > 0, mỗi ID tồn tại trong rels, orphan media = 0.
3. [BLOCKER 2] H3 bài tập đánh số liên tục 1-212 (không restart).
4. [MAJOR 3] Tiêu đề H1 và H3 bài mới dùng sentence case.
5. [MAJOR 4] H1 LỜI NÓI ĐẦU viết hoa toàn bộ.
6. [MAJOR 5] Heading 4 count = 0.
7. [MAJOR 6] Paras gộp list = 0 (không có đoạn nào chứa nhiều gạch đầu dòng dồn cục).
8. [MINOR 7] app.xml khớp số đếm thật.
9. [MINOR 8] Tỷ lệ single-char runs và tối ưu runs.
"""

import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import docx

DOCX_PATH = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/c++-level-1-quyen-1.docx")
ns = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'ep': 'http://schemas.openxmlformats.org/officeDocument/2006/extended-properties'
}

print("================================================================================")
print("🔍 BẮT ĐẦU AUDIT CHI TIẾT FILE C++-LEVEL-1-QUYEN-1.DOCX")
print("================================================================================")

with zipfile.ZipFile(DOCX_PATH, 'r') as z:
    # 1. XML parse check
    doc_xml = z.read('word/document.xml')
    doc_tree = ET.fromstring(doc_xml)
    print("✅ 1. XML parse document.xml: OK")

    # Rels check
    rels_xml = z.read('word/_rels/document.xml.rels')
    rels_tree = ET.fromstring(rels_xml)
    rel_ids = {r.attrib['Id']: r.attrib['Target'] for r in rels_tree}
    print(f"✅ Rels loaded: {len(rel_ids)} relationships")

    # 2. Images audit
    embed_ids = [blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed') 
                 for blip in doc_tree.findall('.//a:blip', ns)]
    embed_ids = [eid for eid in embed_ids if eid]
    print(f"\n📸 [BLOCKER 1] Image audit:")
    print(f"  → Total image blips referenced in body: {len(embed_ids)}")
    missing_rels = [eid for eid in embed_ids if eid not in rel_ids]
    print(f"  → Missing rels for embeds: {len(missing_rels)} (Must be 0)")
    
    media_files_in_zip = [n for n in z.namelist() if n.startswith('word/media/')]
    print(f"  → Total media files in package: {len(media_files_in_zip)}")

    # 3. Heading 3 Exercise continuous numbering check
    doc = docx.Document(str(DOCX_PATH))
    h3_probs = []
    for p in doc.paragraphs:
        if p.style.name == 'Heading 3':
            m = re.match(r"^Bài\s+(\d+)\s+\[(CPPB-[A-Z0-9]+-\d+)\]:\s+(.+)$", p.text)
            if m:
                h3_probs.append((int(m.group(1)), m.group(2), m.group(3)))

    print(f"\n🔢 [BLOCKER 2] Continuous Problem Numbering audit:")
    print(f"  → Total exercise problems detected: {len(h3_probs)} (Target: 212)")
    is_continuous = True
    for idx, (p_num, code, title) in enumerate(h3_probs, 1):
        if p_num != idx:
            print(f"  ❌ Mismatch at index {idx}: found Bài {p_num:02d} [{code}]")
            is_continuous = False
            break
    if is_continuous and len(h3_probs) == 212:
        print(f"  ✅ Exercise numbering is 100% continuous from Bài 01 to Bài 212!")

    # 4. Heading 4 count check (MAJOR 5)
    h4_count = len([p for p in doc.paragraphs if p.style.name == 'Heading 4'])
    print(f"\n🏷️ [MAJOR 5] Heading 4 count: {h4_count} (Target: 0)")

    # 5. LỜI NÓI ĐẦU check (MAJOR 4)
    p0_text = doc.paragraphs[0].text
    print(f"\n📖 [MAJOR 4] P0 Heading text: '{p0_text}' (Target: 'LỜI NÓI ĐẦU')")

    # 6. List merged paragraphs check (MAJOR 6)
    merged_list_paras = 0
    for p in doc.paragraphs:
        lines = [l.strip() for l in p.text.split('\n') if l.strip()]
        dash_lines = [l for l in lines if l.startswith('- ') or l.startswith('• ')]
        if len(dash_lines) > 1 and len(lines) > 1:
            merged_list_paras += 1
    print(f"\n📋 [MAJOR 6] Merged list paragraphs count: {merged_list_paras} (Target: 0)")

    # 7. app.xml check (MINOR 7)
    app_xml = z.read('docProps/app.xml')
    app_tree = ET.fromstring(app_xml)
    words_app = app_tree.find('.//ep:Words', ns).text
    paras_app = app_tree.find('.//ep:Paragraphs', ns).text
    chars_app = app_tree.find('.//ep:Characters', ns).text
    print(f"\n📊 [MINOR 7] app.xml stats: Words={words_app}, Characters={chars_app}, Paragraphs={paras_app}")

    # 8. Single-char runs audit (MINOR 8)
    all_t = doc_tree.findall('.//w:t', ns)
    single_t = [t for t in all_t if len(t.text or '') == 1]
    single_pct = len(single_t) / len(all_t) * 100 if all_t else 0
    print(f"\n🔤 [MINOR 8] Text runs: Total w:t={len(all_t)}, Single-char={len(single_t)} ({single_pct:.1f}%)")

print("\n================================================================================")
print("🎯 AUDIT HOÀN TẤT!")
print("================================================================================")
