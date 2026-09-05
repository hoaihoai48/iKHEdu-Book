# Lát nền phòng học

## Bối cảnh
Phòng học hình chữ nhật có chiều dài $L$ mét và chiều rộng $W$ mét. Người ta dùng các viên gạch hoa hình vuông cạnh $D$ centimet để lát nền.

## Nhiệm vụ
Nhập 3 số nguyên dương $L, W, D$ trên cùng 1 dòng ($L, W$ tính bằng mét, $D$ tính bằng centimet). Giả sử phòng học vừa khít các viên gạch, hãy in ra tổng số viên gạch cần dùng.

## Input
Một dòng chứa 3 số nguyên $L, W, D$ ($1 \le L, W \le 100$, $10 \le D \le 100$).

## Output
In ra số viên gạch cần dùng.

## Sample 1
### Input
```text
6 4 50
```
### Output
```text
96
```
### Giải thích
Đổi $L = 600\text{cm}, W = 400\text{cm}$. Diện tích sàn $= 600 \times 400 = 240000\text{cm}^2$. Diện tích 1 viên gạch $= 50 \times 50 = 2500\text{cm}^2$. Số gạch $= 240000 // 2500 = 96$ viên.

## Ràng buộc
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
