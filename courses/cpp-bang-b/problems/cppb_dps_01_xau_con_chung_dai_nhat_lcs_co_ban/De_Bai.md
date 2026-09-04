# Xâu Con Chung Dài Nhất Cơ Bản (LCS)

## Bối cảnh
Trong lĩnh vực xử lý ngôn ngữ tự nhiên và kiểm tra đạo văn số học, hai văn bản số được chuyển hóa thành hai chuỗi ký tự $S$ và $T$. Một chuỗi con chung là một chuỗi các ký tự cùng xuất hiện trong cả hai văn bản theo đúng thứ tự tương đối ban đầu nhưng không nhất thiết phải đứng liền kề nhau. Các nhà nghiên cứu cần xác định độ dài chuỗi con chung dài nhất giữa hai văn bản để đo lường mức độ tương đồng nội dung.

## Nhiệm vụ
Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm độ dài của xâu con chung dài nhất của hai chuỗi đó.

## Input
- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chứa chuỗi ký tự $T$ ($1 \le |T| \le 2000$).
Các chuỗi chỉ chứa các ký tự chữ cái tiếng Anh in hoa hoặc in thường.

## Output
- In ra trên một dòng duy nhất một số nguyên là độ dài xâu con chung dài nhất.

## Sample 1
### Input
```text
AGGTAB
GXTXAYB
```
### Output
```text
4
```

### Giải thích
Với hai xâu $S = \text{"ABCBDAB"}$ và $T = \text{"BDCAB"}$:
Xâu con chung dài nhất có thể tìm được là $\text{"BCAB"}$ (hoặc $\text{"BDAB"}$) có độ dài đúng bằng 4.

## Ràng buộc
- $100\%$ số test có $1 \le |S|, |T| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
