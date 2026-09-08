# Khoảng Cách Chỉnh Sửa (Edit Distance / Levenshtein)

## Bối cảnh
Trong tính năng gợi ý tự động sửa lỗi chính tả của bàn phím thông minh, khi người dùng gõ nhầm một từ, máy tính cần tìm khoảng cách biến đổi tối thiểu từ chuỗi người dùng gõ thành chuỗi từ điển chuẩn. Có 3 thao tác chỉnh sửa ký tự cơ bản được hỗ trợ: chèn thêm 1 ký tự, xóa bớt 1 ký tự, hoặc thay thế 1 ký tự bằng 1 ký tự khác. Mỗi thao tác đều có chi phí là 1 đơn vị.

## Nhiệm vụ
Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm số lượng thao tác chỉnh sửa ít nhất để biến đổi chuỗi $S$ thành chuỗi $T$.

## Input
- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chứa chuỗi ký tự $T$ ($1 \le |T| \le 2000$).

## Output
- In ra trên một dòng duy nhất số thao tác chỉnh sửa ít nhất cần dùng.

## Sample 1
### Input
```text
horse
ros
```
### Output
```text
3
```

### Giải thích
Để biến đổi chuỗi $S = \text{"kitten"}$ thành $T = \text{"sitting"}$:

1. Thay thế ký tự 'k' thành 's' $\to \text{"sitten"}$.
2. Thay thế ký tự 'e' thành 'i' $\to \text{"sittin"}$.
3. Chèn thêm ký tự 'g' vào cuối $\to \text{"sitting"}$.
Tổng cộng cần đúng 3 thao tác chỉnh sửa, kết quả là 3.

## Ràng buộc
- $100\%$ số test có $1 \le |S|, |T| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
