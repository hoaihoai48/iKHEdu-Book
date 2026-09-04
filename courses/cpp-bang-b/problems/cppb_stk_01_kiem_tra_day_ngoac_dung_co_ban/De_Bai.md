# Kiểm Tra Dãy Ngoặc Đúng Đơn Loại

## Bối cảnh
Trong một trình biên dịch ngôn ngữ lập trình, việc đóng mở các cặp dấu ngoặc tròn `(` và `)` phải tuân thủ nghiêm ngặt quy tắc ngữ pháp: Mỗi dấu mở ngoặc `(` phải có một dấu đóng ngoặc `)` tương ứng xuất hiện sau nó, và tại mọi thời điểm tính từ đầu chuỗi, số lượng dấu mở ngoặc không bao giờ được ít hơn số lượng dấu đóng ngoặc.

## Nhiệm vụ
Cho một chuỗi chỉ gồm các ký tự `(` và `)`. Hãy lập trình kiểm tra xem chuỗi đó có phải là một dãy ngoặc đúng hay không. Nếu đúng in ra `YES`, ngược lại in ra `NO`.

## Input
- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 10^5$).

## Output
- In ra `YES` nếu chuỗi là dãy ngoặc đúng, ngược lại in ra `NO`.

## Sample 1
### Input
```text
(()())
```
### Output
```text
YES
```

### Giải thích
Với chuỗi $S = \text{"(()())"}$:
Mỗi dấu mở ngoặc đều có đúng một dấu đóng ngoặc tương ứng ghép đôi hợp lệ và không có dấu đóng ngoặc nào bị thừa. Kết quả in ra là YES.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
