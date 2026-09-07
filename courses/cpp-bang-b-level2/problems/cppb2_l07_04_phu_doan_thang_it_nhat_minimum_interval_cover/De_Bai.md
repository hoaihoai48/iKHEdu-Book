# Phủ đoạn thẳng ít nhất (minimum interval cover)

## Bối cảnh

Đội thi công được giao nhiệm vụ lắp đèn đường dọc theo con đường dài $L$ kilômét tính từ đầu làng. Công ty đã mua sẵn nhiều loại cột đèn, mỗi cột khi dựng tại một vị trí sẽ chiếu sáng một đoạn đường $[l_i, r_i]$ nhất định. Để tiết kiệm chi phí nhân công, đội trưởng muốn chọn ra ít cột đèn nhất sao cho mọi điểm trên con đường từ $0$ đến $L$ đều được chiếu sáng, bởi mỗi cột dựng thêm đều tốn một ngày công của cả đội.

## Nhiệm vụ

Cho độ dài $L$ của con đường và $N$ đoạn chiếu sáng $[l_i, r_i]$. Hãy lập trình chọn ra ít đoạn nhất sao cho hợp của chúng phủ kín toàn bộ đoạn $[0, L]$, rồi in ra số đoạn đó. Nếu không thể phủ kín thì in ra $-1$.

## Input

- Dòng đầu tiên chứa số nguyên $N$ và số nguyên $L$ ($1 \le N \le 10^5$, $1 \le L \le 10^9$), là số cột đèn và độ dài con đường.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $l_i, r_i$ ($0 \le l_i < r_i \le 10^9$), là đoạn đường mà một cột chiếu sáng.

## Output

- In ra số đoạn ít nhất để phủ kín $[0, L]$, hoặc $-1$ nếu không thể.

## Sample 1

### Input

```text
3 10
0 4
3 8
7 10
```

### Output

```text
3
```

### Giải thích

- Bắt đầu từ điểm $0$: chỉ có đoạn $[0, 4]$ vươn tới được nên buộc phải chọn nó, vùng sáng tới điểm $4$.
- Từ điểm $4$: đoạn $[3, 8]$ bắt đầu trước điểm $4$ và vươn xa nhất tới $8$ nên chọn nó, vùng sáng tới điểm $8$.
- Từ điểm $8$: đoạn $[7, 10]$ bắt đầu trước điểm $8$ và vươn tới $10$ nên chọn nó, cả con đường được phủ kín.
- Tổng cộng cần $3$ đoạn và không thể ít hơn vì mỗi bước đều chỉ có một lựa chọn vươn xa nhất.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le L \le 10^9$, $0 \le l_i < r_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
