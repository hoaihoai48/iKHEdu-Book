# Quy hoạch động trên tập con SOS DP (Sum Over Subsets)
## Mã bài toán: CPPB2-L06-17-SOS-DP-SUM-OVER-SUBSETS

## Bối cảnh & Nhiệm vụ
Cho mảng $A$ kích thước $2^N$. Với mỗi mặt nạ $mask$, tính $F(mask) = \sum_{sub \subseteq mask} A[sub]$.

## Đầu vào (Input)
Số $N$ và $2^N$ số nguyên.

## Đầu ra (Output)
In ra các giá trị $F(mask)$.

## Ví dụ mẫu
### Sample 1
Input:
```text
2
1 2 3 4
```
Output:
```text
1 3 4 10
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
