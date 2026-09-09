#!/usr/bin/env python3
"""
Replace all 27 dark theme images in courses/cpp-bang-b/c++-level-1-quyen-2.docx
with the newly generated high-contrast light theme PNGs.
"""

import zipfile, os, shutil
from pathlib import Path

DOCX_PATH = "courses/cpp-bang-b/c++-level-1-quyen-2.docx"
BACKUP_PATH = "courses/cpp-bang-b/c++-level-1-quyen-2.docx.bak_dark_images"

# Mapping from word/media/imageX.png to the rendered light theme PNG
IMAGE_MAP = {
    'word/media/image1.png': 'courses/cpp-bang-b/lessons/lesson-16-quy-hoach-dong-1d/assets/dp_1d_state_dag_vi.png',
    'word/media/image2.png': 'courses/cpp-bang-b/lessons/lesson-16-quy-hoach-dong-1d/assets/coin_change_dag_vi.png',
    'word/media/image3.png': 'courses/cpp-bang-b/lessons/lesson-16-quy-hoach-dong-1d/assets/lis_quadratic_model_vi.png',
    'word/media/image4.png': 'courses/cpp-bang-b/lessons/lesson-17-quy-hoach-dong-2d-knapsack/assets/grid_dp_matrix_vi.png',
    'word/media/image5.png': 'courses/cpp-bang-b/lessons/lesson-17-quy-hoach-dong-2d-knapsack/assets/knapsack_01_compression_vi.png',
    'word/media/image6.png': 'courses/cpp-bang-b/lessons/lesson-17-quy-hoach-dong-2d-knapsack/assets/unbounded_vs_01_knapsack_vi.png',
    'word/media/image7.png': 'courses/cpp-bang-b/lessons/lesson-18-quy-hoach-dong-chuoi-lcs/assets/lcs_table_traceback_vi.png',
    'word/media/image8.png': 'courses/cpp-bang-b/lessons/lesson-18-quy-hoach-dong-chuoi-lcs/assets/edit_distance_transitions_vi.png',
    'word/media/image9.png': 'courses/cpp-bang-b/lessons/lesson-18-quy-hoach-dong-chuoi-lcs/assets/palindrome_substring_vs_subsequence_vi.png',
    'word/media/image10.png': 'courses/cpp-bang-b/lessons/lesson-19-cau-truc-du-lieu-stl-set-map/assets/stl_set_map_rb_tree_vi.png',
    'word/media/image11.png': 'courses/cpp-bang-b/lessons/lesson-19-cau-truc-du-lieu-stl-set-map/assets/coordinate_compression_model_vi.png',
    'word/media/image12.png': 'courses/cpp-bang-b/lessons/lesson-19-cau-truc-du-lieu-stl-set-map/assets/priority_queue_heap_vi.png',
    'word/media/image13.png': 'courses/cpp-bang-b/lessons/lesson-20-ngan-xep-stack-monotonic/assets/stack_lifo_operation_vi.png',
    'word/media/image14.png': 'courses/cpp-bang-b/lessons/lesson-20-ngan-xep-stack-monotonic/assets/monotonic_stack_nge_vi.png',
    'word/media/image15.png': 'courses/cpp-bang-b/lessons/lesson-20-ngan-xep-stack-monotonic/assets/histogram_max_rectangle_vi.png',
    'word/media/image16.png': 'courses/cpp-bang-b/lessons/lesson-21-hang-doi-queue-deque/assets/queue_fifo_operation_vi.png',
    'word/media/image17.png': 'courses/cpp-bang-b/lessons/lesson-21-hang-doi-queue-deque/assets/deque_sliding_window_minmax_vi.png',
    'word/media/image18.png': 'courses/cpp-bang-b/lessons/lesson-21-hang-doi-queue-deque/assets/bfs_shortest_path_unweighted_vi.png',
    'word/media/image19.png': 'courses/cpp-bang-b/lessons/lesson-22-ly-thuyet-do-thi-bfs-dfs/assets/graph_representations_vi.png',
    'word/media/image20.png': 'courses/cpp-bang-b/lessons/lesson-22-ly-thuyet-do-thi-bfs-dfs/assets/bfs_vs_dfs_traversal_vi.png',
    'word/media/image21.png': 'courses/cpp-bang-b/lessons/lesson-22-ly-thuyet-do-thi-bfs-dfs/assets/connected_components_vi.png',
    'word/media/image22.png': 'courses/cpp-bang-b/lessons/lesson-23-do-thi-luoi-2d-flood-fill/assets/grid_2d_graph_modeling_vi.png',
    'word/media/image23.png': 'courses/cpp-bang-b/lessons/lesson-23-do-thi-luoi-2d-flood-fill/assets/flood_fill_maze_vi.png',
    'word/media/image24.png': 'courses/cpp-bang-b/lessons/lesson-23-do-thi-luoi-2d-flood-fill/assets/tree_properties_and_cycles_vi.png',
    'word/media/image25.png': 'courses/cpp-bang-b/lessons/lesson-24-cay-phan-doan-segment-tree-fenwick/assets/point_update_range_query_vi.png',
    'word/media/image26.png': 'courses/cpp-bang-b/lessons/lesson-24-cay-phan-doan-segment-tree-fenwick/assets/fenwick_tree_lowbit_vi.png',
    'word/media/image27.png': 'courses/cpp-bang-b/lessons/lesson-24-cay-phan-doan-segment-tree-fenwick/assets/segment_tree_binary_tree_vi.png',
}

# Verify all source PNGs exist
for zip_path, disk_path in IMAGE_MAP.items():
    assert os.path.exists(disk_path), f"Missing: {disk_path}"

# Make backup
if not os.path.exists(BACKUP_PATH):
    shutil.copy2(DOCX_PATH, BACKUP_PATH)
    print(f"Created backup at {BACKUP_PATH}")

TEMP_DOCX = "courses/cpp-bang-b/c++-level-1-quyen-2.docx.tmp"

replaced_count = 0
with zipfile.ZipFile(DOCX_PATH, 'r') as zin:
    with zipfile.ZipFile(TEMP_DOCX, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename in IMAGE_MAP:
                disk_file = IMAGE_MAP[item.filename]
                with open(disk_file, 'rb') as f:
                    data = f.read()
                zout.writestr(item, data)
                replaced_count += 1
                print(f"  -> Replaced {item.filename} with {os.path.basename(disk_file)} ({len(data)} bytes)")
            else:
                zout.writestr(item, zin.read(item.filename))

os.replace(TEMP_DOCX, DOCX_PATH)
print(f"\n🎉 Successfully injected all {replaced_count}/27 light theme images into {DOCX_PATH}!")
