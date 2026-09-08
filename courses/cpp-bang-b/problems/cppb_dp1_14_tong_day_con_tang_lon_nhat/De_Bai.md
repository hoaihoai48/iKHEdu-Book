# Tổng Dãy Con Tăng Lớn Nhất (MSIS)

## Bối cảnh
Một nhà đầu tư phân tích lợi nhuận của các cổ phiếu qua $N$ quý liên tiếp. Để xây dựng chiến lược mua vào đón đầu chu kỳ phát triển bền vững, nhà đầu tư muốn chọn ra một chuỗi các quý đầu tư mà lợi nhuận ở quý sau luôn cao hơn quý trước (tăng nghiêm ngặt), đồng thời tổng lợi nhuận thu được từ tất cả các quý được chọn phải là lớn nhất.

## Nhiệm vụ
Cho dãy số nguyên dương $A$ gồm $N$ phần tử. Hãy lập trình tìm tổng giá trị lớn nhất của một dãy con tăng nghiêm ngặt.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^5$).

## Output
- In ra trên một dòng duy nhất tổng giá trị lớn nhất tìm được.

## Sample 1
### Input
```text
7
1 101 2 3 100 4 5
```
### Output
```text
106
```

### Giải thích
Với dãy số gồm 7 phần tử $[1, 101, 2, 3, 100, 4, 5]$:

- Dãy con tăng dài nhất là $[1, 2, 3, 4, 5]$ có tổng là $1 + 2 + 3 + 4 + 5 = 15$.
- Nhưng dãy con tăng $[1, 2, 3, 100]$ lại mang lại tổng giá trị lớn hơn nhiều: $1 + 2 + 3 + 100 = 106$. Đây là tổng lớn nhất có thể đạt được.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 2000, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
