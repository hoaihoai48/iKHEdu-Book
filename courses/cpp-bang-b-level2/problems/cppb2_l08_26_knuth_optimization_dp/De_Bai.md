# Tối ưu hóa Knuth (Knuth DP Optimization)
## Mã bài toán: CPPB2-L08-26-KNUTH-OPTIMIZATION-DP

## Bối cảnh & Nhiệm vụ
Quy hoạch động chia đoạn tối ưu thỏa mãn điều kiện tứ giác $opt[i, j-1] \le opt[i, j] \le opt[i+1, j]$ trong $\mathcal{O}(N^2)$.

## Đầu vào (Input)
Số $N$ và chi phí cắt.

## Đầu ra (Output)
In ra chi phí tối thiểu.

## Ví dụ mẫu
### Sample 1
Input:
```text
3
1 2 3
```
Output:
```text
6
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
