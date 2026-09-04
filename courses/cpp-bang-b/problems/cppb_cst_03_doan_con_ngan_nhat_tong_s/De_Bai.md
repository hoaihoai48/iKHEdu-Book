# Đoạn Con Ngắn Nhất Có Tổng Đạt S

## Bối cảnh
Một vận động viên cử tạ thực hiện N hiệp nâng tạ trong tuần với khối lượng tích lũy mỗi hiệp là các số không âm A1, A2, ..., An. Huấn luyện viên đặt ra chỉ tiêu thành tích là phải đạt tổng khối lượng nâng tối thiểu S trong một chuỗi các hiệp thi đấu liên tiếp. Để tiết kiệm thể lực, vận động viên muốn tìm chuỗi hiệp đấu ngắn nhất (số lượng hiệp ít nhất) đạt được tổng chỉ tiêu S.

## Nhiệm vụ
Cho dãy gồm N số nguyên không âm A1, A2, ..., An và số nguyên dương S. Hãy tìm độ dài nhỏ nhất của một đoạn con liên tiếp có tổng lớn hơn hoặc bằng S. Nếu không tồn tại đoạn con nào thỏa mãn, in ra 0.

## Input
- Dòng 1: Chứa 2 số nguyên dương $N$ và $S$ ($1 \le N \le 10^5, 1 \le S \le 10^{14}$).
- Dòng 2: Chứa $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là độ dài nhỏ nhất tìm được, hoặc `0` nếu không thể đạt tổng $S$.

## Sample 1
### Input
```text
6 7
2 3 1 2 4 3
```
### Output
```text
2
```
### Giải thích
Đoạn con [4, 3] ở cuối dãy có tổng là 4 + 3 = 7 >= 7 và có độ dài bằng 2. Không tồn tại bất kỳ phần tử đơn lẻ nào có giá trị >= 7. Vì vậy độ dài nhỏ nhất đạt chỉ tiêu là 2.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, S \le 10^{14}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
