# Truy Vấn Tổng Đoạn Con 1D

## Bối cảnh
Cho một dãy số nguyên gồm $N$ phần tử $A_1, A_2, \dots, A_N$. Bạn cần trả lời $Q$ câu hỏi, mỗi câu hỏi yêu cầu tính tổng các phần tử trong đoạn từ vị trí $L$ đến vị trí $R$.

## Nhiệm vụ
Hãy sử dụng kỹ thuật mảng tiền tố (Prefix Sum) để trả lời tất cả $Q$ truy vấn trong thời gian tối ưu $\mathcal{O}(1)$ cho mỗi truy vấn.

## Input
- Dòng 1: Gồm 2 số nguyên dương $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Gồm $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L, R$ ($1 \le L \le R \le N$).

## Output
- In ra $Q$ dòng, mỗi dòng là một số nguyên biểu diễn tổng đoạn $[L \dots R]$ tương ứng.

## Sample 1
### Input
```text
5 3
2 4 1 5 3
1 3
2 4
1 5
```
### Output
```text
7
10
15
```

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5, |A_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
