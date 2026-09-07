# Tối đa hóa lợi nhuận giao hàng

## Bối cảnh

Chị chủ cửa hàng cơm trưa nhận được nhiều đơn đặt hàng từ các công ty xung quanh, mỗi đơn có một hạn giao và một khoản lãi khác nhau. Tiệm chỉ có một shipper nên mỗi ngày chỉ giao được đúng một đơn, và đơn nào quá hạn thì khách sẽ hủy. Chị muốn chọn ra những đơn sẽ giao sao cho tất cả đều kịp hạn và tổng tiền lãi thu về là cao nhất, để cuối tháng có thêm tiền thưởng cho nhân viên gắn bó với quán.

## Nhiệm vụ

Cho $N$ đơn hàng, mỗi đơn có hạn giao $deadline_i$ (ngày) và tiền lãi $profit_i$ (mỗi đơn giao trong đúng một ngày). Hãy lập trình chọn ra các đơn có thể giao đúng hạn sao cho tổng tiền lãi lớn nhất, rồi in ra tổng lãi đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số đơn hàng.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $deadline_i, profit_i$ ($1 \le deadline_i \le 10^5$, $1 \le profit_i \le 10^6$), là hạn giao và tiền lãi của một đơn.

## Output

- In ra một số nguyên duy nhất là tổng tiền lãi lớn nhất.

## Sample 1

### Input

```text
4
1 50
1 20
2 100
2 10
```

### Output

```text
150
```

### Giải thích

- Xét các đơn theo hạn giao tăng dần: $(1, 50)$, $(1, 20)$, $(2, 100)$, $(2, 10)$.
- Nhận đơn lãi $50$ hạn ngày $1$ vì còn ngày trống, giỏ đang có $\{50\}$.
- Đơn lãi $20$ hạn ngày $1$ không còn ngày trống và cũng không lớn hơn đơn nào trong giỏ nên bỏ qua.
- Nhận đơn lãi $100$ hạn ngày $2$ vì còn ngày trống, giỏ thành $\{50, 100\}$.
- Đơn lãi $10$ hạn ngày $2$ không còn ngày trống và nhỏ hơn mọi đơn trong giỏ nên bỏ qua.
- Tổng lãi là $50 + 100 = 150$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le deadline_i \le 10^5$, $1 \le profit_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
