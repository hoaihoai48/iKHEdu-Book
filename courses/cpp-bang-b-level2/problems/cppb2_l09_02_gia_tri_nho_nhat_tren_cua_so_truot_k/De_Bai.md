# Giá trị nhỏ nhất trên cửa sổ trượt k

## Bối cảnh

Trạm quan trắc khí tượng đặt dọc bờ sông ghi lại nhiệt độ mỗi giờ trong suốt $N$ giờ liên tiếp của đợt rét đậm. Để cảnh báo sương muối cho bà con nông dân, trạm cần biết trong mỗi khoảng $K$ giờ liên tiếp thì nhiệt độ thấp nhất là bao nhiêu, vì chỉ cần một giờ giá rét là cả cánh đồng rau màu có thể mất trắng. Cửa sổ thời gian trượt dần từng giờ một, và cán bộ trạm muốn có bảng giá trị thấp nhất của mọi cửa sổ để phát bản tin kịp thời.

## Nhiệm vụ

Cho $N$ số nguyên là nhiệt độ từng giờ và độ dài cửa sổ $K$. Với mỗi cửa sổ gồm $K$ giờ liên tiếp (trượt từ đầu đến cuối dãy), hãy lập trình tìm nhiệt độ thấp nhất trong cửa sổ đó, rồi in ra $N - K + 1$ giá trị theo thứ tự.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, K$ ($1 \le K \le N \le 10^6$), là số giờ quan trắc và độ dài cửa sổ.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($-10^9 \le a_i \le 10^9$), là nhiệt độ từng giờ.

## Output

- In ra $N - K + 1$ số nguyên trên một dòng là giá trị nhỏ nhất của từng cửa sổ.

## Sample 1

### Input

```text
8 3
1 3 -1 -3 5 3 6 7
```

### Output

```text
-1 -3 -3 -3 3 3
```

### Giải thích

- Cửa sổ $[1, 3, -1]$ có giá trị nhỏ nhất $-1$; trượt sang $[3, -1, -3]$ được $-3$.
- Cửa sổ $[-1, -3, 5]$ được $-3$; cửa sổ $[-3, 5, 3]$ được $-3$.
- Cửa sổ $[5, 3, 6]$ được $3$; cửa sổ cuối $[3, 6, 7]$ được $3$.
- Sáu cửa sổ cho sáu giá trị $-1, -3, -3, -3, 3, 3$.

## Ràng buộc

- $1 \le K \le N \le 10^6$, $-10^9 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
