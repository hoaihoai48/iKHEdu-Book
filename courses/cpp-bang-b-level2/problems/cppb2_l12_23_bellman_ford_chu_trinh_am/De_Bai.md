# Thuật toán Bellman-Ford phát hiện chu trình âm
## Mã bài toán: CPPB2-L12-23-BELLMAN-FORD-CHU-TRINH-AM

## Bối cảnh & Nhiệm vụ
Kiểm tra xem đồ thị có hướng có chứa chu trình trọng số âm hay không.

## Đầu vào (Input)
Số đỉnh $N, M$ và các cạnh có trọng số âm/dương.

## Đầu ra (Output)
In ra YES nếu có chu trình âm, ngược lại NO.

## Ví dụ mẫu
### Sample 1
Input:
```text
3 3
1 2 1
2 3 -5
3 1 2
```
Output:
```text
YES
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
