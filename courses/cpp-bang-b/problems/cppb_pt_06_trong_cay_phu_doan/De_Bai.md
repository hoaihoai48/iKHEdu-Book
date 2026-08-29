# Trồng Cây Phủ Đoạn Tối Ưu

## Bối cảnh
Dọc một con đường thẳng có $N$ vị trí trồng cây được đánh số từ $1$ đến $N$. Ban đầu, các vị trí đều chưa có cây (mức phủ bằng 0). Có $Q$ tình nguyện viên tham gia tưới nước, người thứ $i$ tưới cho đoạn từ vị trí $L_i$ đến $R_i$. 

## Nhiệm vụ
Hãy đếm xem sau khi tất cả $Q$ người tưới xong, có bao nhiêu vị trí được tưới **ít nhất $K$ lần**.

## Input
- Dòng 1: Gồm 3 số nguyên $N, Q, K$ ($1 \le N, Q \le 10^5, 1 \le K \le Q$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L_i, R_i$ ($1 \le L_i \le R_i \le N$).

## Output
- In ra một số nguyên duy nhất là số lượng vị trí được tưới ít nhất $K$ lần.

## Sample 1
### Input
```text
6 3 2
1 4
2 5
3 6
```
### Output
```text
4
```
*(Giải thích: Các vị trí có số lần tưới lần lượt là $[1, 2, 3, 3, 2, 1]$. Các vị trí $2, 3, 4, 5$ có số lần tưới $\ge 2$, tổng cộng 4 vị trí).*

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
