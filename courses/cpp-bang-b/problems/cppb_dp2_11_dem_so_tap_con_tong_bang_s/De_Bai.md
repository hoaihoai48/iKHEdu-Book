# Đếm Số Tập Con Có Tổng Bằng S

## Bối cảnh
Tại một phòng thí nghiệm hóa học, các nhà nghiên cứu có $N$ lọ dung dịch chuẩn, lọ thứ $i$ có thể tích là $A_i$ (ml). Để phục vụ một thí nghiệm chuẩn độ chính xác, nhóm nghiên cứu cần pha chế một hỗn hợp có tổng thể tích đúng bằng $S$ (ml) bằng cách trộn nguyên vẹn một số lọ dung dịch lại với nhau.

## Nhiệm vụ
Cho danh sách thể tích $N$ lọ dung dịch và thể tích mục tiêu $S$. Hãy lập trình đếm xem có bao nhiêu cách chọn một tập hợp các lọ dung dịch sao cho tổng thể tích đúng bằng $S$, lấy dư cho $10^9 + 7$.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $S$ ($1 \le N \le 1000, 1 \le S \le 1000$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 1000$).

## Output
- In ra số lượng cách chọn hợp lệ theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
4 5
1 2 3 4
```
### Output
```text
2
```

### Giải thích
Với mảng dung dịch $[1, 2, 3, 3]$ và thể tích cần lấy $S = 6$:
Có 3 cách chọn tập con có tổng bằng 6:
1. Chọn các phần tử tại vị trí 1, 2, 3: $1 + 2 + 3 = 6$.
2. Chọn các phần tử tại vị trí 1, 2, 4: $1 + 2 + 3 = 6$.
3. Chọn các phần tử tại vị trí 3, 4: $3 + 3 = 6$.
Kết quả in ra là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 500, 1 \le S \le 5000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
