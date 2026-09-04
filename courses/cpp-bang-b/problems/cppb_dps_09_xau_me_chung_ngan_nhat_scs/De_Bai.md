# Xâu Mẹ Chung Ngắn Nhất (Shortest Common Supersequence)

## Bối cảnh
Một máy phát tín hiệu cần gửi một chuỗi mã nguồn sao cho máy thu khi nhận được có thể trích xuất ra đồng thời cả hai bản tin $S$ và $T$ dưới dạng các chuỗi con. Để tiết kiệm băng thông truyền dẫn số, độ dài của chuỗi mã phát đi phải là ngắn nhất có thể.

## Nhiệm vụ
Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm độ dài ngắn nhất của một chuỗi chứa cả $S$ và $T$ dưới dạng các chuỗi con.

## Input
- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chứa chuỗi ký tự $T$ ($1 \le |T| \le 2000$).

## Output
- In ra trên một dòng duy nhất độ dài ngắn nhất của xâu mẹ chung.

## Sample 1
### Input
```text
abac
cab
```
### Output
```text
5
```

### Giải thích
Với hai chuỗi $S = \text{"abac"}$ và $T = \text{"cab"}$:
Xâu mẹ chung ngắn nhất chứa cả hai chuỗi là $\text{"cabac"}$ có độ dài đúng bằng 5 (chứa "cab" ở tiền tố và "abac" ở hậu tố).

## Ràng buộc
- $100\%$ số test có $1 \le |S|, |T| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
