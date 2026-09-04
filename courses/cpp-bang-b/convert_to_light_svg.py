#!/usr/bin/env python3
"""
Convert dark-theme SVGs to professional high-contrast Light Theme SVGs.
Design System:
- Outer Background: #FFFFFF (White) with subtle border #CBD5E1 and optional #F8FAFC gradient.
- Title: #0F172A (Deep Navy / Slate 900) or #0369A1 (Deep Blue 700).
- Subtitle / Description: #475569 (Slate 600) or #64748B (Slate 500).
- Normal Cards: #F8FAFC fill, #E2E8F0 / #CBD5E1 border, #1E293B body text.
- Highlight Blue/Cyan Cards: #EFF6FF fill, #3B82F6 border, #1E3A8A header, #1E40AF text.
- Success Green Cards: #ECFDF5 fill, #10B981 border, #065F46 header, #047857 text.
- Warning Amber Cards: #FFFBEB fill, #F59E0B border, #92400E header, #B45309 text.
- Danger Red Cards: #FEF2F2 fill, #EF4444 border, #991B1B header, #DC2626 text.
- Purple Cards: #FAF5FF fill, #A855F7 border, #581C87 header, #7E22CE text.
- Code blocks inside cards: #F1F5F9 fill, #CBD5E1 border, #0F172A code text.
- Lines & Connectors: #3B82F6, #10B981, #64748B, #94A3B8 with sharp contrast.
"""

import os
import re
import glob
import subprocess
from pathlib import Path

BASE_DIR = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b")

def convert_svg_to_light(svg_path: Path) -> str:
    with open(svg_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Gradients
    content = re.sub(
        r'<linearGradient id="bgGrad".*?</linearGradient>',
        '''<linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#F8FAFC" />
    </linearGradient>''',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<linearGradient id="bgGrad6".*?</linearGradient>',
        '''<linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#F8FAFC" />
    </linearGradient>''',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<linearGradient id="blueCard".*?</linearGradient>',
        '''<linearGradient id="blueCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF" />
      <stop offset="100%" stop-color="#DBEAFE" />
    </linearGradient>''',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<linearGradient id="cyanCard".*?</linearGradient>',
        '''<linearGradient id="cyanCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F0F9FF" />
      <stop offset="100%" stop-color="#E0F2FE" />
    </linearGradient>''',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<linearGradient id="greenCard".*?</linearGradient>',
        '''<linearGradient id="greenCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5" />
      <stop offset="100%" stop-color="#D1FAE5" />
    </linearGradient>''',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<linearGradient id="purpleCard".*?</linearGradient>',
        '''<linearGradient id="purpleCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF5FF" />
      <stop offset="100%" stop-color="#F3E8FF" />
    </linearGradient>''',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<linearGradient id="redCard".*?</linearGradient>',
        '''<linearGradient id="redCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FEF2F2" />
      <stop offset="100%" stop-color="#FEE2E2" />
    </linearGradient>''',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<linearGradient id="amberCard".*?</linearGradient>',
        '''<linearGradient id="amberCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB" />
      <stop offset="100%" stop-color="#FEF3C7" />
    </linearGradient>''',
        content,
        flags=re.DOTALL
    )

    # 2. Main Outer Card Fills
    content = re.sub(r'<rect width="(\d+)" height="(\d+)" fill="#0f172a" rx="16"\s*/>',
                     r'<rect width="\1" height="\2" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2" rx="16"/>', content)
    content = re.sub(r'<rect width="(\d+)" height="(\d+)" rx="16" fill="url\(#bgGrad\)" stroke="#334155" stroke-width="2"\s*/>',
                     r'<rect width="\1" height="\2" rx="16" fill="url(#bgGrad)" stroke="#CBD5E1" stroke-width="2"/>', content)
    content = re.sub(r'<rect width="(\d+)" height="(\d+)" rx="16" fill="url\(#bgGrad6\)" stroke="#334155" stroke-width="2"\s*/>',
                     r'<rect width="\1" height="\2" rx="16" fill="url(#bgGrad6)" stroke="#CBD5E1" stroke-width="2"/>', content)
    content = re.sub(r'<rect width="(\d+)" height="(\d+)" fill="none" stroke="#334155" stroke-width="1.5" rx="16"\s*/>',
                     r'<rect width="\1" height="\2" fill="none" stroke="#CBD5E1" stroke-width="1.5" rx="16"/>', content)
    content = re.sub(r'<rect width="(\d+)" height="(\d+)" fill="url\(#bgGrad\)" rx="16"\s*/>',
                     r'<rect width="\1" height="\2" fill="url(#bgGrad)" stroke="#CBD5E1" stroke-width="2" rx="16"/>', content)

    # 3. Shadows & Glows
    content = re.sub(r'flood-color="#000000"\s+flood-opacity="0.6"', r'flood-color="#64748B" flood-opacity="0.15"', content)
    content = re.sub(r'filter="url\(#glow[A-Za-z]+\)"', r'', content)

    # 4. Color replacements for background elements and card containers
    # Replace dark container fills
    content = re.sub(r'fill="#0f172a"', r'fill="#F8FAFC"', content)
    content = re.sub(r'fill="#1e293b"', r'fill="#EFF6FF"', content)
    content = re.sub(r'fill="#1e1b4b"', r'fill="#FAF5FF"', content)
    content = re.sub(r'fill="#064e3b"', r'fill="#ECFDF5"', content)
    content = re.sub(r'fill="#022c22"', r'fill="#F0FDF4"', content)
    content = re.sub(r'fill="#082f49"', r'fill="#F0F9FF"', content)
    content = re.sub(r'fill="#312e81"', r'fill="#EEF2FF"', content)
    content = re.sub(r'fill="#581c87"', r'fill="#FAF5FF"', content)
    content = re.sub(r'fill="#991b1b"', r'fill="#FEF2F2"', content)
    content = re.sub(r'fill="#7f1d1d"', r'fill="#FEE2E2"', content)
    content = re.sub(r'fill="#9a3412"', r'fill="#FFFBEB"', content)
    content = re.sub(r'fill="#7c2d12"', r'fill="#FEF3C7"', content)

    # Dark stroke replacements
    content = re.sub(r'stroke="#334155"', r'stroke="#CBD5E1"', content)
    content = re.sub(r'stroke="#475569"', r'stroke="#94A3B8"', content)

    # 5. Text color replacements
    # Main Titles (cyan/light blue/white -> deep slate / navy)
    content = re.sub(r'fill="#38bdf8"(\s+font-family="[^"]*"\s+font-size="[12][89012]"[^>]*)', r'fill="#0F172A"\1', content)
    content = re.sub(r'fill="#f8fafc"(\s+font-family="[^"]*"\s+font-size="[12][89012]"[^>]*)', r'fill="#0F172A"\1', content)
    content = re.sub(r'fill="#ffffff"(\s+font-family="[^"]*"\s+font-size="[12][89012]"[^>]*)', r'fill="#0F172A"\1', content)

    # Subtitles (#94a3b8 -> #475569)
    content = re.sub(r'fill="#94a3b8"', r'fill="#475569"', content)
    content = re.sub(r'fill="#cbd5e1"', r'fill="#334155"', content)

    # Header texts on cards (#38bdf8 in cards -> #1D4ED8 / #0369A1)
    content = re.sub(r'fill="#38bdf8"', r'fill="#0284C7"', content)
    content = re.sub(r'fill="#60a5fa"', r'fill="#1D4ED8"', content)
    content = re.sub(r'fill="#c084fc"', r'fill="#7E22CE"', content)
    content = re.sub(r'fill="#fb7185"', r'fill="#BE123C"', content)
    content = re.sub(r'fill="#f87171"', r'fill="#DC2626"', content)
    content = re.sub(r'fill="#4ade80"', r'fill="#15803D"', content)
    content = re.sub(r'fill="#34d399"', r'fill="#047857"', content)
    content = re.sub(r'fill="#6ee7b7"', r'fill="#065F46"', content)
    content = re.sub(r'fill="#a7f3d0"', r'fill="#047857"', content)
    content = re.sub(r'fill="#facc15"', r'fill="#B45309"', content)
    content = re.sub(r'fill="#fbbf24"', r'fill="#D97706"', content)
    content = re.sub(r'fill="#bae6fd"', r'fill="#0369A1"', content)
    content = re.sub(r'fill="#fde68a"', r'fill="#92400E"', content)
    content = re.sub(r'fill="#7dd3fc"', r'fill="#0284C7"', content)

    # General white text inside cards -> #0F172A or #1E293B
    content = re.sub(r'fill="#ffffff"', r'fill="#0F172A"', content)
    content = re.sub(r'fill="#f8fafc"', r'fill="#1E293B"', content)
    content = re.sub(r'fill="#f0f9ff"', r'fill="#0C4A6E"', content)
    content = re.sub(r'fill="#ecfdf5"', r'fill="#064E3B"', content)
    content = re.sub(r'fill="#fff1f2"', r'fill="#881337"', content)
    content = re.sub(r'fill="#faf5ff"', r'fill="#581C87"', content)

    # Small badge pill fills (e.g. #0369a1, #047857, #be123c, #7e22ce)
    # When text is dark (#0C4A6E), pill background should be light (#BAE6FD)
    content = re.sub(r'fill="#0369a1"', r'fill="#BAE6FD"', content)
    content = re.sub(r'fill="#047857"', r'fill="#A7F3D0"', content)
    content = re.sub(r'fill="#be123c"', r'fill="#FECDD3"', content)
    content = re.sub(r'fill="#7e22ce"', r'fill="#E9D5FF"', content)

    # Line colors
    content = re.sub(r'stroke="#94a3b8"', r'stroke="#64748B"', content)

    return content

def main():
    svg_files = sorted(BASE_DIR.glob("lessons/**/assets/*.svg"))
    print(f"Found {len(svg_files)} SVGs in {BASE_DIR}")

    converted_count = 0
    for svg_path in svg_files:
        new_content = convert_svg_to_light(svg_path)
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        converted_count += 1
        print(f"✓ Converted: {svg_path.name}")

    print(f"\nAll {converted_count} SVGs updated to Light Theme!")

if __name__ == "__main__":
    main()
