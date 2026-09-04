# Logarit rời rạc (baby-step giant-step)

## Bối cảnh
Trò chơi tìm mật mã của đội hướng đạo quy định: xuất phát từ $1$, mỗi lượt nhân tiếp với $a$ rồi lấy phần dư theo $m$; đội nào tìm được số lượt đi $x$ ít nhất để chạm đúng số $b$ sẽ thắng. Có những số $b$ không bao giờ chạm tới được, khi đó trọng tài ghi $-1$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho ba số $a, b, m$. Hãy lập trình tìm số mũ $x$ nhỏ nhất không âm thỏa $a^x \equiv b \pmod m$; in `-1` nếu không tồn tại.

## Input
- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

## Output
- In ra kết quả trên một dòng.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Logarit Rời Rạc (Baby-step Giant-step).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
