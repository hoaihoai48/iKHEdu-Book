# Lựa chọn sự kiện không trùng giờ

## Bối cảnh

Đoàn trường tổ chức ngày hội câu lạc bộ nhưng chỉ có đúng một hội trường lớn để dùng chung. Ban tổ chức nhận được $N$ đề xuất hoạt động, mỗi đề xuất xin dùng hội trường từ giờ $L_i$ đến giờ $R_i$. Vì hội trường không thể phục vụ hai hoạt động cùng lúc, ban tổ chức muốn chấp thuận càng nhiều đề xuất càng tốt. Một hoạt động được phép bắt đầu đúng vào giờ hoạt động trước đó vừa kết thúc, vì lúc ấy hội trường đã được dọn xong.

## Nhiệm vụ

Cho $N$ khoảng thời gian $[L_i, R_i]$. Hãy lập trình chọn ra số lượng hoạt động nhiều nhất sao cho không có hai hoạt động nào trùng giờ nhau, rồi in ra số lượng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số đề xuất hoạt động.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $L_i, R_i$ ($0 \le L_i < R_i \le 10^9$), là giờ bắt đầu và giờ kết thúc của một đề xuất.

## Output

- In ra một số nguyên duy nhất là số lượng hoạt động nhiều nhất có thể chấp thuận.

## Sample 1

### Input

```text
3
10 20
12 25
20 30
```

### Output

```text
2
```

### Giải thích

- Ba đề xuất là $[10, 20]$, $[12, 25]$ và $[20, 30]$. Xếp chúng theo giờ kết thúc được đúng thứ tự trên.
- Chọn hoạt động $[10, 20]$ trước vì nó kết thúc sớm nhất, hội trường bận đến giờ $20$.
- Xét hoạt động $[12, 25]$: giờ bắt đầu $12$ còn nằm trong lúc hội trường đang bận (trước giờ $20$) nên phải bỏ qua.
- Xét hoạt động $[20, 30]$: giờ bắt đầu $20$ đúng bằng giờ hội trường vừa trống nên được chấp thuận.
- Tổng cộng chọn được $2$ hoạt động, và không có cách nào chọn được cả $3$ vì hai hoạt động đầu luôn trùng nhau.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le L_i < R_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
