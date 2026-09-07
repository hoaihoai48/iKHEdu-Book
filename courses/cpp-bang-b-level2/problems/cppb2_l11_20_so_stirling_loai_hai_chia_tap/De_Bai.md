# Số Stirling loại hai chia tập hợp

## Bối cảnh

Ban tổ chức hội trại quốc tế cần xếp N đại biểu đến từ nhiều quốc gia vào đúng K lều sinh hoạt chung, lều nào cũng phải có ít nhất một người và các lều không phân biệt tên với nhau để tránh tranh cãi vị trí đẹp. Trưởng ban hậu cần muốn biết có bao nhiêu cách xếp lều để chuẩn bị suất ăn và chăn màn vừa đủ. Vì đáp án rất lớn nên ban chỉ cần phần dư cho 1 000 000 007.

## Nhiệm vụ

Cho hai số nguyên $N, K$. Hãy lập trình tính số Stirling loại hai $S(N,K)$, tức số cách phân hoạch tập $N$ phần tử thành đúng $K$ tập con khác rỗng không phân biệt thứ tự, rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

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
25
```

### Giải thích

- Chia $5$ đại biểu thành đúng $3$ lều không tên, lều nào cũng có người.
- Dạng $3+1+1$ cho $10$ cách, dạng $2+2+1$ cho $15$ cách.
- Tổng $25$ nên chương trình in ra $25$.

## Ràng buộc

- $1 \le K \le N \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
