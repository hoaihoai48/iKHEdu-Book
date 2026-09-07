# Cây đoạn động trên tọa độ tới 1e9

## Bối cảnh

Sàn đấu giá trực tuyến quản lý dải mã số sản phẩm lên tới một tỉ đơn vị nhưng tại mỗi thời điểm chỉ có rất ít mã được giao dịch thực tế. Mỗi giao dịch cộng thêm một khoản vào đúng một mã số, và ban điều hành cần tra cứu tổng giá trị trên bất kỳ đoạn mã nào để chốt phiên đấu giá theo giờ. Cây đoạn động chỉ tạo nút khi cần giúp tiết kiệm bộ nhớ mà vẫn trả lời mỗi thao tác trong thời gian logarit theo miền tọa độ.

## Nhiệm vụ

Cho $Q$ thao tác trên mảng ảo kích thước $10^9$ (ban đầu toàn $0$). Hãy lập trình xử lý: loại $1$ cộng $val$ vào vị trí $idx$; loại $2$ in ra tổng trên đoạn $[l,r]$.

## Input

- Dòng 1: số nguyên $Q$ ($1 \le Q \le 2 \cdot 10^5$).
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ idx\ val$; loại $2$ gồm $2\ l\ r$ ($1 \le idx, l \le r \le 10^9$, $|val| \le 10^9$).

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là tổng trên đoạn yêu cầu.

## Sample 1

### Input

```text
4
1 1000000000 7
1 5 3
2 1 10
2 1 1000000000
```

### Output

```text
3
10```

### Giải thích

- Cộng $7$ vào vị trí một tỉ và cộng $3$ vào vị trí $5$.
- Đoạn $[1,10]$ chỉ chứa vị trí $5$ nên tổng là $3$; đoạn $[1,10^9]$ chứa cả hai nên tổng là $3 + 7 = 10$.
- Hai truy vấn loại $2$ in ra $3$ rồi $10$ trên hai dòng.

## Ràng buộc

- $1 \le Q \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
