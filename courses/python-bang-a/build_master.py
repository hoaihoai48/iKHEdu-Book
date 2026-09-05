#!/usr/bin/env python3
"""Build the canonical all-in-one Markdown master for Python Bang A."""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
LESSONS_DIR = BASE_DIR / "lessons"
MASTER_FILE = BASE_DIR / "MASTER_ALL_LESSONS.md"
AUDIT_FILE = BASE_DIR / "CURRICULUM_AUDIT.md"
PATTERNS_FILE = BASE_DIR / "ALGORITHM_PATTERNS.md"


def lesson_number(path):
    match = re.search(r"lesson-(\d+)", path.name)
    return int(match.group(1)) if match else 0


def read_markdown(path):
    return path.read_text(encoding="utf-8").strip()


def lesson_title(path):
    content_file = next(path.glob("Lesson*_Production_Content.md"), None)
    if content_file and content_file.exists():
        for line in content_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("# Bài"):
                return line[2:].strip()
    return path.name


def normalize_assets(content):
    # lessons dùng "assets/..." (relative lesson dir, vốn gãy) hoặc
    # "../../assets/..." (đúng relative lesson dir);
    # master nằm cùng cấp assets/ nên chuẩn hóa về "assets/..."
    content = content.replace("../../assets/", "assets/")
    return content


def student_content(content):
    # GIỮ NGUYÊN mã P0..P5 (tránh nhãn kép "Cơ bản (Khởi động)").
    # Chỉ chuẩn hóa thuật ngữ Anh -> Việt.
    return content.replace("Core ", "Bắt buộc ").replace("Challenge ", "Thử thách ")


def build_master():
    lessons = sorted(
        (path for path in LESSONS_DIR.iterdir() if path.is_dir()),
        key=lesson_number,
    )
    output = [
        "# iKHEDU PYTHON BẢNG A — TỔNG HỢP NỘI DUNG 6 CHƯƠNG",
        "",
        "> File tổng hợp tự động toàn bộ nội dung lesson của khóa Python Bảng A — Level 1.",
        "> Nguồn canonical vẫn là các file trong `lessons/`; không chỉnh sửa trực tiếp file này.",
        "",
        "## MỤC LỤC TỔNG QUAN",
        "",
    ]

    chapters = {
        1: "TÍNH TOÁN CƠ BẢN",
        2: "CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP",
        3: "BÀI TOÁN SỐ HỌC & TÁCH CHỮ SỐ",
        4: "DANH SÁCH (LIST) & THỐNG KÊ",
        5: "XỬ LÝ CHUỖI KÝ TỰ",
        6: "LUYỆN THI",
    }
    lesson_chapter = {
        1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3,
        9: 3, 10: 3, 11: 4, 12: 4, 13: 5, 14: 5, 15: 6, 16: 6,
    }
    for chapter_number, chapter_title in chapters.items():
        output.append(f"### Chương {chapter_number}: {chapter_title}")
        for lesson in lessons:
            if lesson_chapter.get(lesson_number(lesson)) == chapter_number:
                output.append(f"- {lesson_title(lesson)}")

    output.extend(
        [
            "",
            "=" * 80,
            "# PHẦN I — CURRICULUM AUDIT VÀ ALGORITHM PATTERNS",
            "=" * 80,
            "",
        ]
    )
    if AUDIT_FILE.exists():
        output.extend([student_content(read_markdown(AUDIT_FILE)), ""])
    if PATTERNS_FILE.exists():
        output.extend([student_content(read_markdown(PATTERNS_FILE)), ""])

    output.extend(
        [
            "",
            "=" * 80,
            "# PHẦN II — NỘI DUNG CHI TIẾT",
            "=" * 80,
            "",
        ]
    )

    current_chapter = None
    for lesson in lessons:
        chapter_number = lesson_chapter.get(lesson_number(lesson), 1)
        content_file = next(lesson.glob("Lesson*_Production_Content.md"), None)
        exercise_file = lesson / "Bai_Tap.md"
        if chapter_number != current_chapter:
            current_chapter = chapter_number
            output.extend(
                [
                    "",
                    "=" * 80,
                    f"# CHƯƠNG {chapter_number:02d}: {chapters[chapter_number]}",
                    "=" * 80,
                    "",
                ]
            )
        output.extend(
            [
                "",
                "-" * 80,
                f"<!-- {lesson_title(lesson)} -->",
                "-" * 80,
                "",
            ]
        )
        if content_file and content_file.exists():
            output.extend(
                [
                    "## Lý thuyết và Concept Quiz",
                    "",
                    normalize_assets(student_content(read_markdown(content_file))),
                    "",
                ]
            )
        if exercise_file.exists():
            output.extend(
                [
                    "## Bài tập lesson",
                    "",
                    normalize_assets(student_content(read_markdown(exercise_file))),
                    "",
                ]
            )

    MASTER_FILE.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
    print(f"Built {MASTER_FILE} from {len(lessons)} lessons")


if __name__ == "__main__":
    build_master()
