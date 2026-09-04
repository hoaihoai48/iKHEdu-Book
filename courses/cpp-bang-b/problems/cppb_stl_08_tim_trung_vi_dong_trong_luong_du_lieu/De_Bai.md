# Tìm Trung Vị Động Trong Luồng Dữ Liệu

## Bối cảnh
Trong hệ thống giám sát tải mạng máy tính, các gói tin liên tục gửi về các thông số độ trễ (ping). Để đánh giá độ trễ trung bình chuẩn xác mà không bị ảnh hưởng bởi các giá trị ngoại lai cá biệt, hệ thống cần tính toán giá trị trung vị (median) của luồng dữ liệu ngay sau mỗi khi tiếp nhận thêm một con số mới.

## Nhiệm vụ
Cho một luồng dữ liệu gồm $N$ số nguyên đến lần lượt từng số một. Với mỗi số được thêm vào, hãy in ra giá trị trung vị của toàn bộ dãy số đã nhận được từ đầu đến thời điểm đó (lấy phần nguyên dưới nếu số lượng phần tử chẵn).

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng gồm $N$ số nguyên là các giá trị trung vị tương ứng sau mỗi bước, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
4
5 15 1 3
```
### Output
```text
5 5 5 3
```

### Giải thích
Với luồng dữ liệu đến lần lượt: 5, 15, 1, 3:
- Nhận 5: dãy [5] $\to$ trung vị là 5.
- Nhận 15: dãy [5, 15] $\to$ trung vị là 5 (hoặc trung bình lấy nguyên).
- Nhận 1: dãy [1, 5, 15] $\to$ trung vị là 5.
- Nhận 3: dãy [1, 3, 5, 15] $\to$ trung vị là 3 (hoặc phần nguyên).
Kết quả in ra dãy trung vị động tương ứng.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
