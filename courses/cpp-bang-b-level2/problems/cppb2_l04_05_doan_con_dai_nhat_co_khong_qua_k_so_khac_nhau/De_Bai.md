# Đoạn con dài nhất có không quá k số khác nhau

## Bối cảnh

Cô giáo ghi lại màu áo học sinh xếp hàng vào lớp mỗi sáng. Cô muốn tìm đoạn hàng dài nhất mà trong đó số màu áo khác nhau không vượt quá $K$ để chụp ảnh kỷ niệm đồng đều.

Cô đi dọc hàng, nới rộng rồi thu hẹp đoạn quan sát sao cho số màu áo luôn trong giới hạn.

## Nhiệm vụ

Cho dãy số và số $K$. Hãy lập trình tìm độ dài đoạn con liên tiếp dài nhất chứa không quá $K$ giá trị khác nhau.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, k$ ($1 \le n \le 2 \cdot 10^5$, $1 \le k \le n$) — độ dài dãy và giới hạn số giá trị phân biệt.
- Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^9$).

## Output

- In ra một dòng duy nhất là độ dài của đoạn con liên tiếp dài nhất chứa không quá $k$ giá trị phân biệt.

## Sample 1
### Input
```text
7 2
1 2 1 3 4 2 3
```
### Output
```text
3
```
### Giải thích

Đoạn $[1, 2, 1]$ ở đầu dãy chỉ chứa $2$ giá trị phân biệt nên dài $3$ thỏa mãn. Mọi đoạn dài $4$ đều chứa ít nhất $3$ giá trị phân biệt: $[1, 2, 1, 3]$, $[2, 1, 3, 4]$, $[1, 3, 4, 2]$, $[3, 4, 2, 3]$ — kiểm tra tay từng đoạn đều thấy $3$ giá trị khác nhau trở lên. Vậy đáp án là $3$.

## Ràng buộc

- $1 \le n \le 2 \cdot 10^5$, $1 \le k \le n$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
