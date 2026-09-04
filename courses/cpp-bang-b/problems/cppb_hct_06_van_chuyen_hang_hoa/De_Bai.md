# Vận Chuyển Thùng Hàng Cực Đại

## Bối cảnh
Một công ty logistics quốc tế phụ trách điều phối N container hàng hóa hạng nặng có khối lượng lần lượt là W1, W2, ..., Wn (có thể lên tới 10^12 kg) từ tổng kho ra cảng biển. Công ty sử dụng dàn xe đầu kéo rơ-moóc đặc chủng: mỗi chuyến xe chỉ được chở tối đa 2 kiện hàng và tổng khối lượng không được vượt quá giới hạn tải trọng cầu đường C. Để tối ưu chi phí nhiên liệu và nhân công, điều độ viên cần tính toán số chuyến xe tối thiểu cần thực hiện.

## Nhiệm vụ
Cho khối lượng N kiện hàng và tải trọng C của xe đầu kéo. Mỗi chuyến xe chở tối đa 2 kiện hàng và tổng khối lượng không quá C. Hãy tính số chuyến xe ít nhất cần dùng để vận chuyển toàn bộ N kiện hàng.

## Input
- Dòng 1: 2 số nguyên dương $N$ và $C$ ($1 \le N \le 10^5, 1 \le C \le 10^{12}$).
- Dòng 2: $N$ số nguyên dương $W_1, W_2, \dots, W_N$ ($1 \le W_i \le C$).

## Output
- In ra số chuyến xe ít nhất.

## Sample 1
### Input
```text
5 10
3 5 8 2 7
```
### Output
```text
3
```
### Giải thích
Sắp xếp khối lượng 5 kiện hàng tăng dần: [2, 3, 5, 7, 8] với tải trọng C = 10. Chiến thuật ghép con trỏ hai đầu: kiện nặng nhất 8 ghép với nhẹ nhất 2 (8 + 2 = 10 <= 10 -> Chuyến 1); kiện nặng tiếp theo 7 ghép với nhẹ tiếp theo 3 (7 + 3 = 10 <= 10 -> Chuyến 2); kiện còn lại 5 đi riêng một xe (Chuyến 3). Tổng cộng cần 3 chuyến xe.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, C \le 10^{12}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
