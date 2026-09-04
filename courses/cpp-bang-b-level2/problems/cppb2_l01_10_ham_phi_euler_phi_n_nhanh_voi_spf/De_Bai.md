# Hàm phi Euler $\phi(n)$ nhanh với SPF

## Bối cảnh
Trong giờ sinh hoạt của câu lạc bộ Toán, cô giáo viết lên bảng một số nguyên $n$ và đố cả lớp: có bao nhiêu số từ $1$ đến $n$ không có ước chung nào với $n$ ngoài $1$? Đó chính là số lượng phân số tối giản có mẫu số bằng $n$. Vì cả lớp thay nhau đọc số liên tục, cần một cách trả lời thật nhanh cho mỗi số được gọi tên.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $n$. Hãy lập trình tính $\phi(n)$ — số lượng số nguyên $k$ ($1 \le k \le n$) nguyên tố cùng nhau với $n$.

## Input
- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

## Output
- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hàm Phi Euler $\phi(N)$ Nhanh Với SPF.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
