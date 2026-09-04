# Sinh Dãy Ngoặc Hợp Lệ Độ Dài 2N

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Trong trình biên dịch ngôn ngữ lập trình của hệ thống iKH-Compiler, việc phân tích cú pháp biểu thức số học đòi hỏi cấu trúc các cặp dấu ngoặc đóng mở phải hoàn toàn cân bằng và hợp lệ. Trước khi đưa vào kiểm thử bộ parser thực tế, kỹ sư phát triển cần sinh ra một tập dữ liệu chuẩn mực gồm toàn bộ các dãy ngoặc tròn đúng có độ dài $2N$ (tương ứng với $N$ cặp ngoặc).

## Nhiệm vụ
Cho số nguyên dương $N$. Hãy áp dụng thuật toán Quay lui có kỹ thuật cắt tỉa điều kiện hợp lệ (`open < N` và `close < open`) để sinh và in ra tất cả các dãy ngoặc đúng gồm $N$ cặp ngoặc tròn `()` theo thứ tự từ điển (`(` đứng trước `)`).

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10$).

## Output
- In ra tất cả các dãy ngoặc đúng độ dài $2N$, mỗi dãy trên một dòng theo đúng thứ tự từ điển.

## Sample 1
### Input
```text
3
```
### Output
```text
((()))
(()())
(())()
()(())
()()()
```
### Giải thích
Với $N = 3$ cặp ngoặc (độ dài 6 ký tự), số lượng dãy ngoặc hợp lệ chính là số Catalan $C_3 = \frac{1}{4} \binom{6}{3} = 5$. Các cấu hình hợp lệ được liệt kê theo thứ tự từ điển chuẩn mực.

## Ràng buộc
- 100% số test có $1 \le N \le 10$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
