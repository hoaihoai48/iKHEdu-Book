# Đếm số có số lượng ước là số lẻ trong đoạn

## Bối cảnh
Trong số học, một số nguyên dương $X$ có số lượng ước nguyên dương là một số lẻ khi và chỉ khi $X$ là một **số chính phương** ($X = k^2$). Cho đoạn $[L, R]$, hãy đếm xem có bao nhiêu số có số lượng ước nguyên dương là số lẻ trong đoạn này.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Đếm Số Có Số Lượng Ước Là Số Lẻ Trong Đoạn với độ phức tạp tối ưu nhất.

## Input
- Một dòng duy nhất chứa hai số nguyên dương $L, R$ ($1 \le L \le R \le 10^{18}$).

## Output
- In ra số lượng số có số ước là số lẻ trong đoạn $[L, R]$.

## Sample 1
### Input
```text
1 100
```
### Output
```text
10
```
### Giải thích
* Các số chính phương từ 1 đến 100 là $1^2, 2^2, \dots, 10^2$ (tổng cộng 10 số).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
