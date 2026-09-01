# Thuật toán 0-1 BFS tìm đường đi ngắn nhất bằng Deque
## Mã bài toán: CPPB2-L12-17-01-BFS-DO-THI-TRONG-SO-0-1

## Bối cảnh & Nhiệm vụ
Tìm đường đi ngắn nhất trên đồ thị có trọng số cạnh chỉ gồm 0 và 1 trong thời gian $\mathcal{O}(V + E)$.

## Đầu vào (Input)
Số đỉnh $N, M$ và các cạnh có trọng số 0 hoặc 1.

## Đầu ra (Output)
In ra khoảng cách ngắn nhất.

## Ví dụ mẫu
### Sample 1
Input:
```text
3 3
1 2 0
2 3 1
1 3 1
```
Output:
```text
1
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
