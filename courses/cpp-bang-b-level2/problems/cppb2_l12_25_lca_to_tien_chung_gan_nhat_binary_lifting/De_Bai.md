# Tổ tiên chung gần nhất (LCA) bằng Binary Lifting
## Mã bài toán: CPPB2-L12-25-LCA-TO-TIEN-CHUNG-GAN-NHAT-BINARY-LIFTING

## Bối cảnh & Nhiệm vụ
Trả lời $Q$ truy vấn tìm tổ tiên chung gần nhất của hai đỉnh $U, V$ trên cây trong $\mathcal{O}(\log N)$.

## Đầu vào (Input)
Cây $N$ đỉnh và $Q$ truy vấn $(U, V)$.

## Đầu ra (Output)
In ra LCA cho mỗi truy vấn.

## Ví dụ mẫu
### Sample 1
Input:
```text
3
1 2
1 3
1
2 3
```
Output:
```text
1
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
