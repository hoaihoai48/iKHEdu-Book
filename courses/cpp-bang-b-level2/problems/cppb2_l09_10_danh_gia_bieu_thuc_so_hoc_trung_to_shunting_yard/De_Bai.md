# Đánh giá biểu thức số học trung tố (shunting-yard)

## Bối cảnh

Em học sinh lớp năm vừa học xong thứ tự thực hiện phép tính và muốn kiểm tra lại các bài tập về nhà bằng một chương trình máy tính tự viết. Mỗi bài tập là một biểu thức gồm các số nguyên, phép cộng trừ nhân và các cặp ngoặc đơn để nhóm phép tính. Quy tắc tính đúng là thực hiện trong ngoặc trước, rồi đến nhân, cuối cùng mới cộng trừ từ trái sang phải.

## Nhiệm vụ

Cho một biểu thức số học gồm các số nguyên không âm, các phép toán `+`, `-`, `*` và các cặp ngoặc đơn (không có dấu cách). Hãy lập trình tính giá trị của biểu thức theo đúng thứ tự ưu tiên (ngoặc trước, nhân trước cộng trừ, cùng mức từ trái sang phải), rồi in ra kết quả.

## Input

- Dòng đầu tiên chứa chuỗi $s$ ($1 \le |s| \le 1000$) là biểu thức cần tính, chỉ gồm chữ số, `+`, `-`, `*`, `(`, `)`. Biểu thức hợp lệ và kết quả trung gian vừa trong số nguyên 64 bit.

## Output

- In ra một số nguyên duy nhất là giá trị của biểu thức.

## Sample 1

### Input

```text
2*(3+4)-5
```

### Output

```text
9
```

### Giải thích

- Tính trong ngoặc trước: $3 + 4 = 7$, biểu thức còn $2 * 7 - 5$.
- Thực hiện phép nhân trước phép trừ: $2 * 7 = 14$, biểu thức còn $14 - 5$.
- Thực hiện phép trừ cuối cùng: $14 - 5 = 9$.

## Ràng buộc

- $1 \le |s| \le 1000$, biểu thức hợp lệ, giá trị trung gian trong phạm vi 64 bit.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
