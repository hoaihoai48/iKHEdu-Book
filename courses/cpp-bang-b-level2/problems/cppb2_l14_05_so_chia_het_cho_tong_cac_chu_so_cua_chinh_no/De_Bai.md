# Số Harshad (chia hết cho tổng chữ số)

## Bối cảnh

Câu lạc bộ toán học của trường phát động trò chơi số Harshad trong đó một số được gọi là đẹp khi nó chia hết cho tổng các chữ số của chính nó để rèn luyện kỹ năng tính nhẩm cho học sinh. Mỗi vòng thi đưa ra một đoạn số liên tiếp và yêu cầu đếm có bao nhiêu số đẹp trong đoạn đó nhằm tính điểm cho các đội chơi. Vì đoạn số có thể rất dài nên ban tổ chức cần chương trình đếm nhanh bằng quy hoạch động chữ số.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình đếm các số $x$ ($L \le x \le R$, $x > 0$) chia hết cho tổng các chữ số của $x$, rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($1 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là số lượng số Harshad trong đoạn.

## Sample 1

### Input

```text
1 20
```

### Output

```text
13```

### Giải thích

- Kiểm tra từng số từ $1$ đến $20$: các số một chữ số $1$ đến $9$ đều chia hết cho chính nó nên cả chín số đều đẹp.
- Trong các số hai chữ số chỉ có $10$ (tổng $1$), $12$ (tổng $3$), $18$ (tổng $9$) và $20$ (tổng $2$) thỏa mãn.
- Tổng $9 + 4 = 13$ nên chương trình in ra $13$.

## Ràng buộc

- $1 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
