import os
import re
import shutil
from pathlib import Path

PY_PROBLEMS_DIR = Path("courses/python-bang-a/problems")
SCA_PROBLEMS_DIR = Path("courses/scratch-bang-a/problems")
SCA_PROBLEMS_DIR.mkdir(parents=True, exist_ok=True)

MAPPING = [
    ("sca_l05", ["pya_l03"]),
    ("sca_l06", ["pya_l04", "pya_l05", "pya_l06"]),
    ("sca_l07", ["pya_l07"]),
    ("sca_l08", ["pya_l08"]),
    ("sca_l09", ["pya_l09"]),
    ("sca_l10", ["pya_l10"]),
    ("sca_l11", ["pya_l11"]),
    ("sca_l12", ["pya_l12"]),
    ("sca_l13", ["pya_l16"]),
    ("sca_l14", ["pya_l17"]),
    ("sca_l15", ["pya_l13"]),
    ("sca_l16", ["pya_l14", "pya_l15"]),
]

LESSON_THEMES = {
    "sca_l05": "Phép Chia Nguyên, Chia Dư & Luỹ Thừa",
    "sca_l06": "Cấu Trúc Rẽ Nhánh & Điều Kiện Logic",
    "sca_l07": "Vòng Lặp Đếm Lần & Biến Đếm",
    "sca_l08": "Vòng Lặp Cho Đến Khi & Biến Cờ",
    "sca_l09": "Quy Luật Dãy Số & Tam Giác Số",
    "sca_l10": "Kỹ Thuật Tách Chữ Số & Số Đặc Biệt",
    "sca_l11": "Ước Số, Bội Số & Số Nguyên Tố",
    "sca_l12": "Đếm Số Theo Quy Luật & Bài Toán Tổ Hợp",
    "sca_l13": "Danh Sách (List) & Thao Tác Cơ Bản",
    "sca_l14": "Thống Kê Danh Sách & Thuật Toán Sắp Xếp",
    "sca_l15": "Chuỗi Ký Tự, Độ Dài & Trích Xuất",
    "sca_l16": "Duyệt Chuỗi Ký Tự, Biến Đổi & Tách Từ",
}

def convert_markdown_for_scratch(text: str, theme: str) -> str:
    # Convert Python terminology to Scratch terminology
    t = text
    t = t.replace("Python Bảng A", "Scratch Bảng A")
    t = t.replace("nền tảng Python", "nền tảng Scratch")
    t = t.replace("Nền Tảng Python", "Nền Tảng Scratch")
    t = t.replace("lệnh print", "khối nói")
    t = t.replace("lệnh `print`", "khối lệnh `nói`")
    t = t.replace("lệnh `input`", "khối lệnh `hỏi và đợi`")
    t = t.replace("input()", "câu trả lời")
    t = t.replace("int(input())", "câu trả lời")
    t = t.replace("khối hỏi và đợi", "hỏi và đợi")
    t = t.replace("in ra màn hình", "nhân vật nói ra màn hình")
    return t

def port_all():
    total_ported = 0
    for sca_prefix, py_prefixes in MAPPING:
        theme = LESSON_THEMES.get(sca_prefix, "Scratch Bảng A")
        py_dirs = []
        for pref in py_prefixes:
            matching = sorted([d for d in os.listdir(PY_PROBLEMS_DIR) if d.startswith(pref + "_") and os.path.isdir(PY_PROBLEMS_DIR / d)])
            py_dirs.extend(matching)
        
        print(f"Porting {len(py_dirs)} problems to {sca_prefix}...")
        for idx, py_name in enumerate(py_dirs, 1):
            # Extract suffix
            # py_name is e.g. pya_l03_p01_hinh_vuong -> name_part = hinh_vuong
            parts = py_name.split("_")
            name_part = "_".join(parts[3:]) if len(parts) >= 4 else "_".join(parts[2:])
            sca_name = f"{sca_prefix}_p{idx:02d}_{name_part}"
            sca_path = SCA_PROBLEMS_DIR / sca_name
            sca_path.mkdir(parents=True, exist_ok=True)
            
            # Copy and convert De_Bai.md
            src_de_bai = PY_PROBLEMS_DIR / py_name / "De_Bai.md"
            dst_de_bai = sca_path / "De_Bai.md"
            if src_de_bai.exists():
                content = src_de_bai.read_text(encoding="utf-8")
                converted = convert_markdown_for_scratch(content, theme)
                dst_de_bai.write_text(converted, encoding="utf-8")
            
            # Copy and convert Huong_Dan_Giang_Day.md
            src_hd = PY_PROBLEMS_DIR / py_name / "Huong_Dan_Giang_Day.md"
            dst_hd = sca_path / "Huong_Dan_Giang_Day.md"
            if src_hd.exists():
                hd_content = src_hd.read_text(encoding="utf-8")
                converted_hd = convert_markdown_for_scratch(hd_content, theme)
                dst_hd.write_text(converted_hd, encoding="utf-8")
                
            total_ported += 1
            
    print(f"SUCCESS: Ported {total_ported} problem packages.")

if __name__ == "__main__":
    port_all()
