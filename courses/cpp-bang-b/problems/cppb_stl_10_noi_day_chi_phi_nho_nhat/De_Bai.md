# Nối Dây Chi Phí Nhỏ Nhất (Huffman Greedy)

## Bối cảnh
Trong một xưởng cơ khí viễn thông, có $N$ đoạn cáp quang rời rạc với chiều dài lần lượt là $L_1, L_2, \dots, L_N$. Công nhân cần hàn nối tất cả các đoạn cáp này lại thành một sợi cáp duy nhất dài liên tục. Mỗi lần hàn nối hai sợi cáp bất kỳ có chiều dài $x$ và $y$, chi phí điện năng tiêu hao đúng bằng tổng chiều dài của hai sợi cáp đó ($x + y$). Sợi cáp mới ghép có chiều dài $x + y$ lại được đưa vào tập hợp để tiếp tục nối tiếp.

## Nhiệm vụ
Cho danh sách chiều dài $N$ đoạn cáp. Hãy lập trình tìm thứ tự nối cáp sao cho tổng chi phí hàn nối là nhỏ nhất có thể.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên dương $L_1, L_2, \dots, L_N$ ($1 \le L_i \le 10^4$).

## Output
- In ra trên một dòng duy nhất tổng chi phí nhỏ nhất tìm được.

## Sample 1
### Input
```text
4
4 3 2 6
```
### Output
```text
29
```

### Giải thích
Với 4 đoạn dây có độ dài $[4, 3, 2, 6]$:
1. Nối hai dây ngắn nhất 2 và 3 thành dây độ dài 5, chi phí tốn $2 + 3 = 5$. Danh sách dây còn: [4, 5, 6].
2. Nối tiếp hai dây ngắn nhất 4 và 5 thành dây độ dài 9, chi phí tốn $4 + 5 = 9$. Danh sách dây còn: [6, 9].
3. Nối hai dây cuối 6 và 9 thành dây độ dài 15, chi phí tốn $6 + 9 = 15$.
Tổng chi phí nhỏ nhất là $5 + 9 + 15 = 29$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000, 1 \le A_i \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
