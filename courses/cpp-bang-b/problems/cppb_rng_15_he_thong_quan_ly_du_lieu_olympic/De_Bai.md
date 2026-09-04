# Hệ Thống Quản Lý Dữ Liệu Olympic (Range Master)

## Bối cảnh
Một hệ thống máy chủ chấm thi Olympic Tin học Quốc tế quản lý dữ liệu điểm số của $N$ thí sinh. Hệ thống cần xử lý đồng thời nhiều loại truy vấn đa năng phức tạp: gán giá trị mới cho một đoạn, cộng thêm giá trị vào một đoạn, tính tổng đoạn, và tìm giá trị lớn nhất/nhỏ nhất trong đoạn.

## Nhiệm vụ
Cho mảng $A$ và $Q$ truy vấn đa năng. Hãy lập trình thực thi chính xác và in ra kết quả tương ứng cho từng yêu cầu truy vấn thông tin.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$.
- $Q$ dòng tiếp theo chứa các thao tác mô tả theo quy ước bài toán.

## Output
- In ra kết quả cho mỗi thao tác truy vấn trên một dòng.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
1 2 4 2
2 1 5
2 2 4
```
### Output
```text
21
15
```

### Giải thích
Hệ thống cập nhật linh hoạt các phân đoạn dữ liệu lớn và trả về tổng điểm cũng như điểm cực trị chính xác cho ban giám khảo trong thời gian thực.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
