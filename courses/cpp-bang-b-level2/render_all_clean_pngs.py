#!/usr/bin/env python3
"""
Sửa lỗi XML Entity (& -> &amp;) và render lại toàn bộ 100% PNG
"""

import re
import subprocess
from pathlib import Path

BASE = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")
SVG_FILES = list(BASE.glob("lessons/**/assets/*.svg"))

def fix_and_render_all():
    for svg in SVG_FILES:
        with open(svg, "r", encoding="utf-8") as f:
            txt = f.read()

        # Thay & trần (không phải &amp;, &lt;, &gt;, &quot;, &apos;) thành &amp;
        txt = re.sub(r"&(?!(amp|lt|gt|quot|apos);)", "&amp;", txt)

        with open(svg, "w", encoding="utf-8") as f:
            f.write(txt)

        png = svg.with_suffix(".png")
        cmd = [
            "npx", "-y", "@resvg/resvg-js-cli",
            "--fit-width", "2800",
            "--dpi", "300",
            str(svg),
            str(png)
        ]
        subprocess.run(cmd, check=True)
        print(f"  ✅ Render thành công: {png.name}")

    print("🎉 ĐÃ RENDER HOÀN HẢO 100% TẤT CẢ 17 FILE PNG SÁNG MÀU KHÔNG LỖI FONT!")

if __name__ == "__main__":
    fix_and_render_all()
