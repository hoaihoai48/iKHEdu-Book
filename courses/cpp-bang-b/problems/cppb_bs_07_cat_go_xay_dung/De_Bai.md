# Cắt Gỗ Xây Dựng (Woodcutting / EKO)

## Bối cảnh
Bác thợ mộc cần lấy ít nhất $M$ mét gỗ. Khu rừng có $N$ cái cây với chiều cao lần lượt là $A_1, A_2, \dots, A_N$. Bác sử dụng một máy cắt có thể điều chỉnh độ cao lưỡi cưa tại mức $H$. Máy sẽ cắt ngang tất cả các cây có chiều cao lớn hơn $H$, phần ngọn bị cắt rời (chiều cao $A_i - H$) sẽ được gom lại làm gỗ. Các cây có chiều cao $\le H$ sẽ giữ nguyên vẹn.

## Nhiệm vụ
Hãy tìm độ cao $H$ nguyên lớn nhất để bác thợ mộc thu được ít nhất $M$ mét gỗ.

## Input
- Dòng 1: Gồm 2 số nguyên $N, M$ ($1 \le N \le 10^5, 1 \le M \le 10^{14}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là độ cao $H$ lớn nhất.

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
*(Giải thích: Cắt ở độ cao 15: Cây 20 cho 5m, cây 17 cho 2m, tổng là $5 + 2 = 7\text{m}$ gỗ).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5, M \le 10^{14}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
