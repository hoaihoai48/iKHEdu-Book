# Hướng Dẫn Giảng Dạy: Đoạn Con Dài Nhất Tổng <= S
- Mở rộng $R$. Khi `cur_sum > S` thì co $L$. Cập nhật `max_len = max(max_len, R - L + 1)`.
