# Truy Vấn Tổng Đoạn Con 1D

## Bối cảnh
Tại một trạm thu phí cao tốc thông minh, doanh thu thu được theo từng giờ trong ngày được ghi nhận thành dãy N số nguyên A1, A2, ..., An. Ban kiểm toán tài chính thường xuyên gửi Q câu hỏi truy vấn độc lập, mỗi câu hỏi yêu cầu báo cáo tổng doanh thu thu được trong khoảng thời gian từ giờ L đến giờ R.

## Nhiệm vụ
Cho dãy số nguyên gồm N phần tử. Với mỗi truy vấn [L, R] (1 <= L <= R <= N), hãy tính và in ra tổng các phần tử từ chỉ số L đến chỉ số R bằng kỹ thuật Mảng tiền tố.

## Input
- Dòng 1: Chứa 2 số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số nguyên $L$ và $R$ ($1 \le L \le R \le N$).

## Output
- In ra $Q$ dòng, mỗi dòng chứa một số nguyên là kết quả của truy vấn tương ứng.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
1 3
2 4
1 5
```
### Output
```text
6
9
15
```
### Giải thích
Mảng tiền tố Pref = [0, 1, 3, 6, 10, 15].
- Truy vấn [1, 3]: Pref[3] - Pref[0] = 6 - 0 = 6.
- Truy vấn [2, 4]: Pref[4] - Pref[1] = 10 - 1 = 9.
- Truy vấn [1, 5]: Pref[5] - Pref[0] = 15 - 0 = 15.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
