# Lazy Propagation — Cập Nhật & Truy Vấn Đoạn (Range Add Range Sum)

## Bối cảnh
Một tuyến đê biển dài $N$ mét, ban đầu mét đê thứ $i$ có độ cao $A_i$. Do điều kiện thi công đắp đập, công nhân sẽ cộng thêm đồng loạt một lượng phù sa có độ dày $V$ mét vào một đoạn đê liên tiếp từ mét thứ $L$ đến mét thứ $R$. Đồng thời, đoàn thanh tra liên tục kiểm tra tổng độ dày của các đoạn đê bất kỳ.

## Nhiệm vụ
Cho mảng $A$ và $Q$ thao tác: `1 L R V` (cộng $V$ vào tất cả các phần tử từ $L$ đến $R$) và `2 L R` (tính tổng các phần tử trong đoạn $[L, R]$). Hãy in ra kết quả cho các thao tác loại 2.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng chứa một thao tác.

## Output
- Với mỗi thao tác loại 2, in ra tổng các phần tử trên đoạn $[L, R]$ trên một dòng.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
1 2 4 2
2 1 5
2 2 4
```
### Output
```text
21
15
```

### Giải thích
Với mảng ban đầu $[1, 2, 3, 4, 5]$:
- Cộng thêm 2 vào đoạn từ vị trí 2 đến 4: mảng trở thành $[1, 4, 5, 6, 5]$.
- Truy vấn tổng đoạn từ 1 đến 5: $1 + 4 + 5 + 6 + 5 = 21$.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
