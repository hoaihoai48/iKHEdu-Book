# Tarjan tìm thành phần liên thông mạnh

## Bối cảnh

Sàn thương mại điện tử phân tích N gian hàng với M lượt giới thiệu sản phẩm lẫn nhau theo hướng một chiều trong tháng khuyến mãi lớn nhất năm. Ban marketing muốn gom các gian hàng thành từng cụm mà trong đó gian nào cũng có thể dẫn khách tới gian nào qua chuỗi giới thiệu để thiết kế combo bán chéo hiệu quả. Chương trình cần đếm số cụm liên thông mạnh bằng thuật toán Tarjan trong thời gian tuyến tính.

## Nhiệm vụ

Cho đồ thị có hướng gồm $N$ đỉnh và $M$ cạnh. Hãy lập trình đếm số thành phần liên thông mạnh bằng thuật toán Tarjan, rồi in ra kết quả.

## Input

- Dòng 1: hai số nguyên $N, M$ ($1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v$ là cạnh có hướng $u \to v$.

## Output

- In ra một dòng duy nhất là số thành phần liên thông mạnh.

## Sample 1

### Input

```text
4 4
1 2
2 1
2 3
3 4
```

### Output

```text
3
```

### Giải thích

- Hai gian hàng $1$ và $2$ giới thiệu lẫn nhau nên tạo thành một cụm, còn $3$ và $4$ chỉ có cạnh một chiều đi tới.
- Các cụm là $\{1,2\}$, $\{3\}$, $\{4\}$, tổng $3$ cụm.
- Chương trình in ra $3$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
