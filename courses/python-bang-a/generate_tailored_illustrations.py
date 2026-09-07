"""
HỆ THỐNG BIÊN TẬP HÌNH MINH HỌA ĐO NI ĐÓNG GIÀY TỪNG BÀI TOÁN (TAILORED SCENARIO SUITE)
- Tỷ lệ chuẩn 600x300, lề an toàn >= 40px, bố cục cân đối theo cả chiều ngang và dọc.
- Tiêu đề trên y=38, nội dung chính từ y=55..235, chú thích dưới y=268.
- Tuyệt đối KHÔNG có bảng lý thuyết, KHÔNG code Python, KHÔNG công thức giải toán.
"""

import html
import subprocess
from pathlib import Path
import json

OUT_DIR = Path("courses/python-bang-a/assets_png")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def render(name, svg_content, width=1200):
    p_svg = OUT_DIR / f"{name}.svg"
    p_png = OUT_DIR / f"{name}.png"
    p_svg.write_text(svg_content, encoding="utf-8")
    res = subprocess.run(["rsvg-convert", "-f", "png", "-w", str(width), str(p_svg), "-o", str(p_png)], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error {name}: {res.stderr}")
    if p_svg.exists():
        p_svg.unlink()

def card_base(title, content, sub=""):
    t_safe = html.escape(title.upper())
    sub_svg = f'<text x="300" y="268" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0F2A44" text-anchor="middle">{html.escape(sub)}</text>' if sub else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="600" height="300">
    <rect width="600" height="300" fill="#F8FAFC" rx="12" stroke="#CBD5E1" stroke-width="2"/>
    <text x="300" y="38" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0F2A44" text-anchor="middle">{t_safe}</text>
    {content}
    {sub_svg}
</svg>'''

# --- LESSON 01 ---
def svg_robot_greeting():
    content = '''
    <g transform="translate(180, 65)">
        <rect x="50" y="25" width="140" height="110" fill="#E2E8F0" stroke="#475569" stroke-width="3" rx="20"/>
        <line x1="120" y1="25" x2="120" y2="5" stroke="#475569" stroke-width="3"/>
        <circle cx="120" cy="2" r="6" fill="#EF4444"/>
        <rect x="36" y="65" width="14" height="30" fill="#64748B" rx="3"/>
        <rect x="190" y="65" width="14" height="30" fill="#64748B" rx="3"/>
        <rect x="65" y="40" width="110" height="80" fill="#0F172A" rx="10"/>
        <circle cx="95" cy="70" r="10" fill="#38BDF8"/>
        <circle cx="145" cy="70" r="10" fill="#38BDF8"/>
        <path d="M 95 95 Q 120 110 145 95" stroke="#38BDF8" stroke-width="3" fill="none" stroke-linecap="round"/>
        <g transform="translate(160, -10)">
            <rect x="0" y="0" width="170" height="45" fill="#FEF08A" stroke="#CA8A04" stroke-width="2" rx="8"/>
            <text x="85" y="28" font-family="Arial" font-size="13" font-weight="bold" fill="#854D0E" text-anchor="middle">"Hello, World!"</text>
        </g>
    </g>
    '''
    return card_base("Hệ thống robot tự hành phát lời chào", content, "Robot công nghiệp khởi động và hiển thị thông điệp")

def svg_couplet_banner():
    content = '''
    <g transform="translate(130, 60)">
        <rect x="0" y="10" width="140" height="150" fill="#DC2626" stroke="#991B1B" stroke-width="2.5" rx="8"/>
        <rect x="8" y="18" width="124" height="134" fill="none" stroke="#FDE047" stroke-width="1.5"/>
        <text x="70" y="70" font-family="Arial" font-size="15" font-weight="bold" fill="#FEF08A" text-anchor="middle">XUÂN AN KHANG</text>
        <text x="70" y="100" font-family="Arial" font-size="15" font-weight="bold" fill="#FEF08A" text-anchor="middle">THỊNH VƯỢNG</text>
        <text x="70" y="175" font-family="Arial" font-size="11" font-weight="bold" fill="#0F2A44" text-anchor="middle">Dòng 1</text>
        
        <text x="170" y="90" font-family="Arial" font-size="28" font-weight="bold" fill="#F59E0B" text-anchor="middle">🏮</text>
        
        <rect x="200" y="10" width="140" height="150" fill="#DC2626" stroke="#991B1B" stroke-width="2.5" rx="8"/>
        <rect x="208" y="18" width="124" height="134" fill="none" stroke="#FDE047" stroke-width="1.5"/>
        <text x="270" y="70" font-family="Arial" font-size="15" font-weight="bold" fill="#FEF08A" text-anchor="middle">NIÊN PHÚC THỌ</text>
        <text x="270" y="100" font-family="Arial" font-size="15" font-weight="bold" fill="#FEF08A" text-anchor="middle">MIÊN TRƯỜNG</text>
        <text x="270" y="175" font-family="Arial" font-size="11" font-weight="bold" fill="#0F2A44" text-anchor="middle">Dòng 2</text>
    </g>
    '''
    return card_base("Bảng điện tử hiển thị hai vế câu đối", content, "Hai vế câu đối được in trên 2 dòng tách biệt")

def svg_ticket_number():
    content = '''
    <g transform="translate(160, 75)">
        <rect x="0" y="0" width="280" height="130" fill="#FEF3C7" stroke="#D97706" stroke-width="2.5" rx="8"/>
        <line x1="80" y1="0" x2="80" y2="130" stroke="#D97706" stroke-width="1.5" stroke-dasharray="4,4"/>
        <text x="40" y="60" font-family="Arial" font-size="12" font-weight="bold" fill="#B45309" text-anchor="middle">VÉ VÀO</text>
        <text x="40" y="80" font-family="Arial" font-size="12" font-weight="bold" fill="#B45309" text-anchor="middle">CỔNG</text>
        <text x="180" y="50" font-family="Arial" font-size="12" fill="#78350F" text-anchor="middle">MÃ SỐ MAY MẮN</text>
        <rect x="110" y="60" width="140" height="50" fill="#FFFFFF" stroke="#B45309" stroke-width="1.5" rx="6"/>
        <text x="180" y="95" font-family="Courier New, monospace" font-size="28" font-weight="bold" fill="#DC2626" text-anchor="middle">886699</text>
    </g>
    '''
    return card_base("Máy quét và hiển thị vé may mắn", content, "Đọc số nguyên mã vé và in xác nhận ra màn hình")

def svg_sep_hyphen():
    boxes = []
    for i in range(5):
        boxes.append(f'''
        <g transform="translate({i*95}, 0)">
            <rect x="0" y="0" width="55" height="70" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" rx="8"/>
            <text x="27" y="44" font-family="Arial" font-size="26" font-weight="bold" fill="#1D4ED8" text-anchor="middle">{i+1}</text>
            {f'<text x="75" y="46" font-family="Arial" font-size="30" font-weight="bold" fill="#EF4444" text-anchor="middle">-</text>' if i < 4 else ''}
        </g>''')
    inner = "".join(boxes)
    content = f'''<g transform="translate(80, 95)">{inner}</g>'''
    return card_base("In các số nối nhau bằng dấu gạch ngang", content, "Các giá trị xuất trên một hàng nối nhau qua ký tự phân cách sep='-'")

def svg_double_harvest():
    content = '''
    <g transform="translate(120, 75)">
        <rect x="0" y="20" width="140" height="100" fill="#DCFCE7" stroke="#16A34A" stroke-width="2" rx="8"/>
        <text x="70" y="55" font-family="Arial" font-size="13" font-weight="bold" fill="#15803D" text-anchor="middle">NĂM ĐẦU TIÊN</text>
        <text x="70" y="92" font-family="Arial" font-size="26" font-weight="bold" fill="#166534" text-anchor="middle">X tấn</text>
        <g transform="translate(155, 45)">
            <text x="25" y="15" font-family="Arial" font-size="14" font-weight="bold" fill="#EA580C" text-anchor="middle">× 2</text>
            <path d="M 5 25 L 45 25" stroke="#EA580C" stroke-width="3"/>
            <polygon points="52,25 42,20 42,30" fill="#EA580C"/>
            <text x="25" y="45" font-family="Arial" font-size="10" font-weight="bold" fill="#C2410C" text-anchor="middle">Gấp đôi</text>
        </g>
        <rect x="220" y="10" width="140" height="120" fill="#FEF08A" stroke="#CA8A04" stroke-width="2.5" rx="8"/>
        <text x="290" y="50" font-family="Arial" font-size="13" font-weight="bold" fill="#854D0E" text-anchor="middle">NĂM THỨ HAI</text>
        <text x="290" y="92" font-family="Arial" font-size="28" font-weight="bold" fill="#B45309" text-anchor="middle">2 × X</text>
        <text x="290" y="115" font-family="Arial" font-size="11" fill="#854D0E" text-anchor="middle">(Sản lượng gấp 2)</text>
    </g>
    '''
    return card_base("Mô hình nhân đôi sản lượng nông nghiệp", content, "Sản lượng năm tiếp theo tăng gấp 2 lần năm đầu")

def svg_swap_cards():
    content = '''
    <g transform="translate(140, 75)">
        <rect x="0" y="10" width="120" height="100" fill="#DBEAFE" stroke="#2563EB" stroke-width="2.5" rx="8"/>
        <text x="60" y="42" font-family="Arial" font-size="13" font-weight="bold" fill="#1E40AF" text-anchor="middle">Thẻ của An</text>
        <text x="60" y="82" font-family="Arial" font-size="30" font-weight="bold" fill="#1D4ED8" text-anchor="middle">A</text>
        <g transform="translate(135, 35)">
            <line x1="0" y1="10" x2="45" y2="10" stroke="#0F2A44" stroke-width="2"/>
            <polygon points="45,10 37,6 37,14" fill="#0F2A44"/>
            <line x1="45" y1="30" x2="0" y2="30" stroke="#0F2A44" stroke-width="2"/>
            <polygon points="0,30 8,26 8,34" fill="#0F2A44"/>
            <text x="22" y="58" font-family="Arial" font-size="11" font-weight="bold" fill="#0F2A44" text-anchor="middle">HOÁN ĐỔI</text>
        </g>
        <rect x="200" y="10" width="120" height="100" fill="#DCFCE7" stroke="#16A34A" stroke-width="2.5" rx="8"/>
        <text x="260" y="42" font-family="Arial" font-size="13" font-weight="bold" fill="#15803D" text-anchor="middle">Thẻ của Bình</text>
        <text x="260" y="82" font-family="Arial" font-size="30" font-weight="bold" fill="#166534" text-anchor="middle">B</text>
    </g>
    '''
    return card_base("Hai bạn An và Bình hoán đổi thẻ số", content, "Sau khi đổi: thẻ An mang giá trị B, thẻ Bình mang giá trị A")

def svg_two_bags_marbles():
    content = '''
    <g transform="translate(130, 75)">
        <g transform="translate(0, 10)">
            <rect x="0" y="0" width="110" height="100" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" rx="12"/>
            <circle cx="35" cy="60" r="11" fill="#3B82F6"/>
            <circle cx="60" cy="50" r="11" fill="#60A5FA"/>
            <circle cx="75" cy="70" r="11" fill="#2563EB"/>
            <text x="55" y="30" font-family="Arial" font-size="12" font-weight="bold" fill="#1E40AF" text-anchor="middle">Túi Minh: A viên</text>
        </g>
        <text x="145" y="70" font-family="Arial" font-size="32" font-weight="bold" fill="#0F2A44" text-anchor="middle">+</text>
        <g transform="translate(180, 10)">
            <rect x="0" y="0" width="110" height="100" fill="#FEF2F2" stroke="#EF4444" stroke-width="2" rx="12"/>
            <circle cx="35" cy="60" r="11" fill="#EF4444"/>
            <circle cx="60" cy="50" r="11" fill="#F87171"/>
            <circle cx="75" cy="70" r="11" fill="#DC2626"/>
            <text x="55" y="30" font-family="Arial" font-size="12" font-weight="bold" fill="#991B1B" text-anchor="middle">Túi Nam: B viên</text>
        </g>
        <text x="315" y="70" font-family="Arial" font-size="28" font-weight="bold" fill="#0F2A44" text-anchor="middle">=</text>
        <text x="340" y="70" font-family="Arial" font-size="15" font-weight="bold" fill="#059669">A + B</text>
    </g>
    '''
    return card_base("Tính tổng số viên bi của hai bạn", content, "Tổng số bi bằng số bi của Minh cộng số bi của Nam")

def svg_fabric_roll():
    content = '''
    <g transform="translate(110, 85)">
        <rect x="0" y="0" width="380" height="40" fill="#E2E8F0" stroke="#64748B" stroke-width="2" rx="4"/>
        <rect x="0" y="0" width="220" height="40" fill="#FCA5A5" stroke="#DC2626" stroke-width="2" rx="4"/>
        <text x="110" y="26" font-family="Arial" font-size="12" font-weight="bold" fill="#991B1B" text-anchor="middle">Đã cắt may: B mét</text>
        <rect x="220" y="0" width="160" height="40" fill="#86EFAC" stroke="#16A34A" stroke-width="2" rx="4"/>
        <text x="300" y="26" font-family="Arial" font-size="12" font-weight="bold" fill="#14532D" text-anchor="middle">Còn lại: A - B</text>
        <line x1="0" y1="75" x2="380" y2="75" stroke="#0F2A44" stroke-width="1.5"/>
        <polygon points="0,75 10,71 10,79" fill="#0F2A44"/><polygon points="380,75 370,71 370,79" fill="#0F2A44"/>
        <text x="190" y="98" font-family="Arial" font-size="13" font-weight="bold" fill="#0F2A44" text-anchor="middle">Tổng chiều dài ban đầu cuộn vải: A mét</text>
    </g>
    '''
    return card_base("Độ dài cuộn vải sau khi cắt may", content, "Chiều dài còn lại = Chiều dài ban đầu A - Phần đã cắt B")

def svg_candy_grid():
    candies = []
    for r in range(3):
        for c in range(6):
            candies.append(f'<circle cx="{30 + c*44}" cy="{25 + r*42}" r="13" fill="#F59E0B" stroke="#B45309" stroke-width="1.5"/><circle cx="{30 + c*44}" cy="{25 + r*42}" r="4" fill="#FEF08A"/>')
    inner = "".join(candies)
    content = f'''
    <g transform="translate(160, 68)">
        <rect x="0" y="0" width="280" height="135" fill="#FEF3C7" stroke="#D97706" stroke-width="2.5" rx="8"/>
        {inner}
        <text x="140" y="-10" font-family="Arial" font-size="12" font-weight="bold" fill="#92400E" text-anchor="middle">Mỗi hộp có B chiếc kẹo</text>
        <text x="-16" y="68" font-family="Arial" font-size="12" font-weight="bold" fill="#92400E" text-anchor="middle" transform="rotate(-90, -16, 68)">A hộp</text>
    </g>
    '''
    return card_base("Dây chuyền đóng gói bánh kẹo tự động", content, "Tổng số kẹo đóng gói = A × B")

def svg_train_carriages():
    content = '''
    <g transform="translate(100, 75)">
        <rect x="0" y="30" width="80" height="65" fill="#3B82F6" stroke="#1D4ED8" stroke-width="2" rx="8"/>
        <rect x="50" y="10" width="30" height="20" fill="#1D4ED8" rx="2"/>
        <circle cx="25" cy="100" r="12" fill="#334155"/>
        <circle cx="65" cy="100" r="12" fill="#334155"/>
        <text x="40" y="68" font-family="Arial" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">ĐẦU TÀU</text>
        <rect x="80" y="60" width="20" height="8" fill="#475569"/>
        <rect x="100" y="25" width="110" height="70" fill="#FEF08A" stroke="#CA8A04" stroke-width="2" rx="6"/>
        <text x="155" y="50" font-family="Arial" font-size="11" font-weight="bold" fill="#854D0E" text-anchor="middle">Toa xe 1</text>
        <text x="155" y="78" font-family="Arial" font-size="22" font-weight="bold" fill="#B45309" text-anchor="middle">Số a</text>
        <circle cx="125" cy="100" r="12" fill="#334155"/>
        <circle cx="185" cy="100" r="12" fill="#334155"/>
        <rect x="210" y="60" width="20" height="8" fill="#475569"/>
        <rect x="230" y="25" width="110" height="70" fill="#BBF7D0" stroke="#16A34A" stroke-width="2" rx="6"/>
        <text x="285" y="50" font-family="Arial" font-size="11" font-weight="bold" fill="#166534" text-anchor="middle">Toa xe 2</text>
        <text x="285" y="78" font-family="Arial" font-size="22" font-weight="bold" fill="#15803D" text-anchor="middle">Số b</text>
        <circle cx="255" cy="100" r="12" fill="#334155"/>
        <circle cx="315" cy="100" r="12" fill="#334155"/>
    </g>
    '''
    return card_base("Đoàn tàu hỏa kéo hai toa xe mang số a và b", content, "Hai toa xe chở hai con số ghép liền nhau")

def svg_four_ops():
    content = '''
    <g transform="translate(120, 70)">
        <g transform="translate(0, 0)">
            <rect x="0" y="0" width="165" height="55" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" rx="6"/>
            <text x="82" y="34" font-family="Arial" font-size="16" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Cộng: a + b</text>
        </g>
        <g transform="translate(195, 0)">
            <rect x="0" y="0" width="165" height="55" fill="#FEF2F2" stroke="#EF4444" stroke-width="2" rx="6"/>
            <text x="82" y="34" font-family="Arial" font-size="16" font-weight="bold" fill="#B91C1C" text-anchor="middle">Trừ: a - b</text>
        </g>
        <g transform="translate(0, 75)">
            <rect x="0" y="0" width="165" height="55" fill="#FEFCE8" stroke="#EAB308" stroke-width="2" rx="6"/>
            <text x="82" y="34" font-family="Arial" font-size="16" font-weight="bold" fill="#854D0E" text-anchor="middle">Nhân: a × b</text>
        </g>
        <g transform="translate(195, 75)">
            <rect x="0" y="0" width="165" height="55" fill="#F0FDF4" stroke="#22C55E" stroke-width="2" rx="6"/>
            <text x="82" y="34" font-family="Arial" font-size="16" font-weight="bold" fill="#15803D" text-anchor="middle">Chia: a / b</text>
        </g>
    </g>
    '''
    return card_base("Bốn phép tính số học cơ bản", content, "Bảng tổng hợp kết quả 4 phép tính đồng thời")

def svg_three_generations():
    content = '''
    <g transform="translate(110, 70)">
        <rect x="0" y="20" width="100" height="100" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" rx="8"/>
        <text x="50" y="50" font-family="Arial" font-size="12" font-weight="bold" fill="#1E40AF" text-anchor="middle">Con</text>
        <text x="50" y="85" font-family="Arial" font-size="22" font-weight="bold" fill="#1D4ED8" text-anchor="middle">a tuổi</text>
        <rect x="130" y="10" width="110" height="110" fill="#F0FDF4" stroke="#22C55E" stroke-width="2" rx="8"/>
        <text x="185" y="45" font-family="Arial" font-size="12" font-weight="bold" fill="#15803D" text-anchor="middle">Bố mẹ</text>
        <text x="185" y="82" font-family="Arial" font-size="22" font-weight="bold" fill="#166534" text-anchor="middle">b tuổi</text>
        <rect x="270" y="0" width="110" height="120" fill="#FEF3C7" stroke="#D97706" stroke-width="2" rx="8"/>
        <text x="325" y="40" font-family="Arial" font-size="12" font-weight="bold" fill="#92400E" text-anchor="middle">Ông bà</text>
        <text x="325" y="80" font-family="Arial" font-size="22" font-weight="bold" fill="#B45309" text-anchor="middle">c tuổi</text>
    </g>
    '''
    return card_base("Cỗ máy thời gian: Tuổi ba thế hệ", content, "Tổng độ tuổi và chênh lệch tuổi trong một gia đình")

def svg_donut_bakery():
    content = '''
    <g transform="translate(130, 70)">
        <rect x="0" y="10" width="150" height="110" fill="#FEF3C7" stroke="#D97706" stroke-width="2" rx="8"/>
        <text x="75" y="42" font-family="Arial" font-size="12" font-weight="bold" fill="#92400E" text-anchor="middle">Bánh rán dâu</text>
        <circle cx="75" cy="78" r="24" fill="#F472B6" stroke="#DB2777" stroke-width="2"/>
        <circle cx="75" cy="78" r="8" fill="#FEF3C7"/>
        <text x="75" y="132" font-family="Arial" font-size="11" fill="#78350F" text-anchor="middle">A chiếc × X đồng</text>
        
        <text x="175" y="70" font-family="Arial" font-size="28" font-weight="bold" fill="#0F2A44" text-anchor="middle">+</text>
        
        <rect x="200" y="10" width="150" height="110" fill="#FEF3C7" stroke="#D97706" stroke-width="2" rx="8"/>
        <text x="275" y="42" font-family="Arial" font-size="12" font-weight="bold" fill="#92400E" text-anchor="middle">Bánh rán mật</text>
        <circle cx="275" cy="78" r="24" fill="#FBBF24" stroke="#D97706" stroke-width="2"/>
        <circle cx="275" cy="78" r="8" fill="#FEF3C7"/>
        <text x="275" y="132" font-family="Arial" font-size="11" fill="#78350F" text-anchor="middle">B chiếc × Y đồng</text>
    </g>
    '''
    return card_base("Hóa đơn thanh toán cửa hàng bánh rán", content, "Tổng số tiền = (A × X) + (B × Y)")

def svg_business_card():
    content = '''
    <g transform="translate(150, 68)">
        <rect x="0" y="0" width="300" height="145" fill="#FFFFFF" stroke="#0F2A44" stroke-width="2.5" rx="8"/>
        <rect x="0" y="0" width="12" height="145" fill="#2563EB" rx="4"/>
        <text x="35" y="48" font-family="Arial" font-size="18" font-weight="bold" fill="#0F2A44">NGUYỄN VĂN AN</text>
        <text x="35" y="75" font-family="Arial" font-size="12" font-weight="bold" fill="#2563EB">KỸ SƯ LẬP TRÌNH ROBOT</text>
        <line x1="35" y1="90" x2="275" y2="90" stroke="#E2E8F0" stroke-width="1.5"/>
        <text x="35" y="112" font-family="Arial" font-size="11" fill="#64748B">Email: contact@ikhedu.vn</text>
        <text x="35" y="130" font-family="Arial" font-size="11" fill="#64748B">Điện thoại: 0912.345.678</text>
    </g>
    '''
    return card_base("Tấm danh thiếp cá nhân thông minh", content, "In thông tin người dùng được định dạng chuyên nghiệp")

# --- LESSON 02 ---
def svg_digit_split():
    content = '''
    <g transform="translate(160, 70)">
        <rect x="0" y="0" width="280" height="55" fill="#F1F5F9" stroke="#64748B" stroke-width="2" rx="8"/>
        <text x="140" y="36" font-family="Courier New, monospace" font-size="26" font-weight="bold" fill="#0F172A" text-anchor="middle">Số nguyên: 7 9 4 8</text>
        <text x="140" y="80" font-family="Arial" font-size="20" font-weight="bold" fill="#2563EB" text-anchor="middle">↓</text>
        <g transform="translate(20, 92)">
            <rect x="0" y="0" width="110" height="48" fill="#FEF08A" stroke="#CA8A04" stroke-width="2" rx="6"/>
            <text x="55" y="30" font-family="Arial" font-size="13" font-weight="bold" fill="#854D0E" text-anchor="middle">Hàng chục: 4</text>
        </g>
        <g transform="translate(150, 92)">
            <rect x="0" y="0" width="110" height="48" fill="#FCA5A5" stroke="#DC2626" stroke-width="2" rx="6"/>
            <text x="55" y="30" font-family="Arial" font-size="13" font-weight="bold" fill="#991B1B" text-anchor="middle">Đơn vị: 8</text>
        </g>
    </g>
    '''
    return card_base("Bóc tách chữ số hàng chục và đơn vị", content, "Kỹ thuật tách từng chữ số của số nguyên")

def svg_clock_24h():
    content = '''
    <g transform="translate(160, 70)">
        <rect x="0" y="0" width="280" height="125" fill="#0F172A" stroke="#334155" stroke-width="3" rx="12"/>
        <text x="140" y="75" font-family="Courier New, monospace" font-size="48" font-weight="bold" fill="#22C55E" text-anchor="middle">23 : 45</text>
        <text x="140" y="108" font-family="Arial" font-size="12" fill="#94A3B8" text-anchor="middle">CHU KỲ ĐỒNG HỒ 24 GIỜ</text>
    </g>
    '''
    return card_base("Đồng hồ điện tử định dạng 24 giờ", content, "Sau 23:59 đồng hồ quay về mốc 00:00")

def svg_week_days():
    days = []
    names = ['CN', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7']
    for i, name in enumerate(names):
        bg = '#FEF2F2' if i==0 else '#EFF6FF'
        border = '#EF4444' if i==0 else '#3B82F6'
        tc = '#B91C1C' if i==0 else '#1D4ED8'
        nc = '#DC2626' if i==0 else '#2563EB'
        days.append(f'''
        <g transform="translate({i*72}, 0)">
            <rect x="0" y="0" width="62" height="75" fill="{bg}" stroke="{border}" stroke-width="2" rx="6"/>
            <text x="31" y="30" font-family="Arial" font-size="12" font-weight="bold" fill="{tc}" text-anchor="middle">{name}</text>
            <text x="31" y="60" font-family="Arial" font-size="18" font-weight="bold" fill="{nc}" text-anchor="middle">{i}</text>
        </g>''')
    inner = "".join(days)
    content = f'''<g transform="translate(50, 90)">{inner}</g>'''
    return card_base("Chu kỳ 7 ngày trong tuần", content, "Quy ước: Chủ Nhật là 0, Thứ Hai là 1, ..., Thứ Bảy là 6")

def svg_running_track():
    content = '''
    <g transform="translate(140, 68)">
        <rect x="0" y="0" width="320" height="140" fill="#EF4444" stroke="#B91C1C" stroke-width="3" rx="70"/>
        <rect x="40" y="25" width="240" height="90" fill="#22C55E" stroke="#15803D" stroke-width="2" rx="45"/>
        <rect x="20" y="12" width="280" height="116" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="8,6" rx="58"/>
        <text x="160" y="75" font-family="Arial" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">SÂN ĐIỀN KINH L MÉT</text>
    </g>
    '''
    return card_base("Vòng chạy điền kinh sân vận động", content, "Vận động viên hoàn thành K vòng quanh sân dài L mét")

def svg_desks():
    desks = []
    for i in range(4):
        x = (i%2) * 165
        y = (i//2) * 70
        desks.append(f'''
        <g transform="translate({x}, {y})">
            <rect x="0" y="0" width="135" height="55" fill="#FEF3C7" stroke="#D97706" stroke-width="2" rx="6"/>
            <circle cx="38" cy="27" r="13" fill="#3B82F6"/>
            <circle cx="97" cy="27" r="13" fill="#3B82F6"/>
            <text x="67" y="46" font-family="Arial" font-size="10" font-weight="bold" fill="#92400E" text-anchor="middle">Bàn đôi #{i+1}</text>
        </g>''')
    inner = "".join(desks)
    content = f'''<g transform="translate(150, 70)">{inner}</g>'''
    return card_base("Phòng thi xếp bàn học sinh", content, "Mỗi bàn ngồi đúng 2 học sinh, tính số bàn cần thiết cho N bạn")

def svg_light_border():
    bulbs = []
    for i in range(7):
        bulbs.append(f'<circle cx="{20 + i*40}" cy="10" r="7" fill="#FDE047" stroke="#EAB308" stroke-width="1.5"/>')
        bulbs.append(f'<circle cx="{20 + i*40}" cy="120" r="7" fill="#FDE047" stroke="#EAB308" stroke-width="1.5"/>')
    for j in range(2):
        bulbs.append(f'<circle cx="10" cy="{45 + j*40}" r="7" fill="#FDE047" stroke="#EAB308" stroke-width="1.5"/>')
        bulbs.append(f'<circle cx="270" cy="{45 + j*40}" r="7" fill="#FDE047" stroke="#EAB308" stroke-width="1.5"/>')
    inner = "".join(bulbs)
    content = f'''
    <g transform="translate(160, 68)">
        <rect x="0" y="0" width="280" height="130" fill="#0F172A" stroke="#334155" stroke-width="3" rx="10"/>
        {inner}
        <text x="140" y="74" font-family="Arial" font-size="16" font-weight="bold" fill="#FDE047" text-anchor="middle">BIỂN HIỆU ĐÈN LED</text>
    </g>
    '''
    return card_base("Bóng đèn mắc viền quanh biển hiệu", content, "Mắc bóng đèn đều đặn theo chu vi biển hiệu hình chữ nhật")

def svg_number_mirror():
    content = '''
    <g transform="translate(140, 70)">
        <rect x="0" y="20" width="120" height="95" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" rx="8"/>
        <text x="60" y="48" font-family="Arial" font-size="12" fill="#1E40AF" text-anchor="middle">Số ban đầu</text>
        <text x="60" y="85" font-family="Courier New, monospace" font-size="34" font-weight="bold" fill="#1D4ED8" text-anchor="middle">4 8 9</text>
        <g transform="translate(155, 0)">
            <rect x="0" y="0" width="10" height="135" fill="#94A3B8" stroke="#475569" rx="3"/>
            <text x="5" y="152" font-family="Arial" font-size="10" font-weight="bold" fill="#475569" text-anchor="middle">GƯƠNG</text>
        </g>
        <rect x="200" y="20" width="120" height="95" fill="#FEF2F2" stroke="#EF4444" stroke-width="2" rx="8"/>
        <text x="260" y="48" font-family="Arial" font-size="12" fill="#991B1B" text-anchor="middle">Số đảo ngược</text>
        <text x="260" y="85" font-family="Courier New, monospace" font-size="34" font-weight="bold" fill="#B91C1C" text-anchor="middle">9 8 4</text>
    </g>
    '''
    return card_base("Trò chơi gương thần: Đảo ngược số 3 chữ số", content, "Chữ số hàng trăm và hàng đơn vị đổi vị trí cho nhau")

def svg_tree_planting():
    trees = []
    for i in range(5):
        trees.append(f'''
        <g transform="translate({i*85}, 0)">
            <line x1="25" y1="50" x2="25" y2="85" stroke="#78350F" stroke-width="4"/>
            <circle cx="25" cy="45" r="22" fill="#22C55E" stroke="#15803D" stroke-width="2"/>
            <text x="25" y="105" font-family="Arial" font-size="11" font-weight="bold" fill="#0F2A44" text-anchor="middle">Cây #{i+1}</text>
        </g>''')
    inner = "".join(trees)
    content = f'''
    <g transform="translate(100, 65)">
        <rect x="0" y="80" width="390" height="14" fill="#E2E8F0" stroke="#94A3B8" stroke-width="1.5" rx="3"/>
        {inner}
        <text x="195" y="132" font-family="Arial" font-size="12" font-weight="bold" fill="#0F2A44" text-anchor="middle">Khoảng cách giữa hai cây liên tiếp: d mét</text>
    </g>
    '''
    return card_base("Trồng cây xanh thẳng tắp dọc đại lộ", content, "Tính số cây cần trồng trên đoạn đường dài L mét")

def svg_clock_hands_12h():
    content = '''
    <g transform="translate(225, 62)">
        <circle cx="75" cy="75" r="70" fill="#FFFFFF" stroke="#0F2A44" stroke-width="3"/>
        <line x1="75" y1="15" x2="75" y2="25" stroke="#0F2A44" stroke-width="3"/>
        <line x1="135" y1="75" x2="125" y2="75" stroke="#0F2A44" stroke-width="3"/>
        <line x1="75" y1="135" x2="75" y2="125" stroke="#0F2A44" stroke-width="3"/>
        <line x1="15" y1="75" x2="25" y2="75" stroke="#0F2A44" stroke-width="3"/>
        <line x1="75" y1="75" x2="75" y2="35" stroke="#2563EB" stroke-width="4" stroke-linecap="round"/>
        <line x1="75" y1="75" x2="115" y2="75" stroke="#DC2626" stroke-width="2.5" stroke-linecap="round"/>
        <circle cx="75" cy="75" r="6" fill="#0F2A44"/>
    </g>
    '''
    return card_base("Kim giờ và kim phút trên mặt đồng hồ tròn", content, "Góc quay của kim đồng hồ theo chu kỳ 12 giờ")

# --- LESSON 03 ---
def svg_square_geo():
    content = '''
    <g transform="translate(215, 62)">
        <rect x="0" y="15" width="140" height="140" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2.5" rx="6"/>
        <text x="70" y="5" font-family="Arial" font-size="14" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Cạnh a</text>
        <text x="-16" y="90" font-family="Arial" font-size="14" font-weight="bold" fill="#1D4ED8" text-anchor="middle" transform="rotate(-90, -16, 90)">Cạnh a</text>
        <text x="70" y="75" font-family="Arial" font-size="14" font-weight="bold" fill="#1E40AF" text-anchor="middle">Chu vi = 4 × a</text>
        <text x="70" y="105" font-family="Arial" font-size="14" font-weight="bold" fill="#1E40AF" text-anchor="middle">Diện tích = a²</text>
    </g>
    '''
    return card_base("Hình vuông: Chu vi và diện tích", content, "Công thức hình học cơ bản của hình vuông cạnh a")

def svg_rect_geo():
    content = '''
    <g transform="translate(180, 65)">
        <rect x="0" y="15" width="240" height="130" fill="#F0FDF4" stroke="#22C55E" stroke-width="2.5" rx="6"/>
        <text x="120" y="5" font-family="Arial" font-size="14" font-weight="bold" fill="#15803D" text-anchor="middle">Chiều dài a</text>
        <text x="-16" y="85" font-family="Arial" font-size="14" font-weight="bold" fill="#15803D" text-anchor="middle" transform="rotate(-90, -16, 85)">Rộng b</text>
        <text x="120" y="70" font-family="Arial" font-size="14" font-weight="bold" fill="#166534" text-anchor="middle">Chu vi = (a + b) × 2</text>
        <text x="120" y="100" font-family="Arial" font-size="14" font-weight="bold" fill="#166534" text-anchor="middle">Diện tích = a × b</text>
    </g>
    '''
    return card_base("Hình chữ nhật: Chu vi và diện tích", content, "Kích thước hai chiều dài và rộng của hình chữ nhật")

def svg_triangle_geo():
    content = '''
    <g transform="translate(195, 60)">
        <polygon points="105,10 10,140 200,140" fill="#FEF3C7" stroke="#D97706" stroke-width="2.5"/>
        <text x="45" y="70" font-family="Arial" font-size="14" font-weight="bold" fill="#B45309" text-anchor="middle">Cạnh a</text>
        <text x="165" y="70" font-family="Arial" font-size="14" font-weight="bold" fill="#B45309" text-anchor="middle">Cạnh b</text>
        <text x="105" y="162" font-family="Arial" font-size="14" font-weight="bold" fill="#B45309" text-anchor="middle">Cạnh c</text>
        <text x="105" y="110" font-family="Arial" font-size="13" font-weight="bold" fill="#78350F" text-anchor="middle">P = a + b + c</text>
    </g>
    '''
    return card_base("Tam giác: Chu vi và ba cạnh", content, "Chu vi tam giác bằng tổng độ dài 3 cạnh")

def svg_crocodile_island():
    content = '''
    <g transform="translate(150, 62)">
        <rect x="0" y="0" width="300" height="145" fill="#38BDF8" stroke="#0284C7" stroke-width="2.5" rx="10"/>
        <text x="150" y="32" font-family="Arial" font-size="13" font-weight="bold" fill="#075985" text-anchor="middle">HỒ NƯỚC CÁ SẤU (Rộng A × B)</text>
        <rect x="75" y="50" width="150" height="70" fill="#FDE047" stroke="#CA8A04" stroke-width="2" rx="6"/>
        <text x="150" y="90" font-family="Arial" font-size="13" font-weight="bold" fill="#854D0E" text-anchor="middle">HÒN ĐẢO (a × b)</text>
    </g>
    '''
    return card_base("Hồ cá sấu và hòn đảo ở giữa", content, "Diện tích mặt nước = Diện tích hồ A×B - Diện tích đảo a×b")

def svg_currency_exchange():
    content = '''
    <g transform="translate(130, 70)">
        <rect x="0" y="15" width="130" height="95" fill="#DCFCE7" stroke="#16A34A" stroke-width="2" rx="8"/>
        <text x="65" y="50" font-family="Arial" font-size="14" font-weight="bold" fill="#15803D" text-anchor="middle">USD ($)</text>
        <text x="65" y="85" font-family="Arial" font-size="24" font-weight="bold" fill="#166534" text-anchor="middle">X Đô la</text>
        <g transform="translate(145, 38)">
            <text x="30" y="15" font-family="Arial" font-size="11" font-weight="bold" fill="#2563EB" text-anchor="middle">Tỷ giá E</text>
            <path d="M 5 25 L 55 25" stroke="#2563EB" stroke-width="3"/>
            <polygon points="62,25 52,20 52,30" fill="#2563EB"/>
        </g>
        <rect x="220" y="15" width="150" height="95" fill="#EFF6FF" stroke="#2563EB" stroke-width="2" rx="8"/>
        <text x="295" y="50" font-family="Arial" font-size="14" font-weight="bold" fill="#1E40AF" text-anchor="middle">VNĐ (đ)</text>
        <text x="295" y="85" font-family="Arial" font-size="22" font-weight="bold" fill="#1D4ED8" text-anchor="middle">X × E đồng</text>
    </g>
    '''
    return card_base("Quầy đổi ngoại tệ: USD sang VNĐ", content, "Số tiền Việt Nam đồng nhận được = X × Tỷ giá")

# --- LESSON 04 & CONDITIONAL ---
def svg_scale_compare():
    content = '''
    <g transform="translate(160, 65)">
        <rect x="130" y="30" width="20" height="110" fill="#64748B" rx="2"/>
        <polygon points="140,140 90,160 190,160" fill="#475569"/>
        <line x1="30" y1="30" x2="250" y2="30" stroke="#0F2A44" stroke-width="4"/>
        <circle cx="140" cy="30" r="7" fill="#EF4444"/>
        <g transform="translate(10, 35)">
            <line x1="25" y1="0" x2="0" y2="50" stroke="#94A3B8" stroke-width="2"/>
            <line x1="25" y1="0" x2="50" y2="50" stroke="#94A3B8" stroke-width="2"/>
            <rect x="-15" y="50" width="80" height="18" fill="#F59E0B" rx="4"/>
            <rect x="0" y="20" width="50" height="30" fill="#3B82F6" rx="4"/>
            <text x="25" y="41" font-family="Arial" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">A</text>
        </g>
        <g transform="translate(200, 35)">
            <line x1="25" y1="0" x2="0" y2="50" stroke="#94A3B8" stroke-width="2"/>
            <line x1="25" y1="0" x2="50" y2="50" stroke="#94A3B8" stroke-width="2"/>
            <rect x="-15" y="50" width="80" height="18" fill="#F59E0B" rx="4"/>
            <rect x="0" y="20" width="50" height="30" fill="#EF4444" rx="4"/>
            <text x="25" y="41" font-family="Arial" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">B</text>
        </g>
    </g>
    '''
    return card_base("Cân so sánh: Tìm số lớn hơn", content, "So sánh hai giá trị A và B để tìm giá trị cực đại")

def svg_even_odd_filter():
    content = '''
    <g transform="translate(130, 75)">
        <rect x="0" y="15" width="130" height="95" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" rx="8"/>
        <text x="65" y="48" font-family="Arial" font-size="14" font-weight="bold" fill="#1D4ED8" text-anchor="middle">SỐ CHẴN</text>
        <text x="65" y="82" font-family="Arial" font-size="18" font-weight="bold" fill="#2563EB" text-anchor="middle">n % 2 == 0</text>
        <text x="170" y="72" font-family="Arial" font-size="32" font-weight="bold" fill="#64748B" text-anchor="middle">⚡</text>
        <rect x="210" y="15" width="130" height="95" fill="#FEF2F2" stroke="#EF4444" stroke-width="2" rx="8"/>
        <text x="275" y="48" font-family="Arial" font-size="14" font-weight="bold" fill="#B91C1C" text-anchor="middle">SỐ LẺ</text>
        <text x="275" y="82" font-family="Arial" font-size="18" font-weight="bold" fill="#DC2626" text-anchor="middle">n % 2 != 0</text>
    </g>
    '''
    return card_base("Phân loại số chẵn và số lẻ", content, "Kiểm tra tính chẵn lẻ dựa vào số dư khi chia cho 2")

def svg_leap_year_cal():
    content = '''
    <g transform="translate(150, 65)">
        <rect x="0" y="0" width="300" height="140" fill="#FFFFFF" stroke="#DC2626" stroke-width="2.5" rx="10"/>
        <rect x="0" y="0" width="300" height="38" fill="#DC2626" rx="8"/>
        <text x="150" y="25" font-family="Arial" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">THÁNG 2 — NĂM NHUẬN</text>
        <text x="80" y="80" font-family="Arial" font-size="13" fill="#64748B" text-anchor="middle">Năm thường</text>
        <text x="80" y="115" font-family="Arial" font-size="26" font-weight="bold" fill="#475569" text-anchor="middle">28 ngày</text>
        <line x1="150" y1="48" x2="150" y2="130" stroke="#CBD5E1" stroke-width="1.5"/>
        <text x="220" y="80" font-family="Arial" font-size="13" font-weight="bold" fill="#DC2626" text-anchor="middle">Năm nhuận</text>
        <text x="220" y="115" font-family="Arial" font-size="26" font-weight="bold" fill="#DC2626" text-anchor="middle">29 ngày</text>
    </g>
    '''
    return card_base("Kiểm tra năm nhuận trên tờ lịch", content, "Năm nhuận chia hết cho 400 hoặc chia hết cho 4 nhưng không cho 100")

def svg_taxi_meter():
    content = '''
    <g transform="translate(140, 70)">
        <rect x="0" y="0" width="320" height="125" fill="#FEF08A" stroke="#CA8A04" stroke-width="2.5" rx="10"/>
        <rect x="25" y="22" width="125" height="80" fill="#0F172A" rx="6"/>
        <text x="87" y="70" font-family="Courier New, monospace" font-size="28" font-weight="bold" fill="#22C55E" text-anchor="middle">12.5 km</text>
        <text x="87" y="90" font-family="Arial" font-size="10" fill="#94A3B8" text-anchor="middle">QUÃNG ĐƯỜNG</text>
        <rect x="170" y="22" width="125" height="80" fill="#0F172A" rx="6"/>
        <text x="232" y="70" font-family="Courier New, monospace" font-size="24" font-weight="bold" fill="#F59E0B" text-anchor="middle">145.000đ</text>
        <text x="232" y="90" font-family="Arial" font-size="10" fill="#94A3B8" text-anchor="middle">CƯỚC TAXI</text>
    </g>
    '''
    return card_base("Đồng hồ tính cước taxi bậc thang", content, "Cước phí tính theo từng bậc cự ly di chuyển")

def svg_electric_bill():
    content = '''
    <g transform="translate(130, 68)">
        <rect x="0" y="0" width="340" height="135" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" rx="10"/>
        <text x="170" y="32" font-family="Arial" font-size="13" font-weight="bold" fill="#1E40AF" text-anchor="middle">BIỂU PHÍ ĐIỆN SINH HOẠT BẬC THANG</text>
        <rect x="20" y="52" width="85" height="60" fill="#DBEAFE" stroke="#3B82F6" rx="6"/>
        <text x="62" y="78" font-family="Arial" font-size="12" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Bậc 1</text>
        <text x="62" y="98" font-family="Arial" font-size="11" fill="#1E40AF" text-anchor="middle">0 - 50 kWh</text>
        <rect x="125" y="52" width="90" height="60" fill="#FDE047" stroke="#EAB308" rx="6"/>
        <text x="170" y="78" font-family="Arial" font-size="12" font-weight="bold" fill="#854D0E" text-anchor="middle">Bậc 2</text>
        <text x="170" y="98" font-family="Arial" font-size="11" fill="#78350F" text-anchor="middle">51 - 100 kWh</text>
        <rect x="235" y="52" width="85" height="60" fill="#FCA5A5" stroke="#EF4444" rx="6"/>
        <text x="277" y="78" font-family="Arial" font-size="12" font-weight="bold" fill="#991B1B" text-anchor="middle">Bậc 3</text>
        <text x="277" y="98" font-family="Arial" font-size="11" fill="#7F1D1D" text-anchor="middle">> 100 kWh</text>
    </g>
    '''
    return card_base("Hóa đơn tiền điện sinh hoạt bậc thang", content, "Lượng điện tiêu thụ được phân chia theo từng bậc định mức")

# --- LOOPS & LISTS ---
def svg_sum_series():
    content = '''
    <g transform="translate(100, 80)">
        <text x="200" y="40" font-family="Courier New, monospace" font-size="28" font-weight="bold" fill="#0F2A44" text-anchor="middle">S = 1 + 2 + 3 + ... + N</text>
        <line x1="40" y1="75" x2="360" y2="75" stroke="#2563EB" stroke-width="2.5"/>
        <text x="200" y="105" font-family="Arial" font-size="13" font-weight="bold" fill="#2563EB" text-anchor="middle">Tích lũy giá trị qua từng bước lặp</text>
    </g>
    '''
    return card_base("Vòng lặp cộng dồn tổng dãy số tự nhiên", content, "Tính tổng dãy số liên tiếp từ 1 đến N bằng vòng lặp")

def svg_factor_tree():
    content = '''
    <g transform="translate(170, 65)">
        <rect x="95" y="0" width="70" height="45" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" rx="6"/>
        <text x="130" y="30" font-family="Arial" font-size="20" font-weight="bold" fill="#1D4ED8" text-anchor="middle">60</text>
        <line x1="110" y1="45" x2="65" y2="85" stroke="#64748B" stroke-width="2.5"/>
        <line x1="150" y1="45" x2="195" y2="85" stroke="#64748B" stroke-width="2.5"/>
        <circle cx="65" cy="105" r="24" fill="#DCFCE7" stroke="#16A34A" stroke-width="2.5"/>
        <text x="65" y="112" font-family="Arial" font-size="18" font-weight="bold" fill="#15803D" text-anchor="middle">2</text>
        <rect x="160" y="80" width="70" height="48" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" rx="6"/>
        <text x="195" y="112" font-family="Arial" font-size="18" font-weight="bold" fill="#1D4ED8" text-anchor="middle">30</text>
    </g>
    '''
    return card_base("Cây phân tích số ra thừa số nguyên tố", content, "Chia liên tiếp cho các ước nguyên tố nhỏ nhất")

def svg_piggy_bank():
    content = '''
    <g transform="translate(160, 65)">
        <ellipse cx="140" cy="80" rx="90" ry="60" fill="#F472B6" stroke="#DB2777" stroke-width="2.5"/>
        <circle cx="70" cy="75" r="18" fill="#F472B6" stroke="#DB2777" stroke-width="2"/>
        <circle cx="65" cy="75" r="3.5" fill="#0F172A"/>
        <circle cx="75" cy="75" r="3.5" fill="#0F172A"/>
        <rect x="115" y="25" width="50" height="10" fill="#DB2777" rx="3"/>
        <circle cx="140" cy="12" r="14" fill="#FBBF24" stroke="#D97706" stroke-width="2"/>
        <text x="140" y="18" font-family="Arial" font-size="15" font-weight="bold" fill="#92400E" text-anchor="middle">$</text>
    </g>
    '''
    return card_base("Nuôi heo đất: Tích lũy tiền tiết kiệm hàng ngày", content, "Cộng dồn số tiền tiết kiệm mỗi ngày vào danh sách tổng")

def svg_tea_queue():
    people = []
    for i in range(4):
        people.append(f'''
        <g transform="translate({i*85}, 0)">
            <circle cx="30" cy="30" r="16" fill="#3B82F6"/>
            <rect x="12" y="50" width="36" height="50" fill="#60A5FA" rx="5"/>
            <text x="30" y="118" font-family="Arial" font-size="11" font-weight="bold" fill="#0F2A44" text-anchor="middle">Khách #{i+1}</text>
        </g>''')
    inner = "".join(people)
    content = f'''
    <g transform="translate(130, 65)">
        {inner}
        <g transform="translate(340, 15)">
            <rect x="0" y="0" width="40" height="85" fill="#FEF3C7" stroke="#D97706" stroke-width="2" rx="6"/>
            <text x="20" y="48" font-family="Arial" font-size="10" font-weight="bold" fill="#B45309" text-anchor="middle">QUẦY</text>
        </g>
    </g>
    '''
    return card_base("Xếp hàng mua trà sữa: Chiến lược tham lam", content, "Sắp xếp thời gian phục vụ tăng dần để tối thiểu tổng thời gian chờ")

def svg_mult_table():
    content = '''
    <g transform="translate(150, 65)">
        <rect x="0" y="0" width="300" height="135" fill="#F8FAFC" stroke="#64748B" stroke-width="2" rx="8"/>
        <text x="55" y="38" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="#0F2A44">5 × 1 = 5</text>
        <text x="55" y="70" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="#0F2A44">5 × 2 = 10</text>
        <text x="55" y="102" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="#0F2A44">5 × 3 = 15</text>
        <text x="195" y="38" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="#0F2A44">5 × 8 = 40</text>
        <text x="195" y="70" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="#0F2A44">5 × 9 = 45</text>
        <text x="195" y="102" font-family="Courier New, monospace" font-size="16" font-weight="bold" fill="#0F2A44">5 × 10 = 50</text>
    </g>
    '''
    return card_base("Bảng cửu chương nhân từ 1 đến 10", content, "In bảng phép nhân từ 1 đến 10 của một số nguyên N")

# RENDER ALL NEW SVG ASSETS
print("🎨 Đang render toàn bộ các hình minh họa thiết kế riêng...")
render("tl_robot_greeting", svg_robot_greeting())
render("tl_couplet_banner", svg_couplet_banner())
render("tl_ticket_number", svg_ticket_number())
render("tl_sep_hyphen", svg_sep_hyphen())
render("tl_double_harvest", svg_double_harvest())
render("tl_swap_cards", svg_swap_cards())
render("tl_two_bags_marbles", svg_two_bags_marbles())
render("tl_fabric_roll", svg_fabric_roll())
render("tl_candy_grid", svg_candy_grid())
render("tl_train_carriages", svg_train_carriages())
render("tl_four_ops", svg_four_ops())
render("tl_three_generations", svg_three_generations())
render("tl_donut_bakery", svg_donut_bakery())
render("tl_business_card", svg_business_card())
render("tl_digit_split", svg_digit_split())
render("tl_clock_24h", svg_clock_24h())
render("tl_week_days", svg_week_days())
render("tl_running_track", svg_running_track())
render("tl_desks", svg_desks())
render("tl_light_border", svg_light_border())
render("tl_number_mirror", svg_number_mirror())
render("tl_tree_planting", svg_tree_planting())
render("tl_clock_hands_12h", svg_clock_hands_12h())
render("tl_square_geo", svg_square_geo())
render("tl_rect_geo", svg_rect_geo())
render("tl_triangle_geo", svg_triangle_geo())
render("tl_crocodile_island", svg_crocodile_island())
render("tl_currency_exchange", svg_currency_exchange())
render("tl_scale_compare", svg_scale_compare())
render("tl_even_odd_filter", svg_even_odd_filter())
render("tl_leap_year_cal", svg_leap_year_cal())
render("tl_taxi_meter", svg_taxi_meter())
render("tl_electric_bill", svg_electric_bill())
render("tl_sum_series", svg_sum_series())
render("tl_factor_tree", svg_factor_tree())
render("tl_piggy_bank", svg_piggy_bank())
render("tl_tea_queue", svg_tea_queue())
render("tl_mult_table", svg_mult_table())

# LOAD AND COMBINE WITH CURATED SCENARIO SUITE
TAILORED_MAP = {
    # Lesson 01
    "pya_l01_p01_loi_chao_robot": ("tl_robot_greeting.png", "Hệ thống robot tự hành phát lời chào"),
    "pya_l01_p02_cau_doi_tet": ("tl_couplet_banner.png", "Bảng điện tử hiển thị hai vế câu đối"),
    "pya_l01_p05_doc_in_so_nguyen": ("tl_ticket_number.png", "Máy đếm vé và in mã số may mắn"),
    "pya_l01_p03_in_so_sep": ("tl_sep_hyphen.png", "In các số nối nhau bằng dấu gạch ngang"),
    "pya_l01_p25_nhan_doi_gia_tri": ("tl_double_harvest.png", "Mô hình nhân đôi sản lượng nông nghiệp"),
    "pya_l01_p11_hoan_doi_hai_bien": ("tl_swap_cards.png", "Hai bạn An và Bình hoán đổi thẻ số"),
    "pya_l01_p21_tong_hai_so_2_dong": ("tl_two_bags_marbles.png", "Tính tổng số viên bi của Minh và Nam"),
    "pya_l01_p22_hieu_hai_so": ("tl_fabric_roll.png", "Độ dài cuộn vải sau khi cắt may"),
    "pya_l01_p23_tich_hai_so": ("tl_candy_grid.png", "Đóng gói bánh kẹo A hộp mỗi hộp B chiếc"),
    "pya_l01_p08_doan_tau_toa_xe_ghep_so": ("tl_train_carriages.png", "Đoàn tàu hỏa kéo hai toa xe mang số a và b"),
    "pya_l01_p13_bon_phep_tinh": ("tl_four_ops.png", "Bốn phép tính số học cơ bản"),
    "pya_l01_p10_co_may_thoi_gian_3_the_he": ("tl_three_generations.png", "Tuổi của ba thành viên thuộc ba thế hệ"),
    "pya_l01_p06_cua_hang_banh_ran": ("tl_donut_bakery.png", "Hóa đơn thanh toán cửa hàng bánh rán"),
    "pya_l01_p17_tam_danh_thiep_thong_minh": ("tl_business_card.png", "Tấm danh thiếp cá nhân thông minh"),
    "pya_l01_p20_doi_thuoc_ke_milimet": ("curated_ruler.png", "Thước kẻ học sinh đo milimet và centimet"),
    "pya_l01_p14_ghep_ngay_thang_nam": ("curated_date_format.png", "Định dạng ngày tháng năm d/m/y"),

    # Lesson 02
    "pya_l02_p04_chu_so_tan_cung": ("tl_digit_split.png", "Tách chữ số tận cùng của tấm vé số"),
    "pya_l02_p10_chu_so_hang_chuc": ("tl_digit_split.png", "Tách chữ số hàng chục của biển số xe"),
    "pya_l02_p29_tach_chu_so_tan_cung": ("tl_digit_split.png", "Tách chữ số tận cùng của mã số may mắn"),
    "pya_l02_p34_dong_ho_24h": ("tl_clock_24h.png", "Đồng hồ điện tử định dạng 24 giờ"),
    "pya_l02_p35_ngay_trong_tuan": ("tl_week_days.png", "Chu kỳ 7 ngày trong tuần (Chủ Nhật = 0)"),
    "pya_l02_p27_vong_chay_dien_kinh": ("tl_running_track.png", "Vòng chạy điền kinh sân vận động"),
    "pya_l02_p28_xep_ban_hoc": ("tl_desks.png", "Phòng thi xếp bàn đôi học sinh"),
    "pya_l02_p05_bong_den_vien_bien_hieu": ("tl_light_border.png", "Bóng đèn mắc viền quanh biển hiệu"),
    "pya_l02_p18_so_dao_nguoc_3_chu_so": ("tl_number_mirror.png", "Gương thần đảo ngược 3 chữ số"),
    "pya_l02_p30_dao_nguoc_so_2_chu_so": ("tl_number_mirror.png", "Giải mã mật thư: Đảo ngược số 2 chữ số"),
    "pya_l02_p26_trong_cay_dai_lo": ("tl_tree_planting.png", "Trồng cây xanh thẳng tắp dọc đại lộ"),
    "pya_l02_p08_kim_dong_ho_12_gio": ("tl_clock_hands_12h.png", "Kim giờ và kim phút trên mặt đồng hồ tròn"),
    "pya_l02_p31_xe_buyt_cho_hoc_sinh": ("curated_bus.png", "Xe buýt chở học sinh theo sức chứa K chỗ"),
    "pya_l02_p19_chuyen_xe_hoc_sinh": ("curated_bus.png", "Tính số chuyến xe buýt chở học sinh"),
    "pya_l02_p16_du_quay_vong_tron": ("curated_ferris_wheel.png", "Vòng đu quay công viên có N cabin"),
    "pya_l02_p12_ban_co_caro_vo_tan": ("curated_caro_board.png", "Bàn cờ Ca-rô và hệ tọa độ ô vuông"),

    # Lesson 03
    "pya_l03_p01_hinh_vuong": ("tl_square_geo.png", "Hình vuông: Chu vi và diện tích"),
    "pya_l03_p20_khung_tranh_hinh_vuong": ("tl_square_geo.png", "Khung tranh hình vuông: Chu vi và diện tích nẹp viền"),
    "pya_l03_p02_hinh_chu_nhat": ("tl_rect_geo.png", "Hình chữ nhật: Chu vi và diện tích"),
    "pya_l03_p19_manh_vuon_chu_nhat": ("tl_rect_geo.png", "Mảnh vườn hình chữ nhật: Kích thước và diện tích"),
    "pya_l03_p04_canh_con_lai_cua_hinh_chu_nhat": ("tl_rect_geo.png", "Tính cạnh còn lại của hình chữ nhật khi biết diện tích"),
    "pya_l03_p03_chu_vi_tam_giac": ("tl_triangle_geo.png", "Chu vi hình tam giác ba cạnh a, b, c"),
    "pya_l03_p21_chu_vi_tam_giac_abc": ("tl_triangle_geo.png", "Chu vi tam giác ABC"),
    "pya_l03_p23_ho_ca_sau_va_dao_nho": ("tl_crocodile_island.png", "Hồ cá sấu và hòn đảo nhỏ ở giữa"),
    "pya_l03_p31_doi_do_la_sang_tien_viet": ("tl_currency_exchange.png", "Quầy đổi ngoại tệ: USD sang VNĐ"),
    "pya_l03_p10_dien_tich_bon_hoa_chu_thap": ("curated_flower_cross.png", "Sơ đồ bồn hoa chữ thập trong công viên"),
    "pya_l03_p16_loi_di_quanh_ho": ("curated_lake_walkway.png", "Mặt bằng hồ nước và đường đi dạo bao quanh"),
    "pya_l03_p15_lat_gach_nen_nha": ("curated_tiling_floor.png", "Lát sàn phòng học bằng các viên gạch vuông"),
    "pya_l03_p25_lat_gach_san_truong": ("curated_tiling_floor.png", "Lát gạch sân trường bằng các viên gạch vuông"),
    "pya_l03_p27_rao_quanh_vuon_hoa_co_cua": ("curated_fence_garden.png", "Làm hàng rào bao quanh vườn hoa có chừa cửa"),
    "pya_l03_p32_hang_rao_manh_dat": ("curated_fence_garden.png", "Hàng rào bao quanh mảnh đất chữ nhật"),
    "pya_l03_p30_the_tich_hop_chu_nhat": ("curated_box3d.png", "Thể tích hình hộp chữ nhật có ba kích thước a, b, h"),
    "pya_l03_p05_dien_tich_hinh_thang": ("curated_trapezoid.png", "Diện tích hình thang với hai đáy a, b và chiều cao h"),
    "pya_l03_p11_dien_tich_tam_giac_vuong": ("curated_right_triangle.png", "Diện tích tam giác vuông hai cạnh góc vuông a, b"),
    "pya_l03_p22_dien_tich_tam_giac_vuong": ("curated_right_triangle.png", "Diện tích tam giác vuông hai cạnh góc vuông a, b"),
    "pya_l03_p17_son_tuong_phong": ("curated_wall_painting.png", "Diện tích quét sơn tường phòng học (trừ cửa ra vào và cửa sổ)"),
    "pya_l03_p14_doi_do_c_sang_do_f": ("curated_thermometer.png", "Thang đo nhiệt độ Celsius và Fahrenheit"),
    "pya_l03_p18_chay_bo_gap_nhau": ("curated_motion_meet.png", "Bài toán hai người chạy bộ ngược chiều gặp nhau"),
    "pya_l03_p08_thuan_di_gap_anh": ("curated_motion_meet.png", "Bài toán hai chuyển động ngược chiều gặp nhau"),
    "pya_l03_p28_doi_giay_sang_gio_phut_giay": ("curated_time_cycle.png", "Sơ đồ chuyển đổi đơn vị thời gian Giờ - Phút - Giây"),
    "pya_l03_p24_doi_giay_sang_gio_phut_giay": ("curated_time_cycle.png", "Sơ đồ chuyển đổi giây sang giờ, phút, giây"),
    "pya_l03_p09_phut_sang_gio_phut": ("curated_time_cycle.png", "Sơ đồ chuyển đổi phút sang giờ và phút"),
    "pya_l03_p29_doi_sang_tong_giay": ("curated_time_cycle.png", "Đổi giờ, phút, giây sang tổng số giây"),

    # Lesson 04 & 05 & 06
    "pya_l04_p04_so_lon_nhat_trong_hai_so": ("tl_scale_compare.png", "Cân so sánh tìm số lớn nhất trong hai số"),
    "pya_l04_p01_kiem_tra_so_chan_le": ("tl_even_odd_filter.png", "Kiểm tra tính chẵn lẻ của một số nguyên"),
    "pya_l06_p01_so_chan_co_hai_chu_so": ("tl_even_odd_filter.png", "Kiểm tra số chẵn có hai chữ số"),
    "pya_l06_p06_kiem_tra_nam_nhuan": ("tl_leap_year_cal.png", "Kiểm tra năm nhuận trên tờ lịch"),
    "pya_l05_p07_tinh_cuoc_taxi_bac_thang": ("tl_taxi_meter.png", "Đồng hồ tính cước taxi bậc thang"),
    "pya_l06_p13_tien_dien_bac_thang": ("tl_electric_bill.png", "Hóa đơn tiền điện sinh hoạt bậc thang"),
    "pya_l05_p01_den_giao_thong_nga_tu": ("curated_traffic_light.png", "Đèn tín hiệu giao thông ngã tư (Đỏ, Vàng, Xanh)"),
    "pya_l06_p04_diem_nam_trong_hinh_chu_nhat": ("curated_point_in_rect.png", "Kiểm tra điểm M(x, y) nằm trong hình chữ nhật"),
    "pya_l06_p08_tam_giac_vuong_hay_khong": ("curated_right_triangle.png", "Định lý Pythagoras kiểm tra tam giác vuông"),

    # Loops (Lessons 07, 08, 09)
    "pya_l07_p04_bang_cuu_chuong": ("tl_mult_table.png", "Bảng cửu chương nhân từ 1 đến 10"),
    "pya_l07_p13_tam_giac_vuong_dau_sao": ("curated_star_triangle.png", "In tam giác vuông dấu sao bằng vòng lặp lồng nhau"),
    "pya_l08_p09_chu_oc_sen_leo_cot_co": ("curated_snail_pole.png", "Hành trình chú ốc sên bò lên cột cờ ngày và đêm"),
    "pya_l09_p09_tam_giac_sao_can": ("curated_star_triangle.png", "In tam giác sao cân bằng vòng lặp lồng nhau"),
    "pya_l07_p01_tinh_tong_tu_1_den_n": ("tl_sum_series.png", "Vòng lặp cộng dồn tổng dãy số tự nhiên"),
    "pya_l11_p13_phan_tich_ra_thua_so_nguyen_to": ("tl_factor_tree.png", "Cây phân tích số ra thừa số nguyên tố"),

    # Lists & Greedy (Lessons 11, 12, 14)
    "pya_l16_p15_heo_dat_tiet_kiem": ("tl_piggy_bank.png", "Nuôi heo đất: Tích lũy tiền tiết kiệm hàng ngày"),
    "pya_l17_p14_xep_hang_mua_tra_sua_greedy": ("tl_tea_queue.png", "Xếp hàng mua trà sữa: Chiến lược tham lam"),
    "pya_l15_p09_mat_ma_caesar_dich_chuyen_k": ("curated_caesar.png", "Mật mã Caesar dịch chuyển K ký tự"),
    "pya_l15_p10_giai_ma_mat_thu_caesar": ("curated_caesar.png", "Giải mã mật thư Caesar dịch chuyển K ký tự")
}

print(f"\n📊 TỔNG CỘNG ĐÃ THIẾT KẾ ĐO NI ĐÓNG GIÀY: {len(TAILORED_MAP)} BÀI TOÁN CHUẨN XÁC.")

with open(Path("courses/python-bang-a/problem_diagrams_full_map.json"), "w", encoding="utf-8") as f:
    json.dump(TAILORED_MAP, f, ensure_ascii=False, indent=2)

print("✅ Đã cập nhật xong problem_diagrams_full_map.json!")
