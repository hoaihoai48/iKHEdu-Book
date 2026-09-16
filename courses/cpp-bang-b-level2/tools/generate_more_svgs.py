#!/usr/bin/env python3
"""
Tạo bổ sung các sơ đồ SVG sáng màu cho các bài học còn lại:
- Lesson 03: Binary Search & Aggressive Cows
- Lesson 07: Greedy Interval Scheduling & Huffman Tree
- Lesson 08: DP 2D Grid Path & Tree DP
- Lesson 10: Running Median với 2 Heaps
- Lesson 11: Tam giác Pascal & Stars and Bars (Chia kẹo Euler)
- Lesson 14: Digit DP Cây trạng thái
"""

from pathlib import Path

BASE_DIR = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")

MORE_SVG_FILES = {
    # Lesson 03: Binary Search
    "lesson-03-tim-kiem-nhi-phan-nang-cao/assets/l03_binary_search_real_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 320" width="100%" height="100%">
  <rect width="900" height="320" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Mô phỏng Chặt nhị phân trên tập số thực (Binary Search on Real Numbers)</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Không gian nghiệm liên tục [L, R]. Lặp cố định 100 lần để đạt độ chính xác tuyệt đối 10⁻¹⁵.</text>

  <!-- Number Line Axis -->
  <g transform="translate(60, 120)">
    <line x1="0" y1="50" x2="780" y2="50" stroke="#94A3B8" stroke-width="4"/>
    
    <!-- Left Boundary L -->
    <circle cx="50" cy="50" r="10" fill="#3B82F6"/>
    <text x="50" y="25" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">L (Cận dưới)</text>
    <text x="50" y="80" fill="#64748B" font-family="monospace" font-size="13" text-anchor="middle">L = 0.0</text>

    <!-- Right Boundary R -->
    <circle cx="730" cy="50" r="10" fill="#3B82F6"/>
    <text x="730" y="25" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">R (Cận trên)</text>
    <text x="730" y="80" fill="#64748B" font-family="monospace" font-size="13" text-anchor="middle">R = 100.0</text>

    <!-- Mid Point -->
    <circle cx="390" cy="50" r="12" fill="#EF4444"/>
    <text x="390" y="20" fill="#DC2626" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">Mid = (L + R) / 2</text>
    <text x="390" y="85" fill="#B91C1C" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Kiểm tra check(mid)</text>

    <!-- Discard Left region -->
    <rect x="50" y="38" width="340" height="24" rx="4" fill="#FEE2E2" opacity="0.6"/>
    <text x="220" y="55" fill="#991B1B" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Loại bỏ nửa trái (L = mid)</text>
  </g>

  <!-- Bottom Box -->
  <g transform="translate(60, 240)">
    <rect width="780" height="48" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="390" y="30" fill="#1E293B" font-family="'Times New Roman', serif" font-size="14" font-weight="bold" text-anchor="middle">💡 Quy tắc vàng: Dùng vòng lặp for (int iter = 0; iter &lt; 100; ++iter) để tránh lỗi lặp vô tận do sai số float/double!</text>
  </g>
</svg>""",

    # Lesson 07: Greedy
    "lesson-07-thuat-toan-tham-lam-greedy/assets/l07_interval_scheduling_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 340" width="100%" height="100%">
  <rect width="900" height="340" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Chiến lược Tham lam Lập lịch sự kiện (Interval Scheduling) — Sắp xếp theo giờ kết thúc</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Luôn ưu tiên chọn sự kiện kết thúc sớm nhất để chừa lại khoảng thời gian trống nhiều nhất cho các sự kiện tiếp theo.</text>

  <!-- Intervals on Timeline -->
  <g transform="translate(60, 100)">
    <!-- Event 1 (Selected) -->
    <rect x="50" y="10" width="160" height="32" rx="6" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
    <text x="130" y="31" fill="#15803D" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Sự kiện 1: [1, 4] (CHỌN)</text>

    <!-- Event 2 (Rejected) -->
    <rect x="80" y="55" width="220" height="32" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-dasharray="4"/>
    <text x="190" y="76" fill="#B91C1C" font-family="sans-serif" font-size="12" text-anchor="middle" text-decoration="line-through">Sự kiện 2: [2, 7] (Trùng)</text>

    <!-- Event 3 (Selected) -->
    <rect x="230" y="100" width="180" height="32" rx="6" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
    <text x="320" y="121" fill="#15803D" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Sự kiện 3: [5, 9] (CHỌN)</text>

    <!-- Event 4 (Rejected) -->
    <rect x="300" y="145" width="150" height="32" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-dasharray="4"/>
    <text x="375" y="166" fill="#B91C1C" font-family="sans-serif" font-size="12" text-anchor="middle" text-decoration="line-through">Sự kiện 4: [6, 10] (Trùng)</text>

    <!-- Event 5 (Selected) -->
    <rect x="430" y="10" width="200" height="32" rx="6" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
    <text x="530" y="31" fill="#15803D" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Sự kiện 5: [10, 14] (CHỌN)</text>

    <!-- Timeline Arrow -->
    <line x1="0" y1="195" x2="780" y2="195" stroke="#475569" stroke-width="3"/>
    <polygon points="785,195 775,190 775,200" fill="#475569"/>
    <text x="785" y="215" fill="#475569" font-family="sans-serif" font-size="12" font-weight="bold">Thời gian (t)</text>
  </g>

  <!-- Bottom Tip -->
  <g transform="translate(60, 260)">
    <rect width="780" height="50" rx="8" fill="#EFF6FF" stroke="#3B82F6"/>
    <text x="390" y="31" fill="#1E3A8A" font-family="'Times New Roman', serif" font-size="14" font-weight="bold" text-anchor="middle">🏆 Thuật toán đạt kết quả tối ưu toàn cục O(N log N) nhờ chứng minh bằng phương pháp Đổi chỗ (Greedy Stays Ahead)!</text>
  </g>
</svg>""",

    # Lesson 08: DP
    "lesson-08-quy-hoach-dong-co-ban-va-chuyen-sau/assets/l08_grid_dp_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 350" width="100%" height="100%">
  <rect width="900" height="350" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Quy hoạch động trên Lưới 2D (Grid DP) — Tìm đường đi có tổng điểm lớn nhất</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Công thức chuyển trạng thái: dp[i][j] = A[i][j] + max(dp[i-1][j], dp[i][j-1]). Chỉ đi xuống hoặc sang phải.</text>

  <!-- Grid Layout -->
  <g transform="translate(80, 100)">
    <!-- Cell (i-1, j) - Top -->
    <g transform="translate(160, 10)">
      <rect width="110" height="55" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="55" y="24" fill="#1E40AF" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">(i-1, j)</text>
      <text x="55" y="44" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">dp[i-1][j]</text>
    </g>

    <!-- Down Arrow -->
    <line x1="215" y1="70" x2="215" y2="105" stroke="#3B82F6" stroke-width="3"/>
    <polygon points="215,110 210,100 220,100" fill="#3B82F6"/>

    <!-- Cell (i, j-1) - Left -->
    <g transform="translate(30, 115)">
      <rect width="110" height="55" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="55" y="24" fill="#1E40AF" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">(i, j-1)</text>
      <text x="55" y="44" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">dp[i][j-1]</text>
    </g>

    <!-- Right Arrow -->
    <line x1="145" y1="142" x2="155" y2="142" stroke="#3B82F6" stroke-width="3"/>
    <polygon points="160,142 150,137 150,147" fill="#3B82F6"/>

    <!-- Target Cell (i, j) -->
    <g transform="translate(160, 115)">
      <rect width="110" height="55" rx="8" fill="#FEF3C7" stroke="#F59E0B" stroke-width="3"/>
      <text x="55" y="24" fill="#92400E" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Ô ĐÍCH (i, j)</text>
      <text x="55" y="44" fill="#B45309" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">dp[i][j]</text>
    </g>
  </g>

  <!-- Complexity and Invariant Panel -->
  <g transform="translate(420, 100)">
    <rect width="420" height="200" rx="10" fill="#F8FAFC" stroke="#CBD5E1"/>
    <text x="25" y="32" fill="#0F172A" font-family="'Times New Roman', serif" font-size="16" font-weight="bold">📌 Đặc điểm cấu trúc DP Lưới 2D:</text>
    <text x="25" y="65" fill="#334155" font-family="'Times New Roman', serif" font-size="13">• <tspan font-weight="bold">Thứ tự tính toán:</tspan> Duyệt theo thứ tự hàng từ trên xuống dưới, cột từ trái sang phải.</text>
    <text x="25" y="95" fill="#334155" font-family="'Times New Roman', serif" font-size="13">• <tspan font-weight="bold">Khởi tạo biên:</tspan> Hàng 1 và Cột 1 là các giá trị cộng dồn trực tiếp.</text>
    <text x="25" y="125" fill="#334155" font-family="'Times New Roman', serif" font-size="13">• <tspan font-weight="bold">Độ phức tạp:</tspan> Thời gian O(N × M), Bộ nhớ O(N × M) hoặc nén về O(M).</text>
    <text x="25" y="160" fill="#15803D" font-family="'Times New Roman', serif" font-size="14" font-weight="bold">👉 Truy vết: Đi ngược từ (N, M) về (1, 1) theo hướng có dp lớn hơn!</text>
  </g>
</svg>""",

    # Lesson 10: STL 2 Heaps
    "lesson-10-thu-vien-stl-c-nang-cao/assets/l10_two_heaps_median_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 330" width="100%" height="100%">
  <rect width="900" height="330" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Kỹ thuật Hai Heap cân bằng duy trì Trung vị động (Running Median) O(log N)</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Max-Heap chứa nửa nhỏ (phần tử lớn nhất ở đỉnh) và Min-Heap chứa nửa lớn (phần tử nhỏ nhất ở đỉnh).</text>

  <!-- Left Max Heap -->
  <g transform="translate(60, 100)">
    <rect width="330" height="150" rx="12" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <text x="165" y="32" fill="#1E40AF" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">MAX-HEAP (Nửa giá trị nhỏ)</text>
    <text x="165" y="58" fill="#3B82F6" font-family="sans-serif" font-size="12" text-anchor="middle">Chứa: {1, 3, 5, 7}</text>

    <!-- Top of Max Heap -->
    <rect x="85" y="80" width="160" height="45" rx="8" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
    <text x="165" y="108" fill="#1D4ED8" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Đỉnh Max = 7</text>
  </g>

  <!-- Median Indicator in the Middle -->
  <g transform="translate(415, 130)">
    <circle cx="35" cy="40" r="32" fill="#FEF3C7" stroke="#F59E0B" stroke-width="3"/>
    <text x="35" y="35" fill="#92400E" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">TRUNG VỊ</text>
    <text x="35" y="54" fill="#B45309" font-family="'Times New Roman', serif" font-size="18" font-weight="bold" text-anchor="middle">7.5</text>
  </g>

  <!-- Right Min Heap -->
  <g transform="translate(510, 100)">
    <rect width="330" height="150" rx="12" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
    <text x="165" y="32" fill="#065F46" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">MIN-HEAP (Nửa giá trị lớn)</text>
    <text x="165" y="58" fill="#10B981" font-family="sans-serif" font-size="12" text-anchor="middle">Chứa: {8, 10, 12, 15}</text>

    <!-- Top of Min Heap -->
    <rect x="85" y="80" width="160" height="45" rx="8" fill="#D1FAE5" stroke="#059669" stroke-width="2"/>
    <text x="165" y="108" fill="#047857" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Đỉnh Min = 8</text>
  </g>

  <!-- Bottom Invariant Rule -->
  <g transform="translate(60, 270)">
    <rect width="780" height="40" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="390" y="25" fill="#1E293B" font-family="'Times New Roman', serif" font-size="13" font-weight="bold" text-anchor="middle">🔒 Bất biến: Chênh lệch kích thước 2 heap ≤ 1. Nếu số phần tử chẵn: Median = (Max.top + Min.top) / 2.0</text>
  </g>
</svg>""",

    # Lesson 11: Tổ hợp (Pascal Triangle)
    "lesson-11-to-hop-hoan-vi-va-xac-suat-co-ban/assets/l11_pascal_triangle_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 340" width="100%" height="100%">
  <rect width="900" height="340" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Tam giác Pascal và Công thức cộng Tổ hợp C(n, k) = C(n-1, k-1) + C(n-1, k)</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Tính toán trước bảng tổ hợp modulo hợp số hoặc số nguyên bất kỳ trong O(N²) không cần chia modulo.</text>

  <!-- Pascal Triangle Layers -->
  <g transform="translate(180, 100)">
    <!-- Row 0: 1 -->
    <g transform="translate(250, 0)">
      <circle cx="20" cy="15" r="18" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="20" y="20" fill="#0F172A" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1</text>
    </g>

    <!-- Row 1: 1, 1 -->
    <g transform="translate(220, 40)">
      <circle cx="20" cy="15" r="18" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="20" y="20" fill="#0F172A" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1</text>
      
      <circle cx="80" cy="15" r="18" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="80" y="20" fill="#0F172A" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1</text>
    </g>

    <!-- Row 2: 1, 2, 1 -->
    <g transform="translate(190, 80)">
      <circle cx="20" cy="15" r="18" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="20" y="20" fill="#0F172A" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1</text>
      
      <circle cx="80" cy="15" r="18" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="80" y="20" fill="#1D4ED8" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2</text>

      <circle cx="140" cy="15" r="18" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="140" y="20" fill="#0F172A" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1</text>
    </g>

    <!-- Row 3: 1, 3, 3, 1 -->
    <g transform="translate(160, 120)">
      <circle cx="20" cy="15" r="18" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="20" y="20" fill="#0F172A" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1</text>
      
      <circle cx="80" cy="15" r="18" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="80" y="20" fill="#1D4ED8" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3</text>

      <circle cx="140" cy="15" r="18" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="140" y="20" fill="#1D4ED8" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3</text>

      <circle cx="200" cy="15" r="18" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="200" y="20" fill="#0F172A" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1</text>
    </g>

    <!-- Row 4: 1, 4, 6, 4, 1 -->
    <g transform="translate(130, 160)">
      <circle cx="20" cy="15" r="18" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="20" y="20" fill="#0F172A" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1</text>
      
      <circle cx="80" cy="15" r="18" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="80" y="20" fill="#1D4ED8" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">4</text>

      <!-- 6 = 3 + 3 -->
      <circle cx="140" cy="15" r="20" fill="#FEF3C7" stroke="#F59E0B" stroke-width="3"/>
      <text x="140" y="21" fill="#B45309" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">6</text>

      <circle cx="200" cy="15" r="18" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="200" y="20" fill="#1D4ED8" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">4</text>

      <circle cx="260" cy="15" r="18" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="260" y="20" fill="#0F172A" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1</text>
    </g>
  </g>
</svg>""",

    # Lesson 14: Digit DP
    "lesson-14-quy-hoach-dong-chu-so-digit-dp/assets/l14_digit_dp_tree_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 340" width="100%" height="100%">
  <rect width="900" height="340" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Mô hình phân nhánh trạng thái Quy hoạch động chữ số (Digit DP)</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Xây dựng số từng chữ số từ trái qua phải với cờ tight (ràng buộc cận trên N) và cờ leading_zero.</text>

  <!-- State Tree Branches -->
  <g transform="translate(60, 100)">
    <!-- Root: index = 0 -->
    <rect x="30" y="40" width="160" height="60" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <text x="110" y="65" fill="#1E40AF" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Trạng thái (idx=0)</text>
    <text x="110" y="85" fill="#3B82F6" font-family="sans-serif" font-size="11" text-anchor="middle">tight = true (S = "345")</text>

    <!-- Branch tight = false (d < 3: d in {0, 1, 2}) -->
    <line x1="190" y1="55" x2="330" y2="25" stroke="#10B981" stroke-width="2.5"/>
    <text x="250" y="32" fill="#059669" font-family="sans-serif" font-size="12" font-weight="bold">Chọn d &lt; 3</text>

    <g transform="translate(340, 0)">
      <rect width="210" height="60" rx="8" fill="#DCFCE7" stroke="#10B981" stroke-width="2"/>
      <text x="105" y="25" fill="#065F46" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">tight = false (Tự do)</text>
      <text x="105" y="48" fill="#047857" font-family="sans-serif" font-size="11" text-anchor="middle">Các vị trí sau chọn từ 0 → 9 (Lưu DP)</text>
    </g>

    <!-- Branch tight = true (d = 3) -->
    <line x1="190" y1="85" x2="330" y2="115" stroke="#F59E0B" stroke-width="2.5"/>
    <text x="250" y="115" fill="#D97706" font-family="sans-serif" font-size="12" font-weight="bold">Chọn d = 3</text>

    <g transform="translate(340, 90)">
      <rect width="210" height="60" rx="8" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
      <text x="105" y="25" fill="#92400E" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">tight = true (Bị chặn)</text>
      <text x="105" y="48" fill="#B45309" font-family="sans-serif" font-size="11" text-anchor="middle">Vị trí sau chỉ được chọn ≤ 4</text>
    </g>
  </g>

  <!-- Bottom Tip -->
  <g transform="translate(60, 270)">
    <rect width="780" height="40" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
    <text x="390" y="25" fill="#1E293B" font-family="'Times New Roman', serif" font-size="13" font-weight="bold" text-anchor="middle">⚡ Memoization: dp[idx][sum][tight][is_zero]. Khi tight = false, kết quả được lưu để tái sử dụng!</text>
  </g>
</svg>""",
}

def main():
    print("🎨 Đang bổ sung trọn bộ SVG cho toàn bộ các bài học còn lại...")
    for rel_path, content in MORE_SVG_FILES.items():
        full_path = BASE_DIR / "lessons" / rel_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"  ✅ Đã tạo SVG: {rel_path}")
    print("🎉 Hoàn tất trọn bộ sơ đồ vector SVG sáng màu cho cả 15 Bài học!")

if __name__ == "__main__":
    main()
