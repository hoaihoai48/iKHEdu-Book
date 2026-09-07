# Đếm số nguyên tố cùng nhau bằng nguyên lý bao hàm-loại trừ

## Bối cảnh

Xưởng cơ khí chính xác cần tiện một lô N chi tiết máy được đánh số từ 1 đến N để lắp vào dây chuyền mới. Kỹ sư trưởng quy định chi tiết số x phải đưa đi kiểm tra lại khi x chia hết cho ít nhất một trong K thông số lỗi do phòng thí nghiệm gửi xuống. Tổ kiểm định cần đếm nhanh có bao nhiêu chi tiết đạt chuẩn trong cả lô hàng nghìn chiếc để kịp báo cáo tiến độ sản xuất.

## Nhiệm vụ

Cho số nguyên $N$ và $K$ số nguyên tố $p_1, \dots, p_K$. Hãy lập trình đếm các số $x$ ($1 \le x \le N$) chia hết cho ít nhất một trong các $p_i$, rồi in ra kết quả.

## Input

- Dòng 1: hai số nguyên $N, K$ ($1 \le N \le 10^{12}$, $1 \le K \le 20$).
- Dòng 2: $K$ số nguyên tố phân biệt $p_i$ ($2 \le p_i \le 100$).

## Output

- In ra một dòng duy nhất là số lượng số đạt chuẩn.

## Sample 1

### Input

```text
10 2
2 3
```

### Output

```text
7
```

### Giải thích

- Xét các số từ $1$ đến $10$: giữ lại các số chia hết cho $2$ hoặc cho $3$.
- Các số thỏa mãn là $2, 3, 4, 6, 8, 9, 10$ (ví dụ $6$ chia hết cho cả hai, $9$ chia hết cho $3$).
- Đếm được $7$ số nên chương trình in ra $7$.

## Ràng buộc

- $1 \le N \le 10^{12}$, $1 \le K \le 20$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
