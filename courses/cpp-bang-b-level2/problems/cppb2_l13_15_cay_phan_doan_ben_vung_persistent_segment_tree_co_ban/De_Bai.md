# Cây đoạn bền vững (persistent) cơ bản

## Bối cảnh

Ngân hàng lưu trữ lịch sử số dư của N tài khoản sau từng lần giao dịch để phục vụ tra soát và giải quyết khiếu nại của khách hàng. Mỗi phiên bản lịch sử tương ứng với tiền tố các giao dịch đã xử lý, và kiểm toán viên cần hỏi tổng số dư trên một đoạn tài khoản tại đúng phiên bản thứ V bất kỳ trong quá khứ. Cây đoạn bền vững chia sẻ nút giữa các phiên bản giúp mỗi truy vấn lịch sử chạy trong thời gian logarit.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(v,l,r)$, tổng các phần tử $a_l, \dots, a_r$ trong phiên bản tiền tố $v$ (tức dùng $a_1, \dots, a_v$), rồi in ra đáp án.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $v, l, r$ ($1 \le v \le N$, $1 \le l \le r \le v$).

## Output

- Gồm $Q$ dòng, mỗi dòng là tổng trên đoạn tại phiên bản tương ứng.

## Sample 1

### Input

```text
5 2
1 2 3 4 5
3 1 3
5 2 4
```

### Output

```text
6
9```

### Giải thích

- Phiên bản $3$ gồm $1\ 2\ 3$: tổng đoạn $[1,3]$ là $1+2+3 = 6$.
- Phiên bản $5$ gồm cả mảng: tổng đoạn $[2,4]$ là $2+3+4 = 9$.
- Hai truy vấn in ra $6$ rồi $9$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
