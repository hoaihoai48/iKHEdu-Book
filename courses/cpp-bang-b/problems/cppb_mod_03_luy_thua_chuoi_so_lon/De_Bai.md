# Lũy Thừa Chuỗi Số Lớn

## Bối cảnh
Khi số mũ B là một chuỗi số nguyên khổng lồ có hàng trăm ngàn chữ số (không thể chứa vừa trong bất kỳ kiểu số nguyên nguyên bản nào), việc áp dụng định lý Fermat nhỏ hoặc phân rã cơ số 10 kết hợp lũy thừa nhị phân giúp tính toán chính xác giá trị A^B mod (10^9 + 7).

## Nhiệm vụ
Cho số nguyên A và số nguyên B rất lớn biểu diễn dưới dạng chuỗi ký tự. Hãy tính A^B mod (10^9 + 7).

## Input
- Dòng 1: Số nguyên dương $A$ ($1 \le A \le 10^9$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 10^5$, $B$ không bắt đầu bằng số 0).

## Output
- In ra giá trị $A^B \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
2
10
```
### Output
```text
1024
```
### Giải thích
2^10 = 1024. Khi lấy dư cho 10^9 + 7 ta được: 1024 mod (10^9 + 7) = 1024.

## Ràng buộc
- $100\%$ số test có $|B| \le 10^5, A \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
