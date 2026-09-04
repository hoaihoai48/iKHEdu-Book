# Xâu Con Đối Xứng Dài Nhất (Longest Palindromic Subsequence)

## Bối cảnh
Một chuỗi ký tự được gọi là đối xứng (Palindrome) nếu đọc từ trái sang phải hay từ phải sang trái đều thu được chuỗi hoàn toàn giống nhau (ví dụ: `RADAR`, `MADAM`). Trong phân tích mã vạch bảo mật, ban kỹ thuật muốn trích xuất từ chuỗi gốc một chuỗi con (không nhất thiết liên tiếp) có tính đối xứng sao cho độ dài của nó là lớn nhất.

## Nhiệm vụ
Cho chuỗi ký tự $S$. Hãy lập trình tìm độ dài của chuỗi con đối xứng dài nhất trích xuất được từ $S$.

## Input
- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).

## Output
- In ra trên một dòng duy nhất độ dài của chuỗi con đối xứng dài nhất.

## Sample 1
### Input
```text
bbbab
```
### Output
```text
4
```

### Giải thích
Với chuỗi $S = \text{"BBABCBCAB"}$:
Một chuỗi con đối xứng dài nhất có thể chọn là $\text{"BABCBAB"}$ (hoặc $\text{"BACBCAB"}$) có độ dài bằng 7.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
