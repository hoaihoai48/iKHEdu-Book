#!/usr/bin/env python3
"""
audit_docx.py — Kiểm toán 7 điểm MASTER_WORD_BUILD_SPECIFICATION cho Word Level 2.

Cách dùng (chạy từ thư mục courses/cpp-bang-b-level2):
    python3 audit_docx.py --volume 1
    python3 audit_docx.py --volume 2
    python3 audit_docx.py --all

7 điểm kiểm tra (khớp PLAN_BUILD_QUYEN1_LEVEL2 B4.2):
    1. Không trang bìa (đoạn đầu = "Lời nói đầu")
    2. Watermark logo đủ 3 header (first/default/even)
    3. Style Normal KHÔNG bị Justify
    4. Đủ bảng Sample IO (Q1: 134, Q2: 212)
    5. 0 tblHeader + đủ cantSplit mọi hàng
    6. Code Source Code căn trái + 0 numPr
    7. 100% math runs trong bảng về 12pt (sz/szCs = 24)

Exit code 0 khi 7/7 PASS, 1 khi còn FAIL.
"""

import argparse
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

BASE_DIR = Path(__file__).parent
EXPECTED_SAMPLE_TABLES = {1: 134, 2: 212}


def check_no_cover(doc):
    for p in doc.paragraphs:
        if p.text.strip():
            ok = p.text.strip().lower() == "lời nói đầu"
            return ok, f"đoạn đầu = {p.text.strip()[:40]!r}"
    return False, "tài liệu rỗng"


def check_watermark(doc):
    ok_headers = 0
    total = 0
    for section in doc.sections:
        for header in (
            section.first_page_header,
            section.header,
            section.even_page_header,
        ):
            total += 1
            xml = header._element.xml
            if "w:pict" in xml and "imagedata" in xml:
                ok_headers += 1
    ok = total > 0 and ok_headers == total
    return ok, f"{ok_headers}/{total} header có watermark"


def check_normal_not_justify(doc):
    normal = doc.styles["Normal"]
    jc = normal.paragraph_format.alignment
    ok = jc != WD_ALIGN_PARAGRAPH.JUSTIFY
    return ok, f"Normal alignment = {jc}"


def is_sample_table(table):
    if len(table.columns) != 2 or len(table.rows) < 1:
        return False
    header = " ".join(c.text for c in table.rows[0].cells).lower()
    return ("input" in header or "đầu vào" in header) and (
        "output" in header or "đầu ra" in header
    )


def check_sample_tables(doc, volume):
    count = sum(1 for t in doc.tables if is_sample_table(t))
    expected = EXPECTED_SAMPLE_TABLES[volume]
    return count == expected, f"{count}/{expected} bảng Sample IO"


def check_tables(doc):
    tbl_header = 0
    rows_total = 0
    rows_no_cantsplit = 0
    for table in doc.tables:
        tbl_header += len(table._tbl.findall(".//" + qn("w:tblHeader")))
        for tr in table._tbl.findall(qn("w:tr")):
            rows_total += 1
            trPr = tr.find(qn("w:trPr"))
            if trPr is None or trPr.find(qn("w:cantSplit")) is None:
                rows_no_cantsplit += 1
    ok = tbl_header == 0 and rows_no_cantsplit == 0
    return ok, f"tblHeader={tbl_header}, thiếu cantSplit={rows_no_cantsplit}/{rows_total}"


def check_code(doc):
    paras = [p for p in doc.paragraphs if p.style.name == "Source Code"]
    bad_align = 0
    numpr = 0
    for p in paras:
        jc = p._p.find(qn("w:pPr"))
        jc_val = None
        if jc is not None:
            jc_el = jc.find(qn("w:jc"))
            if jc_el is not None:
                jc_val = jc_el.get(qn("w:val"))
        if jc_val != "left":
            bad_align += 1
        numpr += len(p._p.findall(".//" + qn("w:numPr")))
    ok = bad_align == 0 and numpr == 0
    return ok, f"{len(paras)} khối code, sai căn lề={bad_align}, numPr={numpr}"


def check_math_12pt(doc):
    NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
          "m": "http://schemas.openxmlformats.org/officeDocument/2006/math"}
    bad = 0
    total = 0
    for rPr in doc.element.xpath("//m:r/w:rPr"):
        total += 1
        sz = rPr.find("w:sz", NS)
        szCs = rPr.find("w:szCs", NS)
        if (
            sz is None
            or sz.get(qn("w:val")) != "24"
            or szCs is None
            or szCs.get(qn("w:val")) != "24"
        ):
            bad += 1
    ok = total > 0 and bad == 0
    return ok, f"sai cỡ chữ={bad}/{total} math runs"


def audit(volume):
    fname = f"IKHEDU_CPP_Nang_Cao_Quyen_{volume}.docx"
    doc = Document(str(BASE_DIR / fname))
    checks = [
        ("1. Không bìa", check_no_cover(doc)),
        ("2. Watermark 3 header", check_watermark(doc)),
        ("3. Normal không Justify", check_normal_not_justify(doc)),
        ("4. Đủ bảng Sample", check_sample_tables(doc, volume)),
        ("5. Bảng sạch", check_tables(doc)),
        ("6. Code trái/sạch", check_code(doc)),
        ("7. Math 12pt", check_math_12pt(doc)),
    ]
    print(f"\n📋 AUDIT {fname}")
    passed = 0
    for name, (ok, detail) in checks:
        print(f"  {'✅' if ok else '❌'} {name}: {detail}")
        passed += ok
    print(f"  → {passed}/7 PASS")
    return passed == 7


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--volume", type=int, choices=[1, 2])
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    volumes = [1, 2] if args.all or not args.volume else [args.volume]
    results = {v: audit(v) for v in volumes}
    if not all(results.values()):
        sys.exit(1)
    print("\n🎉 7/7 PASS toàn bộ!")


if __name__ == "__main__":
    main()
