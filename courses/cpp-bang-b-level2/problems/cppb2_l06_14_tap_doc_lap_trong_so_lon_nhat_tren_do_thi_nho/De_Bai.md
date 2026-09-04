# Tập độc lập trọng số lớn nhất trên đồ thị nhỏ

## Bối cảnh
Huyện muốn chọn vị trí đặt trạm phát sóng, mỗi vị trí mang lại một lợi ích khác nhau. Hai vị trí kề nhau không thể cùng đặt trạm vì sẽ gây nhiễu sóng.

Huyện cần chọn ra các vị trí không kề nhau sao cho tổng lợi ích là lớn nhất.

## Nhiệm vụ
Cho một đồ thị vô hướng gồm $N$ đỉnh (nhỏ), mỗi đỉnh có một trọng số. Hãy lập trình chọn một tập độc lập (không có cạnh nối giữa hai đỉnh nào trong tập) có tổng trọng số lớn nhất.

## Input
- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

## Output
- In ra kết quả trên một dòng.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tập Độc Lập Trọng Số Lớn Nhất Trên Đồ Thị Nhỏ.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
