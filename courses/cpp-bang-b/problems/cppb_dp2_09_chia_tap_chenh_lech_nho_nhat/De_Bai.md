# Chia Tập Chênh Lệch Nhỏ Nhất (Minimum Subset Sum Difference)

## Bối cảnh
Trong một giải đấu thể thao điện tử (E-sports), có $N$ tuyển thủ tham dự với chỉ số kỹ năng lần lượt là $A_1, A_2, \dots, A_N$. Ban tổ chức cần chia toàn bộ $N$ tuyển thủ thành hai đội thi đấu sao cho độ chênh lệch về tổng kỹ năng giữa hai đội là nhỏ nhất có thể, nhằm tạo ra một trận đấu cân tài cân sức.

## Nhiệm vụ
Cho danh sách điểm kỹ năng của $N$ tuyển thủ. Hãy lập trình tìm độ chênh lệch nhỏ nhất giữa tổng điểm của hai đội.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 200$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).

## Output
- In ra trên một dòng duy nhất một số nguyên là độ chênh lệch nhỏ nhất có thể đạt được.

## Sample 1
### Input
```text
4
1 6 11 5
```
### Output
```text
1
```

### Giải thích
Với tập hợp kỹ năng $[1, 6, 11, 5]$:
Tổng toàn bộ kỹ năng là $1 + 6 + 11 + 5 = 23$. Ta chia thành hai đội với các tuyển thủ $\{1, 11\}$ (tổng kỹ năng 12) và $\{6, 5\}$ (tổng kỹ năng 11). Độ chênh lệch giữa hai đội là $|12 - 11| = 1$. Đây là mức chênh lệch nhỏ nhất.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 500, 1 \le A_i \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
