# Hàm phi Euler $\phi(n)$ nhanh với SPF

## Bối cảnh
Trong giờ sinh hoạt của câu lạc bộ Toán, cô giáo viết lên bảng một số nguyên $n$ và đố cả lớp: có bao nhiêu số từ $1$ đến $n$ không có ước chung nào với $n$ ngoài $1$? Đó chính là số lượng phân số tối giản có mẫu số bằng $n$. Vì cả lớp thay nhau đọc số liên tục, cần một cách trả lời thật nhanh cho mỗi số được gọi tên.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $n$. Hãy lập trình tính $\phi(n)$ — số lượng số nguyên $k$ ($1 \le k \le n$) nguyên tố cùng nhau với $n$.

## Input

- Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$) — số lượng truy vấn.
- $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $n$ ($1 \le n \le 10^6$).

## Output

- Với mỗi truy vấn, in ra một dòng là giá trị $\phi(n)$ — số lượng số nguyên $k$ ($1 \le k \le n$) nguyên tố cùng nhau với $n$.

## Sample 1
### Input
```text
3
6 9 10
```
### Output
```text
2
6
4
```
### Giải thích

* Với $n = 6$: các số từ $1$ đến $6$ nguyên tố cùng nhau với $6$ là $1, 5$ → đáp án $2$.
* Với $n = 9$: các số nguyên tố cùng nhau với $9$ là $1, 2, 4, 5, 7, 8$ → đáp án $6$.
* Với $n = 10$: các số nguyên tố cùng nhau với $10$ là $1, 3, 7, 9$ → đáp án $4$.

## Ràng buộc

- $1 \le Q \le 10^5$, $1 \le n \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
