# Kiểm tra xâu đối xứng (Palindrome)

## Bối cảnh
Một xâu ký tự được gọi là đối xứng (Palindrome) nếu đọc từ trái sang phải hay từ phải sang trái đều thu được chuỗi ký tự hoàn toàn giống nhau (ví dụ: `radar`, `madam`, `racecar`). Kiểm tra xâu đối xứng là một bài toán kinh điển trong xử lý chuỗi và là tiền đề cho các thuật toán quy hoạch động chuỗi sau này.

## Nhiệm vụ
Cho một xâu ký tự $S$ chỉ gồm các chữ cái tiếng Anh in thường. Hãy viết hàm `bool isPalindrome(const string& s)` để kiểm tra:

- Nếu $S$ là xâu đối xứng, in ra `YES`.
- Nếu $S$ không phải xâu đối xứng, in ra `NO`.

## Input
- Một dòng duy nhất chứa xâu ký tự $S$ ($1 \le |S| \le 10^5$), chỉ gồm các chữ cái in thường không chứa khoảng trắng.

## Output
- In ra một dòng duy nhất chữ `YES` hoặc `NO`.

## Sample 1
### Input
```text
racecar
```
### Output
```text
YES
```

### Giải thích
Xâu `racecar` đọc xuôi hay ngược đều là `racecar`. Kết quả in ra: `YES`.

## Sample 2
### Input
```text
algorithm
```
### Output
```text
NO
```

### Giải thích
Xâu `algorithm` đọc ngược là `mihtirogla`, không trùng khớp với xâu ban đầu. Kết quả: `NO`.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
