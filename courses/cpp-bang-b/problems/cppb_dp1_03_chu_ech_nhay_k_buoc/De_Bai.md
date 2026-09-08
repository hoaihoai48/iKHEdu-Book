# Chú Ếch Nhảy K Bước

## Bối cảnh
Vẫn tại khu vườn sinh thái có $N$ phiến đá xếp thành hàng ngang với độ cao $H_1, H_2, \dots, H_N$. Lần này chú ếch đã được huấn luyện với thể lực dẻo dai hơn: Từ phiến đá thứ $i$, chú ếch có thể chọn nhảy xa tới bất kỳ phiến đá nào trong phạm vi $K$ bước tiếp theo, tức là các phiến đá $i + 1, i + 2, \dots, \min(N, i + K)$. Chi phí cho mỗi bước nhảy từ phiến đá $i$ tới phiến đá $j$ vẫn bằng độ chênh lệch chiều cao $|H_i - H_j|$.

## Nhiệm vụ
Cho số lượng phiến đá $N$, tầm nhảy tối đa $K$ và danh sách độ cao của các phiến đá. Hãy lập trình tính toán tổng chi phí năng lượng ít nhất để chú ếch đi từ phiến đá $1$ tới phiến đá $N$.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($2 \le N \le 10^5, 1 \le K \le 100$).
- Dòng 2: Chứa $N$ số nguyên dương $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^4$) biểu diễn độ cao của các phiến đá.

## Output
- In ra trên một dòng duy nhất một số nguyên là tổng chi phí năng lượng tối thiểu.

## Sample 1
### Input
```text
5 3
10 30 40 50 20
```
### Output
```text
30
```

### Giải thích
Với $N = 5, K = 3$ và độ cao các phiến đá là $[10, 30, 40, 50, 20]$:

- Từ đá 1 ($H_1 = 10$), chú ếch nhảy sang đá 2 ($H_2 = 30$) với khoảng cách 1 bước hợp lệ ($\le 3$), chi phí là $|10 - 30| = 20$.
- Từ đá 2 ($H_2 = 30$), chú ếch nhảy thẳng tới đích là đá 5 ($H_5 = 20$) với khoảng cách $5 - 2 = 3$ bước (vẫn $\le K = 3$), chi phí là $|30 - 20| = 10$.
Tổng chi phí tối thiểu đạt được là $20 + 10 = 30$.

## Ràng buộc
- $100\%$ số test có $2 \le N \le 10^5, 1 \le K \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
