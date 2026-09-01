# Thuật toán Floyd-Warshall đường đi ngắn nhất giữa mọi cặp đỉnh
## Mã bài toán: CPPB2-L12-24-FLOYD-WARSHALL-MOI-CAP-DINH

## Bối cảnh & Nhiệm vụ
Tìm ma trận khoảng cách ngắn nhất giữa tất cả các cặp đỉnh trong $\mathcal{O}(V^3)$.

## Đầu vào (Input)
Ma trận kề trọng số $N \times N$.

## Đầu ra (Output)
In ra ma trận khoảng cách.

## Ví dụ mẫu
### Sample 1
Input:
```text
2
0 3
3 0
```
Output:
```text
0 3
3 0
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
