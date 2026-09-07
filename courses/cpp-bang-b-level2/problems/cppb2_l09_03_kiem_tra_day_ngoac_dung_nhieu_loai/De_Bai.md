# Kiểm tra dãy ngoặc đúng nhiều loại

## Bối cảnh

Bạn Mai đang học lập trình và viết ra một biểu thức gồm nhiều loại dấu ngoặc tròn, vuông, nhọn để thử trình biên dịch tự viết. Trước khi cho chương trình chạy, bạn muốn kiểm tra xem dãy ngoặc trong biểu thức có cân bằng hay không: mỗi ngoặc mở phải có đúng một ngoặc đóng cùng loại khép lại, và các cặp ngoặc phải lồng nhau đúng thứ tự chứ không được cắt ngang nhau. Một dãy đạt cả hai điều kiện được gọi là dãy ngoặc đúng.

## Nhiệm vụ

Cho một chuỗi chỉ gồm các ký tự `(`, `)`, `[`, `]`, `{`, `}`. Hãy lập trình kiểm tra xem chuỗi có phải là dãy ngoặc đúng hay không, rồi in ra `YES` nếu đúng và `NO` nếu sai. Chuỗi rỗng được coi là đúng.

## Input

- Dòng đầu tiên chứa chuỗi $s$ ($0 \le |s| \le 10^5$) chỉ gồm sáu loại ký tự ngoặc kể trên.

## Output

- In ra `YES` nếu là dãy ngoặc đúng, ngược lại in ra `NO`.

## Sample 1

### Input

```text
{[()]}
```

### Output

```text
YES
```

### Giải thích

- Đọc từng ký tự từ trái sang: gặp `{`, `[`, `(` là ngoặc mở nên tạm giữ lại theo thứ tự.
- Gặp `)` khớp với `(` giữ gần nhất nên loại cặp này ra.
- Gặp `]` khớp với `[` giữ gần nhất nên loại tiếp, rồi `}` khớp với `{` loại nốt.
- Mọi ngoặc đều có cặp khớp đúng thứ tự lồng nhau nên chuỗi là dãy ngoặc đúng, đáp án `YES`.

## Ràng buộc

- $0 \le |s| \le 10^5$, $s$ chỉ gồm `(`, `)`, `[`, `]`, `{`, `}`.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
