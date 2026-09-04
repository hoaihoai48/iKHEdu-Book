# Dãy Con Giảm Dài Nhất (LDS)

## Bối cảnh
Trong quá trình hạ nhiệt độ lò luyện kim công nghiệp, các cảm biến ghi nhận nhiệt độ theo từng chu kỳ làm mát tạo thành dãy $N$ số nguyên $A_1, A_2, \dots, A_N$. Kỹ sư vận hành cần đánh giá tính ổn định của quy trình thông qua độ dài của chuỗi các lần đo có nhiệt độ giảm dần nghiêm ngặt dài nhất.

## Nhiệm vụ
Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm độ dài của dãy con giảm nghiêm ngặt dài nhất.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất độ dài của dãy con giảm nghiêm ngặt dài nhất.

## Sample 1
### Input
```text
5
10 9 2 5 3 7 101 18
```
### Output
```text
4
```

### Giải thích
Với dãy 8 số nguyên $[10, 9, 2, 5, 3, 7, 101, 18]$:
Một dãy con giảm nghiêm ngặt dài nhất có thể trích xuất là $[10, 9, 5, 3]$ (hoặc $[10, 9, 7, 3]$). Độ dài lớn nhất đạt được là 4.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
