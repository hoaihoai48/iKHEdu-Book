# Tầm Nhìn Tòa Tháp (Stock Span)

## Bối cảnh
Trên một tuyến phố ven biển có $N$ tòa tháp cao tầng xếp thẳng hàng từ trái sang phải, tòa tháp thứ $i$ có chiều cao $H_i$. Tầm nhìn về phía sau của một tòa tháp $i$ được định nghĩa là số lượng tòa tháp liên tiếp nằm ngay bên trái nó (tính cả chính nó) mà có chiều cao nhỏ hơn hoặc bằng $H_i$.

## Nhiệm vụ
Cho danh sách chiều cao của $N$ tòa tháp. Hãy lập trình tính tầm nhìn cho từng tòa tháp trong dãy.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên dương $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^9$).

## Output
- In ra trên một dòng gồm $N$ số nguyên là tầm nhìn tương ứng của từng tòa tháp, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
7
100 80 60 70 60 75 85
```
### Output
```text
1 1 1 2 1 4 6
```

### Giải thích
Với chiều cao các tháp $[100, 80, 60, 70, 60, 75, 85]$:
- Tháp 1 (100): tầm nhìn 1 (chính nó).
- Tháp 2 (80): tầm nhìn 1.
- Tháp 3 (60): tầm nhìn 1.
- Tháp 4 (70): bao trùm tháp 60 và chính nó $\to$ tầm nhìn 2.
- Tháp 5 (60): tầm nhìn 1.
- Tháp 6 (75): bao trùm tháp 60, 70, 60 và chính nó $\to$ tầm nhìn 4.
- Tháp 7 (85): bao trùm tất cả các tháp trừ tháp 100 $\to$ tầm nhìn 6.
Kết quả in ra: 1 1 1 2 1 4 6.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le H_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
