# Tổ hợp theo modulo

## Bối cảnh

Ban tổ chức trại hè cần chia nhóm hoạt động từ danh sách học sinh đã đăng ký, mỗi nhóm gồm đúng một số bạn nhất định. Với mỗi phương án chia nhóm, số lượng cách chọn có thể lên tới hàng trăm triệu nên ban tổ chức chỉ cần biết phần dư của con số đó khi chia cho $1\,000\,000\,007$. Vì có rất nhiều lượt hỏi với các quy mô nhóm khác nhau gửi về trong ngày, ban tổ chức cần một chương trình trả lời nhanh từng lượt hỏi theo đúng phần dư yêu cầu.

## Nhiệm vụ

Cho $Q$ truy vấn, mỗi truy vấn gồm hai số nguyên $N, K$. Hãy lập trình tính, với mỗi truy vấn, số cách chọn ra $K$ bạn khác nhau từ $N$ bạn (không phân biệt thứ tự), rồi in ra phần dư của kết quả khi chia cho $1\,000\,000\,007$.

## Input

- Dòng 1: số nguyên $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo, mỗi dòng gồm hai số nguyên $N, K$ ($0 \le K \le N \le 10^6$).

## Output

- Gồm $Q$ dòng, dòng thứ $i$ là đáp án của truy vấn thứ $i$: phần dư của số cách chọn $K$ bạn từ $N$ bạn khi chia cho $1\,000\,000\,007$.

## Sample 1

### Input

```text
2
5 2
10 3
```

### Output

```text
10
120
```

### Giải thích

- Truy vấn 1: chọn $2$ bạn từ $5$ bạn. Đánh số các bạn từ $1$ đến $5$ rồi liệt kê từng cặp theo thứ tự: $(1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)$. Đếm được tất cả $10$ cặp, mà $10$ chia cho $1\,000\,000\,007$ dư $10$ nên đáp án là $10$.
- Truy vấn 2: chọn $3$ bạn từ $10$ bạn. Liệt kê có hệ thống tất cả các bộ $3$ bạn khác nhau (mỗi bộ chỉ tính một lần, không phân biệt thứ tự) sẽ đếm được đúng $120$ bộ. Vì $120$ nhỏ hơn $1\,000\,000\,007$ nên phần dư vẫn là $120$.

## Ràng buộc

- $1 \le Q \le 10^5$; $0 \le K \le N \le 10^6$ trong mỗi truy vấn.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
