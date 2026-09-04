# Cài Đặt Hàng Đợi Cơ Bản

## Bối cảnh
Một hệ thống xếp hàng tự động tại quầy giao dịch ngân hàng hoạt động theo nguyên tắc vào trước ra trước (FIFO - First In First Out). Hệ thống tiếp nhận $Q$ yêu cầu thuộc các dạng: thêm một khách hàng có số định danh $x$ vào cuối hàng đợi, phục vụ khách hàng đang đứng ở đầu hàng (loại bỏ khỏi hàng), và kiểm tra số định danh của khách hàng đang đứng đầu hàng hiện tại.

## Nhiệm vụ
Cho danh sách $Q$ thao tác thuộc 3 loại: `1 x` (thêm $x$ vào cuối hàng), `2` (loại bỏ phần tử đầu hàng nếu hàng không rỗng), `3` (in ra phần tử đầu hàng, nếu rỗng in ra `-1`). Hãy lập trình mô phỏng lại hàng đợi và in ra kết quả cho các thao tác loại 3.

## Input
- Dòng 1: Chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo chứa các thao tác mô tả như trên.

## Output
- Với mỗi thao tác loại 3, in ra kết quả trên một dòng.

## Sample 1
### Input
```text
5
1 10
1 20
3
2
3
```
### Output
```text
10
20
```

### Giải thích
Với chuỗi thao tác: thêm 10, thêm 20, truy vấn đầu hàng -> in ra 10; phục vụ đầu hàng (loại 10), truy vấn đầu hàng -> in ra 20.

## Ràng buộc
- $100\%$ số test có $1 \le Q \le 50000, 1 \le x \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
