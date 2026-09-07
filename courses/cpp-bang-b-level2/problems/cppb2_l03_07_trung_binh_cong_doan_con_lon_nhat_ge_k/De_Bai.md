# Trung bình cộng đoạn con lớn nhất $\ge k$

## Bối cảnh

Cuối học kỳ, cô giáo muốn tìm một dãy ngày liên tiếp mà điểm trung bình của lớp đạt từ mức $K$ trở lên và là cao nhất có thể, để tuyên dương nỗ lực của cả lớp.

Cô ghi lại điểm số từng ngày rồi tìm xem giai đoạn nào lớp học tiến bộ nhất.

## Nhiệm vụ

Cho dãy số và ngưỡng $K$. Hãy lập trình tìm giá trị trung bình đoạn con lớn nhất thỏa mãn không nhỏ hơn $K$.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, k$ ($1 \le k \le n \le 10^5$) — độ dài dãy và độ dài tối thiểu của đoạn con.
- Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^9$).

## Output

- In ra một dòng duy nhất là giá trị trung bình cộng lớn nhất trong tất cả các đoạn con liên tiếp có độ dài ít nhất $k$, làm tròn tới $4$ chữ số thập phân.

## Sample 1
### Input
```text
5 2
1 2 3 4 5
```
### Output
```text
4.5000
```
### Giải thích

Đoạn $[4, 5]$ dài $2$ thỏa điều kiện, trung bình $(4 + 5)/2 = 4{,}5$. Các đoạn dài từ $2$ trở lên khác: $[3, 4, 5]$ trung bình $4$, $[2, 3, 4, 5]$ trung bình $3{,}5$, cả dãy trung bình $3$ — đều không vượt $4{,}5$. Đoạn $[5]$ tuy trung bình $5$ nhưng dài $1 < 2$ nên bị loại. Vậy đáp án là $4{,}5$.

## Ràng buộc

- $1 \le k \le n \le 10^5$, $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
