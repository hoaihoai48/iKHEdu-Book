# Số lượng trạm tiếp nhiên liệu ít nhất (gas station)

## Bối cảnh

Bác tài xế xe tải nhận chuyến hàng đường dài tới kho hàng cách vị trí hiện tại đúng $target$ kilômét. Xe của bác đang có sẵn một lượng nhiên liệu ban đầu, mỗi lít đi được đúng một kilômét. Dọc đường có nhiều trạm xăng, mỗi trạm ở một vị trí xác định và có thể bơm một lượng xăng nhất định. Bác muốn dừng đổ xăng càng ít lần càng tốt để kịp giờ giao hàng cho đối tác, vì mỗi lần dừng đều mất thời gian chờ đợi rất lâu.

## Nhiệm vụ

Cho quãng đường $target$, lượng xăng ban đầu $start\_fuel$ và $N$ trạm xăng, mỗi trạm ở vị trí $dist_i$ với lượng xăng $fuel_i$. Mỗi lít xăng đi được một kilômét. Hãy lập trình tính số lần dừng đổ xăng ít nhất để đi tới đích, rồi in ra số đó. Nếu không thể tới đích thì in ra $-1$.

## Input

- Dòng đầu tiên chứa số nguyên $N$ và hai số nguyên $target, start\_fuel$ ($0 \le N \le 10^5$, $1 \le target, start\_fuel \le 10^9$), là số trạm, quãng đường và xăng ban đầu.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $dist_i, fuel_i$ ($0 \le dist_i < target$, $1 \le fuel_i \le 10^6$), là vị trí và lượng xăng của một trạm.

## Output

- In ra số lần dừng đổ xăng ít nhất, hoặc $-1$ nếu không tới được đích.

## Sample 1

### Input

```text
3 100 10
10 60
20 30
60 40
```

### Output

```text
2
```

### Giải thích

- Xe xuất phát với $10$ lít nên đi được tới điểm $10$, tại đây có trạm $60$ lít.
- Đổ $60$ lít, xe có tổng cộng $10 + 60 = 70$ quãng đường, đi được tới điểm $70$ với một lần dừng.
- Trên đường tới điểm $70$ đi ngang hai trạm $30$ lít (điểm $20$) và $40$ lít (điểm $60$), chọn đổ trạm $40$ lít để đi xa nhất.
- Xe đi được tới $70 + 40 = 110$, vượt qua đích $100$ với tổng cộng $2$ lần dừng.

## Ràng buộc

- $0 \le N \le 10^5$, $1 \le target, start\_fuel \le 10^9$, $0 \le dist_i < target$, $1 \le fuel_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
