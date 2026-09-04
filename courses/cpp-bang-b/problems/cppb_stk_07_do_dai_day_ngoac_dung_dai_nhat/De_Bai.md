# Độ Dài Đoạn Ngoặc Đúng Liên Tiếp Dài Nhất

## Bối cảnh
Trong một chuỗi ký tự ngoặc hỗn độn bị lỗi truyền dẫn, kỹ sư phần mềm muốn khôi phục lại phần thông điệp hợp lệ dài nhất. Hãy tìm độ dài của một đoạn con liên tiếp dài nhất trong chuỗi sao cho đoạn con đó tạo thành một dãy ngoặc đúng hoàn chỉnh.

## Nhiệm vụ
Cho chuỗi $S$ chỉ gồm các ký tự `(` và `)`. Hãy lập trình tìm độ dài lớn nhất của một đoạn con liên tiếp là dãy ngoặc đúng.

## Input
- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 10^5$).

## Output
- In ra trên một dòng duy nhất một số nguyên là độ dài lớn nhất của đoạn ngoặc đúng liên tiếp.

## Sample 1
### Input
```text
)()())
```
### Output
```text
4
```

### Giải thích
Với chuỗi $S = \text{")()())"}$:
Đoạn con liên tiếp bắt đầu từ vị trí 1 đến vị trí 4 là "()()" tạo thành dãy ngoặc đúng hoàn chỉnh có độ dài bằng 4. Đây là đoạn ngoặc đúng dài nhất.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
