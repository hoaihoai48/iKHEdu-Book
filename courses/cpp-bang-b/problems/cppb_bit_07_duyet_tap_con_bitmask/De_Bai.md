# Duyệt Toàn Bộ 2^N Tập Con Bằng Mặt Nạ Bit

## Bối cảnh
Một người đầu tư mạo hiểm cần phân tích toàn bộ 2^N kịch bản danh mục đầu tư từ N dự án khởi nghiệp tiềm năng. Mỗi kịch bản tương ứng với việc chọn hoặc không chọn từng dự án. Hãy sử dụng kỹ thuật mặt nạ bit (Bitmask) để liệt kê tổng giá trị vốn của tất cả 2^N tập con có thể lập ra.

## Nhiệm vụ
Cho tập hợp gồm N số nguyên. Hãy in ra tổng các phần tử của tất cả 2^N tập con theo thứ tự mặt nạ bit tăng dần từ 0 đến 2^N - 1.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 16$).
- Dòng 2: $N$ số nguyên $A_0, A_1, \dots, A_{N-1}$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra $2^N$ dòng, mỗi dòng là tổng các phần tử của tập con tương ứng với mặt nạ bit từ $0$ đến $2^N - 1$.

## Sample 1
### Input
```text
2
3 5
```
### Output
```text
0
3
5
8
```
### Giải thích
- Mask 0 (00_2): tập rỗng -> tổng 0.
- Mask 1 (01_2): tập {A[0]} = {3} -> tổng 3.
- Mask 2 (10_2): tập {A[1]} = {5} -> tổng 5.
- Mask 3 (11_2): tập {A[0], A[1]} = {3, 5} -> tổng 8.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 16$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
