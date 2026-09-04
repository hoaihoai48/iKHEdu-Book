# Tìm Phần Tử Thứ K Nhỏ Nhất (K-th Element on BIT)

## Bối cảnh
Một máy chủ trò chơi trực tuyến liên tục ghi nhận điểm số của người chơi gia nhập phòng chờ. Ban tổ chức muốn tìm điểm số của người chơi có thành tích xếp thứ $K$ từ dưới lên (phần tử thứ $K$ nhỏ nhất trong tập hợp điểm số hiện tại).

## Nhiệm vụ
Cho một tập hợp các số nguyên hỗ trợ hai thao tác: thêm một số vào tập hợp, và tìm phần tử nhỏ thứ $K$ trong tập hợp. Hãy lập trình in ra kết quả cho các thao tác tìm kiếm.

## Input
- Dòng 1: Chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo chứa các thao tác.

## Output
- In ra kết quả cho mỗi thao tác tìm phần tử thứ $K$ trên một dòng.

## Sample 1
### Input
```text
5
1 10
1 20
1 15
2 2
2 3
```
### Output
```text
15
20
```

### Giải thích
Với tập hợp các số {10, 20, 30, 40, 50}:
Phần tử nhỏ thứ 3 trong tập hợp là số 30.

## Ràng buộc
- $100\%$ số test có $1 \le Q \le 50000, 1 \le x \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
