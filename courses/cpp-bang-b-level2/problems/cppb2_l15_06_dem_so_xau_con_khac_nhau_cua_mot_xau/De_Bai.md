# Đếm số xâu con khác nhau

## Bối cảnh

Viện ngôn ngữ học phân tích một văn bản cổ để thống kê vốn từ vựng của tác giả vô danh qua số lượng các đoạn trích phân biệt xuất hiện trong toàn bộ cuộn giấy. Mỗi đoạn trích là một xâu con liên tiếp và hai đoạn ở vị trí khác nhau nhưng cùng mặt chữ chỉ tính một lần. Chương trình dùng mảng hậu tố kết hợp mảng LCP để đếm số xâu con khác nhau trong thời gian N log N thay vì liệt kê toàn bộ.

## Nhiệm vụ

Cho xâu $S$. Hãy lập trình đếm số xâu con liên tiếp phân biệt của $S$, rồi in ra kết quả.

## Input

- Dòng duy nhất: xâu $S$ gồm chữ cái thường ($1 \le |S| \le 2 \cdot 10^5$).

## Output

- In ra một dòng duy nhất là số xâu con phân biệt (dùng số nguyên 64-bit).

## Sample 1

### Input

```text
aba
```

### Output

```text
5```

### Giải thích

- Các xâu con của $aba$ gồm $a, b, a, ab, ba, aba$ (sáu lượt xuất hiện).
- Hai lượt $a$ trùng nhau nên chỉ còn năm xâu phân biệt là $a, b, ab, ba, aba$.
- Chương trình in ra $5$.

## Ràng buộc

- $1 \le |S| \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
