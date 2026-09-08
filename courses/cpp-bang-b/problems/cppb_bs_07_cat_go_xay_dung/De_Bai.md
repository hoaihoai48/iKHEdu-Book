# Cắt Gỗ Xây Dựng (Woodcutting / EKO)

## Bối cảnh
Bác thợ mộc nhận hợp đồng cung ứng gỗ xây dựng trường học vùng cao và cần thu hoạch ít nhất M mét gỗ. Khu rừng có N cây cổ thụ với chiều cao lần lượt là H1, H2, ..., Hn. Máy cắt gỗ công nghiệp có thể thiết lập độ cao cưa H: tất cả các cây có chiều cao lớn hơn H sẽ bị cưa phần ngọn thừa ra (chiều dài gỗ thu được từ mỗi cây là Hi - H nếu Hi > H). Để bảo vệ tài nguyên rừng, bác thợ mộc muốn đặt độ cao cưa H lớn nhất có thể sao cho tổng lượng gỗ thu được vẫn đạt ít nhất M mét.

## Nhiệm vụ
Cho chiều cao N cây gỗ và lượng gỗ tối thiểu cần lấy M. Hãy tìm độ cao cắt H lớn nhất của máy cưa.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $M$ ($1 \le N \le 10^6, 1 \le M \le 2 \cdot 10^9$).
- Dòng 2: Chứa $N$ số nguyên dương $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là độ cao cắt $H$ lớn nhất.

## Sample 1
### Input
```text
4 7
20 15 10 17
```
### Output
```text
15
```
### Giải thích
Khi đặt độ cao cắt H = 15:

- Cây 20m cắt được: 20 - 15 = 5m.
- Cây 15m cắt được: 15 - 15 = 0m.
- Cây 10m không bị cắt: 0m.
- Cây 17m cắt được: 17 - 15 = 2m.
Tổng gỗ thu được là 5 + 0 + 0 + 2 = 7 mét đúng bằng M. Đây là độ cao H lớn nhất.

## Ràng buộc
- $100\%$ số test có $N \le 10^6, M \le 2 \cdot 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
