#!/usr/bin/env python3
"""
create_l0_assets.py
Tạo các SVG và PNG chuẩn 1600px cho Bài 01, Bài 02, Bài 03:
- Lesson 01:
  1. input_process_output_pipeline_vi (Mô hình Input - Process - Output và Vòng đời dữ liệu)
  2. cpp_data_types_memory_vi (Hệ thống kiểu dữ liệu C++ và Giới hạn tràn số)
- Lesson 02:
  1. if_else_control_flow_vi (Sơ đồ khối luồng rẽ nhánh if-else và Bẫy logic)
  2. loop_dry_run_trace_vi (Mô hình 4 mẫu tích lũy và Bảng trace vòng lặp)
- Lesson 03:
  1. vector_array_memory_layout_vi (Cấu trúc bộ nhớ Mảng & Vector 0-based indexing)
  2. ascii_frequency_table_vi (Kỹ thuật Trừ mã ASCII c - 'a' và Bảng đếm tần suất)
"""

import os
import subprocess
from pathlib import Path

BASE_DIR = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b")
LESSONS_DIR = BASE_DIR / "lessons"

# Ensure assets dirs exist
for l in [1, 2, 3]:
    ldir = list(LESSONS_DIR.glob(f"lesson-{l:02d}*"))[0]
    (ldir / "assets").mkdir(parents=True, exist_ok=True)

# SVG 1: Lesson 01 - IPO
svg_l1_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 450" width="1000" height="450" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <linearGradient id="gradInput" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6"/>
      <stop offset="100%" stop-color="#1D4ED8"/>
    </linearGradient>
    <linearGradient id="gradProcess" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="gradOutput" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8B5CF6"/>
      <stop offset="100%" stop-color="#6D28D9"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.1"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748B"/>
    </marker>
  </defs>

  <text x="500" y="45" text-anchor="middle" font-size="22" font-weight="bold" fill="#0F172A">MÔ HÌNH INPUT – PROCESS – OUTPUT TRONG LẬP TRÌNH C++</text>
  <text x="500" y="75" text-anchor="middle" font-size="14" fill="#64748B">Quy trình xử lý dữ liệu chuẩn thi đấu: Nhập an toàn → Biến đổi thuật toán → Xuất định dạng</text>

  <!-- Box 1: Input -->
  <g transform="translate(60, 110)" filter="url(#shadow)">
    <rect width="240" height="260" rx="16" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
    <rect width="240" height="55" rx="16" fill="url(#gradInput)"/>
    <text x="120" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#FFFFFF">1. ĐẦU VÀO (INPUT)</text>
    <text x="20" y="90" font-size="14" font-weight="bold" fill="#1E293B">• cin &gt;&gt; a &gt;&gt; b;</text>
    <text x="35" y="115" font-size="12" fill="#64748B">Đọc từ bàn phím / file</text>
    <text x="20" y="150" font-weight="bold" font-size="14" fill="#1E293B">• Safe Input Pattern:</text>
    <text x="35" y="175" font-size="12" fill="#0284C7" font-family="Consolas">if (!(cin &gt;&gt; n)) return 0;</text>
    <text x="20" y="210" font-size="14" font-weight="bold" fill="#1E293B">• Fast I/O Boilerplate:</text>
    <text x="35" y="235" font-size="11" fill="#475569" font-family="Consolas">ios::sync_with_stdio(0);</text>
  </g>

  <!-- Arrow 1 -->
  <line x1="320" y1="240" x2="370" y2="240" stroke="#64748B" stroke-width="3" marker-end="url(#arrow)"/>

  <!-- Box 2: Process -->
  <g transform="translate(380, 110)" filter="url(#shadow)">
    <rect width="240" height="260" rx="16" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
    <rect width="240" height="55" rx="16" fill="url(#gradProcess)"/>
    <text x="120" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#FFFFFF">2. XỬ LÝ (PROCESS)</text>
    <text x="20" y="90" font-size="14" font-weight="bold" fill="#1E293B">• Khai báo &amp; Tính toán:</text>
    <text x="35" y="115" font-size="12" fill="#047857" font-family="Consolas">long long sum = a + b;</text>
    <text x="20" y="150" font-size="14" font-weight="bold" fill="#1E293B">• Ép kiểu thực:</text>
    <text x="35" y="175" font-size="12" fill="#047857" font-family="Consolas">double avg = 1.0 * sum / n;</text>
    <text x="20" y="210" font-size="14" font-weight="bold" fill="#1E293B">• Toán tử / và %:</text>
    <text x="35" y="235" font-size="12" fill="#64748B">Tách chữ số &amp; Chia nguyên</text>
  </g>

  <!-- Arrow 2 -->
  <line x1="640" y1="240" x2="690" y2="240" stroke="#64748B" stroke-width="3" marker-end="url(#arrow)"/>

  <!-- Box 3: Output -->
  <g transform="translate(700, 110)" filter="url(#shadow)">
    <rect width="240" height="260" rx="16" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
    <rect width="240" height="55" rx="16" fill="url(#gradOutput)"/>
    <text x="120" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#FFFFFF">3. ĐẦU RA (OUTPUT)</text>
    <text x="20" y="90" font-size="14" font-weight="bold" fill="#1E293B">• cout &lt;&lt; res &lt;&lt; '\n';</text>
    <text x="35" y="115" font-size="12" fill="#64748B">Ưu tiên '\n' hơn endl</text>
    <text x="20" y="150" font-size="14" font-weight="bold" fill="#1E293B">• In số thực cố định:</text>
    <text x="35" y="175" font-size="12" fill="#6D28D9" font-family="Consolas">cout &lt;&lt; fixed;</text>
    <text x="35" y="195" font-size="12" fill="#6D28D9" font-family="Consolas">cout &lt;&lt; setprecision(2);</text>
    <text x="20" y="235" font-size="13" font-weight="bold" fill="#1E293B">→ In đúng định dạng đề bài</text>
  </g>
</svg>"""

# SVG 2: Lesson 01 - Data types & Overflow
svg_l1_2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 450" width="1000" height="450" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="sh2" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-opacity="0.08"/>
    </filter>
  </defs>

  <text x="500" y="45" text-anchor="middle" font-size="22" font-weight="bold" fill="#0F172A">HỆ THỐNG KIỂU DỮ LIỆU C++ &amp; GIỚI HẠN TRÀN SỐ</text>
  <text x="500" y="75" text-anchor="middle" font-size="14" fill="#64748B">Quy tắc vàng: Tổng/Tích vượt 2 × 10^9 bắt buộc dùng long long</text>

  <!-- Table Header -->
  <g transform="translate(60, 105)">
    <rect width="880" height="45" rx="8" fill="#1E293B"/>
    <text x="100" y="28" fill="#FFFFFF" font-weight="bold" font-size="15" text-anchor="middle">Kiểu dữ liệu</text>
    <text x="240" y="28" fill="#FFFFFF" font-weight="bold" font-size="15" text-anchor="middle">Kích thước</text>
    <text x="470" y="28" fill="#FFFFFF" font-weight="bold" font-size="15" text-anchor="middle">Phạm vi giá trị xấp xỉ</text>
    <text x="750" y="28" fill="#FFFFFF" font-weight="bold" font-size="15" text-anchor="middle">Tử huyệt lập trình</text>
  </g>

  <!-- Row 1: int -->
  <g transform="translate(60, 160)" filter="url(#sh2)">
    <rect width="880" height="55" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="100" y="33" fill="#0284C7" font-family="Consolas" font-weight="bold" font-size="16" text-anchor="middle">int</text>
    <text x="240" y="33" fill="#334155" font-size="14" text-anchor="middle">32-bit (4 Bytes)</text>
    <text x="470" y="33" fill="#0F172A" font-size="14" text-anchor="middle">-2 × 10^9 đến +2 × 10^9</text>
    <text x="750" y="33" fill="#DC2626" font-weight="bold" font-size="13" text-anchor="middle">Tràn số nếu tích &gt; 2 × 10^9</text>
  </g>

  <!-- Row 2: long long -->
  <g transform="translate(60, 225)" filter="url(#sh2)">
    <rect width="880" height="55" rx="8" fill="#EFF6FF" stroke="#BFDBFE"/>
    <text x="100" y="33" fill="#2563EB" font-family="Consolas" font-weight="bold" font-size="16" text-anchor="middle">long long</text>
    <text x="240" y="33" fill="#1E40AF" font-size="14" text-anchor="middle">64-bit (8 Bytes)</text>
    <text x="470" y="33" fill="#1E40AF" font-weight="bold" font-size="14" text-anchor="middle">-9 × 10^18 đến +9 × 10^18</text>
    <text x="750" y="33" fill="#059669" font-weight="bold" font-size="13" text-anchor="middle">Khởi tạo hậu tố: 1LL, 0LL</text>
  </g>

  <!-- Row 3: double -->
  <g transform="translate(60, 290)" filter="url(#sh2)">
    <rect width="880" height="55" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="100" y="33" fill="#0D9488" font-family="Consolas" font-weight="bold" font-size="16" text-anchor="middle">double</text>
    <text x="240" y="33" fill="#334155" font-size="14" text-anchor="middle">64-bit (8 Bytes)</text>
    <text x="470" y="33" fill="#0F172A" font-size="14" text-anchor="middle">15-17 chữ số có nghĩa</text>
    <text x="750" y="33" fill="#D97706" font-weight="bold" font-size="13" text-anchor="middle">Sai số dấu phẩy động (EPS)</text>
  </g>

  <!-- Row 4: char / string -->
  <g transform="translate(60, 355)" filter="url(#sh2)">
    <rect width="880" height="55" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="100" y="33" fill="#7C3AED" font-family="Consolas" font-weight="bold" font-size="16" text-anchor="middle">char / string</text>
    <text x="240" y="33" fill="#334155" font-size="14" text-anchor="middle">1 Byte / Động</text>
    <text x="470" y="33" fill="#0F172A" font-size="14" text-anchor="middle">Bảng mã ASCII 0..255</text>
    <text x="750" y="33" fill="#6D28D9" font-weight="bold" font-size="13" text-anchor="middle">Trừ mã ký tự: c - '0', c - 'a'</text>
  </g>
</svg>"""

# SVG 3: Lesson 02 - Control Flow
svg_l2_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 450" width="1000" height="450" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <marker id="ar2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#475569"/>
    </marker>
    <filter id="sh3" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-opacity="0.08"/>
    </filter>
  </defs>

  <text x="500" y="45" text-anchor="middle" font-size="22" font-weight="bold" fill="#0F172A">LUỒNG RẼ NHÁNH IF – ELSE &amp; CÁC BẪY LOGIC THƯỜNG GẶP</text>
  <text x="500" y="75" text-anchor="middle" font-size="14" fill="#64748B">Kiểm soát điều kiện biên và chuỗi rẽ nhánh loại trừ tương hỗ</text>

  <!-- Start Node -->
  <rect x="420" y="105" width="160" height="45" rx="22" fill="#3B82F6" filter="url(#sh3)"/>
  <text x="500" y="133" text-anchor="middle" fill="#FFFFFF" font-weight="bold" font-size="15">Bắt đầu điều kiện</text>

  <line x1="500" y1="150" x2="500" y2="185" stroke="#475569" stroke-width="2" marker-end="url(#ar2)"/>

  <!-- Decision Diamond -->
  <polygon points="500,185 640,240 500,295 360,240" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2" filter="url(#sh3)"/>
  <text x="500" y="235" text-anchor="middle" font-weight="bold" font-size="14" fill="#92400E">Kiểm tra biểu thức</text>
  <text x="500" y="255" text-anchor="middle" font-family="Consolas" font-size="13" fill="#B45309">condition == true ?</text>

  <!-- True Branch -->
  <line x1="640" y1="240" x2="740" y2="240" stroke="#059669" stroke-width="2" marker-end="url(#ar2)"/>
  <text x="680" y="230" fill="#059669" font-weight="bold" font-size="14">ĐÚNG</text>
  <rect x="740" y="210" width="180" height="60" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="2" filter="url(#sh3)"/>
  <text x="830" y="235" text-anchor="middle" font-weight="bold" font-size="13" fill="#065F46">Khối lệnh if { ... }</text>
  <text x="830" y="255" text-anchor="middle" font-size="12" fill="#047857">Thực thi khi thỏa mãn</text>

  <!-- False Branch -->
  <line x1="360" y1="240" x2="260" y2="240" stroke="#DC2626" stroke-width="2" marker-end="url(#ar2)"/>
  <text x="300" y="230" fill="#DC2626" font-weight="bold" font-size="14">SAI</text>
  <rect x="80" y="210" width="180" height="60" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-width="2" filter="url(#sh3)"/>
  <text x="170" y="235" text-anchor="middle" font-weight="bold" font-size="13" fill="#991B1B">Khối lệnh else { ... }</text>
  <text x="170" y="255" text-anchor="middle" font-size="12" fill="#B91C1C">Thực thi khi phủ định</text>

  <!-- Join -->
  <path d="M 830 270 L 830 350 L 520 350" fill="none" stroke="#475569" stroke-width="2"/>
  <path d="M 170 270 L 170 350 L 480 350" fill="none" stroke="#475569" stroke-width="2"/>
  <line x1="500" y1="350" x2="500" y2="380" stroke="#475569" stroke-width="2" marker-end="url(#ar2)"/>

  <rect x="410" y="385" width="180" height="45" rx="10" fill="#1E293B" filter="url(#sh3)"/>
  <text x="500" y="413" text-anchor="middle" fill="#FFFFFF" font-weight="bold" font-size="14">Tiếp tục chương trình</text>
</svg>"""

# SVG 4: Lesson 02 - Accumulation patterns
svg_l2_2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 450" width="1000" height="450" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="sh4" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-opacity="0.08"/>
    </filter>
  </defs>

  <text x="500" y="45" text-anchor="middle" font-size="22" font-weight="bold" fill="#0F172A">4 MẪU TÍCH LŨY (ACCUMULATION PATTERNS) KINH ĐIỂN</text>
  <text x="500" y="75" text-anchor="middle" font-size="14" fill="#64748B">Nền tảng xử lý mọi bài toán duyệt dãy số: Khởi tạo đúng → Cập nhật trong vòng lặp</text>

  <!-- Pattern 1: Sum -->
  <g transform="translate(60, 105)" filter="url(#sh4)">
    <rect width="200" height="300" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
    <rect width="200" height="50" rx="12" fill="#3B82F6"/>
    <text x="100" y="32" text-anchor="middle" fill="#FFFFFF" font-weight="bold" font-size="16">1. TÍNH TỔNG (SUM)</text>
    <text x="15" y="80" font-size="13" font-weight="bold" fill="#1E293B">Khởi tạo:</text>
    <text x="15" y="105" font-family="Consolas" font-size="13" fill="#2563EB">long long S = 0;</text>
    <text x="15" y="145" font-size="13" font-weight="bold" fill="#1E293B">Cập nhật lặp:</text>
    <text x="15" y="170" font-family="Consolas" font-size="13" fill="#059669">S += a[i];</text>
    <text x="15" y="210" font-size="13" font-weight="bold" fill="#1E293B">Bẫy tử huyệt:</text>
    <text x="15" y="235" font-size="12" fill="#DC2626">Tràn số int khi N lớn</text>
    <text x="15" y="260" font-size="12" fill="#DC2626">Quên gán S = 0 ban đầu</text>
  </g>

  <!-- Pattern 2: Count -->
  <g transform="translate(280, 105)" filter="url(#sh4)">
    <rect width="200" height="300" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
    <rect width="200" height="50" rx="12" fill="#10B981"/>
    <text x="100" y="32" text-anchor="middle" fill="#FFFFFF" font-weight="bold" font-size="16">2. ĐẾM (COUNT)</text>
    <text x="15" y="80" font-size="13" font-weight="bold" fill="#1E293B">Khởi tạo:</text>
    <text x="15" y="105" font-family="Consolas" font-size="13" fill="#059669">int cnt = 0;</text>
    <text x="15" y="145" font-size="13" font-weight="bold" fill="#1E293B">Cập nhật lặp:</text>
    <text x="15" y="170" font-family="Consolas" font-size="12" fill="#047857">if (thoa_man) cnt++;</text>
    <text x="15" y="210" font-size="13" font-weight="bold" fill="#1E293B">Ứng dụng:</text>
    <text x="15" y="235" font-size="12" fill="#475569">Đếm số chẵn / lẻ</text>
    <text x="15" y="260" font-size="12" fill="#475569">Đếm ước số nguyên</text>
  </g>

  <!-- Pattern 3: Max -->
  <g transform="translate(500, 105)" filter="url(#sh4)">
    <rect width="200" height="300" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
    <rect width="200" height="50" rx="12" fill="#F59E0B"/>
    <text x="100" y="32" text-anchor="middle" fill="#FFFFFF" font-weight="bold" font-size="16">3. TÌM MAX</text>
    <text x="15" y="80" font-size="13" font-weight="bold" fill="#1E293B">Khởi tạo:</text>
    <text x="15" y="105" font-family="Consolas" font-size="12" fill="#D97706">long long mx = -1e18;</text>
    <text x="15" y="125" font-size="11" fill="#64748B">(hoặc mx = a[0])</text>
    <text x="15" y="155" font-size="13" font-weight="bold" fill="#1E293B">Cập nhật lặp:</text>
    <text x="15" y="180" font-family="Consolas" font-size="12" fill="#059669">mx = max(mx, a[i]);</text>
    <text x="15" y="210" font-size="13" font-weight="bold" fill="#1E293B">Bẫy tử huyệt:</text>
    <text x="15" y="235" font-size="12" fill="#DC2626">Gán mx = 0 khi mảng</text>
    <text x="15" y="255" font-size="12" fill="#DC2626">chứa toàn số âm!</text>
  </g>

  <!-- Pattern 4: Min -->
  <g transform="translate(720, 105)" filter="url(#sh4)">
    <rect width="200" height="300" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
    <rect width="200" height="50" rx="12" fill="#8B5CF6"/>
    <text x="100" y="32" text-anchor="middle" fill="#FFFFFF" font-weight="bold" font-size="16">4. TÌM MIN</text>
    <text x="15" y="80" font-size="13" font-weight="bold" fill="#1E293B">Khởi tạo:</text>
    <text x="15" y="105" font-family="Consolas" font-size="12" fill="#7C3AED">long long mn = 1e18;</text>
    <text x="15" y="125" font-size="11" fill="#64748B">(hoặc mn = a[0])</text>
    <text x="15" y="155" font-size="13" font-weight="bold" fill="#1E293B">Cập nhật lặp:</text>
    <text x="15" y="180" font-family="Consolas" font-size="12" fill="#059669">mn = min(mn, a[i]);</text>
    <text x="15" y="210" font-size="13" font-weight="bold" fill="#1E293B">Bẫy tử huyệt:</text>
    <text x="15" y="235" font-size="12" fill="#DC2626">Khởi tạo INT_MAX bị</text>
    <text x="15" y="255" font-size="12" fill="#DC2626">tràn khi cộng thêm</text>
  </g>
</svg>"""

# SVG 5: Lesson 03 - Vector Memory Layout
svg_l3_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 450" width="1000" height="450" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="sh5" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-opacity="0.08"/>
    </filter>
  </defs>

  <text x="500" y="45" text-anchor="middle" font-size="22" font-weight="bold" fill="#0F172A">CẤU TRÚC BỘ NHỚ VECTOR &amp; QUY TẮC CHỈ SỐ 0-BASED</text>
  <text x="500" y="75" text-anchor="middle" font-size="14" fill="#64748B">Vector lưu trữ các phần tử liên tiếp trong bộ nhớ: a[0] đến a[N - 1]</text>

  <!-- Vector Visualization -->
  <g transform="translate(100, 120)">
    <!-- Indices -->
    <text x="70" y="20" text-anchor="middle" font-size="14" font-weight="bold" fill="#64748B">Chỉ số (Index):</text>
    <text x="210" y="20" text-anchor="middle" font-family="Consolas" font-size="16" font-weight="bold" fill="#2563EB">0</text>
    <text x="330" y="20" text-anchor="middle" font-family="Consolas" font-size="16" font-weight="bold" fill="#2563EB">1</text>
    <text x="450" y="20" text-anchor="middle" font-family="Consolas" font-size="16" font-weight="bold" fill="#2563EB">2</text>
    <text x="570" y="20" text-anchor="middle" font-family="Consolas" font-size="16" font-weight="bold" fill="#2563EB">3</text>
    <text x="690" y="20" text-anchor="middle" font-family="Consolas" font-size="16" font-weight="bold" fill="#2563EB">4 (N-1)</text>

    <!-- Cells -->
    <g transform="translate(150, 40)" filter="url(#sh5)">
      <rect x="0" y="0" width="120" height="80" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="60" y="48" text-anchor="middle" font-family="Consolas" font-size="22" font-weight="bold" fill="#1E3A8A">15</text>
      <text x="60" y="105" text-anchor="middle" font-size="12" fill="#64748B">a.front()</text>

      <rect x="120" y="0" width="120" height="80" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="180" y="48" text-anchor="middle" font-family="Consolas" font-size="22" font-weight="bold" fill="#1E3A8A">28</text>

      <rect x="240" y="0" width="120" height="80" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="300" y="48" text-anchor="middle" font-family="Consolas" font-size="22" font-weight="bold" fill="#1E3A8A">42</text>

      <rect x="360" y="0" width="120" height="80" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="420" y="48" text-anchor="middle" font-family="Consolas" font-size="22" font-weight="bold" fill="#1E3A8A">9</text>

      <rect x="480" y="0" width="120" height="80" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <text x="540" y="48" text-anchor="middle" font-family="Consolas" font-size="22" font-weight="bold" fill="#1E3A8A">73</text>
      <text x="540" y="105" text-anchor="middle" font-size="12" fill="#64748B">a.back()</text>
    </g>
  </g>

  <!-- Operations Summary Box -->
  <g transform="translate(100, 280)" filter="url(#sh5)">
    <rect width="800" height="130" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
    <text x="30" y="35" font-size="15" font-weight="bold" fill="#0F172A">CÁC THAO TÁC CỐT LÕI CỦA VECTOR TRONG THI ĐẤU:</text>
    <text x="30" y="70" font-family="Consolas" font-size="14" fill="#0284C7">• a.push_back(x);</text>
    <text x="230" y="70" font-size="13" fill="#475569">Thêm x vào cuối mảng — O(1)</text>

    <text x="30" y="105" font-family="Consolas" font-size="14" fill="#0284C7">• a.pop_back();</text>
    <text x="230" y="105" font-size="13" fill="#475569">Xóa phần tử cuối cùng — O(1)</text>

    <text x="450" y="70" font-family="Consolas" font-size="14" fill="#059669">• a.size();</text>
    <text x="560" y="70" font-size="13" fill="#475569">Lấy số lượng phần tử</text>

    <text x="450" y="105" font-family="Consolas" font-size="14" fill="#DC2626">• Truy cập a[i]:</text>
    <text x="560" y="105" font-size="13" fill="#DC2626">Chỉ số 0 đến N - 1 (Cấm a[N])</text>
  </g>
</svg>"""

# SVG 6: Lesson 03 - ASCII frequency
svg_l3_2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 450" width="1000" height="450" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="sh6" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-opacity="0.08"/>
    </filter>
  </defs>

  <text x="500" y="45" text-anchor="middle" font-size="22" font-weight="bold" fill="#0F172A">KỸ THUẬT BẢNG ĐẾM TẦN SUẤT &amp; PHÉP TRỪ MÃ ASCII</text>
  <text x="500" y="75" text-anchor="middle" font-size="14" fill="#64748B">Ánh xạ ký tự 'a'..'z' về chỉ số 0..25 bằng công thức: int id = c - 'a';</text>

  <!-- Mapping Demonstration -->
  <g transform="translate(80, 110)" filter="url(#sh6)">
    <rect width="840" height="150" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
    <text x="40" y="40" font-size="16" font-weight="bold" fill="#1E293B">Xâu ký tự mẫu S = "banana"</text>

    <g transform="translate(40, 65)">
      <rect x="0" y="0" width="45" height="50" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
      <text x="22" y="32" text-anchor="middle" font-family="Consolas" font-size="20" font-weight="bold" fill="#1E40AF">'b'</text>

      <rect x="55" y="0" width="45" height="50" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
      <text x="77" y="32" text-anchor="middle" font-family="Consolas" font-size="20" font-weight="bold" fill="#1E40AF">'a'</text>

      <rect x="110" y="0" width="45" height="50" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
      <text x="132" y="32" text-anchor="middle" font-family="Consolas" font-size="20" font-weight="bold" fill="#1E40AF">'n'</text>

      <rect x="165" y="0" width="45" height="50" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
      <text x="187" y="32" text-anchor="middle" font-family="Consolas" font-size="20" font-weight="bold" fill="#1E40AF">'a'</text>

      <rect x="220" y="0" width="45" height="50" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
      <text x="242" y="32" text-anchor="middle" font-family="Consolas" font-size="20" font-weight="bold" fill="#1E40AF">'n'</text>

      <rect x="275" y="0" width="45" height="50" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
      <text x="297" y="32" text-anchor="middle" font-family="Consolas" font-size="20" font-weight="bold" fill="#1E40AF">'a'</text>
    </g>

    <text x="400" y="80" font-size="14" font-weight="bold" fill="#0F172A">Phép toán ánh xạ chỉ số:</text>
    <text x="400" y="105" font-family="Consolas" font-size="13" fill="#0284C7">'a' - 'a' = 97 - 97 = 0  → freq[0]++ (Tổng: 3)</text>
    <text x="400" y="125" font-family="Consolas" font-size="13" fill="#0284C7">'b' - 'a' = 98 - 97 = 1  → freq[1]++ (Tổng: 1)</text>
    <text x="400" y="145" font-family="Consolas" font-size="13" fill="#0284C7">'n' - 'a' = 110 - 97 = 13 → freq[13]++ (Tổng: 2)</text>
  </g>

  <!-- Bottom Frequency Array -->
  <g transform="translate(80, 280)" filter="url(#sh6)">
    <rect width="840" height="135" rx="12" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
    <text x="30" y="35" font-size="15" font-weight="bold" fill="#065F46">MẢNG ĐẾM TẦN SUẤT: vector&lt;int&gt; freq(26, 0);</text>
    <text x="30" y="70" font-size="13" fill="#047857">• Duyệt xâu 1 lần duy nhất: O(|S|) thời gian, O(26) = O(1) bộ nhớ.</text>
    <text x="30" y="95" font-size="13" fill="#047857">• Dễ dàng tìm ký tự xuất hiện nhiều nhất, kiểm tra Anagram hoặc kiểm tra Palindrome.</text>
    <text x="30" y="120" font-size="13" font-weight="bold" fill="#065F46">→ Tuyệt chiêu xử lý chuỗi tối ưu vượt trội so với duyệt 2 vòng lặp lồng nhau!</text>
  </g>
</svg>"""

files = [
    (LESSONS_DIR / "lesson-01-nen-tang-bien-nhap-xuat" / "assets" / "input_process_output_pipeline_vi.svg", svg_l1_1),
    (LESSONS_DIR / "lesson-01-nen-tang-bien-nhap-xuat" / "assets" / "cpp_data_types_memory_vi.svg", svg_l1_2),
    (LESSONS_DIR / "lesson-02-re-nhanh-va-vong-lap" / "assets" / "if_else_control_flow_vi.svg", svg_l2_1),
    (LESSONS_DIR / "lesson-02-re-nhanh-va-vong-lap" / "assets" / "loop_dry_run_trace_vi.svg", svg_l2_2),
    (LESSONS_DIR / "lesson-03-mang-vector-xau-va-ham" / "assets" / "vector_array_memory_layout_vi.svg", svg_l3_1),
    (LESSONS_DIR / "lesson-03-mang-vector-xau-va-ham" / "assets" / "ascii_frequency_table_vi.svg", svg_l3_2),
]

for svg_path, svg_content in files:
    svg_path.write_text(svg_content.strip(), encoding="utf-8")
    png_path = svg_path.with_suffix(".png")
    # Render PNG 1600px width using rsvg-convert
    cmd = ["rsvg-convert", "-w", "1600", str(svg_path), "-o", str(png_path)]
    subprocess.run(cmd, check=True)
    print(f"✅ Generated & rendered: {png_path.name} ({png_path.stat().st_size:,} bytes)")

# Insert markdown image tags into Lesson 01, 02, 03
l1_md = LESSONS_DIR / "lesson-01-nen-tang-bien-nhap-xuat" / "Lesson01_Production_Content.md"
l1_text = l1_md.read_text(encoding="utf-8")
if "input_process_output_pipeline_vi" not in l1_text:
    l1_text = l1_text.replace(
        "## 1. Khung tư duy của một lập trình viên: Mô hình Input – Process – Output",
        "## 1. Khung tư duy của một lập trình viên: Mô hình Input – Process – Output\n\n![Mô hình Input – Process – Output và Vòng đời dữ liệu](assets/input_process_output_pipeline_vi.png)"
    )
    l1_text = l1_text.replace(
        "## 3. Biến và hệ thống kiểu dữ liệu trong C++",
        "## 3. Biến và hệ thống kiểu dữ liệu trong C++\n\n![Hệ thống kiểu dữ liệu C++ và Giới hạn tràn số](assets/cpp_data_types_memory_vi.png)"
    )
    l1_md.write_text(l1_text, encoding="utf-8")
    print("✅ Inserted image tags into Lesson 01")

l2_md = LESSONS_DIR / "lesson-02-re-nhanh-va-vong-lap" / "Lesson02_Production_Content.md"
l2_text = l2_md.read_text(encoding="utf-8")
if "if_else_control_flow_vi" not in l2_text:
    l2_text = l2_text.replace(
        "## 1. Cấu trúc rẽ nhánh (Decision Making): Kiểm soát ngã rẽ chương trình",
        "## 1. Cấu trúc rẽ nhánh (Decision Making): Kiểm soát ngã rẽ chương trình\n\n![Sơ đồ khối luồng rẽ nhánh if-else và Bẫy logic](assets/if_else_control_flow_vi.png)"
    )
    l2_text = l2_text.replace(
        "## 4. Bốn mẫu tích lũy (Accumulation Patterns) kinh điển",
        "## 4. Bốn mẫu tích lũy (Accumulation Patterns) kinh điển\n\n![Mô hình 4 mẫu tích lũy và Bảng trace vòng lặp](assets/loop_dry_run_trace_vi.png)"
    )
    l2_md.write_text(l2_text, encoding="utf-8")
    print("✅ Inserted image tags into Lesson 02")

l3_md = LESSONS_DIR / "lesson-03-mang-vector-xau-va-ham" / "Lesson03_Production_Content.md"
l3_text = l3_md.read_text(encoding="utf-8")
if "vector_array_memory_layout_vi" not in l3_text:
    l3_text = l3_text.replace(
        "## 1. Mảng 1 chiều & Cấu trúc dữ liệu hiện đại: `vector<int>`",
        "## 1. Mảng 1 chiều & Cấu trúc dữ liệu hiện đại: `vector<int>`\n\n![Cấu trúc bộ nhớ Mảng & Vector 0-based indexing](assets/vector_array_memory_layout_vi.png)"
    )
    l3_text = l3_text.replace(
        "## 3. Xâu ký tự (`string`): Mảng các ký tự",
        "## 3. Xâu ký tự (`string`): Mảng các ký tự\n\n![Kỹ thuật Trừ mã ASCII c - 'a' và Bảng đếm tần suất](assets/ascii_frequency_table_vi.png)"
    )
    l3_md.write_text(l3_text, encoding="utf-8")
    print("✅ Inserted image tags into Lesson 03")

print("\n🎉 Hoàn tất tạo và nhúng assets cho Chương 01!")
