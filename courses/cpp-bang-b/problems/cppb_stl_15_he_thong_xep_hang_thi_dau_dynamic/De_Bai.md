# Hệ Thống Xếp Hạng Thi Đấu Dynamic

## Bối cảnh
Hệ thống thi đấu online hỗ trợ 2 loại truy vấn: `1 Name Score` (Cộng điểm cho thí sinh Name) và `2 Name` (Hỏi tổng điểm hiện tại của thí sinh Name).

## Nhiệm vụ
Với mỗi truy vấn loại 2, in ra điểm số của thí sinh tương ứng.

## Input
- Dòng 1: Số nguyên $Q$ ($1 \le Q \le 20000$).
- $Q$ dòng tiếp theo chứa các truy vấn.

## Output
- Kết quả các truy vấn loại 2.

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

## Ràng buộc
- $100\%$ số test có $1 \le Q \le 20000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
