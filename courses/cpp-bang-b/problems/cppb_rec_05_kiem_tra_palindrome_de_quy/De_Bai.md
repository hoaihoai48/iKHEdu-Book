# Kiểm Tra Chuỗi Palindrome Bằng Đệ Quy

## Bối cảnh
Trong phân tích chuỗi đối xứng đối xứng sinh học DNA, một chuỗi được gọi là Palindrome nếu đọc xuôi hay đọc ngược đều hoàn toàn như nhau. Cơ chế đệ quy so sánh ký tự đầu và cuối S[L] == S[R] rồi thu hẹp chuỗi con bên trong là phương pháp chuẩn xác.

## Nhiệm vụ
Cho xâu ký tự S gồm các chữ cái in thường. Hãy viết hàm đệ quy isPalindrome(S, L, R) kiểm tra xâu S có phải là Palindrome không. In YES nếu đúng, ngược lại in NO.

## Input
- Một dòng chứa chuỗi ký tự $S$ ($1 \le |S| \le 1000$).

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
radar
```
### Output
```text
YES
```
### Giải thích
Xâu 'radar' đọc xuôi hay đọc ngược đều là 'radar' nên là xâu Palindrome -> in YES.

## Ràng buộc
- $100\%$ số test có $|S| \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
