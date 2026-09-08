#!/usr/bin/env python3
"""
Giai đoạn 3: Làm giàu 135 bài tập với phần Giải thích (Pedagogical Explanation)
theo đúng chuẩn mực c++-level-1-quyen-1.docx và MASTER_WORD_BUILD_SPECIFICATION.md:

- Tìm chính xác 135 bài toán và bảng Sample IO tương ứng trong c++-level-1-quyen-2.docx.
- Thêm tiêu đề 'Giải thích:' (style Compact, Bold) ngay sau bảng Sample IO.
- Thêm nội dung sư phạm phân tích Sample 1 (Font Times New Roman 12.5pt, line spacing 1.15, căn đều Justify).
- Giữ nguyên cấu trúc XML, bảo toàn 100% định dạng gáy sách, watermark, header/footer và các bảng khác.
"""

import re, sys
from pathlib import Path
import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

sys.path.insert(0, str(Path(__file__).parent))
from stage3_explanations_data import EXPLANATIONS

TARGET_FILE = Path("courses/cpp-bang-b/c++-level-1-quyen-2.docx")

def inject_stage3_enrichments():
    print(f"📖 Đang mở tài liệu: {TARGET_FILE}...")
    doc = docx.Document(str(TARGET_FILE))
    body = doc._element.body

    def get_text(elem):
        return "".join(elem.itertext()).strip()

    # 1. Quét tìm tất cả các bài tập trong body
    problems_info = []
    for i, el in enumerate(body):
        tag = el.tag.split("}")[-1]
        if tag == "p":
            txt = get_text(el)
            m = re.search(r"\[(CPPB-[A-Z0-9]+-\d+)\]", txt)
            if m and "Bài " in txt:
                problems_info.append((i, m.group(1)))

    print(f"  → Đã tìm thấy {len(problems_info)} bài tập trong tài liệu.")
    assert len(problems_info) == 135, f"Mong đợi 135 bài tập nhưng tìm thấy {len(problems_info)}"

    # 2. Với mỗi bài tập, tìm bảng Sample IO nằm giữa bài hiện tại và bài kế tiếp
    matched_pairs = []
    for idx, (p_idx, code) in enumerate(problems_info):
        next_limit = problems_info[idx+1][0] if idx+1 < len(problems_info) else min(p_idx+35, len(body))
        table_elem = None
        for j in range(p_idx, next_limit):
            if body[j].tag.split("}")[-1] == "tbl":
                t_txt = get_text(body[j])
                if "Đầu vào" in t_txt or "Input" in t_txt:
                    table_elem = body[j]
                    break
        
        if table_elem is not None:
            matched_pairs.append((code, table_elem))
        else:
            print(f"  ⚠️ Cảnh báo: Không tìm thấy bảng Sample IO cho {code}!")

    print(f"  → Đã khớp chính xác {len(matched_pairs)} / 135 bảng Sample IO.")
    assert len(matched_pairs) == 135, "Số lượng bảng Sample IO khớp không đủ 135!"

    # 3. Chèn 'Giải thích:' và nội dung sư phạm ngay sau bảng Sample IO
    # Đi từ cuối lên đầu để không làm thay đổi thứ tự hay chỉ số đang duyệt
    inserted_count = 0
    for code, tbl in reversed(matched_pairs):
        exp_text = EXPLANATIONS.get(code)
        if not exp_text:
            print(f"  ⚠️ Thiếu giải thích cho {code}!")
            continue

        import html
        exp_text_escaped = html.escape(exp_text)

        # XML cho đoạn tiêu đề 'Giải thích:' (Chuẩn Quyển 1: style Compact, chữ Bold)
        p_title_xml = f'''<w:p {nsdecls("w")}>
            <w:pPr>
                <w:pStyle w:val="Compact"/>
                <w:spacing w:before="60" w:after="30" w:line="276" w:lineRule="auto"/>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    <w:b/>
                    <w:sz w:val="25"/>
                    <w:color w:val="1E293B"/>
                </w:rPr>
                <w:t>Giải thích:</w:t>
            </w:r>
        </w:p>'''

        # XML cho đoạn nội dung giải thích (Chuẩn Quyển 1: Times New Roman 12.5pt, dãn dòng 1.15, căn đều Justify)
        p_content_xml = f'''<w:p {nsdecls("w")}>
            <w:pPr>
                <w:spacing w:before="0" w:after="80" w:line="276" w:lineRule="auto"/>
                <w:jc w:val="both"/>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    <w:sz w:val="25"/>
                    <w:color w:val="1E293B"/>
                </w:rPr>
                <w:t>{exp_text_escaped}</w:t>
            </w:r>
        </w:p>'''

        p_title_elem = parse_xml(p_title_xml)
        p_content_elem = parse_xml(p_content_xml)

        # Chèn vào sau tbl: đầu tiên chèn title sau tbl, sau đó chèn content sau title
        tbl.addnext(p_title_elem)
        p_title_elem.addnext(p_content_elem)
        inserted_count += 1

    print(f"  ✅ Đã chèn thành công {inserted_count} / 135 khối 'Giải thích' sư phạm vào tài liệu!")

    # 4. Lưu lại tài liệu đã làm giàu
    doc.save(str(TARGET_FILE))
    print(f"🎉 Đã lưu thành công: {TARGET_FILE.name}!")

if __name__ == "__main__":
    inject_stage3_enrichments()
