#!/usr/bin/env python3
"""Normalize Python problem statements to the C++ De_Bai.md structure."""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
PROBLEMS_DIR = BASE_DIR / "problems"


def clean_inline_label(line, label):
    pattern = rf"^\*\s+\*\*{re.escape(label)}:\*\*\s*(.*)$"
    match = re.match(pattern, line)
    return match.group(1) if match else None


def table_cell(value):
    return re.sub(r"<br\s*/?>", "\n", value.strip(), flags=re.IGNORECASE)


def convert_sample_table(lines, index):
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index >= len(lines) or not lines[index].lstrip().startswith("| Input |"):
        return None, index
    if index + 2 >= len(lines):
        return None, index
    row_index = index + 2
    rows = []
    while row_index < len(lines) and lines[row_index].lstrip().startswith("|"):
        row = lines[row_index].strip()
        if row != "|---|---|---|" and not re.fullmatch(r"\|[-| :]+\|", row):
            values = [part.strip() for part in row.strip("|").split("|")]
            if len(values) >= 2:
                rows.append(values)
        row_index += 1
    if not rows:
        return None, index
    result = []
    for sample_number, values in enumerate(rows, start=1):
        result.extend(
            [
                f"## Sample {sample_number}",
                "",
                "### Input",
                "```text",
                table_cell(values[0]),
                "```",
                "### Output",
                "```text",
                table_cell(values[1]),
                "```",
            ]
        )
        if len(values) >= 3 and values[2]:
            result.extend(["### Giải thích", "", table_cell(values[2])])
    return result, row_index


def format_statement(path):
    source = path.read_text(encoding="utf-8").splitlines()
    if not source:
        return

    output = [source[0].strip(), ""]
    index = 1
    section = None
    skip_algorithm = False
    while index < len(source):
        line = source[index]

        if line.startswith("## Mã bài"):
            index += 1
            continue
        if line.startswith("## Ràng buộc"):
            section = "constraints"
            output.extend(["## Ràng buộc", ""])
            index += 1
            continue
        if line.startswith("---"):
            index += 1
            continue
        if re.match(r"^\*\s+\*\*Gợi ý thuật toán(?:\s*\([^)]*\))?:\*\*", line):
            skip_algorithm = True
            index += 1
            continue
        if skip_algorithm:
            if line.startswith("## Ràng buộc"):
                skip_algorithm = False
                section = "constraints"
                output.extend(["## Ràng buộc", ""])
            index += 1
            continue
        if line.lstrip().startswith("| Input |"):
            sample, next_index = convert_sample_table(source, index)
            if sample:
                output.extend(sample)
                index = next_index
                continue

        for old_label, new_heading in (
            ("Bối cảnh", "Bối cảnh"),
            ("Yêu cầu", "Nhiệm vụ"),
            ("Đầu vào (Input)", "Input"),
            ("Đầu ra (Output)", "Output"),
            ("Input", "Input"),
            ("Output", "Output"),
        ):
            value = clean_inline_label(line, old_label)
            if value is not None:
                section = new_heading
                output.extend([f"## {new_heading}", ""])
                if value:
                    output.append(value)
                index += 1
                break
        else:
            if clean_inline_label(line, "Ví dụ mẫu") is not None:
                sample, next_index = convert_sample_table(source, index + 1)
                if sample:
                    output.extend(sample)
                    index = next_index
                    continue
                index += 1
                continue
            if (
                section == "constraints"
                and clean_inline_label(line, "Ngôn ngữ mục tiêu") is not None
            ):
                index += 1
                continue
            output.append(line)
            index += 1
            continue
        continue

    while output and not output[-1].strip():
        output.pop()
    path.write_text("\n".join(output) + "\n", encoding="utf-8")


for statement in PROBLEMS_DIR.glob("*/De_Bai.md"):
    format_statement(statement)
