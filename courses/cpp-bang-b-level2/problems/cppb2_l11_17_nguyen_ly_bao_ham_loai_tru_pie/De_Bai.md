# Nguyên lý bao hàm-loại trừ đếm số nguyên tố cùng nhau

## Bối cảnh

Nhà máy sản xuất vòng bi cần kiểm tra lô N sản phẩm được đánh số từ 1 đến N trước khi đóng thùng xuất khẩu sang thị trường khó tính. Phòng kỹ thuật liệt kê K thông số lỗi, sản phẩm nào có số thứ tự chia hết cho bất kỳ thông số nào cũng bị giữ lại để kiểm tra thủ công. Giám đốc xưởng muốn biết có bao nhiêu sản phẩm sạch không vướng thông số lỗi nào để ký lệnh xuất kho ngay trong ca sáng.

## Nhiệm vụ

Cho số nguyên $N$ và $K$ số nguyên $p_1, \dots, p_K$. Hãy lập trình đếm các số $x$ ($1 \le x \le N$) không chia hết cho bất kỳ $p_i$ nào (dùng nguyên lý bao hàm-loại trừ), rồi in ra kết quả.

## Input

- Dòng 1: hai số nguyên $N, K$ ($1 \le N \le 10^{12}$, $1 \le K \le 20$).
- Dòng 2: $K$ số nguyên $p_i$ ($2 \le p_i \le 100$).

## Output

- In ra một dòng duy nhất là số lượng số sạch.

## Sample 1

### Input

```text
10 2
2 3
```

### Output

```text
3
```

### Giải thích

- Xét các số từ $1$ đến $10$: các số chia hết cho $2$ hoặc $3$ là $2, 3, 4, 6, 8, 9, 10$, tổng $7$ số.
- Lấy $10 - 7 = 3$ là số lượng số sạch gồm $1, 5, 7$.
- Chương trình in ra $3$.

## Ràng buộc

- $1 \le N \le 10^{12}$, $1 \le K \le 20$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
