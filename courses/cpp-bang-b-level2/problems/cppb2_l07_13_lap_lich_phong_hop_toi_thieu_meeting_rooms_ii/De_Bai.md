# Lập lịch phòng họp tối thiểu (meeting rooms ii)

## Bối cảnh

Tòa nhà văn phòng cho thuê nhận được $N$ đơn đặt phòng họp trong ngày, mỗi đơn xin dùng phòng từ giờ $s_i$ đến giờ $e_i$. Ban quản lý có thể huy động nhiều phòng họp cùng lúc nhưng muốn dùng càng ít phòng càng tốt để tiết kiệm tiền điện và nhân viên phục vụ. Hai cuộc họp có thể dùng chung một phòng nếu cuộc trước kết thúc đúng lúc cuộc sau bắt đầu, vì nhân viên dọn phòng làm việc rất nhanh gọn giữa hai ca.

## Nhiệm vụ

Cho $N$ khoảng thời gian $[s_i, e_i]$. Hãy lập trình tính số phòng họp ít nhất cần chuẩn bị để mọi cuộc họp đều có phòng, rồi in ra số đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số cuộc họp.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $s_i, e_i$ ($0 \le s_i < e_i \le 10^9$), là giờ bắt đầu và giờ kết thúc của một cuộc họp.

## Output

- In ra một số nguyên duy nhất là số phòng họp ít nhất.

## Sample 1

### Input

```text
3
0 30
5 10
15 20
```

### Output

```text
2
```

### Giải thích

- Xét các cuộc họp theo giờ bắt đầu: $[0, 30]$, $[5, 10]$, $[15, 20]$.
- Cuộc $[0, 30]$ dùng phòng thứ nhất, phòng này bận đến giờ $30$.
- Cuộc $[5, 10]$ bắt đầu lúc phòng thứ nhất đang bận nên phải mở phòng thứ hai.
- Cuộc $[15, 20]$ bắt đầu lúc phòng thứ hai vừa trống (kết thúc giờ $10$) nên dùng chung phòng thứ hai.
- Tổng cộng cần $2$ phòng và không thể ít hơn vì hai cuộc đầu trùng giờ nhau.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le s_i < e_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
