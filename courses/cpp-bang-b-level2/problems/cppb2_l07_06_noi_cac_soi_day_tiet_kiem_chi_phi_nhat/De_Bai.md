# Nối các sợi dây tiết kiệm chi phí nhất

## Bối cảnh

Xưởng cơ khí của hợp tác xã có nhiều đoạn dây cáp ngắn còn thừa sau các công trình, mỗi đoạn dài một số mét nhất định. Chú thợ cả muốn nối tất cả các đoạn rời này thành một sợi cáp dài duy nhất để dùng cho công trình mới. Mỗi lần nối hai sợi dây tốn chi phí đúng bằng tổng độ dài của hai sợi đem nối, và sợi dây tạo thành có thể đem nối tiếp với các sợi khác. Chú muốn chọn thứ tự nối sao cho tổng chi phí là thấp nhất.

## Nhiệm vụ

Cho $N$ số nguyên là độ dài của từng đoạn dây ban đầu. Mỗi lần được nối hai sợi thành một với chi phí bằng tổng độ dài của chúng. Hãy lập trình tính tổng chi phí nhỏ nhất để nối tất cả thành một sợi duy nhất, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số đoạn dây.
- Dòng thứ hai chứa $N$ số nguyên $x_i$ ($1 \le x_i \le 10^6$), là độ dài từng đoạn.

## Output

- In ra một số nguyên duy nhất là tổng chi phí nối nhỏ nhất.

## Sample 1

### Input

```text
4
1 2 3 4
```

### Output

```text
19
```

### Giải thích

- Nối hai sợi ngắn nhất $1$ và $2$ tốn $1 + 2 = 3$, còn lại các sợi $3, 3, 4$.
- Nối hai sợi $3$ và $3$ tốn $3 + 3 = 6$, còn lại các sợi $4, 6$.
- Nối hai sợi cuối $4$ và $6$ tốn $4 + 6 = 10$, chỉ còn một sợi duy nhất.
- Tổng chi phí là $3 + 6 + 10 = 19$, và mọi thứ tự nối khác đều tốn từ $19$ trở lên.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le x_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
