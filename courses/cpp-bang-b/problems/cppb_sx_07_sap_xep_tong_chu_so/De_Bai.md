# Sắp Xếp Theo Tổng Chữ Số

## Bối cảnh
Trong một trò chơi giải mật mã cổ xưa, người chơi nhận được $N$ phiến đá mang các con số nguyên dương bí ẩn $A_1, A_2, \dots, A_N$. Quy luật mở cánh cổng cổ thành yêu cầu người chơi phải đặt các phiến đá vào rãnh theo thứ tự tăng dần của **tổng các chữ số** cấu thành nên con số đó. Trong trường hợp có nhiều con số có cùng tổng chữ số, phiến đá có giá trị nhỏ hơn sẽ được ưu tiên đặt trước.

## Nhiệm vụ
Cho danh sách $N$ số nguyên dương. Hãy sắp xếp dãy số theo quy tắc:

1. Tổng các chữ số tăng dần.
2. Nếu hai số có cùng tổng các chữ số, số có giá trị nguyên nhỏ hơn sẽ đứng trước.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$) — số lượng phiến đá.
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$) — giá trị ghi trên các phiến đá.

## Output
- In ra dãy số sau khi sắp xếp trên một dòng, các số cách nhau bởi một khoảng trắng.

## Sample 1
### Input
```text
5
13 20 4 103 11
```
### Output
```text
11 20 4 13 103
```
### Giải thích
Tính tổng chữ số của từng số trong dãy ban đầu:

- Số $13$: tổng chữ số là $1 + 3 = 4$.
- Số $20$: tổng chữ số là $2 + 0 = 2$.
- Số $4$: tổng chữ số là $4$.
- Số $103$: tổng chữ số là $1 + 0 + 3 = 4$.
- Số $11$: tổng chữ số là $1 + 1 = 2$.

Sắp xếp theo tổng chữ số tăng dần:

- Nhóm có tổng chữ số bằng $2$: gồm $\{20, 11\}$. Vì $11 < 20$ nên $11$ đứng trước $20$.
- Nhóm có tổng chữ số bằng $4$: gồm $\{13, 4, 103\}$. Sắp xếp theo giá trị tăng dần: $4 < 13 < 103$.

Kết quả cuối cùng: `11 20 4 13 103`.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
