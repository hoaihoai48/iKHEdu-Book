import zipfile
import shutil
import tempfile
from pathlib import Path
import xml.etree.ElementTree as ET

from make_l0_xml import (
    W_NS, PROBLEMS, clean_latex, format_problem_tag, create_p, create_heading3,
    parse_de_bai, create_source_code_p
)

DOCX_IN = Path("c++-level-1-quyen-1.docx")
DOCX_OUT = Path("c++-level-1-quyen-1.docx")

ET.register_namespace('w', W_NS)
ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')
ET.register_namespace('m', 'http://schemas.openxmlformats.org/officeDocument/2006/math')
ET.register_namespace('v', 'urn:schemas-microsoft-com:vml')
ET.register_namespace('wp', 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing')
ET.register_namespace('a', 'http://schemas.openxmlformats.org/drawingml/2006/main')
ET.register_namespace('pic', 'http://schemas.openxmlformats.org/drawingml/2006/picture')

with zipfile.ZipFile(DOCX_IN) as z:
    doc_xml_bytes = z.read('word/document.xml')

root = ET.fromstring(doc_xml_bytes)
body = root.find(f"{{{W_NS}}}body")

# 1. Tìm vị trí kết thúc của Phụ lục A (ngay trước Heading1 Phụ lục B)
pa_end_idx = -1
for i, child in enumerate(list(body)):
    t = ''.join(r.text or '' for r in child.iter(f"{{{W_NS}}}t"))
    if 'Phụ lục B: Lời giải bài tập tham khảo' in t:
        pa_end_idx = i
        break

if pa_end_idx == -1:
    raise ValueError("Không tìm thấy Heading1 Phụ lục B!")

print(f"Phụ lục B bắt đầu tại index: {pa_end_idx}")

# Chuẩn bị khối XML Bài tập thực hành của Phụ lục A
l0_elements = []

# Tiêu đề mục: Bài tập thực hành (Heading2 màu đỏ #FF0000 theo chuẩn)
p_bt = ET.Element(f"{{{W_NS}}}p")
pPr_bt = ET.SubElement(p_bt, f"{{{W_NS}}}pPr")
pStyle_bt = ET.SubElement(pPr_bt, f"{{{W_NS}}}pStyle")
pStyle_bt.set(f"{{{W_NS}}}val", "Heading2")
sp_bt = ET.SubElement(pPr_bt, f"{{{W_NS}}}spacing")
sp_bt.set(f"{{{W_NS}}}before", "220")
sp_bt.set(f"{{{W_NS}}}after", "60")
rPr_p_bt = ET.SubElement(pPr_bt, f"{{{W_NS}}}rPr")
ET.SubElement(rPr_p_bt, f"{{{W_NS}}}b")
col_p_bt = ET.SubElement(rPr_p_bt, f"{{{W_NS}}}color")
col_p_bt.set(f"{{{W_NS}}}val", "FF0000")

r_bt = ET.SubElement(p_bt, f"{{{W_NS}}}r")
rPr_bt = ET.SubElement(r_bt, f"{{{W_NS}}}rPr")
rf_bt = ET.SubElement(rPr_bt, f"{{{W_NS}}}rFonts")
rf_bt.set(f"{{{W_NS}}}ascii", "Times New Roman")
rf_bt.set(f"{{{W_NS}}}hAnsi", "Times New Roman")
ET.SubElement(rPr_bt, f"{{{W_NS}}}b")
col_bt = ET.SubElement(rPr_bt, f"{{{W_NS}}}color")
col_bt.set(f"{{{W_NS}}}val", "FF0000")
sz_bt = ET.SubElement(rPr_bt, f"{{{W_NS}}}sz")
sz_bt.set(f"{{{W_NS}}}val", "28")
t_bt = ET.SubElement(r_bt, f"{{{W_NS}}}t")
t_bt.text = "Bài tập thực hành"

l0_elements.append(p_bt)

intro_p = create_p("Dưới đây là 16 bài tập lập trình cơ bản bám sát 6 nhóm kỹ năng nền tảng (Biến, Toán tử, Điều kiện, Vòng lặp, Tích lũy, Mảng & Xâu) giúp học sinh rèn luyện tư duy và làm chủ cú pháp C++ chuẩn.", style="BlockText", space_before=60, space_after=120)
l0_elements.append(intro_p)

# Duyệt qua 16 bài tập
for idx, p_info in enumerate(PROBLEMS, 1):
    num_str = f"{idx:02d}"
    code = p_info["code"]
    title = p_info["title"]
    print(f"Generating XML for problem {num_str}: {code}")
    prob_elems = parse_de_bai(code, num_str, title)
    l0_elements.extend(prob_elems)

# Chèn 16 bài tập vào ngay trước Phụ lục B
for elem in reversed(l0_elements):
    body.insert(pa_end_idx, elem)

print(f"Đã chèn {len(l0_elements)} elements cho 16 bài tập L0 vào Phụ lục A.")

# 2. Chèn 3 lời giải mẫu vào Phụ lục B
h2_c01_idx = -1
for i, child in enumerate(list(body)):
    t = ''.join(r.text or '' for r in child.iter(f"{{{W_NS}}}t"))
    if 'Chương 01 — Bài 01: Sắp xếp' in t:
        h2_c01_idx = i
        break

if h2_c01_idx == -1:
    raise ValueError("Không tìm thấy Heading2 Chương 01 trong Phụ lục B!")

sol_elements = []

p_h2_pa = ET.Element(f"{{{W_NS}}}p")
pPr_h2_pa = ET.SubElement(p_h2_pa, f"{{{W_NS}}}pPr")
pStyle_h2_pa = ET.SubElement(pPr_h2_pa, f"{{{W_NS}}}pStyle")
pStyle_h2_pa.set(f"{{{W_NS}}}val", "Heading2")
sp_h2_pa = ET.SubElement(pPr_h2_pa, f"{{{W_NS}}}spacing")
sp_h2_pa.set(f"{{{W_NS}}}before", "220")
sp_h2_pa.set(f"{{{W_NS}}}after", "60")

r_h2_pa = ET.SubElement(p_h2_pa, f"{{{W_NS}}}r")
rPr_h2_pa = ET.SubElement(r_h2_pa, f"{{{W_NS}}}rPr")
rf_h2_pa = ET.SubElement(rPr_h2_pa, f"{{{W_NS}}}rFonts")
rf_h2_pa.set(f"{{{W_NS}}}ascii", "Times New Roman")
rf_h2_pa.set(f"{{{W_NS}}}hAnsi", "Times New Roman")
ET.SubElement(rPr_h2_pa, f"{{{W_NS}}}b")
col_h2_pa = ET.SubElement(rPr_h2_pa, f"{{{W_NS}}}color")
col_h2_pa.set(f"{{{W_NS}}}val", "1E293B")
sz_h2_pa = ET.SubElement(rPr_h2_pa, f"{{{W_NS}}}sz")
sz_h2_pa.set(f"{{{W_NS}}}val", "28")
t_h2_pa = ET.SubElement(r_h2_pa, f"{{{W_NS}}}t")
t_h2_pa.text = "Phụ lục A — Nền tảng C++"

sol_elements.append(p_h2_pa)

for i in [0, 1, 2]:
    p_info = PROBLEMS[i]
    code = p_info["code"]
    title = p_info["title"]
    code_text = Path(f"problems/{code}/solution.cpp").read_text(encoding="utf-8")

    code_tag = format_problem_tag(code)

    h3_p = ET.Element(f"{{{W_NS}}}p")
    pPr_h3 = ET.SubElement(h3_p, f"{{{W_NS}}}pPr")
    pStyle_h3 = ET.SubElement(pPr_h3, f"{{{W_NS}}}pStyle")
    pStyle_h3.set(f"{{{W_NS}}}val", "Heading3")
    sp_h3 = ET.SubElement(pPr_h3, f"{{{W_NS}}}spacing")
    sp_h3.set(f"{{{W_NS}}}before", "180")
    sp_h3.set(f"{{{W_NS}}}after", "60")

    r1 = ET.SubElement(h3_p, f"{{{W_NS}}}r")
    rPr1 = ET.SubElement(r1, f"{{{W_NS}}}rPr")
    rStyle1 = ET.SubElement(rPr1, f"{{{W_NS}}}rStyle")
    rStyle1.set(f"{{{W_NS}}}val", "VerbatimChar")
    rf1 = ET.SubElement(rPr1, f"{{{W_NS}}}rFonts")
    rf1.set(f"{{{W_NS}}}ascii", "Times New Roman")
    rf1.set(f"{{{W_NS}}}hAnsi", "Times New Roman")
    ET.SubElement(rPr1, f"{{{W_NS}}}b")
    col1 = ET.SubElement(rPr1, f"{{{W_NS}}}color")
    col1.set(f"{{{W_NS}}}val", "1E293B")
    sz1 = ET.SubElement(rPr1, f"{{{W_NS}}}sz")
    sz1.set(f"{{{W_NS}}}val", "26")
    t1 = ET.SubElement(r1, f"{{{W_NS}}}t")
    t1.text = code_tag

    r2 = ET.SubElement(h3_p, f"{{{W_NS}}}r")
    rPr2 = ET.SubElement(r2, f"{{{W_NS}}}rPr")
    ET.SubElement(rPr2, f"{{{W_NS}}}b")
    col2 = ET.SubElement(rPr2, f"{{{W_NS}}}color")
    col2.set(f"{{{W_NS}}}val", "1E293B")
    sz2 = ET.SubElement(rPr2, f"{{{W_NS}}}sz")
    sz2.set(f"{{{W_NS}}}val", "26")
    t2 = ET.SubElement(r2, f"{{{W_NS}}}t")
    t2.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t2.text = f" — {title}"

    sol_elements.append(h3_p)
    sol_elements.append(create_source_code_p(code_text))

p_note = ET.Element(f"{{{W_NS}}}p")
pPr_note = ET.SubElement(p_note, f"{{{W_NS}}}pPr")
sp_note = ET.SubElement(pPr_note, f"{{{W_NS}}}spacing")
sp_note.set(f"{{{W_NS}}}before", "160")
sp_note.set(f"{{{W_NS}}}after", "280")
r_note = ET.SubElement(p_note, f"{{{W_NS}}}r")
rPr_note = ET.SubElement(r_note, f"{{{W_NS}}}rPr")
ET.SubElement(rPr_note, f"{{{W_NS}}}i")
sz_note = ET.SubElement(rPr_note, f"{{{W_NS}}}sz")
sz_note.set(f"{{{W_NS}}}val", "22")
t_note = ET.SubElement(r_note, f"{{{W_NS}}}t")
t_note.text = "Các bài tập còn lại có phương pháp và cấu trúc tương tự, học sinh tự suy luận và cài đặt."
sol_elements.append(p_note)

for elem in reversed(sol_elements):
    body.insert(h2_c01_idx, elem)

print(f"Đã chèn {len(sol_elements)} elements lời giải L0 vào Phụ lục B.")

# Ghi lại file docx
new_xml_bytes = ET.tostring(root, encoding='utf-8', xml_declaration=True)

with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp:
    tmp_path = Path(tmp.name)

shutil.copyfile(DOCX_IN, tmp_path)

with zipfile.ZipFile(DOCX_IN, 'r') as zin, zipfile.ZipFile(tmp_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        if item.filename == 'word/document.xml':
            zout.writestr(item, new_xml_bytes)
        else:
            zout.writestr(item, zin.read(item.filename))

shutil.move(tmp_path, DOCX_OUT)
print(f"✅ Hoàn tất cập nhật OpenXML chuẩn đẹp cho {DOCX_OUT}!")
