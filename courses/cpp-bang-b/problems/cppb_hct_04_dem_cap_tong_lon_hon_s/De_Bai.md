# Đếm Cặp Có Tổng Lớn Hơn Hoặc Bằng S

## Bối cảnh
Trong một trò chơi đối kháng trực tuyến, hệ thống cần ghép cặp 2 người chơi trong danh sách N game thủ để tạo thành một đội đặc nhiệm tham gia chiến dịch liên server. Để đội có đủ sức mạnh hoàn thành chiến dịch, tổng điểm chiến lực của hai thành viên trong đội phải đạt từ mức chuẩn S trở lên. Ban quản trị cần tính toán có bao nhiêu cách chọn 2 người chơi thỏa mãn tiêu chuẩn này.

## Nhiệm vụ
Cho mảng gồm N số nguyên và một số nguyên S. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N thỏa mãn: A[i] + A[j] >= S.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 2 \cdot 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

## Sample 1
### Input
```text
5 8
2 5 1 4 3
```
### Output
```text
2
```
### Giải thích
Sắp xếp dãy điểm chiến lực tăng dần: [1, 2, 3, 4, 5]. Các cặp có tổng >= 8 là: cặp (3, 5) có tổng 3 + 5 = 8 >= 8 và cặp (4, 5) có tổng 4 + 5 = 9 >= 8. Tổng cộng có đúng 2 cặp thỏa mãn.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
