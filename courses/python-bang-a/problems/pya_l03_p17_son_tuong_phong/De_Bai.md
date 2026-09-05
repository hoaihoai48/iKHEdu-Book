# Tính tiền mua sơn quét tường

## Bối cảnh
Một bức tường hình chữ nhật có chiều dài $A$ mét và chiều cao $H$ mét. Trên tường có một cửa sổ hình chữ nhật kích thước $X \times Y$ mét không cần quét sơn. Biết mỗi mét vuông tường tốn $G$ đồng tiền sơn.

## Nhiệm vụ
Nhập 5 số nguyên $A, H, X, Y, G$ trên cùng 1 dòng. In ra tổng số tiền sơn cần chuẩn bị.

## Input
Một dòng chứa 5 số nguyên dương ($X < A, Y < H$, $1 \le A, H \le 100$, $1 \le G \le 10^5$).

## Output
In ra tổng số tiền sơn.

## Sample 1
### Input
```text
6 3 2 1 50000
```
### Output
```text
800000
```
### Giải thích
Diện tích tường $= 6 \times 3 = 18\text{m}^2$. Diện tích cửa sổ $= 2 \times 1 = 2\text{m}^2$. Diện tích cần sơn $= 18 - 2 = 16\text{m}^2$. Tổng tiền $= 16 \times 50000 = 800000$ đồng.

## Ràng buộc
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
