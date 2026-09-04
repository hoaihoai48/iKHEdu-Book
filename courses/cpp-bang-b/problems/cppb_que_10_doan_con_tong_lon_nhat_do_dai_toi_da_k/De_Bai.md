# Đoạn Con Tổng Lớn Nhất Độ Dài Tối Đa K

## Bối cảnh
Một công ty dầu khí phân tích chỉ số lưu lượng khai thác của một giếng dầu qua $N$ ngày liên tiếp tạo thành dãy số $A_1, A_2, \dots, A_N$. Ban giám đốc muốn chọn một đợt vận hành thử nghiệm gồm một chuỗi các ngày liên tiếp sao cho số ngày vận hành không vượt quá $K$ ngày và tổng lưu lượng khai thác thu được là lớn nhất có thể.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên và số nguyên $K$. Hãy lập trình tìm tổng lớn nhất của một đoạn con liên tiếp có độ dài tối đa là $K$.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất tổng lớn nhất tìm được.

## Sample 1
### Input
```text
5 3
-1 2 4 -3 5
```
### Output
```text
6
```

### Giải thích
Với mảng $[-1, 2, 3, -2, 4]$ và độ dài tối đa $K = 2$:
Đoạn con liên tiếp có độ dài không quá 2 có tổng lớn nhất là đoạn $[2, 3]$ (độ dài 2) cho tổng là $2 + 3 = 5$ (hoặc đoạn [4] có tổng 4).

## Ràng buộc
- $100\%$ số test có $1 \le K \le N \le 10^5, -10^9 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
