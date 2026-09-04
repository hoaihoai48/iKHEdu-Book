# Xâu Con Chung Của Ba Chuỗi (LCS 3 Strings)

## Bối cảnh
Ba viện nghiên cứu sinh học độc lập cùng giải mã trình tự một đoạn gen kháng bệnh ở ba giống cây trồng khác nhau, thu được 3 chuỗi ADN ký hiệu là $S_1, S_2$ và $S_3$. Để xác định đoạn gen chung cốt lõi quy định tính trạng kháng bệnh, các nhà khoa học cần tìm độ dài của chuỗi con chung dài nhất xuất hiện đồng thời trong cả ba chuỗi ADN.

## Nhiệm vụ
Cho ba chuỗi ký tự $S_1, S_2$ và $S_3$. Hãy lập trình tính độ dài chuỗi con chung dài nhất của cả ba chuỗi.

## Input
- Dòng 1: Chứa chuỗi ký tự $S_1$ ($1 \le |S_1| \le 100$).
- Dòng 2: Chứa chuỗi ký tự $S_2$ ($1 \le |S_2| \le 100$).
- Dòng 3: Chứa chuỗi ký tự $S_3$ ($1 \le |S_3| \le 100$).

## Output
- In ra trên một dòng duy nhất một số nguyên là độ dài xâu con chung dài nhất của 3 chuỗi.

## Sample 1
### Input
```text
geeks
geek
geekfor
```
### Output
```text
4
```

### Giải thích
Với 3 chuỗi ký tự:
$S_1 = \text{"geeks"}$, $S_2 = \text{"geeksfor"}$, $S_3 = \text{"geeksforgeeks"}$:
Chuỗi con chung dài nhất xuất hiện trong cả 3 chuỗi là $\text{"geeks"}$ với độ dài bằng 5.

## Ràng buộc
- $100\%$ số test có $1 \le |S_i| \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
