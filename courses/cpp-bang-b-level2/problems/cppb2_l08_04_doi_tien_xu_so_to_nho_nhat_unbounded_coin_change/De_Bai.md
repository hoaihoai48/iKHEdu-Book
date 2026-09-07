# Đổi tiền xu số tờ nhỏ nhất (unbounded coin change)

## Bối cảnh

Cô thu ngân siêu thị cần thối lại cho khách đúng $S$ nghìn đồng bằng số tờ tiền ít nhất có thể, vì quầy đang đông mà trong ngăn kéo có nhiều mệnh giá khác nhau với số lượng mỗi loại coi như không giới hạn. Cô muốn kẹp vào hóa đơn càng ít tờ càng tốt để khách dễ cất ví và hàng người chờ phía sau không phải sốt ruột. Trước khi mở ngăn kéo, cô cần biết với các mệnh giá hiện có thì số tờ ít nhất là bao nhiêu.

## Nhiệm vụ

Cho tổng số tiền $S$ và $N$ mệnh giá tiền, mỗi mệnh giá dùng bao nhiêu tờ tùy ý. Hãy lập trình tính số tờ ít nhất để cộng đúng bằng $S$, rồi in ra số đó. Nếu không thể tạo đúng $S$ thì in ra $-1$.

## Input

- Dòng đầu tiên chứa số nguyên $N$ và số nguyên $S$ ($1 \le N \le 100$, $1 \le S \le 10^4$), là số mệnh giá và số tiền cần thối.
- Dòng thứ hai chứa $N$ số nguyên $c_i$ ($1 \le c_i \le 10^4$), là các mệnh giá tiền.

## Output

- In ra số tờ ít nhất, hoặc $-1$ nếu không thể tạo đúng $S$.

## Sample 1

### Input

```text
3 11
1 5 7
```

### Output

```text
3
```

### Giải thích

- Cần thối đúng $11$ nghìn bằng các tờ mệnh giá $1, 5, 7$.
- Phương án hai tờ $5$ và một tờ $1$ cho tổng $5 + 5 + 1 = 11$ với $3$ tờ.
- Mọi phương án dùng tờ $7$ đều cần thêm ít nhất $4$ tờ $1$ mới đủ $11$ nên tốn tới $5$ tờ.
- Không có cách nào chỉ dùng $1$ hay $2$ tờ vì hai tờ lớn nhất $7 + 7 = 14$ đã vượt quá, nên đáp án là $3$.

## Ràng buộc

- $1 \le N \le 100$, $1 \le S \le 10^4$, $1 \le c_i \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
