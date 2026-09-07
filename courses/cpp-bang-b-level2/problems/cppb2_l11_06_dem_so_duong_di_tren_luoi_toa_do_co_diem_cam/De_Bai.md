# Đếm đường đi trên lưới có điểm cấm

## Bối cảnh

Ban quản lý khu du lịch sinh thái cần vạch tuyến tuần tra cho đội kiểm lâm trên bản đồ lưới ô vuông kích thước R hàng và C cột. Một số ô bị ngập không thể đi qua, chốt xuất phát ở góc trên trái và trạm cuối ở góc dưới phải. Mỗi bước tuần tra chỉ được đi sang phải hoặc đi xuống dưới để tiết kiệm nhiên liệu xe điện. Đội trưởng cần biết có bao nhiêu lộ trình khác nhau, lấy phần dư cho 1 000 000 007 để lập lịch phân ca trực.

## Nhiệm vụ

Cho lưới $R \times C$ và $K$ ô cấm. Hãy lập trình đếm số đường đi từ ô $(1,1)$ đến ô $(R,C)$, mỗi bước chỉ đi sang phải hoặc xuống dưới, không đi qua ô cấm, rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng 1: ba số nguyên $R, C, K$ ($1 \le R, C \le 1000$, $0 \le K < R \times C$).
- $K$ dòng tiếp theo, mỗi dòng gồm $x, y$ là tọa độ một ô cấm (ô xuất phát và ô đích không bao giờ bị cấm).

## Output

- In ra một dòng duy nhất là số lộ trình hợp lệ theo modulo $1\,000\,000\,007$.

## Sample 1

### Input

```text
3 3 1
2 2
```

### Output

```text
2```

### Giải thích

- Lưới $3 \times 3$ cấm đúng ô giữa $(2,2)$.
- Không có ô cấm sẽ có $6$ đường, nhưng mọi đường đi qua $(2,2)$ đều bị loại: từ đầu đến $(2,2)$ có $2$ cách, từ $(2,2)$ đến đích có $2$ cách, tức loại $2 \times 2 = 4$ đường.
- Còn lại $6 - 4 = 2$ lộ trình nên chương trình in ra $2$.

## Ràng buộc

- $1 \le R, C \le 1000$; $0 \le K < R \times C$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
