import re, subprocess
from pathlib import Path

def convert_l13_l15_svg_to_light(svg_path, out_svg_path):
    with open(svg_path, "r", encoding="utf-8") as f:
        txt = f.read()

    # 1. Update linearGradient bgGrad
    # Change stop-color="#0b0f19" -> "#FFFFFF", "#111827" -> "#F8FAFC"
    txt = txt.replace('stop-color="#0b0f19"', 'stop-color="#FFFFFF"')
    txt = txt.replace('stop-color="#111827"', 'stop-color="#F8FAFC"')

    # 2. Update background rect stroke to visible light border
    # <rect width="1000" height="360" fill="url(#bgGrad)" rx="16" />
    # <rect width="1000" height="360" fill="none" stroke="#334155" stroke-width="1.5" rx="16" />
    txt = re.sub(r'<rect width="(\d+)" height="(\d+)" fill="url\(#bgGrad\)" rx="16" ?/>',
                 r'<rect width="\1" height="\2" fill="url(#bgGrad)" stroke="#CBD5E1" stroke-width="2" rx="16" />', txt)
    # remove duplicate border rect if present
    txt = re.sub(r'<rect width="\d+" height="\d+" fill="none" stroke="#334155" stroke-width="1\.5" rx="16" ?/>', '', txt)

    # 3. Update Title & Subtitle text colors
    # Title: fill="#38bdf8" -> fill="#0F172A" (Dark navy)
    # Subtitle: fill="#94a3b8" -> fill="#475569" (Slate gray)
    # Match title (y="40" or y="42" or y="45")
    txt = re.sub(r'(<text[^>]*y="4[0-5]"[^>]*fill=)"#38bdf8"', r'\1"#0F172A"', txt)
    txt = re.sub(r'(<text[^>]*y="6[0-8]"[^>]*fill=)"#94a3b8"', r'\1"#475569"', txt)

    # 4. Update Card / Box gradients and fills
    # blueCard:
    # stop-color="#1e293b" -> stop-color="#F0F9FF"
    # stop-color="#0f172a" -> stop-color="#E0F2FE"
    txt = txt.replace('stop-color="#1e293b"', 'stop-color="#F0F9FF"')
    txt = txt.replace('stop-color="#0f172a"', 'stop-color="#E0F2FE"')

    # greenCard:
    # stop-color="#065f46" -> stop-color="#ECFDF5"
    # stop-color="#064e3b" -> stop-color="#D1FAE5"
    txt = txt.replace('stop-color="#065f46"', 'stop-color="#ECFDF5"')
    txt = txt.replace('stop-color="#064e3b"', 'stop-color="#D1FAE5"')

    # cyanCard:
    # stop-color="#0369a1" -> stop-color="#EFF6FF"
    # stop-color="#0c4a6e" -> stop-color="#DBEAFE"
    txt = txt.replace('stop-color="#0369a1"', 'stop-color="#EFF6FF"')
    txt = txt.replace('stop-color="#0c4a6e"', 'stop-color="#DBEAFE"')

    # purpleCard:
    # stop-color="#581c87" -> stop-color="#FAF5FF"
    # stop-color="#3b0764" -> stop-color="#F3E8FF"
    txt = txt.replace('stop-color="#581c87"', 'stop-color="#FAF5FF"')
    txt = txt.replace('stop-color="#3b0764"', 'stop-color="#F3E8FF"')

    # amberCard:
    # stop-color="#9a3412" -> stop-color="#FFFBEB"
    # stop-color="#7c2d12" -> stop-color="#FEF3C7"
    txt = txt.replace('stop-color="#9a3412"', 'stop-color="#FFFBEB"')
    txt = txt.replace('stop-color="#7c2d12"', 'stop-color="#FEF3C7"')

    # redCard:
    # stop-color="#991b1b" -> stop-color="#FEF2F2"
    # stop-color="#7f1d1d" -> stop-color="#FEE2E2"
    txt = txt.replace('stop-color="#991b1b"', 'stop-color="#FEF2F2"')
    txt = txt.replace('stop-color="#7f1d1d"', 'stop-color="#FEE2E2"')

    # Card shadow filter
    txt = txt.replace('flood-color="#000000" flood-opacity="0.6"', 'flood-color="#64748B" flood-opacity="0.12"')

    # Specific fills for legend/boxes: fill="#0f172a" or fill="#1e293b" -> fill="#F8FAFC", stroke="#E2E8F0"
    txt = txt.replace('fill="#0f172a" stroke="#334155"', 'fill="#F8FAFC" stroke="#CBD5E1"')
    txt = txt.replace('fill="#0f2b46" stroke="#0ea5e9"', 'fill="#F0F9FF" stroke="#0284C7"')

    # Inverted text colors inside cards:
    # Text in dp nodes: fill="#38bdf8" -> fill="#0369A1"
    # Text in green nodes: fill="#ffffff" -> fill="#065F46"
    # Text in blueCard: fill="#ffffff" -> fill="#0F172A"
    # Text in legend: fill="#cbd5e1" -> fill="#334155"
    txt = txt.replace('fill="#cbd5e1"', 'fill="#334155"')

    with open(out_svg_path, "w", encoding="utf-8") as f:
        f.write(txt)

convert_l13_l15_svg_to_light('courses/cpp-bang-b/lessons/lesson-16-quy-hoach-dong-1d/assets/dp_1d_state_dag_vi.svg', 'courses/cpp-bang-b/test_light.svg')
cmd = ["npx", "-y", "@resvg/resvg-js-cli", "--fit-width", "2800", "--dpi", "300", "courses/cpp-bang-b/test_light.svg", "courses/cpp-bang-b/test_light.png"]
subprocess.run(cmd, check=True)
print("Rendered test_light.png successfully!")
