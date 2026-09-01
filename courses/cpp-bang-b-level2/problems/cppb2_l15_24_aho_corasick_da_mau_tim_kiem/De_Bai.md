# Thuật toán Aho-Corasick tìm kiếm đồng thời đa mẫu
## Mã bài toán: CPPB2-L15-24-AHO-CORASICK-DA-MAU-TIM-KIEM

## Bối cảnh & Nhiệm vụ
Xây dựng cây tự động Aho-Corasick để tìm kiếm đồng thời $K$ xâu mẫu trong văn bản $T$ trong $\mathcal{O}(|T| + \sum |P_i|)$.

## Đầu vào (Input)
Văn bản $T$ và $K$ xâu mẫu.

## Đầu ra (Output)
In ra tổng số lần xuất hiện.

## Ví dụ mẫu
### Sample 1
Input:
```text
ushers 2
he
she
```
Output:
```text
2
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
