# Hệ Thống Xếp Hạng Thi Đấu Dynamic

## Bối cảnh
Tại kỳ thi lập trình thuật toán trực tuyến DKOJ của iKHEDU, hệ thống chấm thi thời gian thực cần liên tục ghi nhận điểm số và cập nhật kết quả thi đấu của các thí sinh. Mỗi khi thí sinh nộp bài hoặc cần tra cứu điểm, hệ thống sẽ thực thi một trong hai loại thao tác: cộng điểm cho một thí sinh hoặc truy vấn điểm tích lũy hiện tại của thí sinh đó.

## Nhiệm vụ
Cho danh sách $Q$ thao tác của hệ thống. Bạn hãy lập trình mô phỏng lại hệ thống và in ra kết quả cho mỗi thao tác tra cứu điểm.

## Input
- Dòng 1: Chứa số nguyên dương $Q$ ($1 \le Q \le 20000$) là số lượng thao tác.
- $Q$ dòng tiếp theo biểu diễn các thao tác thuộc một trong hai dạng:
  - `1 Name Score`: Cộng thêm $Score$ điểm cho thí sinh có tên $Name$.
  - `2 Name`: Yêu cầu in ra tổng điểm tích lũy hiện tại của thí sinh $Name$.

## Output
- Với mỗi thao tác loại `2`, in ra trên một dòng một số nguyên duy nhất là tổng điểm của thí sinh đó (nếu thí sinh chưa có điểm, in ra `0`).

## Sample 1
### Input
```text
4
1 Alice 100
1 Bob 150
2 Alice
1 Alice 60
```
### Output
```text
100
```

### Giải thích
Diễn biến 4 thao tác của hệ thống thi đấu:

1. Thao tác 1 (`1 Alice 100`): Alice được cộng 100 điểm. Điểm hiện tại của Alice là 100.
2. Thao tác 2 (`1 Bob 150`): Bob được cộng 150 điểm. Điểm hiện tại của Bob là 150.
3. Thao tác 3 (`2 Alice`): Truy vấn điểm của Alice. Hệ thống in ra điểm hiện tại là 100.
4. Thao tác 4 (`1 Alice 60`): Alice được cộng thêm 60 điểm nữa. Điểm tích lũy mới của Alice trở thành $100 + 60 = 160$.

## Ràng buộc
- $100\%$ số test có $1 \le Q \le 20000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
