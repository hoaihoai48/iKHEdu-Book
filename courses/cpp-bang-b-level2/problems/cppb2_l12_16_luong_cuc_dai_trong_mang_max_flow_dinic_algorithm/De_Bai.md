# Luồng cực đại trong mạng (Dinic)

## Bối cảnh

Nhà máy nước sạch vận hành mạng lưới N trạm bơm với M đường ống một chiều có công suất giới hạn khác nhau tùy đường kính ống dẫn. Nước được bơm từ trạm nguồn S đến trạm tiêu thụ T, và ban giám đốc cần biết lưu lượng lớn nhất hệ thống có thể đáp ứng trong giờ cao điểm để ký hợp đồng cung cấp cho khu công nghiệp mới. Phòng kỹ thuật dùng thuật toán Dinic để tính luồng cực đại vì mạng lưới có quy mô lớn.

## Nhiệm vụ

Cho mạng chảy gồm $N$ đỉnh, $M$ cạnh có hướng với sức chứa, nguồn $S$ và đích $T$. Hãy lập trình tính luồng cực đại từ $S$ đến $T$ bằng thuật toán Dinic, rồi in ra kết quả.

## Input

- Dòng 1: bốn số nguyên $N, M, S, T$ ($1 \le S, T \le N \le 500$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v, c$ là ống một chiều sức chứa $c$ ($1 \le c \le 10^9$).

## Output

- In ra một dòng duy nhất là giá trị luồng cực đại.

## Sample 1

### Input

```text
4 5 1 4
1 2 3
1 3 2
2 3 1
2 4 2
3 4 3
```

### Output

```text
5```

### Giải thích

- Nguồn $1$ đẩy tối đa $3$ đơn vị sang $2$ và $2$ đơn vị sang $3$, tổng $5$ đơn vị rời nguồn.
- Trạm $2$ chuyển $2$ đơn vị thẳng tới đích $4$; trạm $3$ nhận $2$ từ nguồn cộng $1$ từ trạm $2$ rồi chuyển hết $3$ đơn vị tới đích.
- Đích $4$ nhận $2 + 3 = 5$ đơn vị, đây cũng là nhát cắt nhỏ nhất nên chương trình in ra $5$.

## Ràng buộc

- $1 \le N \le 500$, $0 \le M \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
