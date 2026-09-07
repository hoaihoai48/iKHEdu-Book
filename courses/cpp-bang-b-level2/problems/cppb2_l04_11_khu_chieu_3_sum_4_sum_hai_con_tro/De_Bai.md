# Khử chiều 3-sum & 4-sum hai con trỏ

## Bối cảnh

Trong buổi sinh hoạt câu lạc bộ toán, các bạn viết lên bảng một dãy số rồi đố nhau tìm các bộ ba (hoặc bộ bốn) có tổng đúng bằng một số cho trước.

Cả nhóm sắp xếp dãy số rồi dùng hai đầu danh sách kẹp dần vào giữa để tìm các bộ số thỏa mãn.

## Nhiệm vụ

Cho dãy số gồm $n$ phần tử phân biệt và giá trị mục tiêu $target$. Hãy lập trình đếm số bộ ba chỉ số $(i, j, k)$ với $i < j < k$ sao cho tổng ba phần tử đúng bằng $target$.

## Input

- Dòng đầu tiên chứa số nguyên $n$ và số nguyên $target$ ($3 \le n \le 2000$, $|target| \le 10^{18}$).
- Dòng thứ hai chứa $n$ số nguyên phân biệt $a_i$ ($|a_i| \le 10^9$).

## Output

- In ra một dòng duy nhất là số bộ ba có tổng đúng bằng $target$.

## Sample 1
### Input
```text
5 6
1 2 3 4 5
```
### Output
```text
1
```
### Giải thích

Sắp xếp dãy (vốn đã tăng dần): $1, 2, 3, 4, 5$. Cố định số đầu $1$: cần hai số còn lại tổng bằng $5$ — cặp $(2, 3)$ thỏa mãn. Cố định số đầu $2$: cần tổng $4$ từ các số phía sau ($3, 4, 5$) — cặp nhỏ nhất $3 + 4 = 7 > 4$ nên không có. Cố định $3$ trở đi tổng chỉ càng lớn hơn. Vậy chỉ có đúng $1$ bộ ba $(1, 2, 3)$.

## Ràng buộc

- $3 \le n \le 2000$, các phần tử phân biệt.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
