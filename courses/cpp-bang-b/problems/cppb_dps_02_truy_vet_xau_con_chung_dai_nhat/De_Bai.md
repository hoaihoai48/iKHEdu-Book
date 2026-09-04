# Truy Vết Xâu Con Chung Dài Nhất

## Bối cảnh
Sau khi tính toán được độ dài tương đồng giữa hai chuỗi văn bản, hệ thống kiểm tra đạo văn cần trích xuất chính xác chuỗi ký tự chung dài nhất đó để làm bằng chứng đánh dấu nổi bật (highlight) trên giao diện phần mềm cho người thẩm định theo dõi.

## Nhiệm vụ
Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm và in ra xâu con chung dài nhất của hai chuỗi. Nếu có nhiều xâu con chung cùng đạt độ dài lớn nhất, in ra một xâu bất kỳ thỏa mãn.

## Input
- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chứa chuỗi ký tự $T$ ($1 \le |T| \le 2000$).

## Output
- In ra trên một dòng duy nhất xâu con chung dài nhất tìm được.

## Sample 1
### Input
```text
ABCBDAB
BDCAB
```
### Output
```text
4
BDAB
```

### Giải thích
Với hai xâu $S = \text{"ABCBDAB"}$ và $T = \text{"BDCAB"}$:
Xâu con chung dài nhất đồng thời xuất hiện trong cả hai xâu là $\text{"BCAB"}$ với độ dài là 4. Kết quả in ra chuỗi BCAB.

## Ràng buộc
- $100\%$ số test có $1 \le |S|, |T| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
