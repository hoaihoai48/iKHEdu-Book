# Khớp Chuỗi Ký Tự Đại Diện (Wildcard Matching)

## Bối cảnh
Một công cụ tìm kiếm tệp tin hỗ trợ tìm kiếm theo mẫu (pattern) chứa các ký tự đại diện thông dụng: Ký tự `` có thể khớp với đúng một ký tự bất kỳ, và ký tự `*` có thể khớp với bất kỳ chuỗi ký tự nào (kể cả chuỗi rỗng). Quản trị viên cần kiểm tra xem tên tệp văn bản $S$ có khớp hoàn toàn với mẫu $P$ hay không.

## Nhiệm vụ
Cho chuỗi văn bản $S$ và chuỗi mẫu $P$. Hãy lập trình kiểm tra xem chuỗi $S$ có khớp toàn bộ với mẫu $P$ hay không. Nếu khớp in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa chuỗi văn bản $S$ ($0 \le |S| \le 2000$).
- Dòng 2: Chứa chuỗi mẫu $P$ ($0 \le |P| \le 2000$).

## Output
- In ra `YES` nếu khớp hoàn toàn, ngược lại in ra `NO`.

## Sample 1
### Input
```text
adceb
*a*b
```
### Output
```text
YES
```

### Giải thích
Với văn bản $S = \text{"adceb"}$ và mẫu $P = \text{"*a*b"}$:
Ký tự '*' đầu tiên khớp với chuỗi rỗng, sau đó ký tự 'a' khớp 'a', ký tự '*' thứ hai khớp với đoạn "dce", và cuối cùng ký tự 'b' khớp 'b'. Chuỗi khớp hoàn toàn với mẫu, kết quả in ra là YES.

## Ràng buộc
- $100\%$ số test có $1 \le |S|, |P| \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
