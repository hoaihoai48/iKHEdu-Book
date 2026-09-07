# Định lý Lucas tính tổ hợp modulo p (nhiều truy vấn)

## Bối cảnh

Đội tuyển tin học của tỉnh đang luyện tập chuyên đề số học cho kỳ thi quốc gia với nội dung tính hệ số tổ hợp khổng lồ theo mô-đun nguyên tố nhỏ. Huấn luyện viên yêu cầu mỗi học viên xử lý trôi chảy hàng nghìn truy vấn dạng C(n, k) mod p bằng cách tách n, k theo cơ số p đúng như định lý Lucas đã dạy trên lớp. Bài nộp của học viên phải in đáp án từng truy vấn theo đúng thứ tự đề bài phát ra.

## Nhiệm vụ

Cho $T$ truy vấn, mỗi truy vấn gồm $N, K, p$ ($p$ nguyên tố). Hãy lập trình tính, với mỗi truy vấn, $C(N,K) \bmod p$ bằng định lý Lucas, rồi in ra đáp án (bằng $0$ khi $K > N$ hoặc $K < 0$).

## Input

- Dòng 1: số nguyên $T$ ($1 \le T \le 10^4$).
- $T$ dòng tiếp theo, mỗi dòng gồm $N, K, p$ ($0 \le K \le N \le 10^{18}$, $p$ nguyên tố, $2 \le p \le 10^9$).

## Output

- Gồm $T$ dòng, mỗi dòng là $C(N,K) \bmod p$ của truy vấn tương ứng.

## Sample 1

### Input

```text
2
5 2 3
10 1 7
```

### Output

```text
1
3
```

### Giải thích

- Truy vấn một: $C(5,2) = 10$, chia $3$ dư $1$.
- Truy vấn hai: $C(10,1) = 10$, chia $7$ dư $3$.
- Chương trình in ra $1$ rồi $3$ trên hai dòng.

## Ràng buộc

- $1 \le T \le 10^4$; $0 \le K \le N \le 10^{18}$; $p$ nguyên tố.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
