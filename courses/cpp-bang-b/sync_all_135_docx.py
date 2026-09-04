#!/usr/bin/env python3
"""
sync_all_135_docx.py
Đồng bộ toàn diện nội dung Bối cảnh, Nhiệm vụ và Giải thích sư phạm
cho 135 bài toán trong c++-level-1-quyen-2.docx theo đúng chuẩn mực
c++-level-1-quyen-1.docx và MASTER_WORD_BUILD_SPECIFICATION.md.
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
    """Chuyển đổi công thức toán học Markdown sang ký hiệu Unicode sạch cho Word."""
    t = txt.replace("$", "")
    t = t.replace(r"\le", "≤").replace(r"\ge", "≥")
    t = t.replace(r"\times", "×").replace(r"\ne", "≠")
    t = t.replace(r"\dots", "...").replace(r"\in", "∈")
    t = t.replace(r"\min", "min").replace(r"\max", "max")
    t = t.replace(r"\gcd", "gcd")
    t = t.replace(r"\{", "{").replace(r"\}", "}")
    t = t.replace(r"\text{", "").replace("}", "")
    return t

def sync_docx():
    print(f"📖 Đang mở tài liệu: {TARGET_FILE}...")
    doc = docx.Document(str(TARGET_FILE))

    # 1. Tìm tất cả 135 bài toán và chỉ số đoạn văn
    probs = []
    for i, p in enumerate(doc.paragraphs):
        m = re.search(r"\[(CPPB-[A-Z0-9]+-\d+)\]", p.text)
        if m and "Bài " in p.text:
            probs.append((m.group(1), i))

    print(f"  → Đã tìm thấy {len(probs)} bài toán.")
    assert len(probs) == 135, f"Mong đợi 135 bài toán nhưng tìm thấy {len(probs)}"

    updated_count = 0
    for idx, (code, p_idx) in enumerate(probs):
        data = ALL_DATA.get(code)
        if not data:
            print(f"  ⚠️ Không có dữ liệu cho {code}")
            continue

        next_limit = probs[idx+1][1] if idx+1 < len(probs) else p_idx + 35

        p_bc_idx = None
        p_nv_idx = None
        p_gt_title_idx = None
        p_gt_content_idx = None

        for j in range(p_idx, next_limit):
            t = doc.paragraphs[j].text.strip()
            if t.startswith("Bối cảnh:") and p_bc_idx is None:
                p_bc_idx = j
            elif t.startswith("Nhiệm vụ:") and p_nv_idx is None:
                p_nv_idx = j
            elif t.startswith("Giải thích:") and p_gt_title_idx is None:
                p_gt_title_idx = j
                if j + 1 < len(doc.paragraphs):
                    p_gt_content_idx = j + 1

        if p_bc_idx is None or p_nv_idx is None or p_gt_content_idx is None:
            print(f"  ⚠️ Thiếu đoạn văn cho {code}: bc={p_bc_idx}, nv={p_nv_idx}, gt={p_gt_content_idx}")
            continue

        # Cập nhật Tiêu đề bài (đảm bảo đúng tên)
        doc.paragraphs[p_idx].text = f"Bài {idx+1:02d} [{code}]: {data['title']}"

        # Cập nhật Bối cảnh (First Paragraph, Bối cảnh: in đậm, nội dung sau căn đều Justify)
        bc_clean = clean_math_text(data["bc"])
        p_bc = doc.paragraphs[p_bc_idx]
        p_bc.clear()
        p_bc.style = "First Paragraph"
        r_bold = p_bc.add_run("Bối cảnh: ")
        r_bold.bold = True
        r_text = p_bc.add_run(bc_clean)
        # Ép font Times New Roman 12.5pt
        for r in [r_bold, r_text]:
            r.font.name = "Times New Roman"
            r.font.size = docx.shared.Pt(12.5)

        # Cập nhật Nhiệm vụ (Body Text, Nhiệm vụ: in đậm)
        nv_clean = clean_math_text(data["nv"])
        p_nv = doc.paragraphs[p_nv_idx]
        p_nv.clear()
        p_nv.style = "Body Text"
        r_bold = p_nv.add_run("Nhiệm vụ: ")
        r_bold.bold = True
        r_text = p_nv.add_run(nv_clean)
        for r in [r_bold, r_text]:
            r.font.name = "Times New Roman"
            r.font.size = docx.shared.Pt(12.5)

        # Cập nhật Giải thích (Normal, Justify, sạch 100% công thức)
        gt_clean = clean_math_text(data["gt"])
        p_gt = doc.paragraphs[p_gt_content_idx]
        p_gt.clear()
        p_gt.style = "Normal"
        p_gt.paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.JUSTIFY
        r_gt = p_gt.add_run(gt_clean)
        r_gt.font.name = "Times New Roman"
        r_gt.font.size = docx.shared.Pt(12.5)

        updated_count += 1

    print(f"  ✅ Đã cập nhật đồng bộ hoàn hảo {updated_count} / 135 bài toán trong DOCX!")
    doc.save(str(TARGET_FILE))
    print(f"🎉 Đã lưu thành công file Word: {TARGET_FILE.name}!")

if __name__ == "__main__":
    sync_docx()
