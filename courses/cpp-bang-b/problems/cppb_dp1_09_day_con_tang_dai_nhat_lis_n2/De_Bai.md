# Dãy Con Tăng Dài Nhất LIS O(N^2)

## Bối cảnh
Tại trạm quan trắc địa chấn ven biển, các chuyên gia theo dõi sự biến thiên áp suất lớp vỏ trái đất qua một chuỗi $N$ lần đo liên tiếp, tương ứng với dãy số $A_1, A_2, \dots, A_N$. Để nhận diện xu thế gia tăng địa chấn qua các chu kỳ, các chuyên gia cần trích xuất một chuỗi các mốc đo có giá trị áp suất tăng dần nghiêm ngặt theo thời gian, sao cho số lượng mốc đo được chọn là nhiều nhất có thể.

## Nhiệm vụ
Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm độ dài lớn nhất của một dãy con tăng nghiêm ngặt (không nhất thiết phải là các phần tử liên tiếp trong dãy ban đầu).

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$) biểu diễn số lượng phần tử của dãy.
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$), các số cách nhau bởi khoảng trắng.

## Output
- In ra trên một dòng duy nhất độ dài của dãy con tăng nghiêm ngặt dài nhất.

## Sample 1
### Input
```text
6
10 20 10 30 20 50
```
### Output
```text
4
```

### Giải thích
Với dãy số gồm 6 phần tử $[10, 20, 10, 30, 20, 50]$:
Một dãy con tăng nghiêm ngặt dài nhất có thể chọn là $[10, 20, 30, 50]$ (tương ứng với các chỉ số 1, 2, 4, 6 trong dãy gốc). Độ dài của dãy con này là 4.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 2000, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
