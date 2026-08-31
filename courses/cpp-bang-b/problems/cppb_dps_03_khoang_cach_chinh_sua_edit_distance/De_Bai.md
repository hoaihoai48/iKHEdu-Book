# Khoảng Cách Chỉnh Sửa (Edit Distance / Levenshtein)

## Bối cảnh
Cho hai chuỗi $S$ và $T$. Bạn có thể thực hiện 3 phép biến đổi: Chèn 1 ký tự, Xóa 1 ký tự, hoặc Thay thế 1 ký tự.

## Nhiệm vụ
Tìm số phép biến đổi ít nhất để biến chuỗi $S$ thành chuỗi $T$.

## Input
- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chuỗi $T$ ($1 \le |T| \le 2000$).

## Output
- Số phép biến đổi ít nhất.

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

## Ràng buộc
- $100\%$ số test có $1 \le |S|, |T| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
