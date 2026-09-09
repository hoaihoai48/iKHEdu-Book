# Lập bảng đếm tần suất các chữ cái thường

## Bối cảnh
Trong cuộc thi đánh vần tiếng Anh, ban tổ chức đưa ra một từ vựng và đố các thí sinh: "Ký tự nào xuất hiện nhiều lần nhất trong từ này và xuất hiện bao nhiêu lần". Bạn hãy lập trình xây dựng bảng đếm tần suất để giải quyết bài toán một cách nhanh chóng và chính xác nhất.

## Nhiệm vụ
Cho một xâu ký tự $S$ chỉ gồm các chữ cái tiếng Anh in thường (`a`–`z`). Hãy lập trình tìm ký tự xuất hiện nhiều nhất cùng số lần xuất hiện của nó. Nếu có nhiều ký tự có cùng số lần xuất hiện lớn nhất, hãy in ra ký tự có thứ tự bảng chữ cái nhỏ nhất.

## Input
- Một dòng duy nhất chứa xâu ký tự $S$ ($1 \le |S| \le 10^5$), chỉ gồm các chữ cái tiếng Anh in thường.

## Output
- In ra trên một dòng duy nhất: ký tự xuất hiện nhiều nhất và số lần xuất hiện, cách nhau bởi một khoảng trắng.

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
Xâu `abracadabra` có 11 ký tự. Thống kê tần suất:

- `a`: xuất hiện $5$ lần.
- `b`: xuất hiện $2$ lần.
- `r`: xuất hiện $2$ lần.
- `c`: xuất hiện $1$ lần.
- `d`: xuất hiện $1$ lần.
Ký tự `a` xuất hiện nhiều nhất ($5$ lần). Kết quả in ra: `a 5`.

## Sample 2
### Input
```text
baab
```
### Output
```text
a 2
```

### Giải thích
Cả `a` và `b` đều xuất hiện $2$ lần. Vì ký tự `a` đứng trước `b` trong bảng chữ cái nên ta chọn `a`.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
