# Số Stirling loại 2 với nhiều truy vấn

## Bối cảnh

Sở giáo dục thí điểm mô hình lớp học mở với N học sinh được chia thành đúng K nhóm thảo luận không phân biệt tên nhóm, nhóm nào cũng phải có ít nhất một thành viên để buổi học diễn ra sôi nổi. Vì có tới hàng chục nghìn lượt hỏi đáp với các quy mô lớp khác nhau gửi về cổng thông tin, máy chủ cần trả lời nhanh từng lượt hỏi và chỉ đưa phần dư cho 1 000 000 007 để tiết kiệm băng thông đường truyền.

## Nhiệm vụ

Cho $Q$ truy vấn, mỗi truy vấn gồm $N, K$. Hãy lập trình tính, với mỗi truy vấn, số Stirling loại hai $S(N,K)$ rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng 1: số nguyên $Q$ ($1 \le Q \le 10^4$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $N, K$ ($1 \le K \le N \le 1000$).

## Output

- Gồm $Q$ dòng, mỗi dòng là đáp án của truy vấn tương ứng theo modulo $1\,000\,000\,007$.

## Sample 1

### Input

```text
2
5 3
4 2
```

### Output

```text
25
7```

### Giải thích

- Truy vấn một $N = 5, K = 3$: phân hoạch $5$ bạn thành $3$ nhóm không tên được $25$ cách.
- Truy vấn hai $N = 4, K = 2$: dạng cỡ nhóm $3+1$ có $4$ cách, dạng $2+2$ có $3$ cách, tổng $7$ cách.
- Chương trình in ra $25$ rồi $7$ trên hai dòng.

## Ràng buộc

- $1 \le Q \le 10^4$; $1 \le K \le N \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
