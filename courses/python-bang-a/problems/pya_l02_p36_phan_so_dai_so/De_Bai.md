# Tính phân số đại số

## Bối cảnh
Trong phòng thí nghiệm vật lý, hai nhóm học sinh đo được các thông số $a$, $b$, $c$, $d$ từ thí nghiệm đo quang phổ. Công thức tổng hợp kết quả cuối cùng là một biểu thức phân số: $S = \frac{a + b}{c + d}$. Thầy giáo yêu cầu mỗi nhóm viết chương trình Python để tính tự động giá trị $S$, đảm bảo kết quả là số thực (phép chia thực) chứ không phải phép chia nguyên.


## Nhiệm vụ
Nhập 4 số nguyên $a, b, c, d$ trên 1 dòng. In ra giá trị $S$ (làm tròn 2 chữ số thập phân).

## Input
Một dòng chứa 4 số nguyên ($c + d \ne 0$).

## Output
In ra giá trị số thực dạng `f"{S:.2f}"`.

## Sample 1
### Input
```text
7 8 2 3
```
### Output
```text
3.00
```
### Giải thích
$(7 + 8) / (2 + 3) = 15 / 5 = 3.00$.

## Ràng buộc
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
