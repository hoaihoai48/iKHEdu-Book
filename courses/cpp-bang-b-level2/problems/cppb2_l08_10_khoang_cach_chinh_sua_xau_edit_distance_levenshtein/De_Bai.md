# Khoảng cách chỉnh sửa xâu (edit distance / levenshtein)

## Bối cảnh

Nhóm biên tập từ điển của nhà xuất bản nhận được hai bản thảo cùng một mục từ do hai cộng tác viên đánh máy độc lập, và hai bản có đôi chỗ khác nhau vì lỗi gõ phím. Để hợp nhất thành một bản duy nhất, nhóm cần biết phải sửa ít nhất bao nhiêu thao tác (thêm một ký tự, xóa một ký tự hoặc thay một ký tự thành ký tự khác) để biến bản này thành bản kia. Số thao tác càng ít thì hai bản thảo càng gần nhau và việc đối chiếu càng nhanh.

## Nhiệm vụ

Cho hai chuỗi $s$ và $t$. Được thực hiện các thao tác: chèn một ký tự, xóa một ký tự, thay thế một ký tự. Hãy lập trình tính số thao tác ít nhất để biến $s$ thành $t$, rồi in ra số đó.

## Input

- Dòng đầu tiên chứa hai chuỗi $s$ và $t$ ($1 \le |s|, |t| \le 1000$), mỗi chuỗi chỉ gồm chữ cái thường.

## Output

- In ra một số nguyên duy nhất là số thao tác ít nhất.

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

- Biến `horse` thành `ros` trong đúng $3$ thao tác: thay `h` thành `r` được `rorse`, xóa `r` ở giữa được `rose`, xóa `e` cuối được `ros`.
- Không thể làm ít hơn $3$ thao tác vì hai chuỗi khác độ dài tới $2$ ký tự (buộc phải xóa ít nhất $2$) mà ký tự đầu `h` và `r` cũng khác nhau (buộc thêm ít nhất $1$ thao tác thay hoặc xóa chèn).

## Ràng buộc

- $1 \le |s|, |t| \le 1000$, chỉ gồm chữ cái thường.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
