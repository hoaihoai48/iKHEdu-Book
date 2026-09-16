import docx
from docx.shared import Pt, Inches, RGBColor
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import xml.etree.ElementTree as ET

DOCX = "c++-level-1-quyen-1.docx"
doc = docx.Document(DOCX)

# 1. P[11] là Tiêu đề Chương 00
# Format chuẩn như Chương 01:
# CHƯƠNG 00
# ÔN TẬP & NỀN TẢNG LẬP TRÌNH C++
p11 = doc.paragraphs[11]
p11.text = ""
pPr11 = p11._p.get_or_add_pPr()
if pPr11.find(qn('w:pageBreakBefore')) is None:
    pPr11.append(OxmlElement('w:pageBreakBefore'))
sp11 = pPr11.find(qn('w:spacing'))
if sp11 is not None:
    sp11.set(qn('w:after'), '100')
    sp11.set(qn('w:before'), '0')
jc11 = pPr11.find(qn('w:jc'))
if jc11 is None:
    jc11 = OxmlElement('w:jc')
    pPr11.append(jc11)
jc11.set(qn('w:val'), 'center')

r1 = p11.add_run("CHƯƠNG 00")
r1.bold = True
r1.font.name = "Times New Roman"
r1.font.size = Pt(18)
r1.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

r_br = p11.add_run()
r_br.add_break()

r2 = p11.add_run("ÔN TẬP & NỀN TẢNG LẬP TRÌNH C++")
r2.bold = True
r2.font.name = "Times New Roman"
r2.font.size = Pt(18)
r2.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

# 2. P[12] Chuyển thành Heading 1 có gạch chân "Bài 00: Ôn tập kỹ năng lập trình cơ bản"
# Như các bài khác: <w:pPr><w:pStyle w:val="Heading1"/><w:spacing w:before="200"/><w:rPr><w:u w:val="single"/></w:rPr></w:pPr>
p12 = doc.paragraphs[12]
p12.text = ""
p12.style = "Heading 1"
pPr12 = p12._p.get_or_add_pPr()
sp12 = pPr12.find(qn('w:spacing'))
if sp12 is None:
    sp12 = OxmlElement('w:spacing')
    pPr12.append(sp12)
sp12.set(qn('w:before'), '200')
sp12.set(qn('w:after'), '60')

r_b00 = p12.add_run("Bài 00: Ôn tập kỹ năng lập trình cơ bản")
r_b00.bold = True
r_b00.font.name = "Times New Roman"
r_b00.font.size = Pt(15.5) # 31 dxa
r_b00.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
r_b00.font.underline = True

# 3. P[13] là Lời dẫn Block Text:
# Giữ nguyên nội dung, đảm bảo style='Block Text'
p13 = doc.paragraphs[13]
p13.style = 'Block Text'
p13.paragraph_format.space_before = Pt(4)
p13.paragraph_format.space_after = Pt(10)

# 4. Ngay sau P[13], chèn Heading 2 màu đỏ chuẩn "Bài tập thực hành"
# Format chuẩn giống hệt Bài tập thực hành của Bài 01:
# <w:pPr>
#   <w:pStyle w:val="Heading2"/>
#   <w:spacing w:before="220" w:after="60"/>
#   <w:rPr><w:b/><w:color w:val="FF0000"/></w:rPr>
# </w:pPr>
# <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:b/><w:color w:val="FF0000"/><w:sz w:val="28"/></w:rPr><w:t>Bài tập thực hành</w:t></w:r>
p_target_first_prob = doc.paragraphs[14] # Hiện tại là Bài 01

p_bt_red = doc.add_paragraph(style='Heading 2')
p_bt_red.paragraph_format.space_before = Pt(11)
p_bt_red.paragraph_format.space_after = Pt(3)
r_red = p_bt_red.add_run("Bài tập thực hành")
r_red.bold = True
r_red.font.name = "Times New Roman"
r_red.font.size = Pt(14)
r_red.font.color.rgb = RGBColor(0xFF, 0x00, 0x00)

p_target_first_prob._p.addprevious(p_bt_red._p)

print("Đã chèn Heading 2 'Bài tập thực hành' màu đỏ chuẩn xác!")

# 5. Cập nhật Mục lục (TOC):
# Cần hiển thị chuẩn đồng bộ:
# CHƯƠNG 00: ÔN TẬP & NỀN TẢNG LẬP TRÌNH C++
# •  Bài 00: Ôn tập kỹ năng lập trình cơ bản
# CHƯƠNG 01: THUẬT TOÁN SẮP XẾP & KỸ THUẬT MẢNG
# •  Bài 01: Thuật toán sắp xếp
# ...
toc_ch00 = None
toc_ch01 = None

for p in doc.paragraphs:
    t = p.text.strip()
    if "CHƯƠNG 00" in t and p._p.find('.//w:hyperlink', {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}) is not None:
        toc_ch00 = p
    elif "CHƯƠNG 01" in t and p._p.find('.//w:hyperlink', {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}) is not None:
        toc_ch01 = p

if toc_ch00 and toc_ch01:
    # Update toc_ch00 text
    for r in toc_ch00.runs:
        r.text = "CHƯƠNG 00: ÔN TẬP & NỀN TẢNG LẬP TRÌNH C++"
    
    # Check if bullet Bài 00 already exists
    has_b00_bullet = False
    for p in doc.paragraphs:
        if "Bài 00: Ôn tập kỹ năng" in p.text and p._p.find('.//w:hyperlink', {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}) is not None:
            has_b00_bullet = True
            break
            
    if not has_b00_bullet:
        toc_b00_xml = f'''
        <w:p {nsdecls("w")}>
            <w:pPr>
                <w:spacing w:before="20" w:after="30" w:line="276" w:lineRule="auto"/>
                <w:ind w:left="280"/>
                <w:jc w:val="both"/>
            </w:pPr>
            <w:hyperlink w:anchor="bm_sec_18">
                <w:r>
                    <w:rPr>
                        <w:color w:val="1A4A6B"/>
                        <w:sz w:val="21"/>
                    </w:rPr>
                    <w:t>•  Bài 00: Ôn tập kỹ năng lập trình cơ bản</w:t>
                </w:r>
            </w:hyperlink>
        </w:p>
        '''
        toc_b00_elem = parse_xml(toc_b00_xml)
        toc_ch01._p.addprevious(toc_b00_elem)
        print("Đã thêm bullet Bài 00 vào Mục lục đồng bộ 100%!")

# 6. Lưu file
doc.save(DOCX)
print("✅ Đồng bộ format Chương 00 thành công!")
