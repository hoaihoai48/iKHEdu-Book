# Xóa Ký Tự Trùng Lặp Liền Kề

## Bối cảnh
Một trò chơi xếp chữ tương tác có quy tắc: Khi hai ký tự giống hệt nhau đứng sát cạnh nhau trong chuỗi, chúng sẽ tự động va chạm và cùng biến mất. Sau khi hai ký tự đó biến mất, hai phần còn lại của chuỗi sẽ dồn sát vào nhau và nếu lại tạo ra hai ký tự giống nhau kề nhau thì quá trình triệt tiêu lại tiếp tục diễn ra cho đến khi không còn cặp ký tự kề nhau nào giống nhau.

## Nhiệm vụ
Cho chuỗi ký tự $S$. Hãy lập trình xác định chuỗi ký tự cuối cùng thu được sau khi tất cả các cặp trùng lặp liền kề đã bị triệt tiêu hoàn toàn.

## Input
- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 10^5$).

## Output
- In ra chuỗi ký tự còn lại sau khi triệt tiêu. Nếu chuỗi bị triệt tiêu hết, in ra chuỗi rỗng hoặc thông báo quy định.

## Sample 1
### Input
```text
abbaca
```
### Output
```text
ca
```

### Giải thích
Với chuỗi $S = \text{"abbaca"}$:
1. Cặp "bb" ở giữa triệt tiêu $\to$ chuỗi còn lại là "aaca".
2. Cặp "aa" mới tạo thành kề nhau lại tiếp tục triệt tiêu $\to$ chuỗi còn lại là "ca".
Không còn cặp nào trùng nhau kề nhau, chuỗi kết quả in ra là ca.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
