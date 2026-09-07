# Định lý Lucas cho tổ hợp modulo nguyên tố nhỏ (nhiều truy vấn)

## Bối cảnh

Trung tâm dữ liệu quốc gia lưu trữ các bảng hệ số nhị thức phục vụ hệ thống chữ ký số, trong đó mô-đun p là một số nguyên tố nhỏ được thay đổi theo từng phiên làm việc để tăng tính bảo mật. Mỗi ngày hệ thống nhận hàng nghìn yêu cầu tính C(n, k) mod p với n, k cực lớn nên kỹ sư vận hành triển khai định lý Lucas để tách mỗi yêu cầu thành tích các hệ số nhỏ. Chương trình cần trả lời đúng từng dòng yêu cầu trong nhật ký xử lý.

## Nhiệm vụ

Cho $T$ truy vấn, mỗi truy vấn gồm $N, K, p$ ($p$ nguyên tố). Hãy lập trình tính, với mỗi truy vấn, $C(N,K) \bmod p$ bằng định lý Lucas, rồi in ra đáp án (bằng $0$ khi $K > N$ hoặc $K < 0$).

## Input

- Dòng 1: số nguyên $T$ ($1 \le T \le 10^4$).
- $T$ dòng tiếp theo, mỗi dòng gồm $N, K, p$ ($0 \le K \le N \le 10^{18}$, $p$ nguyên tố, $2 \le p \le 100$).

## Output

- Gồm $T$ dòng, mỗi dòng là $C(N,K) \bmod p$ của truy vấn tương ứng.

## Sample 1

### Input

```text
2
5 2 3
10 3 7
```

### Output

```text
1
1```

### Giải thích

- Truy vấn một: $C(5,2) = 10$, chia $3$ dư $1$.
- Truy vấn hai: $C(10,3) = 120$, mà $119$ chia hết cho $7$ nên $120$ chia $7$ dư $1$.
- Chương trình in ra $1$ rồi $1$ trên hai dòng.

## Ràng buộc

- $1 \le T \le 10^4$; $0 \le K \le N \le 10^{18}$; $p$ nguyên tố $\le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
