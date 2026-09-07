# Tổng hiệu cực đại và cực tiểu mọi đoạn con

## Bối cảnh

Phòng phân tích chứng khoán muốn đo mức độ biến động của một mã cổ phiếu trong $N$ ngày liên tiếp. Với mỗi khoảng thời gian liên tục (từ một ngày đến toàn bộ $N$ ngày), phòng tính biên độ dao động bằng giá cao nhất trừ giá thấp nhất trong khoảng đó. Tổng biên độ của tất cả các khoảng thời gian cho thấy cổ phiếu này nhảy giá mạnh đến mức nào, giúp nhà đầu tư quyết định có nên rót tiền vào mã đầy rủi ro nhưng cũng đầy cơ hội này hay không.

## Nhiệm vụ

Cho $N$ số nguyên là giá cổ phiếu mỗi ngày. Với mỗi đoạn liên tục, tính hiệu của giá lớn nhất và giá nhỏ nhất trong đoạn. Hãy lập trình tính tổng các hiệu này trên mọi đoạn liên tục, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số ngày.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^6$), là giá mỗi ngày.

## Output

- In ra một số nguyên duy nhất là tổng hiệu trên mọi đoạn liên tục.

## Sample 1

### Input

```text
3
1 2 3
```

### Output

```text
4
```

### Giải thích

- Liệt kê cả $6$ đoạn liên tục cùng hiệu lớn nhất trừ nhỏ nhất của từng đoạn.
- Ba đoạn một ngày $[1], [2], [3]$ đều có hiệu $0$.
- Đoạn $[1, 2]$ có hiệu $2 - 1 = 1$; đoạn $[2, 3]$ có hiệu $3 - 2 = 1$.
- Đoạn $[1, 2, 3]$ có hiệu $3 - 1 = 2$.
- Tổng sáu hiệu là $0 + 0 + 0 + 1 + 1 + 2 = 4$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le a_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
