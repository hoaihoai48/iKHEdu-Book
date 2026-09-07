# Cây Trie đếm tiền tố

## Bối cảnh

Nhà mạng di động lưu kho N số thuê bao dạng chuỗi ký tự để tra cứu nhanh đầu số khi khách hàng gọi đến tổng đài chăm sóc. Mỗi yêu cầu tra cứu đưa ra một tiền tố và cần biết có bao nhiêu thuê bao trong kho bắt đầu bằng đúng tiền tố đó nhằm thống kê mật độ thuê bao theo từng đầu số. Cây Trie lưu số lượng chuỗi đi qua mỗi nút giúp trả lời từng truy vấn trong thời gian tuyến tính theo độ dài tiền tố.

## Nhiệm vụ

Cho $N$ xâu (chữ cái thường) và $Q$ truy vấn. Hãy lập trình xây dựng cây Trie rồi trả lời, với mỗi truy vấn $p$, có bao nhiêu xâu trong kho nhận $p$ làm tiền tố, rồi in ra đáp án.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$, tổng độ dài tới $2 \cdot 10^5$).
- $N$ dòng tiếp theo, mỗi dòng là một xâu chữ cái thường.
- $Q$ dòng tiếp theo, mỗi dòng là một tiền tố $p$ cần hỏi.

## Output

- Gồm $Q$ dòng, mỗi dòng là đáp án của truy vấn tương ứng.

## Sample 1

### Input

```text
3 2
apple
app
apricot
app
apr
```

### Output

```text
2
1
```

### Giải thích

- Kho có ba xâu $apple, app, apricot$: hai xâu đầu bắt đầu bằng $app$ nên đáp án truy vấn một là $2$.
- Chỉ có $apricot$ bắt đầu bằng $apr$ nên đáp án truy vấn hai là $1$.
- Chương trình in ra $2$ rồi $1$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; tổng độ dài tới $2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
