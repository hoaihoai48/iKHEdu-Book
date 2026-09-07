# Logarit rời rạc (baby-step giant-step)

## Bối cảnh
Trò chơi tìm mật mã của đội hướng đạo quy định: xuất phát từ $1$, mỗi lượt nhân tiếp với $a$ rồi lấy phần dư theo $m$; đội nào tìm được số lượt đi $x$ ít nhất để chạm đúng số $b$ sẽ thắng. Có những số $b$ không bao giờ chạm tới được, khi đó trọng tài ghi $-1$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho ba số $a, b, m$. Hãy lập trình tìm số mũ $x$ nhỏ nhất không âm thỏa $a^x \equiv b \pmod m$; in `-1` nếu không tồn tại.

## Input

- Gồm một dòng duy nhất chứa ba số nguyên $a, b, m$ ($0 \le a, b < m$, $m$ là số nguyên tố, $2 \le m \le 10^9$), cách nhau bởi dấu cách.

## Output

- In ra một dòng duy nhất là số mũ $x$ nhỏ nhất không âm thỏa $a^x \equiv b \pmod m$; in `-1` nếu không tồn tại.

## Sample 1
### Input
```text
3 4 7
```
### Output
```text
4
```
### Giải thích

Thử tay từng số mũ: $3^0 = 1$, $3^1 = 3$, $3^2 = 9 = 7 + 2$ dư $2$, $3^3 = 6$, $3^4 = 81 = 11 \cdot 7 + 4$ dư $4$. Các số mũ $0, 1, 2, 3$ đều cho kết quả khác $4$ nên đáp án là $4$.

## Ràng buộc

- $0 \le a, b < m$, $m$ nguyên tố không quá $10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
