# Bảng Tra Cứu Tần Suất Từ Khóa

## Bối cảnh
Một công cụ tìm kiếm dữ liệu lớn ghi nhận $N$ từ khóa được người dùng nhập vào thanh tìm kiếm trong ngày. Để phục vụ việc tối ưu hóa máy chủ và đề xuất xu hướng tìm kiếm hàng đầu, kỹ sư hệ thống cần thiết lập một bảng thống kê tần suất xuất hiện của từng từ khóa theo thứ tự bảng chữ cái (thứ tự từ điển tăng dần).

## Nhiệm vụ
Cho danh sách gồm $N$ từ khóa. Hãy lập trình đếm tần suất xuất hiện của mỗi từ khóa và in ra kết quả theo thứ tự từ điển tăng dần của các từ khóa.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- $N$ dòng tiếp theo, mỗi dòng chứa một từ khóa gồm các chữ cái tiếng Anh in thường có độ dài từ 1 đến 30 ký tự.

## Output
- In ra các dòng, mỗi dòng gồm một từ khóa và số lần xuất hiện của từ khóa đó, cách nhau bởi một dấu cách.

## Sample 1
### Input
```text
4
apple
banana
apple
orange
```
### Output
```text
apple 2
banana 1
orange 1
```

### Giải thích
Với danh sách 4 từ khóa: ["apple", "banana", "apple", "cherry"]:
- Từ khóa "apple" xuất hiện 2 lần.
- Từ khóa "banana" xuất hiện 1 lần.
- Từ khóa "cherry" xuất hiện 1 lần.
Các từ khóa được sắp xếp đúng thứ tự từ điển a -> b -> c.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
