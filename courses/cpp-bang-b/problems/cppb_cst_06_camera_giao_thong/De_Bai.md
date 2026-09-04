# Giám Sát Camera Giao Thông Thông Minh

## Bối cảnh
Trên một tuyến cao tốc huyết mạch dài, cảnh sát giao thông thiết lập N cột gắn camera giám sát, trạng thái mỗi camera được ghi nhận: 1 là hoạt động tốt, 0 là bị hư hỏng. Để đảm bảo an toàn tuyệt đối, quy chế cao tốc quy định mọi đoạn đường liên tiếp có chiều dài K cột camera bắt buộc phải có ít nhất B camera hoạt động bình thường. Đội bảo trì cần tính toán số lượng camera hư hỏng tối thiểu cần sửa chữa để mọi phân đoạn K cột đều đạt chuẩn an toàn.

## Nhiệm vụ
Cho mảng nhị phân A gồm N phần tử (1: hoạt động, 0: hỏng). Hãy tìm số lượng camera hỏng ít nhất cần sửa thành hoạt động sao cho trong mọi đoạn gồm K camera liên tiếp đều có ít nhất B camera hoạt động.

## Input
- Dòng 1: Chứa 3 số nguyên $N, K, B$ ($1 \le B \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($A_i \in \{0, 1\}$).

## Output
- In ra số camera tối thiểu cần sửa chữa.

## Sample 1
### Input
```text
10 6 5
1 0 1 1 0 1 1 1 0 1
```
### Output
```text
1
```
### Giải thích
Đoạn từ vị trí 1 đến 6 là [1, 0, 1, 1, 0, 1] chỉ có 4 camera hoạt động (thiếu 1 camera so với chuẩn B = 5). Ta sửa camera thứ 2 (hoặc thứ 5) từ 0 thành 1. Khi đó mọi đoạn 6 camera liên tiếp đều có ít nhất 5 camera hoạt động. Do đó chỉ cần sửa tối thiểu 1 camera.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
