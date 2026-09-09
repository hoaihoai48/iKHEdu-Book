# Hòn Đảo Nhân Tạo Lớn Nhất (Making A Large Island)

## Bối cảnh
Một dự án lấn biển quy hoạch trên vùng biển lưới $N × M$ gồm các ô đất liền `'1'` và các ô nước biển `'0'`. Ban quản lý dự án được cấp ngân sách để cải tạo đúng một ô nước biển `'0'` duy nhất thành ô đất liền `'1'`. Hãy tìm diện tích hòn đảo lớn nhất có thể tạo thành sau khi đã biến đổi đúng một ô nước biển thích hợp.

## Nhiệm vụ
Cho ma trận nhị phân $N × M$. Hãy lập trình tìm diện tích lớn nhất của một hòn đảo sau khi chuyển đổi tối đa một ô `0` thành `1`.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên `0` hoặc `1`.

## Output
- In ra trên một dòng duy nhất diện tích lớn nhất của hòn đảo thu được.

## Sample 1
### Input
```text
2 2
10
01
```
### Output
```text
3
```

### Giải thích
Với hai hòn đảo nhỏ diện tích 2 và 3 nằm cách nhau đúng một ô nước biển '0':
Khi chuyển ô nước đó thành ô đất '1', hai hòn đảo sẽ được nối liền thành một hòn đảo duy nhất có diện tích $2 + 3 + 1 = 6$. Diện tích lớn nhất đạt được là 6.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
