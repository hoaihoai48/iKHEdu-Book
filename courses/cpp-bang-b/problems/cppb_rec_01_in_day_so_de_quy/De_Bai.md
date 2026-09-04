# In Dãy Số Đệ Quy 1..N và N..1

## Bối cảnh
Để làm quen với cơ chế hoạt động của ngăn xếp cuộc gọi hàm (Call Stack), một huấn luyện viên lập trình yêu cầu học viên viết hàm đệ quy in ra dãy số từ 1 đến N (theo chiều xuôi) và từ N về 1 (theo chiều ngược) mà tuyệt đối không được sử dụng bất kỳ vòng lặp for hay while nào.

## Nhiệm vụ
Cho số nguyên dương N. Hãy in ra 2 dòng: dòng 1 in các số từ 1 đến N, dòng 2 in các số từ N về 1 bằng hàm đệ quy.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 1000$).

## Output
- Dòng 1: In các số từ $1$ đến $N$ cách nhau bởi khoảng trắng.
- Dòng 2: In các số từ $N$ về $1$ cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
5
```
### Output
```text
1 2 3 4 5
5 4 3 2 1
```
### Giải thích
- Dòng 1 in xuôi từ 1 đến 5: 1 2 3 4 5.
- Dòng 2 in ngược từ 5 về 1: 5 4 3 2 1.

## Ràng buộc
- $100\%$ số test có $N \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
