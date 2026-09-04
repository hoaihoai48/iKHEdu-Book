# Dãy Ngoặc Hỗn Hợp Nhiều Loại

## Bối cảnh
Trình biên dịch mã nguồn mở rộng hỗ trợ đồng thời 3 loại cặp dấu ngoặc khác nhau: ngoặc tròn `()`, ngoặc vuông `[]` và ngoặc nhọn `{}`. Một chuỗi ngoặc hỗn hợp được coi là hợp lệ nếu các cặp ngoặc cùng loại được đóng mở đúng quy tắc lồng nhau, không bị đóng chéo (ví dụ: `([)]` là sai quy tắc vì ngoặc tròn mở trước nhưng lại bị ngoặc vuông xen vào đóng trước).

## Nhiệm vụ
Cho chuỗi $S$ chỉ gồm các ký tự `(`, `)`, `[`, `]`, `{`, `}`. Hãy lập trình kiểm tra tính hợp lệ của chuỗi. Nếu hợp lệ in ra `YES`, ngược lại in ra `NO`.

## Input
- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 10^5$).

## Output
- In ra `YES` nếu chuỗi hợp lệ, ngược lại in ra `NO`.

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
Với chuỗi $S = \text{"{[()]}"}$:
Cặp ngoặc tròn nằm hoàn toàn bên trong ngoặc vuông, và ngoặc vuông nằm bên trong ngoặc nhọn. Quy tắc lồng nhau được bảo đảm trọn vẹn, kết quả in ra là YES.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
