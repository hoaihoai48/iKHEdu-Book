import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import xml.etree.ElementTree as ET

DOCX = "c++-level-1-quyen-1.docx"
doc = docx.Document(DOCX)

# Bảng từ 0 đến 15 là 16 bảng của Chương 00
tbl_borders_xml = f'''
<w:tblBorders {nsdecls("w")}>
    <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
    <w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
    <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
    <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
    <w:insideV w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
</w:tblBorders>
'''

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

fixed_count = 0
for i in range(16):
    tbl = doc.tables[i]
    tblPr = tbl._tbl.find(f'{{{W_NS}}}tblPr')
    if tblPr is not None:
        # Cập nhật tblW w="6800" type="dxa"
        tblW = tblPr.find(f'{{{W_NS}}}tblW')
        if tblW is not None:
            tblW.set(f'{{{W_NS}}}w', '6800')
            tblW.set(f'{{{W_NS}}}type', 'dxa')
            
        # Xóa tblBorders cũ nếu có và gắn tblBorders chuẩn
        old_b = tblPr.find(f'{{{W_NS}}}tblBorders')
        if old_b is not None:
            tblPr.remove(old_b)
            
        new_b = parse_xml(tbl_borders_xml)
        tblPr.append(new_b)
        fixed_count += 1

print(f"Đã cập nhật border và kích thước cho {fixed_count} bảng Sample IO của Chương 00!")

doc.save(DOCX)
print("✅ Lưu file thành công!")
