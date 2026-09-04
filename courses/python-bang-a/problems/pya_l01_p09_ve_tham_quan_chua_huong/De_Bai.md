# Vé Tham Quan Chùa Hương


*(Lấy cảm hứng từ Bài 4 Đề thi Tin học trẻ Thị xã Thái Hòa - Nghệ An)*

## Bối cảnh

Cuối tuần này, một đoàn khách nhí nhố chuẩn bị đi tham quan Chùa Hương Tích. Để lên chùa, đoàn phải đi thuyền rồi đi cáp treo ngắm cảnh núi rừng:
  * Vé thuyền: người lớn $a$ nghìn đồng/người, trẻ em $b$ nghìn đồng/người.
  * Vé cáp treo: người lớn $x$ nghìn đồng/người, trẻ em $y$ nghìn đồng/người.
  * Đoàn khách có tổng cộng $n$ người, trong đó có $m$ trẻ em.
Cô hướng dẫn viên cần tính tiền thật nhanh để mua vé cho cả đoàn. Em hãy giúp cô tính tổng số tiền cần chuẩn bị nhé!
## Nhiệm vụ

Em hãy tính tổng số tiền (đơn vị nghìn đồng) cần chuẩn bị để mua toàn bộ vé thuyền và vé cáp treo cho cả đoàn khách.
## Input

Gồm 6 dòng lần lượt chứa các số tự nhiên: $a, b, x, y, n, m$ ($0 < a, b, x, y < 100$; $0 \le m \le n < 100$).
## Output

In ra một số nguyên duy nhất là tổng số tiền cần chuẩn bị.
## Sample 1

### Input
```text
20
10
50
30
10
4
```
### Output
```text
540
```
### Giải thích

- Số trẻ em: $4$, số người lớn: $10 - 4 = 6$ người.
- Tiền thuyền: $6 \times 20 + 4 \times 10 = 120 + 40 = 160$.
- Tiền cáp treo: $6 \times 50 + 4 \times 30 = 300 + 120 = 420$.
- Tổng tiền: $160 + 420 = 580$ nghìn đồng.
## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$