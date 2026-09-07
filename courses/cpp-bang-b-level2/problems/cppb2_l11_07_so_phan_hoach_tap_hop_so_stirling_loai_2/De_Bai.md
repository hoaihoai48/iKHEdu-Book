# Số Stirling loại 2 (chia tập hợp)

## Bối cảnh

Trường năng khiếu tổ chức trại hè với N học sinh ưu tú cần chia thành đúng K nhóm sinh hoạt, mỗi nhóm có ít nhất một bạn và không phân biệt tên gọi giữa các nhóm với nhau. Thầy tổng phụ trách muốn biết có bao nhiêu cách chia nhóm để chuẩn bị đủ số lượng phòng họp và huy hiệu tổ trưởng. Vì con số này tăng rất nhanh nên thầy chỉ cần phần dư khi chia cho 1 000 000 007 để ghi vào kế hoạch hậu cần.

## Nhiệm vụ

Cho hai số nguyên $N, K$. Hãy lập trình tính số Stirling loại hai $S(N,K)$ là số cách phân hoạch tập $N$ phần tử thành đúng $K$ tập con khác rỗng không phân biệt thứ tự, rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng duy nhất: hai số nguyên $N, K$ ($1 \le K \le N \le 1000$).

## Output

- In ra một dòng duy nhất là $S(N,K) \bmod 1\,000\,000\,007$.

## Sample 1

### Input

```text
5 3
```

### Output

```text
25```

### Giải thích

- Chia $5$ bạn thành đúng $3$ nhóm không tên, mỗi nhóm ít nhất một bạn.
- Dạng phân hoạch theo cỡ nhóm chỉ có thể là $3+1+1$ (chọn $3$ bạn cho nhóm đông: $10$ cách) hoặc $2+2+1$ (chọn bạn đơn lẻ rồi chia $4$ bạn còn lại thành hai cặp: $5 \times 3 = 15$ cách).
- Tổng $10 + 15 = 25$ nên chương trình in ra $25$.

## Ràng buộc

- $1 \le K \le N \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
