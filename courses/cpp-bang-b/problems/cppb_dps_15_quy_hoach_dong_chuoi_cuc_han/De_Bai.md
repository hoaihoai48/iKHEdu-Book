# Tách Từ Trong Chuỗi (Word Break)

## Bối cảnh
Một hệ thống nhận dạng quang học chữ viết (OCR) quét văn bản tiếng Anh cổ nhưng do lỗi khoảng cách, tất cả các từ trong câu bị dính liền thành một chuỗi ký tự duy nhất $S$. Cho trước một cuốn từ điển gồm $N$ từ vựng chuẩn. Kỹ sư ngôn ngữ cần xác định xem chuỗi ký tự dính liền $S$ có thể được phân tách thành một chuỗi các từ hợp lệ nằm trong cuốn từ điển hay không.

## Nhiệm vụ
Cho chuỗi ký tự $S$ và từ điển gồm $N$ từ. Hãy lập trình kiểm tra xem chuỗi $S$ có thể được phân tách hoàn toàn thành các từ trong từ điển hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 300$).
- Dòng 2: Chứa số nguyên dương $N$ ($1 \le N \le 1000$) là số lượng từ trong từ điển.
- $N$ dòng tiếp theo, mỗi dòng chứa một từ trong từ điển có độ dài không quá 20 ký tự.

## Output
- In ra `YES` nếu chuỗi có thể phân tách hợp lệ, ngược lại in ra `NO`.

## Sample 1
### Input
```text
leetcode
2
leet
code
```
### Output
```text
YES
```

### Giải thích
Với chuỗi $S = \text{"leetcode"}$ và từ điển gồm các từ {"leet", "code"}:
Chuỗi $S$ có thể phân tách thành hai từ hợp lệ là "leet" và "code". Cả hai từ đều có mặt trong từ điển, do đó kết quả in ra là YES.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 300, 1 \le K \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
