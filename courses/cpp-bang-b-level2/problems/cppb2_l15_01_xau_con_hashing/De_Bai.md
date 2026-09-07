# So Khớp Các Đoạn Mật Thư

## Bối cảnh

Đội mật mã nhận được một dải ký tự dài $S$ gồm các chữ cái viết thường, trong đó ẩn chứa nhiều đoạn tin nhắn lặp lại. Để kiểm tra hai đoạn tin có giống hệt nhau hay không, các bạn phải đối chiếu từng ký tự, việc này rất mất thời gian khi $S$ dài và số lần kiểm tra rất lớn. Vì vậy đội trưởng yêu cầu viết chương trình trả lời nhanh từng cặp đoạn có giống nhau hay không.

## Nhiệm vụ

Cho xâu $S$ và $Q$ truy vấn, mỗi truy vấn cho bốn chỉ số $a, b, c, d$. Hãy lập trình trả lời mỗi truy vấn xem xâu con $S[a..b]$ và xâu con $S[c..d]$ có giống nhau hoàn toàn hay không.

## Input

- Dòng đầu tiên chứa xâu $S$ gồm các chữ cái tiếng Anh viết thường ($1 \le |S| \le 10^5$).
- Dòng thứ hai chứa số nguyên $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo, mỗi dòng chứa bốn số nguyên $a, b, c, d$ ($1 \le a \le b \le |S|$, $1 \le c \le d \le |S|$), mô tả một truy vấn so sánh hai xâu con $S[a..b]$ và $S[c..d]$ theo chỉ số bắt đầu từ $1$.

## Output

- Với mỗi truy vấn, in ra trên một dòng `YES` nếu hai xâu con bằng nhau từng ký tự, ngược lại in ra `NO`.
- Thứ tự các dòng đáp án đúng bằng thứ tự các truy vấn trong input.

## Sample 1

### Input

```text
abacaba
2
1 3 5 7
1 3 2 4
```

### Output

```text
YES
NO
```

### Giải thích

- Xâu $S$ là `abacaba`, ký tự thứ $1$ đến thứ $3$ là `aba`, ký tự thứ $5$ đến thứ $7$ cũng là `aba`.
- Truy vấn thứ nhất so sánh `aba` với `aba`, từng ký tự đều trùng nhau nên trả lời `YES`.
- Truy vấn thứ hai so sánh `aba` với ký tự thứ $2$ đến thứ $4$ là `bac`, ký tự đầu tiên đã khác nhau (`a` và `b`) nên trả lời `NO`.

## Ràng buộc

- $1 \le |S| \le 10^5$, $1 \le Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
