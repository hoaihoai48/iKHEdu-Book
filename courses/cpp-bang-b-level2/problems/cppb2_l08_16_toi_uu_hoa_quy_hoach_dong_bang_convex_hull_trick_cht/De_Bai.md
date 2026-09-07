# Tối ưu hóa quy hoạch động bằng convex hull trick (CHT)

## Bối cảnh

Chú ếch muốn sang bờ bên kia của con suối bằng cách nhảy qua $N$ cột đá xếp thành hàng theo đúng thứ tự, mỗi cột có một độ cao khác nhau. Từ một cột, chú có thể nhảy tới bất kỳ cột nào phía trước, và năng lượng tốn cho một cú nhảy bằng bình phương chênh lệch độ cao giữa cột đáp và cột xuất phát. Chú muốn chọn hành trình từ cột đầu tiên tới cột cuối cùng sao cho tổng năng lượng tiêu hao là ít nhất.

## Nhiệm vụ

Cho $N$ số nguyên là độ cao $h_i$ của từng cột đá theo thứ tự. Mỗi cú nhảy từ cột $j$ tới cột $i$ ($j < i$) tốn $(h_i - h_j)^2$ năng lượng. Hãy lập trình tính tổng năng lượng ít nhất để đi từ cột đầu tiên tới cột cuối cùng, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 5000$), là số cột đá.
- Dòng thứ hai chứa $N$ số nguyên $h_i$ ($0 \le h_i \le 10^6$), là độ cao từng cột.

## Output

- In ra một số nguyên duy nhất là tổng năng lượng ít nhất.

## Sample 1

### Input

```text
4
0 1 2 3
```

### Output

```text
3
```

### Giải thích

- Bốn cột có độ cao $0, 1, 2, 3$ theo thứ tự.
- Nhảy từng bước một: $(1 - 0)^2 + (2 - 1)^2 + (3 - 2)^2 = 1 + 1 + 1 = 3$.
- Mọi hành trình nhảy xa hơn đều tốn nhiều hơn, ví dụ nhảy $0 \to 2 \to 3$ tốn $(2 - 0)^2 + (3 - 2)^2 = 4 + 1 = 5$.

## Ràng buộc

- $1 \le N \le 5000$, $0 \le h_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
