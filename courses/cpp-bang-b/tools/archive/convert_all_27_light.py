#!/usr/bin/env python3
"""
Convert all 27 SVGs for Lessons 13-21 to high-contrast, premium Light Theme (Offset 300 DPI)
and re-render PNGs with resvg-js-cli.
"""

import re, os, subprocess
from pathlib import Path

# Mapping of images 1..27 to SVG files
IMAGE_SVG_MAP = [
    ('image1.png', 'courses/cpp-bang-b/lessons/lesson-16-quy-hoach-dong-1d/assets/dp_1d_state_dag_vi.svg'),
    ('image2.png', 'courses/cpp-bang-b/lessons/lesson-16-quy-hoach-dong-1d/assets/coin_change_dag_vi.svg'),
    ('image3.png', 'courses/cpp-bang-b/lessons/lesson-16-quy-hoach-dong-1d/assets/lis_quadratic_model_vi.svg'),
    ('image4.png', 'courses/cpp-bang-b/lessons/lesson-17-quy-hoach-dong-2d-knapsack/assets/grid_dp_matrix_vi.svg'),
    ('image5.png', 'courses/cpp-bang-b/lessons/lesson-17-quy-hoach-dong-2d-knapsack/assets/knapsack_01_compression_vi.svg'),
    ('image6.png', 'courses/cpp-bang-b/lessons/lesson-17-quy-hoach-dong-2d-knapsack/assets/unbounded_vs_01_knapsack_vi.svg'),
    ('image7.png', 'courses/cpp-bang-b/lessons/lesson-18-quy-hoach-dong-chuoi-lcs/assets/lcs_table_traceback_vi.svg'),
    ('image8.png', 'courses/cpp-bang-b/lessons/lesson-18-quy-hoach-dong-chuoi-lcs/assets/edit_distance_transitions_vi.svg'),
    ('image9.png', 'courses/cpp-bang-b/lessons/lesson-18-quy-hoach-dong-chuoi-lcs/assets/palindrome_substring_vs_subsequence_vi.svg'),
    ('image10.png', 'courses/cpp-bang-b/lessons/lesson-19-cau-truc-du-lieu-stl-set-map/assets/stl_set_map_rb_tree_vi.svg'),
    ('image11.png', 'courses/cpp-bang-b/lessons/lesson-19-cau-truc-du-lieu-stl-set-map/assets/coordinate_compression_model_vi.svg'),
    ('image12.png', 'courses/cpp-bang-b/lessons/lesson-19-cau-truc-du-lieu-stl-set-map/assets/priority_queue_heap_vi.svg'),
    ('image13.png', 'courses/cpp-bang-b/lessons/lesson-20-ngan-xep-stack-monotonic/assets/stack_lifo_operation_vi.svg'),
    ('image14.png', 'courses/cpp-bang-b/lessons/lesson-20-ngan-xep-stack-monotonic/assets/monotonic_stack_nge_vi.svg'),
    ('image15.png', 'courses/cpp-bang-b/lessons/lesson-20-ngan-xep-stack-monotonic/assets/histogram_max_rectangle_vi.svg'),
    ('image16.png', 'courses/cpp-bang-b/lessons/lesson-21-hang-doi-queue-deque/assets/queue_fifo_operation_vi.svg'),
    ('image17.png', 'courses/cpp-bang-b/lessons/lesson-21-hang-doi-queue-deque/assets/deque_sliding_window_minmax_vi.svg'),
    ('image18.png', 'courses/cpp-bang-b/lessons/lesson-21-hang-doi-queue-deque/assets/bfs_shortest_path_unweighted_vi.svg'),
    ('image19.png', 'courses/cpp-bang-b/lessons/lesson-22-ly-thuyet-do-thi-bfs-dfs/assets/graph_representations_vi.svg'),
    ('image20.png', 'courses/cpp-bang-b/lessons/lesson-22-ly-thuyet-do-thi-bfs-dfs/assets/bfs_vs_dfs_traversal_vi.svg'),
    ('image21.png', 'courses/cpp-bang-b/lessons/lesson-22-ly-thuyet-do-thi-bfs-dfs/assets/connected_components_vi.svg'),
    ('image22.png', 'courses/cpp-bang-b/lessons/lesson-23-do-thi-luoi-2d-flood-fill/assets/grid_2d_graph_modeling_vi.svg'),
    ('image23.png', 'courses/cpp-bang-b/lessons/lesson-23-do-thi-luoi-2d-flood-fill/assets/flood_fill_maze_vi.svg'),
    ('image24.png', 'courses/cpp-bang-b/lessons/lesson-23-do-thi-luoi-2d-flood-fill/assets/tree_properties_and_cycles_vi.svg'),
    ('image25.png', 'courses/cpp-bang-b/lessons/lesson-24-cay-phan-doan-segment-tree-fenwick/assets/point_update_range_query_vi.svg'),
    ('image26.png', 'courses/cpp-bang-b/lessons/lesson-24-cay-phan-doan-segment-tree-fenwick/assets/fenwick_tree_lowbit_vi.svg'),
    ('image27.png', 'courses/cpp-bang-b/lessons/lesson-24-cay-phan-doan-segment-tree-fenwick/assets/segment_tree_binary_tree_vi.svg'),
]

def convert_l13_l15(txt):
    # 1. Gradients
    txt = txt.replace('stop-color="#0b0f19"', 'stop-color="#FFFFFF"')
    txt = txt.replace('stop-color="#111827"', 'stop-color="#F8FAFC"')

    # Card gradients
    txt = txt.replace('stop-color="#1e293b"', 'stop-color="#F0F9FF"')
    txt = txt.replace('stop-color="#0f172a"', 'stop-color="#E0F2FE"')
    txt = txt.replace('stop-color="#065f46"', 'stop-color="#ECFDF5"')
    txt = txt.replace('stop-color="#064e3b"', 'stop-color="#D1FAE5"')
    txt = txt.replace('stop-color="#0369a1"', 'stop-color="#EFF6FF"')
    txt = txt.replace('stop-color="#0c4a6e"', 'stop-color="#DBEAFE"')
    txt = txt.replace('stop-color="#581c87"', 'stop-color="#FAF5FF"')
    txt = txt.replace('stop-color="#3b0764"', 'stop-color="#F3E8FF"')
    txt = txt.replace('stop-color="#9a3412"', 'stop-color="#FFFBEB"')
    txt = txt.replace('stop-color="#7c2d12"', 'stop-color="#FEF3C7"')
    txt = txt.replace('stop-color="#991b1b"', 'stop-color="#FEF2F2"')
    txt = txt.replace('stop-color="#7f1d1d"', 'stop-color="#FEE2E2"')

    # 2. Main border
    txt = re.sub(r'<rect width="(\d+)" height="(\d+)" fill="url\(#bgGrad\)" rx="16" ?/>',
                 r'<rect width="\1" height="\2" fill="url(#bgGrad)" stroke="#CBD5E1" stroke-width="2" rx="16" />', txt)
    txt = re.sub(r'<rect width="\d+" height="\d+" fill="none" stroke="#334155" stroke-width="1\.5" rx="16" ?/>', '', txt)

    # 3. Main titles
    txt = re.sub(r'(<text[^>]*y="4[0-5]"[^>]*fill=)"#38bdf8"', r'\1"#0F172A"', txt)
    txt = re.sub(r'(<text[^>]*y="6[0-8]"[^>]*fill=)"#94a3b8"', r'\1"#475569"', txt)

    # 4. Filters
    txt = txt.replace('flood-color="#000000" flood-opacity="0.6"', 'flood-color="#64748B" flood-opacity="0.12"')

    # 5. Legend & inner boxes
    txt = txt.replace('fill="#0f172a" stroke="#334155"', 'fill="#F8FAFC" stroke="#CBD5E1"')
    txt = txt.replace('fill="#0f2b46" stroke="#0ea5e9"', 'fill="#EFF6FF" stroke="#3B82F6"')
    txt = txt.replace('fill="#1e293b" stroke="#64748b"', 'fill="#F1F5F9" stroke="#94A3B8"')
    txt = txt.replace('fill="#1e293b"', 'fill="#F8FAFC"')

    # 6. Text inside cards / nodes / legends
    txt = txt.replace('fill="#cbd5e1"', 'fill="#334155"')
    txt = txt.replace('fill="#38bdf8" font-family="system-ui', 'fill="#0369A1" font-family="system-ui')
    txt = txt.replace('fill="#38bdf8" font-family="monospace"', 'fill="#0F172A" font-family="monospace"')
    txt = txt.replace('fill="#ffffff" font-family="monospace"', 'fill="#065F46" font-family="monospace"')
    txt = txt.replace('fill="#bae6fd"', 'fill="#0369A1"')
    txt = txt.replace('fill="#a7f3d0"', 'fill="#065F46"')
    txt = txt.replace('fill="#34d399"', 'fill="#059669"')
    txt = txt.replace('fill="#94a3b8" font-family="system-ui', 'fill="#64748B" font-family="system-ui')
    txt = txt.replace('fill="#f8fafc" font-family="monospace"', 'fill="#0F172A" font-family="monospace"')

    return txt

def convert_l16_l21(txt):
    # These SVGs start with:
    # <rect width="900" height="380" fill="#0f172a" rx="16"/>
    # <text x="450" y="40" fill="#f8fafc" ...>TITLE</text>
    
    # 1. Defs for gradient and shadow if not present
    defs = """  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#64748B" flood-opacity="0.1" />
    </filter>
  </defs>
"""
    if '<defs>' not in txt:
        txt = txt.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 380" width="100%" height="100%">',
                          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 380" width="100%" height="100%">\n' + defs)
        txt = txt.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">',
                          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">\n' + defs)

    # 2. Background card
    txt = re.sub(r'<rect width="(\d+)" height="(\d+)" fill="#0f172a" rx="16"/>',
                 r'<rect width="\1" height="\2" fill="url(#bgGrad)" stroke="#CBD5E1" stroke-width="2" rx="16"/>', txt)

    # 3. Main title
    txt = re.sub(r'(<text[^>]*y="40"[^>]*fill=)"#f8fafc"', r'\1"#0F172A"', txt)

    # 4. Box/Card containers: fill="#1e293b" -> fill="#F8FAFC" or fill="#FFFFFF"
    txt = txt.replace('fill="#1e293b" stroke="#38bdf8"', 'fill="#F0F9FF" stroke="#0284C7"')
    txt = txt.replace('fill="#1e293b" stroke="#c084fc"', 'fill="#FAF5FF" stroke="#A855F7"')
    txt = txt.replace('fill="#1e293b" stroke="#4ade80"', 'fill="#ECFDF5" stroke="#10B981"')
    txt = txt.replace('fill="#1e293b" stroke="#facc15"', 'fill="#FFFBEB" stroke="#F59E0B"')
    txt = txt.replace('fill="#1e293b" stroke="#f87171"', 'fill="#FEF2F2" stroke="#EF4444"')
    txt = txt.replace('fill="#1e293b" stroke="#334155"', 'fill="#F8FAFC" stroke="#CBD5E1"')
    txt = txt.replace('fill="#1e293b"', 'fill="#F8FAFC"')

    # Dark inner boxes
    txt = txt.replace('fill="#0f172a" stroke="#334155"', 'fill="#FFFFFF" stroke="#E2E8F0"')
    txt = txt.replace('fill="#0f172a"', 'fill="#F1F5F9"')
    txt = txt.replace('fill="#1e1b4b" stroke="#38bdf8"', 'fill="#E0F2FE" stroke="#0284C7"')
    txt = txt.replace('fill="#1e1b4b" stroke="#c084fc"', 'fill="#F3E8FF" stroke="#A855F7"')
    txt = txt.replace('fill="#1e1b4b" stroke="#334155"', 'fill="#F1F5F9" stroke="#94A3B8"')
    txt = txt.replace('fill="#1e1b4b"', 'fill="#F1F5F9"')
    txt = txt.replace('fill="#312e81"', 'fill="#DBEAFE"')
    txt = txt.replace('fill="#064e3b" stroke="#4ade80"', 'fill="#D1FAE5" stroke="#059669"')
    txt = txt.replace('fill="#047857" stroke="#4ade80"', 'fill="#D1FAE5" stroke="#059669"')
    txt = txt.replace('fill="#047857"', 'fill="#059669"')
    txt = txt.replace('fill="#854d0e" stroke="#facc15"', 'fill="#FEF3C7" stroke="#D97706"')
    txt = txt.replace('fill="#854d0e"', 'fill="#D97706"')
    txt = txt.replace('fill="#065f46" stroke="#4ade80"', 'fill="#D1FAE5" stroke="#059669"')
    txt = txt.replace('fill="#065f46"', 'fill="#059669"')

    # 5. Text colors
    # White text -> Dark Slate
    txt = txt.replace('fill="#f8fafc"', 'fill="#1E293B"')
    # Muted text -> Slate 600
    txt = txt.replace('fill="#94a3b8"', 'fill="#475569"')
    # Cyan text -> Sky 700
    txt = txt.replace('fill="#38bdf8"', 'fill="#0369A1"')
    # Green text -> Emerald 700
    txt = txt.replace('fill="#4ade80"', 'fill="#065F46"')
    # Purple text -> Purple 700
    txt = txt.replace('fill="#c084fc"', 'fill="#7E22CE"')
    # Yellow text -> Amber 800
    txt = txt.replace('fill="#facc15"', 'fill="#92400E"')
    # Red text -> Rose 700
    txt = txt.replace('fill="#f87171"', 'fill="#B91C1C"')

    return txt

def main():
    for img_name, svg_path in IMAGE_SVG_MAP:
        with open(svg_path, "r", encoding="utf-8") as f:
            txt = f.read()

        # Fix unescaped ampersands first
        txt = re.sub(r"&(?!(amp|lt|gt|quot|apos);)", "&amp;", txt)

        if any(f'lesson-{n}' in svg_path for n in [13, 14, 15]):
            txt = convert_l13_l15(txt)
        else:
            txt = convert_l16_l21(txt)

        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(txt)

        png_path = Path(svg_path).with_suffix(".png")
        cmd = [
            "npx", "-y", "@resvg/resvg-js-cli",
            "--fit-width", "2800",
            "--dpi", "300",
            str(svg_path),
            str(png_path)
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Converted & rendered: {png_path.name}")

    print("\n🎉 ALL 27 SVGs & PNGs SUCCESSFULLY CONVERTED TO LIGHT THEME!")

if __name__ == "__main__":
    main()
