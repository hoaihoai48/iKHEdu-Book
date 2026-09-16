import docx
from docx.shared import Pt, Inches, RGBColor
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import xml.etree.ElementTree as ET

DOCX_IN = "c++-level-1-quyen-1.docx"
DOCX_OUT = "c++-level-1-quyen-1.docx"

doc = docx.Document(DOCX_IN)
body_elem = doc._body._element

# 1. Tìm các phần tử mốc:
# - Heading 1 của Chương 00 hiện tại: P11
# - Paragraph 'TÓM TẮT MỘT TRANG' hoặc 'Bài tập thực hành' ở Chương 00
# - Heading 1 của Chương 01: P386
# - Heading 1 của Phụ lục B: P3630
# - Mục lục: P3736

h1_ch00 = None
p_bt_th = None
h1_ch01 = None
h1_pb = None
toc_ch00_p = None
toc_pb_p = None

for p in doc.paragraphs:
    t = p.text.strip()
    if p.style.name == "Heading 1" and "CHƯƠNG 00" in t:
        h1_ch00 = p
    elif p.text.strip() == "Bài tập thực hành" and p.style.name == "Heading 2" and h1_ch01 is None and h1_ch00 is not None:
        p_bt_th = p
    elif p.style.name == "Heading 1" and "CHƯƠNG 01" in t:
        h1_ch01 = p
    elif p.style.name == "Heading 1" and "Phụ lục B: Lời giải bài tập tham khảo" in t:
        h1_pb = p
    elif "CHƯƠNG 00: NỀN TẢNG LẬP TRÌNH C++" in t and p._p.find('.//w:hyperlink', {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}) is not None:
        toc_ch00_p = p
    elif "Phụ lục B: Lời giải bài tập tham khảo" in t and p._p.find('.//w:hyperlink', {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}) is not None:
        toc_pb_p = p

print("Found anchors:")
print("- h1_ch00:", h1_ch00.text if h1_ch00 else "NONE")
print("- p_bt_th:", p_bt_th.text if p_bt_th else "NONE")
print("- h1_ch01:", h1_ch01.text[:30] if h1_ch01 else "NONE")
print("- h1_pb:", h1_pb.text if h1_pb else "NONE")
print("- toc_ch00_p:", toc_ch00_p.text if toc_ch00_p else "NONE")
print("- toc_pb_p:", toc_pb_p.text if toc_pb_p else "NONE")

all_body_children = list(body_elem)
idx_h1_ch00 = all_body_children.index(h1_ch00._p)
idx_bt_th = all_body_children.index(p_bt_th._p)
idx_h1_ch01 = all_body_children.index(h1_ch01._p)
idx_h1_pb = all_body_children.index(h1_pb._p)

print(f"Indices: ch00={idx_h1_ch00}, bt_th={idx_bt_th}, ch01={idx_h1_ch01}, pb={idx_h1_pb}")

# Khối lý thuyết = từ ngay sau h1_ch00 đến ngay trước p_bt_th (tức là all_body_children[idx_h1_ch00 + 1 : idx_bt_th])
theory_elements = all_body_children[idx_h1_ch00 + 1 : idx_bt_th]
print(f"Số element lý thuyết cần chuyển về Phụ lục A: {len(theory_elements)}")

# 2. Tạo Heading 1 mới cho "Phụ lục A: Nền tảng C++" trước Phụ lục B
pa_heading_xml = f'''
<w:p {nsdecls("w")}>
    <w:pPr>
        <w:pStyle w:val="Heading1"/>
        <w:pageBreakBefore/>
        <w:spacing w:before="320"/>
    </w:pPr>
    <w:bookmarkStart w:id="356" w:name="bm_sec_18"/>
    <w:bookmarkStart w:id="357" w:name="phụ-lục-a-nền-tảng-c"/>
    <w:r>
        <w:rPr>
            <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
            <w:b/>
            <w:color w:val="1E293B"/>
            <w:sz w:val="31"/>
        </w:rPr>
        <w:t>Phụ lục A: Nền tảng C++</w:t>
    </w:r>
    <w:bookmarkEnd w:id="356"/>
</w:p>
'''
pa_heading_elem = parse_xml(pa_heading_xml)

# Chèn pa_heading_elem trước h1_pb
h1_pb._p.addprevious(pa_heading_elem)

# Di chuyển toàn bộ theory_elements về sau pa_heading_elem (ngay trước h1_pb)
for elem in theory_elements:
    body_elem.remove(elem)
    h1_pb._p.addprevious(elem)

print("Đã chuyển toàn bộ lý thuyết về Phụ lục A (trước Phụ lục B) thành công!")

# 3. Ở Chương 00 đầu sách:
# Sửa tiêu đề và lời dẫn cho rõ ràng là chương bài tập khởi động / ôn tập:
# h1_ch00:
# CHƯƠNG 00
# BÀI TẬP ÔN TẬP & NỀN TẢNG C++
h1_ch00.text = ""
pPr_ch00 = h1_ch00._p.get_or_add_pPr()
if pPr_ch00.find(qn('w:pageBreakBefore')) is None:
    pPr_ch00.append(OxmlElement('w:pageBreakBefore'))
sp = pPr_ch00.find(qn('w:spacing'))
if sp is not None:
    sp.set(qn('w:after'), '100')
jc = pPr_ch00.find(qn('w:jc'))
if jc is None:
    jc = OxmlElement('w:jc')
    pPr_ch00.append(jc)
jc.set(qn('w:val'), 'center')

r_ch00_1 = h1_ch00.add_run("CHƯƠNG 00")
r_ch00_1.bold = True
r_ch00_1.font.name = "Times New Roman"
r_ch00_1.font.size = Pt(18)
r_ch00_1.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

r_br = h1_ch00.add_run()
r_br.add_break()

r_ch00_2 = h1_ch00.add_run("BÀI TẬP ÔN TẬP & NỀN TẢNG C++")
r_ch00_2.bold = True
r_ch00_2.font.name = "Times New Roman"
r_ch00_2.font.size = Pt(18)
r_ch00_2.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

# Xóa thẻ "Bài tập thực hành" (p_bt_th) vì cả Chương 00 chính là tập bài tập rồi, hoặc giữ lại lời dẫn ngắn gọn
# Thay vì để Heading 2 "Bài tập thực hành" lặp lại, đổi thành Heading 2: "Các bài toán thực hành nền tảng"
p_bt_th.text = "16 Bài tập thực hành nền tảng"
p_bt_th.style = "Heading 2"
p_bt_th.runs[0].font.color.rgb = RGBColor(0xFF, 0x00, 0x00)
p_bt_th.runs[0].bold = True

# 4. Cập nhật Mục lục:
# - Sửa dòng Chương 00 trong TOC: CHƯƠNG 00: BÀI TẬP ÔN TẬP & NỀN TẢNG C++
# - Thêm lại dòng "Phụ lục A: Nền tảng C++" trước "Phụ lục B: Lời giải bài tập tham khảo" trong TOC
for r in toc_ch00_p.runs:
    r.text = "CHƯƠNG 00: BÀI TẬP ÔN TẬP & NỀN TẢNG C++"

toc_pa_xml = f'''
<w:p {nsdecls("w")}>
    <w:pPr>
        <w:spacing w:before="120" w:after="30" w:line="276" w:lineRule="auto"/>
        <w:jc w:val="both"/>
    </w:pPr>
    <w:hyperlink w:anchor="bm_sec_18">
        <w:r>
            <w:rPr>
                <w:b/>
                <w:color w:val="0F2A44"/>
                <w:sz w:val="22"/>
            </w:rPr>
            <w:t>Phụ lục A: Nền tảng C++</w:t>
        </w:r>
    </w:hyperlink>
</w:p>
'''
toc_pa_elem = parse_xml(toc_pa_xml)
toc_pb_p._p.addprevious(toc_pa_elem)

print("Đã cập nhật mục lục với cả Chương 00 ở đầu và Phụ lục A ở cuối!")

# 5. Lưu docx
doc.save(DOCX_OUT)
print("✅ Lưu file docx thành công!")

# Verify
doc_check = docx.Document(DOCX_OUT)
for i, p in enumerate(doc_check.paragraphs):
    if p.style.name.startswith('Heading 1'):
        print(f"H1 [{i}]: {repr(p.text)}")
