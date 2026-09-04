# Dãy Con Hình Sóng Núi (Longest Bitonic Subsequence)

## Bối cảnh
Một thiết bị bay không người lái (drone) thực hiện hành trình bay thám hiểm qua một dãy núi. Độ cao của drone tại các điểm quan sát tạo thành một chuỗi $N$ số nguyên. Một hành trình bay được gọi là có hình dạng sóng núi (Bitonic) nếu độ cao đầu tiên tăng dần nghiêm ngặt lên đến một đỉnh nào đó, sau đó giảm dần nghiêm ngặt từ đỉnh đó xuống cuối (cho phép phần tăng hoặc phần giảm rỗng). Ban điều hành muốn tìm một hành trình sóng núi chứa nhiều điểm quan sát nhất.

## Nhiệm vụ
Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm độ dài lớn nhất của một dãy con có dạng sóng núi.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^5$).

## Output
- In ra trên một dòng duy nhất độ dài lớn nhất của dãy con hình sóng núi.

## Sample 1
### Input
```text
8
1 11 2 10 4 5 2 1
```
### Output
```text
6
```

### Giải thích
Với dãy số gồm 8 phần tử $[1, 11, 2, 10, 4, 5, 2, 1]$:
Dãy con hình sóng núi dài nhất có thể chọn là $[1, 2, 10, 5, 2, 1]$ (với đỉnh là 10; phần tăng gồm 1, 2, 10 và phần giảm gồm 10, 5, 2, 1). Tổng số phần tử của dãy sóng núi này là 6.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 2000, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
