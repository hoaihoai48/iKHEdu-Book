# Chặt nhị phân cắt gỗ (eko)

## Bối cảnh
Có $N$ cây gỗ có chiều cao $H_1, H_2, \dots, H_N$. Cần cưa ở độ cao $H$ sao cho tổng lượng gỗ thu được $\ge M$. Tìm độ cao $H$ lớn nhất có thể.

## Nhiệm vụ

Cho số cây $N$, lượng gỗ cần $M$ và chiều cao từng cây $H_i$. Hãy lập trình tìm độ cao cưa $H$ lớn nhất sao cho tổng lượng gỗ thu được không nhỏ hơn $M$.

## Input
- Dòng 1: $N, M$ ($1 \le N \le 10^6, 1 \le M \le 10^{18}$). Dòng 2: $N$ số $H_i$ ($1 \le H_i \le 10^9$).

## Output
- In ra độ cao cưa $H$ lớn nhất.

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
* Thử cưa ở độ cao $H = 15$: cây cao $20$ cho $20 - 15 = 5$, cây cao $15$ cho $0$, cây cao $10$ cho $0$, cây cao $17$ cho $17 - 15 = 2$. Tổng gỗ thu được là $5 + 0 + 0 + 2 = 7$, vừa đủ lượng cần ($\ge 7$).
* Thử nâng lưỡi cưa lên $H = 16$: chỉ còn $(20 - 16) + (17 - 16) = 4 + 1 = 5 < 7$, không đủ gỗ. Vì vậy $15$ là độ cao lớn nhất thỏa mãn.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
