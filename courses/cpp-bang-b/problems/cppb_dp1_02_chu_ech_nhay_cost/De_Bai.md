# Chú Ếch Nhảy Chi Phí Nhỏ Nhất

## Bối cảnh
Trong một khu vườn sinh thái, có $N$ phiến đá được xếp thành hàng ngang từ trái sang phải, đánh số thứ tự từ $1$ đến $N$. Phiến đá thứ $i$ có độ cao là $H_i$. Một chú ếch đang ở phiến đá số $1$ và muốn di chuyển tới phiến đá cuối cùng số $N$. Từ phiến đá số $i$, chú ếch có thể chọn nhảy sang phiến đá ngay cạnh $i + 1$ hoặc nhảy vượt qua một phiến để tới phiến đá $i + 2$. Năng lượng tiêu hao (chi phí) cho mỗi cú nhảy từ phiến đá $i$ sang phiến đá $j$ đúng bằng độ chênh lệch chiều cao giữa hai phiến đá, tức $|H_i - H_j|$.

## Nhiệm vụ
Cho số lượng phiến đá $N$ và độ cao của từng phiến đá. Hãy lập trình tìm tổng chi phí năng lượng tối thiểu để chú ếch có thể di chuyển từ phiến đá $1$ tới phiến đá $N$.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($2 \le N \le 10^5$) biểu diễn số lượng phiến đá.
- Dòng 2: Chứa $N$ số nguyên dương $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^4$) biểu diễn độ cao của các phiến đá, các số cách nhau bởi khoảng trắng.

## Output
- In ra trên một dòng duy nhất một số nguyên là tổng chi phí nhỏ nhất tìm được.

## Sample 1
### Input
```text
4
10 30 40 20
```
### Output
```text
30
```

### Giải thích
Với 4 phiến đá có độ cao lần lượt là $[10, 30, 40, 20]$:

- Bước 1: Từ phiến đá 1 ($H_1 = 10$) nhảy sang phiến đá 2 ($H_2 = 30$), chi phí tiêu hao là $|10 - 30| = 20$.
- Bước 2: Từ phiến đá 2 ($H_2 = 30$) nhảy vượt sang phiến đá 4 ($H_4 = 20$), chi phí tiêu hao là $|30 - 20| = 10$.
Tổng chi phí tiêu hao cho toàn bộ hành trình là $20 + 10 = 30$, đây là phương án tốn ít năng lượng nhất.

## Ràng buộc
- $100\%$ số test có $2 \le N \le 10^5, 1 \le H_i \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
