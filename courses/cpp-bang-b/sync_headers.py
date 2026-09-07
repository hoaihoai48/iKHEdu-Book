#!/usr/bin/env python3
"""
SCRIPT: sync_headers.py
Mục đích: Đồng bộ 100% header của tất cả các trang con trong file Word 
courses/cpp-bang-b/cpp-giaovien-quyen-1.docx giống hệt header trang đầu (header3.xml).
"""

import os
import sys
import shutil
import zipfile
from pathlib import Path

def sync_headers(docx_path):
    target_path = Path(docx_path).resolve()
    if not target_path.exists():
        print(f"❌ File không tồn tại: {target_path}")
        return False

    temp_zip = target_path.with_name(f"{target_path.stem}.temp_sync.docx")

    with zipfile.ZipFile(target_path, "r") as z:
        h3_xml = z.read("word/header3.xml").decode("utf-8")

    # Header 1 (trang chẵn)
    h1_xml = h3_xml.replace("WordPictureWatermark1286990221", "WordPictureWatermark1286990222")
    h1_xml = h1_xml.replace("_x0000_s2049", "_x0000_s2052")
    h1_xml = h1_xml.replace("id=\"318338836\"", "id=\"318338837\"")

    # Header 2 (trang lẻ / default)
    h2_xml = h3_xml.replace("WordPictureWatermark1286990221", "WordPictureWatermark1286990223")
    h2_xml = h2_xml.replace("_x0000_s2049", "_x0000_s2051")
    h2_xml = h2_xml.replace("id=\"318338836\"", "id=\"318338838\"")

    with zipfile.ZipFile(target_path, "r") as zin:
        with zipfile.ZipFile(temp_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == "word/header1.xml":
                    zout.writestr(item, h1_xml.encode("utf-8"))
                elif item.filename == "word/header2.xml":
                    zout.writestr(item, h2_xml.encode("utf-8"))
                else:
                    zout.writestr(item, zin.read(item.filename))

    temp_zip.replace(target_path)
    print("✅ Đã đồng bộ sạch header1.xml và header2.xml khớp 100% header3.xml chuẩn OpenXML!")
    return True

if __name__ == "__main__":
    target = "courses/cpp-bang-b/cpp-giaovien-quyen-1.docx"
    if len(sys.argv) > 1:
        target = sys.argv[1]
    sync_headers(target)
