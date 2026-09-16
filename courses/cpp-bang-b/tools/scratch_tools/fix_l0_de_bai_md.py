import re
from pathlib import Path

# Cập nhật De_Bai.md của 16 bài L0 chuẩn format như các bài mẫu (Dòng 1, Dòng 2, Bullet, Giải thích chuẩn)

L0_UPDATES = {
    "cppb_l0_01_tinh_tong_hai_so": {
        "title": "Tính Tổng Hai Số",
        "boi_canh": "Trong giờ Toán, thầy giáo giao cho mỗi bạn hai số nguyên và yêu cầu tính tổng của chúng. Bạn An muốn viết một chương trình C++ để giải nhanh bài tập này thay vì tính bằng tay.",
        "nhiem_vu": "Cho hai số nguyên $a$ và $b$. Hãy lập trình tính và in ra tổng $a + b$.",
        "input_bullets": [
            "Một dòng duy nhất chứa hai số nguyên $a$ và $b$ ($-10^9 \\le a, b \\le 10^9$), cách nhau bởi khoảng trắng."
        ],
        "output_bullets": [
            "In ra một số nguyên duy nhất là tổng $a + b$."
        ],
        "sample_in": "3 5",
        "sample_out": "8",
        "giai_thich": [
            "Ta có hai số nguyên $a = 3$ và $b = 5$.",
            "Tổng của hai số là: $3 + 5 = 8$.",
            "Chương trình in ra kết quả: 8."
        ],
        "rang_buoc_bullets": [
            "$100\\%$ số test có $-10^9 \\le a, b \\le 10^9$.",
            "Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$."
        ]
    },
    "cppb_l0_02_dien_tich_hinh_chu_nhat": {
        "title": "Diện Tích Hình Chữ Nhật",
        "boi_canh": "Bạn Bình muốn tính diện tích mảnh vườn hình chữ nhật của gia đình để biết cần mua bao nhiêu cây giống. Bạn ấy đã đo được chiều dài và chiều rộng của mảnh vườn và cần một chương trình tính nhanh diện tích.",
        "nhiem_vu": "Cho chiều dài $a$ và chiều rộng $b$ của hình chữ nhật. Hãy lập trình tính và in ra chu vi và diện tích của hình chữ nhật đó.",
        "input_bullets": [
            "Một dòng duy nhất chứa hai số nguyên dương $a$ và $b$ ($1 \\le a, b \\le 10^4$), cách nhau bởi khoảng trắng."
        ],
        "output_bullets": [
            "In ra hai số nguyên trên một dòng, cách nhau bởi khoảng trắng: chu vi $P$ và diện tích $S$ của hình chữ nhật."
        ],
        "sample_in": "5 3",
        "sample_out": "16 15",
        "giai_thich": [
            "Chiều dài $a = 5$, chiều rộng $b = 3$.",
            "Chu vi: $P = 2 \\times (a + b) = 2 \\times (5 + 3) = 2 \\times 8 = 16$.",
            "Diện tích: $S = a \\times b = 5 \\times 3 = 15$.",
            "Kết quả in ra: 16 15."
        ],
        "rang_buoc_bullets": [
            "$100\\%$ số test có $1 \\le a, b \\le 10^4$.",
            "Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$."
        ]
    },
    "cppb_l0_03_trung_binh_ba_so": {
        "title": "Trung Bình Ba Số",
        "boi_canh": "Sau đợt kiểm tra giữa kỳ, cô giáo chấm xong 3 bài thi môn Toán, Văn, Anh của bạn Chi. Cô cần tính điểm trung bình cộng của 3 môn học này và làm tròn đúng 2 chữ số thập phân.",
        "nhiem_vu": "Cho ba số nguyên $a, b, c$. Hãy lập trình tính và in ra giá trị trung bình cộng của ba số, làm tròn đúng 2 chữ số thập phân.",
        "input_bullets": [
            "Một dòng duy nhất chứa ba số nguyên $a, b, c$ ($0 \\le a, b, c \\le 100$), cách nhau bởi khoảng trắng."
        ],
        "output_bullets": [
            "In ra một số thực duy nhất là giá trị trung bình cộng của ba số, định dạng đúng 2 chữ số thập phân."
        ],
        "sample_in": "7 8 9",
        "sample_out": "8.00",
        "giai_thich": [
            "Ba điểm số lần lượt là: $7, 8, 9$.",
            "Tổng điểm là: $7 + 8 + 9 = 24$.",
            "Điểm trung bình cộng: $\\frac{24}{3} = 8.00$."
        ],
        "rang_buoc_bullets": [
            "$100\\%$ số test có $0 \\le a, b, c \\le 100$.",
            "Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$."
        ]
    }
}

for code, data in L0_UPDATES.items():
    p = Path(f"problems/{code}/De_Bai.md")
    lines = [
        f"# {data['title']}",
        "",
        "## Bối cảnh",
        data['boi_canh'],
        "",
        "## Nhiệm vụ",
        data['nhiem_vu'],
        "",
        "## Input"
    ]
    for b in data['input_bullets']:
        lines.append(f"- {b}")
    lines.extend([
        "",
        "## Output"
    ])
    for b in data['output_bullets']:
        lines.append(f"- {b}")
    lines.extend([
        "",
        "## Sample 1",
        "### Input",
        "```text",
        data['sample_in'],
        "```",
        "### Output",
        "```text",
        data['sample_out'],
        "```",
        "",
        "### Giải thích"
    ])
    for g in data['giai_thich']:
        lines.append(g)
    lines.extend([
        "",
        "## Ràng buộc"
    ])
    for b in data['rang_buoc_bullets']:
        lines.append(f"- {b}")
    lines.append("")
    p.write_text("\n".join(lines), encoding="utf-8")
    print(f"Updated {code}/De_Bai.md")
