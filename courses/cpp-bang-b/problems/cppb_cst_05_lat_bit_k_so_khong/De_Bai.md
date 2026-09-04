# Đoạn Con Chứa Tối Đa K Số 0 (Lật Bit)

## Bối cảnh
Trong đường truyền dữ liệu viễn thông cáp quang, chuỗi bit truyền đi gồm N ký tự 0 và 1. Do suy hao tín hiệu quang, một số bit 1 bị biến thành bit 0. Bộ giải mã thông minh tại đầu nhận được phép phục hồi (lật) tối đa K bit 0 trở lại thành bit 1. Kỹ sư viễn thông cần tìm chuỗi bit 1 liên tiếp dài nhất có thể tạo ra sau khi thực hiện tối đa K phép lật bit.

## Nhiệm vụ
Cho một mảng nhị phân A gồm N phần tử (Ai thuộc {0, 1}) và số nguyên không âm K. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp chỉ toàn bit 1 sau khi lật tối đa K số 0 thành số 1.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le N \le 10^5, 0 \le K \le N$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($A_i \in \{0, 1\}$).

## Output
- In ra độ dài lớn nhất của đoạn con toàn số 1 tạo được.

## Sample 1
### Input
```text
11 2
1 1 1 0 0 0 1 1 1 1 0
```
### Output
```text
6
```
### Giải thích
Xét đoạn từ vị trí 5 đến vị trí 10: [0, 0, 1, 1, 1, 1]. Đoạn này có độ dài 6 và chứa đúng hai số 0. Khi lật 2 số 0 này thành 1, ta thu được chuỗi 6 số 1 liên tiếp. Đây là độ dài dài nhất có thể tạo được.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
