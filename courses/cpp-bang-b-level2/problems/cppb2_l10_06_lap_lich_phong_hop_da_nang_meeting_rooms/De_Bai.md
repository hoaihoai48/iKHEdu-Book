# Lập lịch phòng họp đa năng (meeting rooms)

## Bối cảnh

Trung tâm hội nghị nhận đặt chỗ theo từng khung giờ trong ngày, mỗi đơn đặt là một khoảng thời gian $[l_i, r_i]$. Khi có đơn mới đến mà khung giờ của nó giao nhau hoặc chạm với các đơn đã nhận, lễ tân sẽ gộp chúng thành một khung bận liên tục duy nhất để tiện theo dõi. Cuối ngày, giám đốc muốn biết tổng số giờ phòng họp thực sự bận (độ dài của hợp các khung giờ sau khi gộp) để tính tiền điện và lên kế hoạch vệ sinh cho ngày hôm sau.

## Nhiệm vụ

Cho $Q$ thao tác, mỗi thao tác thêm một khoảng $[l_i, r_i]$ vào lịch (các khoảng giao nhau hoặc chạm nhau được gộp lại). Sau khi thực hiện tất cả các thao tác, hãy lập trình tính tổng độ dài của các khoảng rời nhau còn lại, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $Q$ ($1 \le Q \le 10^5$), là số đơn đặt chỗ.
- $Q$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $l_i, r_i$ ($0 \le l_i < r_i \le 10^9$), là khung giờ của một đơn.

## Output

- In ra một số nguyên duy nhất là tổng độ dài sau khi gộp.

## Sample 1

### Input

```text
3
1 3
2 4
6 8
```

### Output

```text
5
```

### Giải thích

- Thêm khoảng $[1, 3]$, lịch đang có một khung bận $[1, 3]$.
- Thêm khoảng $[2, 4]$ giao với $[1, 3]$ nên gộp thành khung $[1, 4]$.
- Thêm khoảng $[6, 8]$ rời hẳn với $[1, 4]$ nên lịch gồm hai khung $[1, 4]$ và $[6, 8]$.
- Tổng độ dài là $(4 - 1) + (8 - 6) = 3 + 2 = 5$.

## Ràng buộc

- $1 \le Q \le 10^5$, $0 \le l_i < r_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
