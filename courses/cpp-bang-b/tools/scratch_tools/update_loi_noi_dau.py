import docx
from docx.shared import Pt, RGBColor

DOCX = "c++-level-1-quyen-1.docx"
doc = docx.Document(DOCX)

# Cập nhật đoạn P[3] trong Lời nói đầu:
# "Phần nội dung này gồm Chương 00 (Khởi động & Ôn tập 16 bài toán nền tảng) cùng 4 Chương trọng tâm (Chương 01 đến Chương 04) với 12 Bài học và 205 bài toán thực hành, trang bị toàn diện kỹ thuật lập trình C++, mảng, con trỏ, cửa sổ trượt, tìm kiếm nhị phân, bit, số học, đệ quy và quay lui."

p3 = doc.paragraphs[3]
print("Old P[3]:", p3.text)

new_text = "Phần nội dung này gồm Chương 00 (Ôn tập & rèn luyện 16 bài toán nền tảng C++) cùng 4 Chương trọng tâm (Chương 01 đến Chương 04) với 12 Bài học và tổng cộng 205 bài toán thực hành chuẩn mực, trang bị toàn diện kỹ thuật lập trình C++, mảng, con trỏ, cửa sổ trượt, tìm kiếm nhị phân, bit, số học, đệ quy và quay lui."

# Giữ nguyên cấu trúc run và format
for r in p3.runs:
    r.text = ""

run = p3.runs[0] if p3.runs else p3.add_run()
run.text = new_text
run.font.size = Pt(14)

print("New P[3]:", p3.text)

doc.save(DOCX)
print("✅ Đã cập nhật Lời nói đầu thành công!")
