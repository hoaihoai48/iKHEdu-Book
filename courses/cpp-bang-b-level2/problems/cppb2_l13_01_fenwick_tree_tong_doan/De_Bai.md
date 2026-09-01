# Truy Vấn Tổng Đoạn Fenwick Tree

## Bối cảnh
Cho mảng $N$ phần tử. Có $Q$ thao tác: `1 u v` (cộng $v$ vào $A[u]$) và `2 l r` (tính tổng $A[l..r]$).

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Truy Vấn Tổng Đoạn Fenwick Tree với độ phức tạp tối ưu nhất.

## Input
- Dòng 1: $N, Q$. Dòng 2: $N$ số $A_i$. $Q$ dòng tiếp theo: các truy vấn.

## Output
- In ra kết quả của các truy vấn loại 2.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
2 1 5
1 3 2
2 1 5
```
### Output
```text
15
17
```

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
