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


def student_content(content):
    replacements = {
        "P0": "Cơ bản",
        "P1": "Cơ bản",
        "P2": "Luyện tập",
        "P3": "Luyện tập",
        "P4": "Vận dụng",
        "P5": "Thử thách",
    }
    for source, target in replacements.items():
        content = re.sub(rf"(?<![A-Z0-9]){source}(?![A-Z0-9])", target, content)
    return content.replace("Core ", "Bắt buộc ").replace("Challenge ", "Thử thách ")


def build_master():
    lessons = sorted(
        (path for path in LESSONS_DIR.iterdir() if path.is_dir()),
        key=lesson_number,
    )
    output = [
        "# iKHEDU PYTHON BẢNG A — TỔNG HỢP NỘI DUNG 7 CHƯƠNG",
        "",
        "> File tổng hợp tự động toàn bộ nội dung lesson của khóa Python Bảng A — Level 1.",
        "> Nguồn canonical vẫn là các file trong `lessons/`; không chỉnh sửa trực tiếp file này.",
        "",
        "## MỤC LỤC TỔNG QUAN",
        "",
    ]

    chapters = {
        1: "TÍNH TOÁN CƠ BẢN",
        2: "TƯ DUY RẼ NHÁNH & ĐIỀU KIỆN LOGIC",
        3: "VÒNG LẶP",
        4: "BÀI TOÁN SỐ HỌC",
        5: "DANH SÁCH (LIST)",
        6: "XỬ LÝ CHUỖI & KÝ TỰ",
        7: "LUYỆN ĐỀ THI",
    }
    lesson_chapter = {
        1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4,
        9: 4, 10: 4, 11: 5, 12: 5, 13: 6, 14: 6, 15: 7, 16: 7,
    }
    for chapter_number, chapter_title in chapters.items():
        output.append(f"### Chương {chapter_number}: {chapter_title}")
        for lesson in lessons:
            if lesson_chapter.get(lesson_number(lesson)) == chapter_number:
                output.append(f"- Bài {lesson_number(lesson):02d}: {lesson.name}")

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
                f"<!-- Bài {lesson_number(lesson):02d}: {lesson.name} -->",
                "-" * 80,
                "",
            ]
        )
        if content_file and content_file.exists():
            output.extend(
                [
                    "## Lý thuyết và Concept Quiz",
                    "",
                    student_content(read_markdown(content_file)),
                    "",
                ]
            )
        if exercise_file.exists():
            output.extend(
                [
                    "## Bài tập lesson",
                    "",
                    student_content(read_markdown(exercise_file)),
                    "",
                ]
            )

    MASTER_FILE.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
    print(f"Built {MASTER_FILE} from {len(lessons)} lessons")


if __name__ == "__main__":
    build_master()
