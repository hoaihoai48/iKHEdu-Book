#!/usr/bin/env python3
"""
fix_titles_and_explanations.py
Sửa triệt để 2 lỗi:
1. Sửa màu Tiêu đề (Heading 3) của toàn bộ 135 bài toán thành màu đen đậm chuẩn #1E293B (Bold, 13pt).
2. Sửa toàn bộ 135 khối Giải thích: Tách từng dòng thành đoạn văn riêng biệt (<w:p>),
   style Normal, font Times New Roman 12.5pt, CĂN TRÁI TỰ NHIÊN (Left-aligned),
   loại bỏ hoàn toàn thẻ <w:br/> dồn dòng và triệt tiêu lỗi kéo dãn chữ (Justify).
"""

import re, sys, html
from pathlib import Path
import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

sys.path.insert(0, str(Path(__file__).parent))
from enrich_data_dp1 import DP1_DATA
from enrich_data_dp2 import DP2_DATA
from enrich_data_dps import DPS_DATA
from enrich_data_stl import STL_DATA
from enrich_data_stk import STK_DATA
from enrich_data_que import QUE_DATA
from enrich_data_gra import GRA_DATA
from enrich_data_grd import GRD_DATA
from enrich_data_rng import RNG_DATA

ALL_DATA = {}
for m in [DP1_DATA, DP2_DATA, DPS_DATA, STL_DATA, STK_DATA, QUE_DATA, GRA_DATA, GRD_DATA, RNG_DATA]:
    ALL_DATA.update(m)

TARGET_FILE = Path("courses/cpp-bang-b/c++-level-1-quyen-2.docx")

def clean_math_text(txt):
    t = txt.replace("$", "")
    t = t.replace(r"\le", "≤").replace(r"\ge", "≥")
    t = t.replace(r"\times", "×").replace(r"\ne", "≠")
    t = t.replace(r"\dots", "...").replace(r"\in", "∈")
    t = t.replace(r"\min", "min").replace(r"\max", "max")
    t = t.replace(r"\gcd", "gcd")
    t = t.replace(r"\{", "{").replace(r"\}", "}")
    t = t.replace(r"\text{", "").replace("}", "")
    t = t.replace("\t", " × ")
    t = t.replace(" × imes ", " × ").replace("× imes", "×")
    t = t.replace("&", "&amp;") # Escape ampersand for XML
    return t

def fix_all():
    print(f"📖 Đang mở tài liệu: {TARGET_FILE}...")
    doc = docx.Document(str(TARGET_FILE))
    body = doc._element.body

    # 1. Tìm tất cả 135 bài toán và chỉ số đoạn văn trong body
    problems = []
    for i, el in enumerate(body):
        tag = el.tag.split("}")[-1]
        if tag == "p":
            txt = "".join(el.itertext()).strip()
            m = re.search(r"\[(CPPB-[A-Z0-9]+-\d+)\]", txt)
            if m and "Bài " in txt:
                problems.append((m.group(1), i))

    print(f"  → Đã tìm thấy {len(problems)} bài toán trong body.")
    assert len(problems) == 135, f"Mong đợi 135 bài nhưng tìm thấy {len(problems)}"

    # 2. Duyệt ngược từ bài cuối lên bài đầu để chèn/sửa mà không làm xáo trộn chỉ số
    fixed_titles = 0
    fixed_explanations = 0

    for idx in reversed(range(len(problems))):
        code, p_idx = problems[idx]
        data = ALL_DATA.get(code)
        if not data:
            print(f"  ⚠️ Thiếu dữ liệu cho {code}")
            continue

        # SỬA LỖI 2: Ép chuẩn màu #1E293B, Bold, 13pt cho Tiêu đề bài toán (Heading 3)
        p_title = body[p_idx]
        title_text = f"Bài {idx+1:02d} [{code}]: {data['title']}"
        title_text_escaped = html.escape(title_text)
        new_title_xml = f'''<w:p {nsdecls("w")}>
            <w:pPr>
                <w:pStyle w:val="Heading3"/>
                <w:spacing w:before="180" w:after="60" w:line="276" w:lineRule="auto"/>
                <w:jc w:val="left"/>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    <w:b/>
                    <w:color w:val="1E293B"/>
                    <w:sz w:val="26"/>
                </w:rPr>
                <w:t>{title_text_escaped}</w:t>
            </w:r>
        </w:p>'''
        new_p_title = parse_xml(new_title_xml)
        p_title.getparent().replace(p_title, new_p_title)
        fixed_titles += 1

        # SỬA LỖI 1: Tìm đoạn 'Giải thích:' của bài hiện tại
        next_limit = problems[idx+1][1] if idx+1 < len(problems) else p_idx + 40
        gt_title_el = None

        for j in range(p_idx, min(next_limit, len(body))):
            if body[j].tag.split("}")[-1] == "p":
                t = "".join(body[j].itertext()).strip()
                if "Giải thích:" in t:
                    gt_title_el = body[j]
                    break

        if gt_title_el is None:
            print(f"  ⚠️ Không tìm thấy 'Giải thích:' cho {code}")
            continue

        # Chuẩn hóa lại thẻ tiêu đề 'Giải thích:' (style Compact, Bold, màu 1E293B, không gán Justify)
        gt_title_xml = f'''<w:p {nsdecls("w")}>
            <w:pPr>
                <w:pStyle w:val="Compact"/>
                <w:spacing w:before="60" w:after="30" w:line="276" w:lineRule="auto"/>
                <w:jc w:val="left"/>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                    <w:b/>
                    <w:color w:val="1E293B"/>
                </w:rPr>
                <w:t>Giải thích:</w:t>
            </w:r>
        </w:p>'''
        new_gt_title = parse_xml(gt_title_xml)
        gt_title_el.getparent().replace(gt_title_el, new_gt_title)

        # Xóa bỏ các đoạn văn giải thích cũ nằm giữa 'Giải thích:' và 'Ràng buộc & Giới hạn:'
        curr = new_gt_title.getnext()
        while curr is not None:
            c_tag = curr.tag.split("}")[-1]
            c_text = "".join(curr.itertext()).strip()
            if c_tag == "p" and ("Ràng buộc" in c_text or "Bài " in c_text or "Thống kê" in c_text or "Phụ lục" in c_text):
                break
            nxt = curr.getnext()
            curr.getparent().remove(curr)
            curr = nxt

        # Tách nội dung giải thích thành từng dòng riêng biệt
        raw_gt = clean_math_text(data["gt"])
        lines = [line.strip() for line in raw_gt.split("\n") if line.strip()]

        # Chèn từng dòng thành một đoạn văn <w:p> độc lập, style Normal, CĂN TRÁI Left, không Justify
        anchor = new_gt_title
        for line in lines:
            line_escaped = html.escape(line)
            p_line_xml = f'''<w:p {nsdecls("w")}>
                <w:pPr>
                    <w:pStyle w:val="Normal"/>
                    <w:spacing w:before="0" w:after="40" w:line="276" w:lineRule="auto"/>
                    <w:jc w:val="left"/>
                </w:pPr>
                <w:r>
                    <w:rPr>
                        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                        <w:sz w:val="25"/>
                        <w:color w:val="1E293B"/>
                    </w:rPr>
                    <w:t>{line_escaped}</w:t>
                </w:r>
            </w:p>'''
            p_line_el = parse_xml(p_line_xml)
            anchor.addnext(p_line_el)
            anchor = p_line_el

        fixed_explanations += 1

    print(f"  ✅ Đã sửa màu tiêu đề cho {fixed_titles}/135 bài toán (#1E293B Bold 13pt)!")
    print(f"  ✅ Đã tái cấu trúc tách dòng căn trái tự nhiên cho {fixed_explanations}/135 khối Giải thích!")

    doc.save(str(TARGET_FILE))
    print(f"🎉 Đã lưu thành công file Word: {TARGET_FILE.name}!")

if __name__ == "__main__":
    fix_all()
