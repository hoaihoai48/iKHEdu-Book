# Chỉnh hợp P(n, k) theo modulo

## Bối cảnh

Câu lạc bộ Robotics của trường vừa nhập về một lô linh kiện gồm đúng N mô-đun cảm biến khác nhau để lắp ráp robot dự thi hội thao thành phố. Mỗi đội thi phải đăng ký một ban điều hành gồm K vị trí có phân biệt vai trò rõ ràng như đội trưởng, thủ quỹ và kỹ thuật viên. Ban giám khảo cần biết có tất cả bao nhiêu cách xếp K bạn khác nhau vào K vai trò này, lấy phần dư khi chia cho 1 000 000 007 để in lên bảng tin.

## Nhiệm vụ

Cho hai số nguyên $N$ và $K$. Hãy lập trình tính số chỉnh hợp chập $K$ của $N$ phần tử, tức $P(N,K) = N \times (N-1) \times \dots \times (N-K+1)$, rồi in ra phần dư của kết quả khi chia cho $1\,000\,000\,007$.

## Input

- Dòng duy nhất: hai số nguyên $N, K$ ($0 \le K, N \le 10^6$).

## Output

- In ra một dòng duy nhất là $P(N,K) \bmod 1\,000\,000\,007$. Quy ước $P(N,K) = 0$ khi $K > N$ hoặc $K < 0$, và $P(N,0) = 1$.

## Sample 1

### Input

```text
5 2
```

### Output

```text
20
```

### Giải thích

- Với $N = 5, K = 2$: các số nhân vào tích là $5$ rồi $4$.
- Tích $5 \times 4 = 20$, phần dư khi chia cho $1\,000\,000\,007$ vẫn là $20$.
- Chương trình in ra $20$.

## Ràng buộc

- $0 \le N \le 10^6$, $0 \le K \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
