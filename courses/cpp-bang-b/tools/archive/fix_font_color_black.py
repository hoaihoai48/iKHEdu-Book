#!/usr/bin/env python3
"""
SCRIPT: fix_font_color_black.py
Mục đích: Sửa trực tiếp file Word .docx, chuyển toàn bộ màu chữ #1E293B (xám xanh nhạt)
sang đen tuyền #000000 để khi in ấn tài liệu đạt độ sắc nét, tương phản tối đa.

Yêu cầu nghiêm ngặt từ User:
1. SỬA TRỰC TIẾP file Word (.docx) thông qua XML, CẤM build lại, CẤM động vào nội dung/bảng/ảnh/cấu trúc.
2. Style Normal + Heading 1/2/3/4: w:color val 1E293B -> 000000 (cả trong styles.xml).
3. Mọi run trực tiếp mang màu 1E293B trong document.xml: đổi hết sang 000000.
4. GIỮ NGUYÊN:
   - Heading 2 đỏ #FF0000 ("Bài tập thực hành" và run đỏ tương đương)
   - Code Consolas #0F2A44
   - Màu nền callout (#EFF6FF, viền #3B82F6), màu nền bảng (#F1F5F9, #F8FAFC)
   - Thẻ tô nền <w:shd w:fill="1E293B"/> (nếu có, không chạm vào thuộc tính fill nền)
   - Header, footer, logo/watermark
5. AUDIT:
   - Đếm số lượng thay thế trong styles.xml và document.xml
   - Grep lại "1E293B" trong text color: phải = 0
   - Kiểm tra số đoạn văn (paragraphs) và tổng số từ trước vs sau: BẮT BUỘC bằng nhau 100%.
"""

import os
import re
import sys
import shutil
import zipfile
from pathlib import Path

def get_doc_stats(docx_path):
    """Đếm số paragraphs và words để đảm bảo an toàn tuyệt đối nội dung."""
    import docx
    doc = docx.Document(str(docx_path))
    para_count = len(doc.paragraphs)
    word_count = sum(len(p.text.split()) for p in doc.paragraphs)
    table_count = len(doc.tables)
    return para_count, word_count, table_count

def fix_docx_font_colors(target_docx_path):
    target_path = Path(target_docx_path).resolve()
    if not target_path.exists():
        print(f"❌ File không tồn tại: {target_path}")
        return False

    print("=" * 80)
    print(f"🔧 BẮT ĐẦU FIX MÀU CHỮ NHẠT: {target_path.name}")
    print("=" * 80)

    # 1. Thống kê trước khi sửa
    print("📊 Đang kiểm tra thống kê nội dung trước khi sửa...")
    para_before, word_before, tbl_before = get_doc_stats(target_path)
    print(f"  → Trước: {para_before:,} paragraphs | {word_before:,} words | {tbl_before:,} tables")

    # 2. Tạo backup an toàn
    backup_path = target_path.with_name(f"{target_path.stem}.backup_before_black_fix.docx")
    shutil.copy2(target_path, backup_path)
    print(f"  🔒 Đã tạo bản backup an toàn tại: {backup_path.name}")

    temp_zip_path = target_path.with_name(f"{target_path.stem}.temp_fixing.docx")

    styles_replaced = 0
    doc_replaced = 0

    # Pattern thay thế màu chữ font:
    # Bắt chính xác thẻ <w:color ... w:val="1E293B" .../> hoặc các biến thể viết hoa/thường
    # KHÔNG chạm vào <w:shd w:fill="1E293B"/> (màu nền bảng)
    color_pattern = re.compile(r'(<w:color\b[^>]*?\bw:val=[\'"])1E293B([\'"][^>]*?>)', re.IGNORECASE)

    with zipfile.ZipFile(target_path, "r") as zin:
        with zipfile.ZipFile(temp_zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)

                if item.filename == "word/styles.xml":
                    text = data.decode("utf-8")
                    # Thay thế w:color w:val="1E293B" -> "000000"
                    new_text, count = color_pattern.subn(r'\g<1>000000\g<2>', text)
                    styles_replaced += count
                    # Đồng thời xóa themeColor/themeShade nếu đi kèm màu này để Word không tự biến tấu màu
                    new_text = re.sub(r'w:color\s+w:themeColor="[^"]*"\s+w:themeShade="[^"]*"\s+w:val="000000"', 'w:color w:val="000000"', new_text)
                    data = new_text.encode("utf-8")

                elif item.filename == "word/document.xml":
                    text = data.decode("utf-8")
                    # Thay thế chỉ thẻ <w:color ... w:val="1E293B" .../> sang 000000
                    new_text, count = color_pattern.subn(r'\g<1>000000\g<2>', text)
                    doc_replaced += count
                    data = new_text.encode("utf-8")

                zout.writestr(item, data)

    # Ghi đè file gốc
    temp_zip_path.replace(target_path)
    print(f"  ✅ Đã thay thế {styles_replaced} vị trí trong word/styles.xml")
    print(f"  ✅ Đã thay thế {doc_replaced:,} vị trí trong word/document.xml")

    # 3. Thống kê sau khi sửa
    print("\n🔍 Đang kiểm tra thống kê nội dung sau khi sửa...")
    para_after, word_after, tbl_after = get_doc_stats(target_path)
    print(f"  → Sau:   {para_after:,} paragraphs | {word_after:,} words | {tbl_after:,} tables")

    # Kiểm tra tính toàn vẹn
    assert para_before == para_after, f"Lỗi lệch paragraph: {para_before} != {para_after}"
    assert word_before == word_after, f"Lỗi lệch word count: {word_before} != {word_after}"
    assert tbl_before == tbl_after, f"Lỗi lệch table count: {tbl_before} != {tbl_after}"
    print("  💯 XÁC NHẬN TOÀN VẸN: Số đoạn văn, số từ và bảng khớp 100%!")

    # 4. Audit XML còn 1E293B trong thẻ màu chữ không
    with zipfile.ZipFile(target_path, "r") as z:
        for fname in ["word/styles.xml", "word/document.xml"]:
            content = z.read(fname).decode("utf-8")
            remain_color = color_pattern.findall(content)
            print(f"  🔎 Audit {fname}: còn lại {len(remain_color)} thẻ w:color mang màu 1E293B.")
            if remain_color:
                print(f"     ⚠️ Cảnh báo: vẫn còn thẻ màu 1E293B trong {fname}!")

    print("\n🎉 HOÀN THÀNH FIX MÀU ĐEN TUYỀN #000000 CHO FILE!")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Sử dụng: python3 fix_font_color_black.py <path_to_docx>")
        sys.exit(1)

    target_file = sys.argv[1]
    fix_docx_font_colors(target_file)
