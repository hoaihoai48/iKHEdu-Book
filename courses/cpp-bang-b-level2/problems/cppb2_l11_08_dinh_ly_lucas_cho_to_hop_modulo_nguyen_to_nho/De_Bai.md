# Định lý Lucas cho tổ hợp modulo nguyên tố nhỏ

## Bối cảnh

Phòng thí nghiệm mật mã của trường đại học cần kiểm tra nhanh các hệ số nhị thức khổng lồ trong giao thức chia sẻ khóa học mới. Vì mô-đun dùng trong giao thức là một số nguyên tố nhỏ p nên nhóm nghiên cứu áp dụng định lý Lucas để rút gọn bài toán lớn thành tích các hệ số nhỏ theo từng chữ số cơ số p. Cán bộ kỹ thuật cần một chương trình tính C(n, k) mod p cho các tham số n, k tới hàng tỉ để nạp vào thiết bị phần cứng.

## Nhiệm vụ

Cho ba số nguyên $N, K$ và số nguyên tố $p$. Hãy lập trình tính hệ số tổ hợp $C(N,K)$ rồi in ra phần dư khi chia cho $p$ (dùng định lý Lucas, quy ước $C(N,K) = 0$ khi $K > N$ hoặc $K < 0$).

## Input

- Dòng duy nhất: ba số nguyên $N, K, p$ ($0 \le K \le N \le 10^{18}$, $2 \le p \le 100$, $p$ nguyên tố).

## Output

- In ra một dòng duy nhất là $C(N,K) \bmod p$.

## Sample 1

### Input

```text
5 2 3
```

### Output

```text
1```

### Giải thích

- Cần $C(5,2) = 10$ rồi lấy dư cho $3$.
- Viết theo cơ số $3$: $5 = (12)_3$, $2 = (02)_3$; áp dụng Lucas được $C(1,0) \times C(2,2) = 1 \times 1 = 1$.
- Kiểm tra trực tiếp $10 \div 3$ dư $1$ nên chương trình in ra $1$.

## Ràng buộc

- $0 \le K \le N \le 10^{18}$, $p$ nguyên tố $\le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
