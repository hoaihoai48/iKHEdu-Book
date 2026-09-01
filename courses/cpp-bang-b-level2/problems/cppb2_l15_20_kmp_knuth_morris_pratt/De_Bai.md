# Thuật toán KMP (Knuth-Morris-Pratt) tìm kiếm xâu mẫu
## Mã bài toán: CPPB2-L15-20-KMP-KNUTH-MORRIS-PRATT

## Bối cảnh & Nhiệm vụ
Đếm số lần xuất hiện của xâu mẫu $P$ trong xâu văn bản $T$ bằng mảng tiền tố $\pi$ (KMP).

## Đầu vào (Input)
Hai xâu $T$ và $P$.

## Đầu ra (Output)
In ra số lần xuất hiện.

## Ví dụ mẫu
### Sample 1
Input:
```text
ababababa aba
```
Output:
```text
4
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
