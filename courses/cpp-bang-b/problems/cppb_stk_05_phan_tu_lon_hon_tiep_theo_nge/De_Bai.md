# Phần Tử Lớn Hơn Tiếp Theo (Next Greater Element)

## Bối cảnh
Một đồ thị phân tích thị trường chứng khoán gồm $N$ mốc thời gian liên tiếp với mức giá cổ phiếu lần lượt là $A_1, A_2, \dots, A_N$. Với mỗi phiên giao dịch tại mốc $i$, nhà phân tích tài chính muốn biết mức giá của phiên giao dịch đầu tiên xuất hiện sau phiên $i$ (bên phải $i$) có giá trị lớn hơn hẳn $A_i$. Nếu từ mốc $i$ về sau không có phiên nào có giá cao hơn, ghi nhận giá trị `-1`.

## Nhiệm vụ
Cho dãy số nguyên $A$ gồm $N$ phần tử. Với mỗi phần tử trong mảng, hãy tìm phần tử đầu tiên nằm bên phải nó có giá trị lớn hơn nó. Nếu không có, gán giá trị `-1`.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng gồm $N$ số nguyên là phần tử lớn hơn tiếp theo tương ứng, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
4
4 5 2 25
```
### Output
```text
5 25 25 -1
```

### Giải thích
Với mảng gồm 4 phần tử $[4, 5, 2, 25]$:
- Phần tử 4: Bên phải phần tử đầu tiên lớn hơn 4 là 5.
- Phần tử 5: Bên phải phần tử đầu tiên lớn hơn 5 là 25.
- Phần tử 2: Bên phải phần tử đầu tiên lớn hơn 2 là 25.
- Phần tử 25: Bên phải không còn số nào lớn hơn 25 $\to$ in ra -1.
Kết quả in ra: 5 25 25 -1.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
