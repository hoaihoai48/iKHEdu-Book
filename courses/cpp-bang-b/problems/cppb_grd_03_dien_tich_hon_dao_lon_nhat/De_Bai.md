# Diện Tích Hòn Đảo Lớn Nhất (Max Area of Island)

## Bối cảnh
Vẫn trên bản đồ hải đồ nhị phân $N × M$ gồm các ô đất liền `'1'` và nước biển `'0'`, ban quản lý khu bảo tồn thiên nhiên muốn chọn ra hòn đảo có diện tích lớn nhất (chứa số lượng ô đất liền liên thông nhiều nhất) để quy hoạch xây dựng trung tâm cứu hộ động vật hoang dã.

## Nhiệm vụ
Cho bản đồ ma trận $N × M$. Hãy lập trình tìm diện tích (số lượng ô đất) của hòn đảo lớn nhất. Nếu bản đồ không có đảo nào, in ra `0`.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi gồm $M$ ký tự `'0'` hoặc `'1'`.

## Output
- In ra trên một dòng duy nhất diện tích của hòn đảo lớn nhất.

## Sample 1
### Input
```text
4 5
11000
11000
00100
00011
```
### Output
```text
4
```

### Giải thích
Với bản đồ có cụm đảo lớn nhất gồm 5 ô đất liền kề cạnh kết nối liên tục với nhau, diện tích lớn nhất đo được là 5.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
