# Đếm đường đi trên lưới có điểm cấm (nhiều truy vấn)

## Bối cảnh

Công ty giao hàng bằng drone vẽ lại bản đồ kho hàng thành lưới R hàng C cột để robot lấy hàng tự di chuyển. Mỗi chuyến robot xuất phát từ ô trên cùng bên trái về ô dưới cùng bên phải, chỉ tiến sang phải hoặc xuống dưới, và phải tránh các ô đang bảo trì. Vì danh sách ô bảo trì thay đổi mỗi ca nên hệ thống cần đếm lại số lộ trình khả thi cho từng ca làm việc, lấy dư cho 1 000 000 007.

## Nhiệm vụ

Cho lưới $R \times C$ và danh sách $K$ ô cấm. Hãy lập trình đếm số đường đi từ $(1,1)$ đến $(R,C)$ chỉ đi sang phải hoặc xuống dưới, tránh mọi ô cấm, rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng 1: ba số nguyên $R, C, K$ ($1 \le R, C \le 100$, $0 \le K < R \times C$).
- $K$ dòng tiếp theo, mỗi dòng gồm $x, y$ là tọa độ một ô cấm (ô xuất phát và ô đích không bị cấm).

## Output

- In ra một dòng duy nhất là số lộ trình hợp lệ theo modulo $1\,000\,000\,007$.

## Sample 1

### Input

```text
2 4 1
1 3
```

### Output

```text
2```

### Giải thích

- Lưới $2 \times 4$ cấm đúng ô $(1,3)$: không có ô cấm sẽ có $C(4,1) = 4$ đường (một bước xuống, ba bước sang phải).
- Mọi đường đi qua $(1,3)$ đều bị loại: từ đầu đến $(1,3)$ chỉ có $1$ cách (đi sang phải hai lần), từ $(1,3)$ đến đích có $2$ cách (xuống rồi sang phải, hoặc sang phải rồi xuống).
- Còn lại $4 - 1 \times 2 = 2$ lộ trình nên chương trình in ra $2$.

## Ràng buộc

- $1 \le R, C \le 100$; $0 \le K < R \times C$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
