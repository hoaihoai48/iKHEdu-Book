# Đảo ngược mảng bằng kỹ thuật swap hai đầu

## Bối cảnh
Trong tối ưu thuật toán, thay vì tạo ra một mảng mới tốn thêm bộ nhớ để chứa kết quả đảo ngược, các lập trình viên thường dùng kỹ thuật Hai con trỏ đối xứng từ hai đầu mảng và hoán đổi trực tiếp các cặp phần tử (`in-place reversal`). Bạn hãy viết một hàm thực hiện công việc này.

## Nhiệm vụ
Cho một dãy gồm $N$ số nguyên. Hãy viết hàm `void reverseArray(vector<int>& a)` sử dụng kỹ thuật hoán đổi (`swap`) để đảo ngược dãy số ngay trên mảng ban đầu, sau đó in ra dãy số sau khi đã đảo ngược.

## Input
- Dòng thứ nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $a_1, a_2, \dots, a_N$ ($-10^9 \le a_i \le 10^9$), cách nhau bởi một khoảng trắng.

## Output
- In ra một dòng duy nhất gồm $N$ số nguyên của mảng sau khi đã đảo ngược, cách nhau bởi một khoảng trắng.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
5 4 3 2 1
```

### Giải thích
- Bước 1: Hoán đổi $a[0]$ và $a[4]$ $\implies [5, 2, 3, 4, 1]$.
- Bước 2: Hoán đổi $a[1]$ và $a[3]$ $\implies [5, 4, 3, 2, 1]$.
- Bước 3: Hai con trỏ gặp nhau tại phần tử giữa $a[2]$, kết thúc. Kết quả: `5 4 3 2 1`.

## Sample 2
### Input
```text
4
10 20 30 40
```
### Output
```text
40 30 20 10
```

### Giải thích
Hoán đổi $(10, 40)$ và $(20, 30)$ thu được `40 30 20 10`.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, -10^9 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
