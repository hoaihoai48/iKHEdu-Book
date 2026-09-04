# Cài Đặt Segment Tree Tìm Min Đoạn (RMQ)

## Bối cảnh
Một trạm quan trắc khí tượng ghi nhận nhiệt độ thấp nhất tại $N$ trạm cảm biến ven biển. Các chuyên gia cần liên tục thực hiện hai loại thao tác: cập nhật lại nhiệt độ mới tại một trạm cảm biến cụ thể, và truy vấn tìm mức nhiệt độ thấp nhất (Min) trong một phân đoạn các trạm quan sát từ $L$ đến $R$.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên và $Q$ truy vấn thuộc hai dạng: `1 pos val` (gán $A[pos] = val$) và `2 L R` (tìm giá trị nhỏ nhất trong đoạn từ $L$ đến $R$). Hãy in ra kết quả của các truy vấn loại 2.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng chứa một truy vấn theo định dạng trên.

## Output
- Với mỗi truy vấn loại 2, in ra giá trị nhỏ nhất trong đoạn $[L, R]$ trên một dòng.

## Sample 1
### Input
```text
5 3
5 2 4 1 3
2 1 3
1 4 10
2 3 5
```
### Output
```text
2
3
```

### Giải thích
Với mảng $[5, 2, 8, 1, 9]$:
- Truy vấn tìm min đoạn từ 1 đến 3: $\min(5, 2, 8) = 2$.
- Cập nhật vị trí 2 thành 10: mảng thành $[5, 10, 8, 1, 9]$.
- Truy vấn lại min đoạn từ 1 đến 3: $\min(5, 10, 8) = 5$.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
