# Sinh Tất Cả Tổ Hợp Chập K Của N

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Để chuẩn bị cho kỳ thi Olympic Tin học quốc tế, ban huấn luyện gồm $N$ chuyên gia xuất sắc (được đánh số từ $1$ đến $N$). Trong mỗi vòng phỏng vấn chuyên sâu, hội đồng cần thành lập một tiểu ban gồm đúng $K$ chuyên gia để trực tiếp chấm vấn đáp học sinh. Để đảm bảo tính khách quan và xoay tua công việc, thư ký hội đồng cần lập danh sách tất cả các phương án thành lập tiểu ban $K$ người theo thứ tự từ điển chuẩn.

## Nhiệm vụ
Cho hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 16$). Hãy sử dụng thuật toán Quay lui có điều kiện chặn dưới tăng dần để sinh và in ra tất cả các tổ hợp chập $K$ của tập $\{1, 2, \dots, N\}$ theo thứ tự từ điển tăng dần.

## Input
- Một dòng duy nhất chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 16$).

## Output
- In ra tất cả các tổ hợp chập $K$, mỗi tổ hợp trên một dòng, các phần tử cách nhau bởi dấu cách.

## Sample 1
### Input
```text
4 2
```
### Output
```text
1 2
1 3
1 4
2 3
2 4
3 4
```
### Giải thích
Số lượng tổ hợp chập 2 của 4 chuyên gia là $C(4, 2) = \frac{4!}{2!2!} = 6$ tiểu ban. Các tiểu ban được liệt kê lần lượt theo thứ tự từ điển: `1 2`, `1 3`, `1 4`, `2 3`, `2 4`, `3 4`.

## Ràng buộc
- 100% số test có $1 \le K \le N \le 16$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
