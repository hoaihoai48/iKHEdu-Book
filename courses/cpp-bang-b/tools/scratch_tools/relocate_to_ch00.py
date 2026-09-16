import docx
from docx.shared import Pt, Inches, RGBColor
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import xml.etree.ElementTree as ET

DOCX_IN = "c++-level-1-quyen-1.docx"
DOCX_OUT = "c++-level-1-quyen-1.docx"

doc = docx.Document(DOCX_IN)
body_elem = doc._body._element

# 1. Xác định phạm vi các phần tử thuộc Phụ lục A (từ Heading 1 Phụ lục A đến ngay trước Heading 1 Phụ lục B)
pa_start_p = None
pb_start_p = None
p_c01_heading = None
toc_heading_p = None
toc_c01_p = None
toc_pa_p = None

for p in doc.paragraphs:
    t = p.text.strip()
    if p.style.name == "Heading 1" and "CHƯƠNG 01" in t:
        p_c01_heading = p
    elif p.style.name == "Heading 1" and t == "Phụ lục A: Nền tảng C++":
        pa_start_p = p
    elif p.style.name == "Heading 1" and t == "Phụ lục B: Lời giải bài tập tham khảo":
        pb_start_p = p
    elif p.style.name == "Heading 1" and t == "Mục lục":
        toc_heading_p = p
    elif "CHƯƠNG 01: THUẬT TOÁN SẮP XẾP" in t and p._p.find('.//w:hyperlink', {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}) is not None:
        toc_c01_p = p
    elif "Phụ lục A: Nền tảng C++" in t and p._p.find('.//w:hyperlink', {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}) is not None:
        toc_pa_p = p

print("Found elements:")
print("- Chương 01 heading:", p_c01_heading.text[:40] if p_c01_heading else "NOT FOUND")
print("- Phụ lục A heading:", pa_start_p.text if pa_start_p else "NOT FOUND")
print("- Phụ lục B heading:", pb_start_p.text if pb_start_p else "NOT FOUND")
print("- TOC C01 entry:", toc_c01_p.text if toc_c01_p else "NOT FOUND")
print("- TOC PA entry:", toc_pa_p.text if toc_pa_p else "NOT FOUND")

if not (p_c01_heading and pa_start_p and pb_start_p and toc_c01_p and toc_pa_p):
    raise ValueError("Thiếu các mốc quan trọng trong document!")

# Thu thập tất cả các phần tử (paragraphs + tables) từ pa_start_p._p đến pb_start_p._p (không bao gồm pb_start_p._p)
all_body_children = list(body_elem)
start_idx = all_body_children.index(pa_start_p._p)
end_idx = all_body_children.index(pb_start_p._p)

print(f"Index trong body_elem: start_idx={start_idx}, end_idx={end_idx}, số elements={end_idx - start_idx}")

ch00_elements = all_body_children[start_idx:end_idx]

# 2. Thay đổi nội dung của pa_start_p thành CHƯƠNG 00: NỀN TẢNG LẬP TRÌNH C++
# Format Heading 1 chuẩn như Chương 01:
# Đặt text: CHƯƠNG 00\nNỀN TẢNG LẬP TRÌNH C++
pa_start_p.text = ""
pPr = pa_start_p._p.get_or_add_pPr()

# Đảm bảo có pageBreakBefore
if pPr.find(qn('w:pageBreakBefore')) is None:
    pPr.append(OxmlElement('w:pageBreakBefore'))

# Spacing và jc
sp = pPr.find(qn('w:spacing'))
if sp is not None:
    sp.set(qn('w:after'), '100')
    sp.set(qn('w:before'), '0')
jc = pPr.find(qn('w:jc'))
if jc is None:
    jc = OxmlElement('w:jc')
    pPr.append(jc)
jc.set(qn('w:val'), 'center')

# Thêm 2 dòng run
r1 = pa_start_p.add_run("CHƯƠNG 00")
r1.bold = True
r1.font.name = "Times New Roman"
r1.font.size = Pt(18)
r1.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

r_br = pa_start_p.add_run()
r_br.add_break()

r2 = pa_start_p.add_run("NỀN TẢNG LẬP TRÌNH C++")
r2.bold = True
r2.font.name = "Times New Roman"
r2.font.size = Pt(18)
r2.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

# Đặt bookmark bm_sec_18 (hoặc giữ nguyên bm_sec_18 để hyperlink TOC trỏ tới)
# 3. Di chuyển ch00_elements lên trước p_c01_heading._p
for elem in ch00_elements:
    # remove from current location
    body_elem.remove(elem)
    # insert before p_c01_heading._p
    p_c01_heading._p.addprevious(elem)

print("Đã di chuyển thành công khối Chương 00 lên trước Chương 01!")

# 4. Cập nhật Mục lục:
# Xóa dòng TOC của Phụ lục A cũ
body_elem.remove(toc_pa_p._p)

# Tạo dòng TOC mới cho Chương 00 và chèn ngay trước dòng Chương 01 trong Mục lục
# Format của TOC Chương:
# <w:p>
#   <w:pPr><w:spacing w:before="180" w:line="276" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr>
#   <w:hyperlink w:anchor="bm_sec_18">
#     <w:r><w:rPr><w:b/><w:color w:val="0F2A44"/><w:sz w:val="23"/></w:rPr><w:t>CHƯƠNG 00: NỀN TẢNG LẬP TRÌNH C++</w:t></w:r>
#   </w:hyperlink>
# </w:p>
toc_ch00_xml = f'''
<w:p {nsdecls("w")}>
    <w:pPr>
        <w:spacing w:before="180" w:line="276" w:lineRule="auto"/>
        <w:jc w:val="both"/>
    </w:pPr>
    <w:hyperlink w:anchor="bm_sec_18">
        <w:r>
            <w:rPr>
                <w:b/>
                <w:color w:val="0F2A44"/>
                <w:sz w:val="23"/>
            </w:rPr>
            <w:t>CHƯƠNG 00: NỀN TẢNG LẬP TRÌNH C++</w:t>
        </w:r>
    </w:hyperlink>
</w:p>
'''
toc_ch00_elem = parse_xml(toc_ch00_xml)
toc_c01_p._p.addprevious(toc_ch00_elem)

# Đồng thời sửa lại tiêu đề trong Lời giải mẫu ở Phụ lục B: "Phụ lục A — Nền tảng C++" -> "Chương 00 — Nền tảng C++"
for p in doc.paragraphs:
    if "Phụ lục A — Nền tảng C++" in p.text:
        p.text = "Chương 00 — Nền tảng C++"
        p.style = 'Heading 2'
        p.runs[0].bold = True
        p.runs[0].font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        p.runs[0].font.size = Pt(14)
        print("Đã cập nhật tiêu đề mục lời giải trong Phụ lục B thành: Chương 00 — Nền tảng C++")

# Lưu lại file
doc.save(DOCX_OUT)
print("✅ Hoàn tất chuyển Chương 00 lên đầu và cập nhật Mục lục!")

# Verify lại
doc_check = docx.Document(DOCX_OUT)
print(f"Verify paragraphs: {len(doc_check.paragraphs)}")
for i, p in enumerate(doc_check.paragraphs):
    if p.style.name.startswith('Heading 1'):
        print(f"H1 [{i}]: {repr(p.text)}")
