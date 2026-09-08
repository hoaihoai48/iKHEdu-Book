# Đếm Ký Tự Trong Xâu

## Bối cảnh
Trong cuộc thi đánh vần, ban tổ chức cho một từ tiếng Anh và hỏi: "Ký tự nào xuất hiện nhiều nhất trong từ này?". Bạn hãy viết chương trình để trả lời nhanh câu hỏi.

## Nhiệm vụ
Cho một xâu ký tự $S$ chỉ gồm các chữ cái thường (`a`–`z`). Hãy lập trình tìm và in ra ký tự xuất hiện nhiều nhất cùng số lần xuất hiện. Nếu có nhiều ký tự cùng tần suất cao nhất, in ra ký tự có thứ tự bảng chữ cái nhỏ nhất.

## Input
- Một dòng duy nhất chứa xâu $S$ ($1 \le |S| \le 10^5$), chỉ gồm chữ cái thường.

## Output
- In ra trên một dòng: ký tự xuất hiện nhiều nhất và số lần xuất hiện, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
abracadabra
```
### Output
```text
a 5
```

### Giải thích
Xâu `abracadabra` có 11 ký tự. Đếm tần suất:
- `a`: xuất hiện $5$ lần (vị trí 0, 3, 5, 7, 10).
- `b`: xuất hiện $2$ lần.
- `r`: xuất hiện $2$ lần.
- `c`: xuất hiện $1$ lần.
- `d`: xuất hiện $1$ lần.
Ký tự `a` xuất hiện nhiều nhất ($5$ lần), nên kết quả là `a 5`.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
