# Đường Đi Chi Phí Nhỏ Nhất Trên Lưới

## Bối cảnh
Một tuyến cáp quang ngầm cần được thi công băng qua khu vực địa chất hình chữ nhật $N  × M$ ô. Mỗi ô $(i, j)$ có chi phí khoan đào đất đá tương ứng là $A_{i,j}$. Tuyến cáp bắt đầu từ trạm phát tín hiệu tại ô $(1, 1)$ và kết thúc tại trạm thu ở ô $(N, M)$. Để hạn chế tối đa góc uốn cong của dây cáp, hướng thi công chỉ được tiến sang phải hoặc xuống dưới.

## Nhiệm vụ
Cho ma trận chi phí của lưới $N  × M$. Hãy lập trình tìm tổng chi phí khoan đào nhỏ nhất để hoàn thành tuyến cáp từ ô $(1, 1)$ tới ô $(N, M)$.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên không âm $A_{i,j}$ ($0 \le A_{i,j} \le 10^4$).

## Output
- In ra trên một dòng duy nhất tổng chi phí nhỏ nhất tìm được.

## Sample 1
### Input
```text
3 3
1 3 1
1 5 1
4 2 1
```
### Output
```text
7
```

### Giải thích
Với ma trận chi phí kích thước $3  × 3$:
Lộ trình có chi phí nhỏ nhất là đi qua các ô $(1,1)  × o (1,2)  × o (2,2)  × o (2,3)  × o (3,3)$ hoặc tương đương, mang lại tổng chi phí tối thiểu là 12.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000, 0 \le A_{i, j} \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
