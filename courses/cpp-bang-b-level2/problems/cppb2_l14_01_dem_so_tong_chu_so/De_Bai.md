# Đếm Số Có Tổng Chữ Số Bằng K

## Bối cảnh

Cô giáo viết lên bảng tất cả các số nguyên từ $L$ đến $R$ để cả lớp quan sát quy luật của các chữ số. Bạn An nhận ra có những số mà khi cộng tất cả các chữ số lại thì được đúng giá trị $K$ cho trước, ví dụ số $23$ có tổng là $2 + 3 = 5$. An muốn nhờ máy tính đếm giúp có tất cả bao nhiêu số trong đoạn $[L, R]$ thỏa mãn điều kiện này.

## Nhiệm vụ

Cho ba số nguyên $L, R, K$. Hãy lập trình đếm có bao nhiêu số nguyên $x$ trong đoạn $[L, R]$ mà tổng các chữ số thập phân của $x$ đúng bằng $K$.

## Input

- Một dòng duy nhất chứa ba số nguyên $L, R, K$ ($1 \le L \le R \le 10^{18}$, $1 \le K \le 180$).

## Output

- In ra một số nguyên duy nhất là số lượng số trong đoạn $[L, R]$ có tổng các chữ số đúng bằng $K$.
- Nếu không có số nào thỏa mãn thì in ra `0`.

## Sample 1

### Input

```text
1 100 5
```

### Output

```text
6
```

### Giải thích

- Xét từng số từ $1$ đến $100$ và cộng các chữ số của nó lại.
- Số $5$ có tổng chữ số $5$ nên được đếm, số $14$ có tổng $1 + 4 = 5$ nên được đếm.
- Làm tương tự, các số được đếm là $5, 14, 23, 32, 41, 50$, tổng cộng $6$ số.
- Các số còn lại trong đoạn, ví dụ $6$ có tổng $6$ hay $15$ có tổng $1 + 5 = 6$, đều không được đếm.

## Ràng buộc

- $1 \le L \le R \le 10^{18}$, $1 \le K \le 180$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
