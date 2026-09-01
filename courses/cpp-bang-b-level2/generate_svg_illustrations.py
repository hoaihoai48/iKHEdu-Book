#!/usr/bin/env python3
"""
Generator tạo trọn bộ hình ảnh minh họa vector SVG chuẩn in màu (Light theme sang trọng, sắc nét, 300 DPI)
cho 15 Bài học Level 2 — Khoá học C++ Bảng B (Level 2).
"""

import os
from pathlib import Path

BASE_DIR = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")

SVG_FILES = {
    # -------------------------------------------------------------
    # LESSON 01: SỐ HỌC
    # -------------------------------------------------------------
    "lesson-01-so-hoc-co-ban-chuyen-sau/assets/l01_spf_sieve_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
  </defs>
  <rect width="900" height="360" rx="16" fill="url(#cardBg)" stroke="#CBD5E1" stroke-width="2"/>
  
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Sơ đồ cơ chế Sàng SPF (Smallest Prime Factor) — Phân tích thừa số trong O(log N)</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Mỗi số N được phân tích cực nhanh bằng cách nhảy liên tiếp theo spf[N]: N = 60 → spf[60]=2 → 30 → spf[30]=2 → 15 → spf[15]=3 → 5 → spf[5]=5 → 1</text>
  
  <!-- Step 1: 60 -->
  <g transform="translate(50, 110)">
    <rect width="110" height="130" rx="12" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <text x="55" y="38" fill="#1E3A8A" font-family="'Times New Roman', serif" font-size="24" font-weight="bold" text-anchor="middle">N = 60</text>
    <rect x="15" y="55" width="80" height="28" rx="6" fill="#DBEAFE"/>
    <text x="55" y="74" fill="#1D4ED8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">spf[60] = 2</text>
    <text x="55" y="108" fill="#2563EB" font-family="'Times New Roman', serif" font-size="12" text-anchor="middle">Lấy thừa số 2</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 170 175 L 210 175" stroke="#3B82F6" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
  <polygon points="215,175 205,170 205,180" fill="#3B82F6"/>

  <!-- Step 2: 30 -->
  <g transform="translate(225, 110)">
    <rect width="110" height="130" rx="12" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <text x="55" y="38" fill="#1E3A8A" font-family="'Times New Roman', serif" font-size="24" font-weight="bold" text-anchor="middle">N = 30</text>
    <rect x="15" y="55" width="80" height="28" rx="6" fill="#DBEAFE"/>
    <text x="55" y="74" fill="#1D4ED8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">spf[30] = 2</text>
    <text x="55" y="108" fill="#2563EB" font-family="'Times New Roman', serif" font-size="12" text-anchor="middle">Lấy thừa số 2</text>
  </g>

  <!-- Arrow 2 -->
  <polygon points="390,175 380,170 380,180" fill="#3B82F6"/>
  <line x1="345" y1="175" x2="385" y2="175" stroke="#3B82F6" stroke-width="3"/>

  <!-- Step 3: 15 -->
  <g transform="translate(400, 110)">
    <rect width="110" height="130" rx="12" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
    <text x="55" y="38" fill="#92400E" font-family="'Times New Roman', serif" font-size="24" font-weight="bold" text-anchor="middle">N = 15</text>
    <rect x="15" y="55" width="80" height="28" rx="6" fill="#FDE68A"/>
    <text x="55" y="74" fill="#B45309" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">spf[15] = 3</text>
    <text x="55" y="108" fill="#D97706" font-family="'Times New Roman', serif" font-size="12" text-anchor="middle">Lấy thừa số 3</text>
  </g>

  <!-- Arrow 3 -->
  <polygon points="565,175 555,170 555,180" fill="#F59E0B"/>
  <line x1="520" y1="175" x2="560" y2="175" stroke="#F59E0B" stroke-width="3"/>

  <!-- Step 4: 5 -->
  <g transform="translate(575, 110)">
    <rect width="110" height="130" rx="12" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
    <text x="55" y="38" fill="#065F46" font-family="'Times New Roman', serif" font-size="24" font-weight="bold" text-anchor="middle">N = 5</text>
    <rect x="15" y="55" width="80" height="28" rx="6" fill="#A7F3D0"/>
    <text x="55" y="74" fill="#047857" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">spf[5] = 5</text>
    <text x="55" y="108" fill="#059669" font-family="'Times New Roman', serif" font-size="12" text-anchor="middle">Lấy thừa số 5</text>
  </g>

  <!-- Arrow 4 -->
  <polygon points="740,175 730,170 730,180" fill="#10B981"/>
  <line x1="695" y1="175" x2="735" y2="175" stroke="#10B981" stroke-width="3"/>

  <!-- Final Step: 1 -->
  <g transform="translate(750, 110)">
    <rect width="100" height="130" rx="12" fill="#F1F5F9" stroke="#64748B" stroke-width="2"/>
    <text x="50" y="45" fill="#334155" font-family="'Times New Roman', serif" font-size="28" font-weight="bold" text-anchor="middle">N = 1</text>
    <rect x="15" y="65" width="70" height="26" rx="6" fill="#E2E8F0"/>
    <text x="50" y="82" fill="#475569" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">DỪNG</text>
    <text x="50" y="112" fill="#64748B" font-family="'Times New Roman', serif" font-size="11" text-anchor="middle">Hoàn tất</text>
  </g>

  <!-- Result Banner -->
  <rect x="50" y="275" width="800" height="50" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
  <text x="450" y="306" fill="#166534" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">Kết quả phân tích: 60 = 2² × 3¹ × 5¹ (Thời gian truy vấn: O(log N) với 4 phép chia)</text>
</svg>""",

    "lesson-01-so-hoc-co-ban-chuyen-sau/assets/l01_segmented_sieve_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 320" width="100%" height="100%">
  <rect width="900" height="320" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Mô phỏng Sàng số nguyên tố phân đoạn trên đoạn [L, R] = [100, 115]</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Dùng các số nguyên tố p ≤ √R = √115 ≈ 10 (primes = [2, 3, 5, 7]) để gạch bỏ các bội số trong mảng ánh xạ [0 .. R-L].</text>

  <!-- Cells for 100 to 115 -->
  <g transform="translate(40, 110)">
    <!-- 100 -->
    <g transform="translate(0, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">100</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 2</text>
    </g>
    <!-- 101 -->
    <g transform="translate(52, 0)">
      <rect width="48" height="60" rx="6" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
      <text x="24" y="32" fill="#15803D" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">101</text>
      <text x="24" y="50" fill="#16A34A" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">PRIME</text>
    </g>
    <!-- 102 -->
    <g transform="translate(104, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">102</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 2,3</text>
    </g>
    <!-- 103 -->
    <g transform="translate(156, 0)">
      <rect width="48" height="60" rx="6" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
      <text x="24" y="32" fill="#15803D" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">103</text>
      <text x="24" y="50" fill="#16A34A" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">PRIME</text>
    </g>
    <!-- 104 -->
    <g transform="translate(208, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">104</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 2</text>
    </g>
    <!-- 105 -->
    <g transform="translate(260, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">105</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 3,5,7</text>
    </g>
    <!-- 106 -->
    <g transform="translate(312, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">106</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 2</text>
    </g>
    <!-- 107 -->
    <g transform="translate(364, 0)">
      <rect width="48" height="60" rx="6" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
      <text x="24" y="32" fill="#15803D" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">107</text>
      <text x="24" y="50" fill="#16A34A" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">PRIME</text>
    </g>
    <!-- 108 -->
    <g transform="translate(416, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">108</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 2,3</text>
    </g>
    <!-- 109 -->
    <g transform="translate(468, 0)">
      <rect width="48" height="60" rx="6" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
      <text x="24" y="32" fill="#15803D" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">109</text>
      <text x="24" y="50" fill="#16A34A" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">PRIME</text>
    </g>
    <!-- 110 -->
    <g transform="translate(520, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">110</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 2,5</text>
    </g>
    <!-- 111 -->
    <g transform="translate(572, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">111</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 3</text>
    </g>
    <!-- 112 -->
    <g transform="translate(624, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">112</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 2,7</text>
    </g>
    <!-- 113 -->
    <g transform="translate(676, 0)">
      <rect width="48" height="60" rx="6" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
      <text x="24" y="32" fill="#15803D" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">113</text>
      <text x="24" y="50" fill="#16A34A" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">PRIME</text>
    </g>
    <!-- 114 -->
    <g transform="translate(728, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">114</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 2,3</text>
    </g>
    <!-- 115 -->
    <g transform="translate(780, 0)">
      <rect width="48" height="60" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="24" y="28" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" text-decoration="line-through">115</text>
      <text x="24" y="48" fill="#DC2626" font-family="sans-serif" font-size="10" text-anchor="middle">bội 5</text>
    </g>
  </g>

  <!-- Legend -->
  <g transform="translate(40, 210)">
    <rect x="0" y="0" width="820" height="75" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="20" y="30" fill="#1E293B" font-family="'Times New Roman', serif" font-size="14" font-weight="bold">📌 Các số nguyên tố tìm được trong đoạn [100, 115]:</text>
    <text x="20" y="55" fill="#15803D" font-family="sans-serif" font-size="15" font-weight="bold">👉 101,  103,  107,  109,  113 (Tổng cộng: 5 số nguyên tố — Bộ nhớ mảng chỉ tốn R - L + 1 = 16 phần tử)</text>
  </g>
</svg>""",

    # -------------------------------------------------------------
    # LESSON 02: MODULO & FAST POWER
    # -------------------------------------------------------------
    "lesson-02-modulo-va-fast-power/assets/l02_matrix_fibonacci_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 320" width="100%" height="100%">
  <rect width="900" height="320" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Sơ đồ nhân Ma trận 2×2 tính số Fibonacci thứ N trong O(log N)</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Chuyển hệ thức truy hồi tuyến tính Fn = Fn-1 + Fn-2 thành phép nhân lũy thừa ma trận cơ sở.</text>

  <!-- Matrix Equation -->
  <g transform="translate(50, 110)">
    <!-- Matrix Vector 1 -->
    <rect x="0" y="0" width="80" height="110" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
    <text x="40" y="45" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="20" font-weight="bold" text-anchor="middle">F(n+1)</text>
    <text x="40" y="85" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="20" font-weight="bold" text-anchor="middle">F(n)</text>
    
    <text x="105" y="65" fill="#1E293B" font-family="sans-serif" font-size="24" font-weight="bold">=</text>

    <!-- Transition Matrix T -->
    <g transform="translate(135, 0)">
      <rect x="0" y="0" width="120" height="110" rx="8" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
      <text x="60" y="25" fill="#92400E" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Ma trận T</text>
      <text x="35" y="60" fill="#B45309" font-family="'Times New Roman', serif" font-size="22" font-weight="bold" text-anchor="middle">1</text>
      <text x="85" y="60" fill="#B45309" font-family="'Times New Roman', serif" font-size="22" font-weight="bold" text-anchor="middle">1</text>
      <text x="35" y="95" fill="#B45309" font-family="'Times New Roman', serif" font-size="22" font-weight="bold" text-anchor="middle">1</text>
      <text x="85" y="95" fill="#B45309" font-family="'Times New Roman', serif" font-size="22" font-weight="bold" text-anchor="middle">0</text>
    </g>

    <text x="275" y="65" fill="#1E293B" font-family="sans-serif" font-size="24" font-weight="bold">×</text>

    <!-- Matrix Vector 2 -->
    <g transform="translate(305, 0)">
      <rect x="0" y="0" width="80" height="110" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
      <text x="40" y="45" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="20" font-weight="bold" text-anchor="middle">F(n)</text>
      <text x="40" y="85" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="20" font-weight="bold" text-anchor="middle">F(n-1)</text>
    </g>

    <text x="415" y="65" fill="#1E293B" font-family="sans-serif" font-size="24" font-weight="bold">=</text>

    <!-- Result Matrix Power -->
    <g transform="translate(450, 0)">
      <rect x="0" y="0" width="130" height="110" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
      <text x="65" y="25" fill="#065F46" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Ma trận T^n</text>
      <text x="40" y="60" fill="#047857" font-family="'Times New Roman', serif" font-size="20" font-weight="bold" text-anchor="middle">F(n+1)</text>
      <text x="95" y="60" fill="#047857" font-family="'Times New Roman', serif" font-size="20" font-weight="bold" text-anchor="middle">F(n)</text>
      <text x="40" y="95" fill="#047857" font-family="'Times New Roman', serif" font-size="20" font-weight="bold" text-anchor="middle">F(n)</text>
      <text x="95" y="95" fill="#047857" font-family="'Times New Roman', serif" font-size="20" font-weight="bold" text-anchor="middle">F(n-1)</text>
    </g>

    <text x="605" y="65" fill="#1E293B" font-family="sans-serif" font-size="24" font-weight="bold">×</text>

    <!-- Base Vector -->
    <g transform="translate(635, 0)">
      <rect x="0" y="0" width="80" height="110" rx="8" fill="#F1F5F9" stroke="#64748B" stroke-width="1.5"/>
      <text x="40" y="25" fill="#475569" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Cơ sở</text>
      <text x="40" y="55" fill="#0F172A" font-family="'Times New Roman', serif" font-size="20" font-weight="bold" text-anchor="middle">F(1)=1</text>
      <text x="40" y="90" fill="#0F172A" font-family="'Times New Roman', serif" font-size="20" font-weight="bold" text-anchor="middle">F(0)=0</text>
    </g>
  </g>

  <!-- Bottom Tip -->
  <g transform="translate(50, 245)">
    <rect width="800" height="48" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="400" y="30" fill="#334155" font-family="'Times New Roman', serif" font-size="14" font-weight="bold" text-anchor="middle">💡 Áp dụng lũy thừa nhị phân ma trận (Matrix Exponentiation) cho phép tính F(10¹⁸) chỉ trong ~60 phép nhân ma trận!</text>
  </g>
</svg>""",

    # -------------------------------------------------------------
    # LESSON 04: MẢNG 2D & TWO POINTERS
    # -------------------------------------------------------------
    "lesson-04-ky-thuat-mang-nang-cao/assets/l04_2d_prefix_sum_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <rect width="900" height="360" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Nguyên lý Mảng cộng dồn 2D (2D Prefix Sum) & Truy vấn hình chữ nhật O(1)</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Công thức tính tổng vùng đỏ (x1,y1) → (x2,y2): Sum = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]</text>

  <!-- Big Matrix Representation -->
  <g transform="translate(50, 100)">
    <!-- Base Matrix Grid -->
    <rect x="0" y="0" width="360" height="220" fill="#F8FAFC" stroke="#94A3B8" stroke-width="2"/>
    
    <!-- Top-Left Overlap (x1-1, y1-1) - Purple -->
    <rect x="0" y="0" width="120" height="80" fill="#E0E7FF" stroke="#6366F1" stroke-width="1.5"/>
    <text x="60" y="45" fill="#4338CA" font-family="'Times New Roman', serif" font-size="14" font-weight="bold" text-anchor="middle">S[x1-1][y1-1] (Cộng lại)</text>

    <!-- Top Strip - Yellow -->
    <rect x="120" y="0" width="180" height="80" fill="#FEF3C7" stroke="#F59E0B" stroke-dasharray="4" stroke-width="1.5"/>
    <text x="210" y="45" fill="#B45309" font-family="'Times New Roman', serif" font-size="13" text-anchor="middle">Vùng trừ trên</text>

    <!-- Left Strip - Blue -->
    <rect x="0" y="80" width="120" height="110" fill="#DBEAFE" stroke="#3B82F6" stroke-dasharray="4" stroke-width="1.5"/>
    <text x="60" y="140" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="13" text-anchor="middle">Vùng trừ trái</text>

    <!-- Target Rectangle - Red -->
    <rect x="120" y="80" width="180" height="110" fill="#FEE2E2" stroke="#EF4444" stroke-width="3"/>
    <text x="210" y="130" fill="#B91C1C" font-family="'Times New Roman', serif" font-size="18" font-weight="bold" text-anchor="middle">VÙNG CẦN TÍNH</text>
    <text x="210" y="155" fill="#DC2626" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">(x1, y1) → (x2, y2)</text>

    <!-- Boundary Points -->
    <circle cx="120" cy="80" r="5" fill="#EF4444"/>
    <text x="105" y="75" fill="#B91C1C" font-family="sans-serif" font-size="11" font-weight="bold">(x1, y1)</text>

    <circle cx="300" cy="190" r="5" fill="#EF4444"/>
    <text x="310" y="205" fill="#B91C1C" font-family="sans-serif" font-size="11" font-weight="bold">(x2, y2)</text>
  </g>

  <!-- Explanation Panel on the Right -->
  <g transform="translate(450, 100)">
    <rect width="400" height="220" rx="10" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="20" y="32" fill="#0F172A" font-family="'Times New Roman', serif" font-size="16" font-weight="bold">Bản chất nguyên lý Bao hàm - Loại trừ:</text>
    
    <text x="20" y="65" fill="#1E293B" font-family="'Times New Roman', serif" font-size="14">1. Lấy toàn bộ hình chữ nhật lớn từ gốc (1,1) đến (x2,y2):</text>
    <text x="40" y="88" fill="#2563EB" font-family="monospace" font-size="13" font-weight="bold">+ S[x2][y2]</text>

    <text x="20" y="115" fill="#1E293B" font-family="'Times New Roman', serif" font-size="14">2. Trừ đi phần thừa phía trên và phía bên trái:</text>
    <text x="40" y="138" fill="#DC2626" font-family="monospace" font-size="13" font-weight="bold">- S[x1-1][y2]  -  S[x2][y1-1]</text>

    <text x="20" y="165" fill="#1E293B" font-family="'Times New Roman', serif" font-size="14">3. Phần góc giao (x1-1, y1-1) bị trừ 2 lần nên phải cộng lại:</text>
    <text x="40" y="188" fill="#16A34A" font-family="monospace" font-size="13" font-weight="bold">+ S[x1-1][y1-1]</text>
  </g>
</svg>""",

    # -------------------------------------------------------------
    # LESSON 05: MEET IN THE MIDDLE
    # -------------------------------------------------------------
    "lesson-05-de-quy-chia-de-tri-mitm/assets/l05_mitm_split_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 340" width="100%" height="100%">
  <rect width="900" height="340" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Kỹ thuật Meet in the Middle (Phân đôi tập hợp) giảm độ phức tạp từ O(2^N) về O(2^(N/2))</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Với N = 40: 2⁴⁰ ≈ 10¹² (TLE không thể chạy) → Chia đôi thành 2 nửa N/2 = 20: 2²⁰ ≈ 10⁶ (Chạy mượt mà trong 0.1s)</text>

  <!-- Left Set (N/2 = 20) -->
  <g transform="translate(60, 100)">
    <rect width="340" height="150" rx="12" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <text x="170" y="32" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="18" font-weight="bold" text-anchor="middle">Nửa đầu: N₁ = 20 phần tử</text>
    <text x="170" y="60" fill="#3B82F6" font-family="sans-serif" font-size="13" text-anchor="middle">Sinh tất cả 2²⁰ = 1,048,576 tập con</text>
    
    <rect x="30" y="80" width="280" height="45" rx="6" fill="#DBEAFE"/>
    <text x="170" y="108" fill="#1E40AF" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Lưu vào mảng Vector A &amp; Sắp xếp O(M log M)</text>
  </g>

  <!-- Middle Bridge / Binary Search -->
  <g transform="translate(420, 140)">
    <circle cx="30" cy="35" r="28" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
    <text x="30" y="32" fill="#B45309" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">BS</text>
    <text x="30" y="48" fill="#B45309" font-family="sans-serif" font-size="9" text-anchor="middle">O(log M)</text>
    
    <!-- Double sided arrow -->
    <line x1="-15" y1="35" x2="0" y2="35" stroke="#F59E0B" stroke-width="3"/>
    <line x1="60" y1="35" x2="75" y2="35" stroke="#F59E0B" stroke-width="3"/>
  </g>

  <!-- Right Set (N/2 = 20) -->
  <g transform="translate(500, 100)">
    <rect width="340" height="150" rx="12" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
    <text x="170" y="32" fill="#047857" font-family="'Times New Roman', serif" font-size="18" font-weight="bold" text-anchor="middle">Nửa sau: N₂ = 20 phần tử</text>
    <text x="170" y="60" fill="#10B981" font-family="sans-serif" font-size="13" text-anchor="middle">Duyệt từng tập con sumB trong 2²⁰</text>
    
    <rect x="30" y="80" width="280" height="45" rx="6" fill="#D1FAE5"/>
    <text x="170" y="108" fill="#065F46" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Tìm kiếm nhị phân target - sumB trên mảng A</text>
  </g>

  <!-- Bottom Total Complexity Summary -->
  <g transform="translate(60, 270)">
    <rect width="780" height="45" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="390" y="28" fill="#0F172A" font-family="'Times New Roman', serif" font-size="14" font-weight="bold" text-anchor="middle">⚡ Tổng độ phức tạp: O(2^(N/2) × (N/2)) ≈ 20 × 10⁶ phép tính → Hoàn thành trong ~0.08 giây!</text>
  </g>
</svg>""",

    # -------------------------------------------------------------
    # LESSON 06: BITWISE & BITMASK
    # -------------------------------------------------------------
    "lesson-06-phep-toan-bit-va-bitmask-nang-cao/assets/l06_bitmask_operations_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <rect width="900" height="360" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Bảng tổng hợp các thao tác Thao tác Bitmask chuẩn thi đấu</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Biểu diễn tập hợp N phần tử bằng một số nguyên không âm mask (Bit thứ i = 1 nếu phần tử i được chọn, = 0 nếu không chọn).</text>

  <!-- Table Grid Layout -->
  <g transform="translate(40, 95)">
    <!-- Header -->
    <rect x="0" y="0" width="820" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="20" y="23" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="14" font-weight="bold">Thao tác tập hợp</text>
    <text x="260" y="23" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="14" font-weight="bold">Cú pháp C++ tối ưu</text>
    <text x="560" y="23" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="14" font-weight="bold">Ý nghĩa toán học</text>

    <!-- Row 1: Kiểm tra bit -->
    <rect x="0" y="35" width="820" height="38" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="20" y="60" fill="#1E293B" font-family="'Times New Roman', serif" font-size="13">1. Kiểm tra phần tử i có trong tập</text>
    <text x="260" y="60" fill="#2563EB" font-family="monospace" font-size="14" font-weight="bold">(mask &gt;&gt; i) &amp; 1  hoặc  mask &amp; (1 &lt;&lt; i)</text>
    <text x="560" y="60" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Kiểm tra bit thứ i là 1 hay 0</text>

    <!-- Row 2: Bật bit -->
    <rect x="0" y="73" width="820" height="38" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="20" y="98" fill="#1E293B" font-family="'Times New Roman', serif" font-size="13">2. Thêm phần tử i vào tập (Bật bit)</text>
    <text x="260" y="98" fill="#16A34A" font-family="monospace" font-size="14" font-weight="bold">mask = mask | (1 &lt;&lt; i)</text>
    <text x="560" y="98" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Gán bit thứ i thành 1</text>

    <!-- Row 3: Tắt bit -->
    <rect x="0" y="111" width="820" height="38" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="20" y="136" fill="#1E293B" font-family="'Times New Roman', serif" font-size="13">3. Xóa phần tử i khỏi tập (Tắt bit)</text>
    <text x="260" y="136" fill="#DC2626" font-family="monospace" font-size="14" font-weight="bold">mask = mask &amp; ~(1 &lt;&lt; i)</text>
    <text x="560" y="136" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Gán bit thứ i về 0</text>

    <!-- Row 4: Đảo bit -->
    <rect x="0" y="149" width="820" height="38" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="20" y="174" fill="#1E293B" font-family="'Times New Roman', serif" font-size="13">4. Đảo trạng thái phần tử i (Toggle)</text>
    <text x="260" y="174" fill="#D97706" font-family="monospace" font-size="14" font-weight="bold">mask = mask ^ (1 &lt;&lt; i)</text>
    <text x="560" y="174" fill="#475569" font-family="'Times New Roman', serif" font-size="13">0 → 1 hoặc 1 → 0</text>

    <!-- Row 5: Đếm số lượng phần tử -->
    <rect x="0" y="187" width="820" height="38" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="20" y="212" fill="#1E293B" font-family="'Times New Roman', serif" font-size="13">5. Đếm số phần tử trong tập</text>
    <text x="260" y="212" fill="#7C3AED" font-family="monospace" font-size="14" font-weight="bold">__builtin_popcountll(mask)</text>
    <text x="560" y="212" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Đếm số lượng bit 1 trong O(1)</text>

    <!-- Row 6: Duyệt tất cả tập con -->
    <rect x="0" y="225" width="820" height="38" fill="#EFF6FF" stroke="#3B82F6"/>
    <text x="20" y="250" fill="#1E3A8A" font-family="'Times New Roman', serif" font-size="13" font-weight="bold">6. Duyệt tập con của mask (Submask)</text>
    <text x="260" y="250" fill="#1D4ED8" font-family="monospace" font-size="13" font-weight="bold">for (int s = mask; s &gt; 0; s = (s - 1) &amp; mask)</text>
    <text x="560" y="250" fill="#1E40AF" font-family="'Times New Roman', serif" font-size="13" font-weight="bold">Duyệt 3^N thay vì 4^N</text>
  </g>
</svg>""",

    # -------------------------------------------------------------
    # LESSON 09: MONOTONIC STACK & DEQUE
    # -------------------------------------------------------------
    "lesson-09-ngan-xep-hang-doi-deque-don-dieu/assets/l09_monotonic_stack_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 330" width="100%" height="100%">
  <rect width="900" height="330" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Mô phỏng Ngăn xếp đơn điệu (Monotonic Stack) — Next Greater Element O(N)</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Duyệt mảng từ phải qua trái. Duy trì stack giảm dần: phần tử nào nhỏ hơn hoặc bằng A[i] sẽ bị pop ra ngoài.</text>

  <!-- Array Display -->
  <g transform="translate(60, 95)">
    <text x="0" y="20" fill="#1E293B" font-family="'Times New Roman', serif" font-size="15" font-weight="bold">Mảng ban đầu A:</text>
    
    <g transform="translate(140, 0)">
      <rect x="0" y="0" width="55" height="40" rx="6" fill="#F1F5F9" stroke="#CBD5E1"/>
      <text x="27" y="25" fill="#334155" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2</text>

      <rect x="65" y="0" width="55" height="40" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="92" y="25" fill="#1D4ED8" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">7</text>

      <rect x="130" y="0" width="55" height="40" rx="6" fill="#F1F5F9" stroke="#CBD5E1"/>
      <text x="157" y="25" fill="#334155" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">3</text>

      <rect x="195" y="0" width="55" height="40" rx="6" fill="#F1F5F9" stroke="#CBD5E1"/>
      <text x="222" y="25" fill="#334155" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">5</text>

      <rect x="260" y="0" width="55" height="40" rx="6" fill="#F1F5F9" stroke="#CBD5E1"/>
      <text x="287" y="25" fill="#334155" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">4</text>
    </g>
  </g>

  <!-- Simulation Step at i = 1 (A[i] = 7) -->
  <g transform="translate(60, 160)">
    <rect width="780" height="135" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    
    <!-- Stack container -->
    <g transform="translate(40, 20)">
      <rect x="0" y="0" width="160" height="95" rx="6" fill="#FFFFFF" stroke="#64748B" stroke-dasharray="4"/>
      <text x="80" y="22" fill="#475569" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">MONOTONIC STACK</text>
      
      <rect x="20" y="35" width="120" height="24" rx="4" fill="#FEE2E2" stroke="#EF4444"/>
      <text x="80" y="52" fill="#B91C1C" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Pop: 3, 5, 4 ≤ 7</text>

      <rect x="20" y="65" width="120" height="24" rx="4" fill="#DCFCE7" stroke="#22C55E"/>
      <text x="80" y="82" fill="#15803D" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Push: 7</text>
    </g>

    <!-- Arrow -->
    <g transform="translate(230, 50)">
      <line x1="0" y1="15" x2="40" y2="15" stroke="#3B82F6" stroke-width="3"/>
      <polygon points="45,15 35,10 35,20" fill="#3B82F6"/>
    </g>

    <!-- Explanation Box -->
    <g transform="translate(300, 20)">
      <text x="0" y="20" fill="#0F172A" font-family="'Times New Roman', serif" font-size="15" font-weight="bold">Tại vị trí A[1] = 7:</text>
      <text x="0" y="45" fill="#334155" font-family="'Times New Roman', serif" font-size="13">• Stack đang chứa [3, 5, 4]. Do 7 &gt; 3, 5, 4 nên 7 che khuất toàn bộ các phần tử này.</text>
      <text x="0" y="68" fill="#334155" font-family="'Times New Roman', serif" font-size="13">• Ta pop toàn bộ các phần tử ≤ 7 ra ngoài → Stack rỗng → Next Greater của 7 là <tspan fill="#DC2626" font-weight="bold">-1</tspan>.</text>
      <text x="0" y="90" fill="#15803D" font-family="'Times New Roman', serif" font-size="13" font-weight="bold">👉 Mỗi phần tử chỉ vào/ra stack đúng 1 lần → Độ phức tạp tuyến tính O(N)!</text>
    </g>
  </g>
</svg>""",

    # -------------------------------------------------------------
    # LESSON 12: ĐỒ THỊ (TARJAN & DIJKSTRA)
    # -------------------------------------------------------------
    "lesson-12-ly-thuyet-do-thi-chuyen-sau/assets/l12_tarjan_bridges_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 350" width="100%" height="100%">
  <rect width="900" height="350" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Thuật toán Tarjan tìm Khớp (Articulation Points) và Cầu (Bridges) trong O(V + E)</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Dựa trên mảng thời gian thăm tin[u] và mảng low[u] (thời gian thăm nhỏ nhất của đỉnh mà u có thể đi tới bằng 1 cạnh ngược).</text>

  <!-- Graph Layout -->
  <g transform="translate(60, 95)">
    <!-- Bridge Edge (1 - 3) -->
    <line x1="220" y1="60" x2="360" y2="60" stroke="#EF4444" stroke-width="4" stroke-dasharray="6"/>
    <text x="290" y="50" fill="#DC2626" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">CẦU (Bridge)</text>
    <text x="290" y="80" fill="#B91C1C" font-family="monospace" font-size="11" text-anchor="middle">low[3] &gt; tin[1]</text>

    <!-- Cycle 1 (1 - 2, 2 - 4, 4 - 1) -->
    <polygon points="80,130 180,30 80,30" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    
    <!-- Node 1 (Khớp) -->
    <circle cx="180" cy="60" r="24" fill="#FEE2E2" stroke="#EF4444" stroke-width="3"/>
    <text x="180" y="55" fill="#991B1B" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1</text>
    <text x="180" y="73" fill="#DC2626" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">KHỚP</text>

    <!-- Node 2 -->
    <circle cx="80" cy="30" r="20" fill="#DBEAFE" stroke="#3B82F6" stroke-width="2"/>
    <text x="80" y="36" fill="#1E40AF" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">2</text>

    <!-- Node 4 -->
    <circle cx="80" cy="130" r="20" fill="#DBEAFE" stroke="#3B82F6" stroke-width="2"/>
    <text x="80" y="136" fill="#1E40AF" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">4</text>

    <!-- Cycle 2 (3 - 5, 5 - 6, 6 - 3) -->
    <polygon points="380,60 480,20 480,120" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>

    <!-- Node 3 -->
    <circle cx="380" cy="60" r="20" fill="#D1FAE5" stroke="#10B981" stroke-width="2"/>
    <text x="380" y="66" fill="#065F46" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">3</text>

    <!-- Node 5 -->
    <circle cx="480" cy="20" r="20" fill="#D1FAE5" stroke="#10B981" stroke-width="2"/>
    <text x="480" y="26" fill="#065F46" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">5</text>

    <!-- Node 6 -->
    <circle cx="480" cy="120" r="20" fill="#D1FAE5" stroke="#10B981" stroke-width="2"/>
    <text x="480" y="126" fill="#065F46" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">6</text>
  </g>

  <!-- Rules Panel on Right -->
  <g transform="translate(580, 95)">
    <rect width="280" height="220" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
    <text x="20" y="30" fill="#0F172A" font-family="'Times New Roman', serif" font-size="15" font-weight="bold">📌 Điều kiện nhận diện:</text>
    
    <text x="20" y="65" fill="#B91C1C" font-family="'Times New Roman', serif" font-size="13" font-weight="bold">1. Cạnh (u, v) là CẦU khi:</text>
    <text x="35" y="88" fill="#DC2626" font-family="monospace" font-size="13" font-weight="bold">low[v] &gt; tin[u]</text>
    <text x="35" y="108" fill="#64748B" font-family="'Times New Roman', serif" font-size="11">(Nhánh v không có đường về tổ tiên của u)</text>

    <text x="20" y="145" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="13" font-weight="bold">2. Đỉnh u là KHỚP khi:</text>
    <text x="35" y="168" fill="#2563EB" font-family="monospace" font-size="13" font-weight="bold">low[v] ≥ tin[u]</text>
    <text x="35" y="188" fill="#64748B" font-family="'Times New Roman', serif" font-size="11">(Hoặc u là gốc cây DFS có ≥ 2 con)</text>
  </g>
</svg>""",

    # -------------------------------------------------------------
    # LESSON 13: SEGMENT TREE & FENWICK TREE
    # -------------------------------------------------------------
    "lesson-13-cay-phan-doan-segment-tree-va-fenwick-tree/assets/l13_segment_tree_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 370" width="100%" height="100%">
  <rect width="900" height="370" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Kiến trúc Cây phân đoạn (Segment Tree) quản lý dãy số N = 4 phần tử [1, 3, 5, 7]</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Mỗi nút quản lý tổng của đoạn [L, R]. Nút cha = Nút trái + Nút phải. Cập nhật và truy vấn trong O(log N).</text>

  <!-- Tree Structure -->
  <g transform="translate(50, 95)">
    <!-- Edges -->
    <line x1="400" y1="30" x2="200" y2="105" stroke="#94A3B8" stroke-width="2"/>
    <line x1="400" y1="30" x2="600" y2="105" stroke="#94A3B8" stroke-width="2"/>

    <line x1="200" y1="125" x2="100" y2="200" stroke="#94A3B8" stroke-width="2"/>
    <line x1="200" y1="125" x2="300" y2="200" stroke="#94A3B8" stroke-width="2"/>

    <line x1="600" y1="125" x2="500" y2="200" stroke="#94A3B8" stroke-width="2"/>
    <line x1="600" y1="125" x2="700" y2="200" stroke="#94A3B8" stroke-width="2"/>

    <!-- Root Node: [1..4] Sum = 16 -->
    <g transform="translate(340, 10)">
      <rect width="120" height="45" rx="8" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
      <text x="60" y="20" fill="#92400E" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Nút 1: [1..4]</text>
      <text x="60" y="38" fill="#B45309" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">Sum = 16</text>
    </g>

    <!-- Level 1 Left: [1..2] Sum = 4 -->
    <g transform="translate(140, 100)">
      <rect width="120" height="45" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="60" y="20" fill="#1E40AF" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Nút 2: [1..2]</text>
      <text x="60" y="38" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">Sum = 4</text>
    </g>

    <!-- Level 1 Right: [3..4] Sum = 12 -->
    <g transform="translate(540, 100)">
      <rect width="120" height="45" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="60" y="20" fill="#1E40AF" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Nút 3: [3..4]</text>
      <text x="60" y="38" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle">Sum = 12</text>
    </g>

    <!-- Leaves -->
    <!-- Leaf [1..1] = 1 -->
    <g transform="translate(50, 195)">
      <rect width="100" height="45" rx="8" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
      <text x="50" y="20" fill="#166534" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Nút 4: [1..1]</text>
      <text x="50" y="38" fill="#15803D" font-family="'Times New Roman', serif" font-size="15" font-weight="bold" text-anchor="middle">A[1] = 1</text>
    </g>

    <!-- Leaf [2..2] = 3 -->
    <g transform="translate(250, 195)">
      <rect width="100" height="45" rx="8" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
      <text x="50" y="20" fill="#166534" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Nút 5: [2..2]</text>
      <text x="50" y="38" fill="#15803D" font-family="'Times New Roman', serif" font-size="15" font-weight="bold" text-anchor="middle">A[2] = 3</text>
    </g>

    <!-- Leaf [3..3] = 5 -->
    <g transform="translate(450, 195)">
      <rect width="100" height="45" rx="8" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
      <text x="50" y="20" fill="#166534" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Nút 6: [3..3]</text>
      <text x="50" y="38" fill="#15803D" font-family="'Times New Roman', serif" font-size="15" font-weight="bold" text-anchor="middle">A[3] = 5</text>
    </g>

    <!-- Leaf [4..4] = 7 -->
    <g transform="translate(650, 195)">
      <rect width="100" height="45" rx="8" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
      <text x="50" y="20" fill="#166534" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Nút 7: [4..4]</text>
      <text x="50" y="38" fill="#15803D" font-family="'Times New Roman', serif" font-size="15" font-weight="bold" text-anchor="middle">A[4] = 7</text>
    </g>
  </g>

  <!-- Bottom Banner -->
  <g transform="translate(50, 310)">
    <rect width="800" height="40" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="400" y="25" fill="#1E293B" font-family="'Times New Roman', serif" font-size="13" font-weight="bold" text-anchor="middle">💡 Quy tắc chỉ số: Nút id có con trái là 2 × id và con phải là 2 × id + 1. Mảng cây cần kích thước 4N.</text>
  </g>
</svg>""",

    "lesson-13-cay-phan-doan-segment-tree-va-fenwick-tree/assets/l13_fenwick_tree_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 340" width="100%" height="100%">
  <rect width="900" height="340" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Cấu trúc Cây nhị phân Fenwick Tree (Binary Indexed Tree — BIT) &amp; Hàm lowbit</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Mỗi BIT[i] quản lý một đoạn có độ dài đúng bằng lowbit(i) = i &amp; (-i), kết thúc tại chỉ số i.</text>

  <!-- BIT Bars -->
  <g transform="translate(60, 100)">
    <!-- 1: BIT[1] length 1 -->
    <g transform="translate(0, 130)">
      <rect width="85" height="35" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
      <text x="42" y="22" fill="#1D4ED8" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">BIT[1]: [1..1]</text>
    </g>

    <!-- 2: BIT[2] length 2 -->
    <g transform="translate(0, 90)">
      <rect width="180" height="35" rx="4" fill="#DBEAFE" stroke="#2563EB" stroke-width="1.5"/>
      <text x="90" y="22" fill="#1E40AF" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">BIT[2]: [1..2] (len=2)</text>
    </g>

    <!-- 3: BIT[3] length 1 -->
    <g transform="translate(190, 130)">
      <rect width="85" height="35" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
      <text x="42" y="22" fill="#1D4ED8" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">BIT[3]: [3..3]</text>
    </g>

    <!-- 4: BIT[4] length 4 -->
    <g transform="translate(0, 50)">
      <rect width="370" height="35" rx="4" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
      <text x="185" y="22" fill="#92400E" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">BIT[4]: [1..4] (len=4)</text>
    </g>

    <!-- 5: BIT[5] length 1 -->
    <g transform="translate(380, 130)">
      <rect width="85" height="35" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
      <text x="42" y="22" fill="#1D4ED8" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">BIT[5]: [5..5]</text>
    </g>

    <!-- 6: BIT[6] length 2 -->
    <g transform="translate(380, 90)">
      <rect width="180" height="35" rx="4" fill="#DBEAFE" stroke="#2563EB" stroke-width="1.5"/>
      <text x="90" y="22" fill="#1E40AF" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">BIT[6]: [5..6] (len=2)</text>
    </g>

    <!-- 7: BIT[7] length 1 -->
    <g transform="translate(570, 130)">
      <rect width="85" height="35" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
      <text x="42" y="22" fill="#1D4ED8" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">BIT[7]: [7..7]</text>
    </g>

    <!-- 8: BIT[8] length 8 -->
    <g transform="translate(0, 10)">
      <rect width="760" height="35" rx="4" fill="#DCFCE7" stroke="#10B981" stroke-width="2"/>
      <text x="380" y="22" fill="#065F46" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">BIT[8]: [1..8] (len=8) — Quản lý toàn bộ 8 phần tử</text>
    </g>
  </g>

  <!-- Bottom Tip -->
  <g transform="translate(60, 280)">
    <rect width="760" height="40" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
    <text x="380" y="25" fill="#334155" font-family="'Times New Roman', serif" font-size="13" font-weight="bold" text-anchor="middle">⚡ Thao tác: Truy vấn tổng i -= lowbit(i)  •  Cập nhật giá trị i += lowbit(i)  (Code cực ngắn chỉ 5 dòng!)</text>
  </g>
</svg>""",

    # -------------------------------------------------------------
    # LESSON 15: STRING HASHING & TRIE
    # -------------------------------------------------------------
    "lesson-15-xu-ly-chuoi-string-hashing-va-bigint/assets/l15_trie_tree_visual.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 350" width="100%" height="100%">
  <rect width="900" height="350" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <text x="40" y="42" fill="#0F2A44" font-family="'Times New Roman', serif" font-size="20" font-weight="bold">Kiến trúc Cây tiền tố (Trie) lưu trữ tập từ: {"cat", "cap", "car", "dog"}</text>
  <text x="40" y="68" fill="#475569" font-family="'Times New Roman', serif" font-size="13">Các từ có chung tiền tố sẽ dùng chung các nút nhánh ban đầu. Tìm kiếm từ độ dài L chỉ mất O(L).</text>

  <!-- Trie Layout -->
  <g transform="translate(100, 95)">
    <!-- Root -->
    <circle cx="350" cy="20" r="22" fill="#F1F5F9" stroke="#475569" stroke-width="2"/>
    <text x="350" y="25" fill="#0F172A" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Root</text>

    <!-- Branch 'c' and 'd' -->
    <line x1="335" y1="38" x2="220" y2="95" stroke="#3B82F6" stroke-width="2"/>
    <text x="265" y="60" fill="#2563EB" font-family="monospace" font-size="14" font-weight="bold">'c'</text>

    <line x1="365" y1="38" x2="480" y2="95" stroke="#F59E0B" stroke-width="2"/>
    <text x="435" y="60" fill="#D97706" font-family="monospace" font-size="14" font-weight="bold">'d'</text>

    <!-- Node 'c' -->
    <circle cx="220" cy="105" r="20" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <text x="220" y="111" fill="#1D4ED8" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">c</text>

    <!-- Node 'd' -->
    <circle cx="480" cy="105" r="20" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
    <text x="480" y="111" fill="#B45309" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">d</text>

    <!-- Branch 'a' from 'c' -->
    <line x1="220" y1="125" x2="220" y2="175" stroke="#3B82F6" stroke-width="2"/>
    <text x="205" y="155" fill="#2563EB" font-family="monospace" font-size="14" font-weight="bold">'a'</text>

    <!-- Node 'a' -->
    <circle cx="220" cy="185" r="20" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <text x="220" y="191" fill="#1D4ED8" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">a</text>

    <!-- Branch 'o' from 'd' -->
    <line x1="480" y1="125" x2="480" y2="175" stroke="#F59E0B" stroke-width="2"/>
    <text x="495" y="155" fill="#D97706" font-family="monospace" font-size="14" font-weight="bold">'o'</text>

    <!-- Node 'o' -->
    <circle cx="480" cy="185" r="20" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
    <text x="480" y="191" fill="#B45309" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">o</text>

    <!-- Branches from 'a': 't', 'p', 'r' -->
    <line x1="205" y1="198" x2="120" y2="250" stroke="#10B981" stroke-width="2"/>
    <text x="150" y="220" fill="#059669" font-family="monospace" font-size="13" font-weight="bold">'t'</text>

    <line x1="220" y1="205" x2="220" y2="250" stroke="#10B981" stroke-width="2"/>
    <text x="230" y="235" fill="#059669" font-family="monospace" font-size="13" font-weight="bold">'p'</text>

    <line x1="235" y1="198" x2="320" y2="250" stroke="#10B981" stroke-width="2"/>
    <text x="290" y="220" fill="#059669" font-family="monospace" font-size="13" font-weight="bold">'r'</text>

    <!-- End Nodes (Words) -->
    <!-- 't' -> "cat" -->
    <circle cx="120" cy="260" r="20" fill="#DCFCE7" stroke="#10B981" stroke-width="3"/>
    <text x="120" y="266" fill="#047857" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">t*</text>

    <!-- 'p' -> "cap" -->
    <circle cx="220" cy="260" r="20" fill="#DCFCE7" stroke="#10B981" stroke-width="3"/>
    <text x="220" y="266" fill="#047857" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">p*</text>

    <!-- 'r' -> "car" -->
    <circle cx="320" cy="260" r="20" fill="#DCFCE7" stroke="#10B981" stroke-width="3"/>
    <text x="320" y="266" fill="#047857" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">r*</text>

    <!-- Branch 'g' from 'o' -> "dog" -->
    <line x1="480" y1="205" x2="480" y2="250" stroke="#10B981" stroke-width="2"/>
    <text x="495" y="235" fill="#059669" font-family="monospace" font-size="13" font-weight="bold">'g'</text>

    <circle cx="480" cy="260" r="20" fill="#DCFCE7" stroke="#10B981" stroke-width="3"/>
    <text x="480" y="266" fill="#047857" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">g*</text>
  </g>

  <!-- Legend on Right -->
  <g transform="translate(620, 110)">
    <rect width="240" height="190" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
    <text x="20" y="30" fill="#0F172A" font-family="'Times New Roman', serif" font-size="14" font-weight="bold">📌 Ghi chú ký hiệu:</text>
    <text x="20" y="65" fill="#15803D" font-family="'Times New Roman', serif" font-size="13" font-weight="bold">• Dấu * (Màu xanh):</text>
    <text x="30" y="85" fill="#334155" font-family="'Times New Roman', serif" font-size="12">Đánh dấu kết thúc một từ hoàn chỉnh (`is_end = true`).</text>

    <text x="20" y="125" fill="#1D4ED8" font-family="'Times New Roman', serif" font-size="13" font-weight="bold">• Tiết kiệm bộ nhớ:</text>
    <text x="30" y="145" fill="#334155" font-family="'Times New Roman', serif" font-size="12">3 từ "cat", "cap", "car" dùng chung nút 'c' và 'a'.</text>
  </g>
</svg>""",
}

def main():
    print("🎨 Đang khởi tạo toàn bộ hệ thống SVG minh họa sáng màu chuẩn in ấn cho Level 2...")
    total = 0
    for rel_path, content in SVG_FILES.items():
        full_path = BASE_DIR / "lessons" / rel_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"  ✅ Đã tạo SVG: {rel_path}")
        total += 1
    print(f"🎉 Hoàn tất tạo {total} sơ đồ minh họa vector chuẩn Light Theme!")

if __name__ == "__main__":
    main()
