# Tối ưu hóa bao lồi Convex Hull Trick (CHT)
## Mã bài toán: CPPB2-L08-18-CONVEX-HULL-TRICK-DP-TOI-UU-DUONG-THANG

## Bối cảnh & Nhiệm vụ
Tối ưu hóa quy hoạch động dạng $dp[i] = \min(dp[j] + m_j \cdot x_i + c_j)$ trong $\mathcal{O}(N)$.

## Đầu vào (Input)
Số $N$ và các hệ số đường thẳng.

## Đầu ra (Output)
In ra giá trị $dp[N]$.

## Ví dụ mẫu
### Sample 1
Input:
```text
3
1 2
2 1
3 0
```
Output:
```text
2
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
