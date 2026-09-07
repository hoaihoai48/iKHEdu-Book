# Chia để trị trên cây (centroid decomposition cơ bản)

## Bối cảnh
Hệ thống đường làng nối các thôn tạo thành một mạng cây, tức không hề có đường vòng. Huyện muốn trả lời nhanh nhiều câu hỏi của người dân về các tuyến đường trên mạng cây này.

Vì số thôn và số câu hỏi đều lớn, huyện cần một cách tổ chức dữ liệu thật khéo léo.

## Nhiệm vụ

Cho một cây gồm $n$ đỉnh (đánh số $1$–$n$). Một trọng tâm (centroid) của cây là đỉnh mà khi xóa nó đi, mọi thành phần liên thông còn lại đều có kích thước không vượt quá $n/2$. Hãy lập trình tìm một trọng tâm của cây.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 2 \cdot 10^5$) — số đỉnh.
- $n - 1$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u, v$ mô tả một cạnh của cây.

## Output

- In ra một dòng duy nhất là chỉ số của một trọng tâm của cây.

## Sample 1
### Input
```text
5
1 2
1 3
3 4
3 5
```
### Output
```text
3
```
### Giải thích

Thử xóa đỉnh $3$: các thành phần còn lại là $\{1, 2\}$ (kích thước $2$), $\{4\}$ ($1$), $\{5\}$ ($1$) — lớn nhất là $2 \le 5/2 = 2{,}5$ nên $3$ là trọng tâm. (Xóa đỉnh $1$ thì thành phần $\{3, 4, 5\}$ kích thước $3 > 2{,}5$ nên $1$ không phải.) Đáp án là $3$.

## Ràng buộc

- $1 \le n \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
