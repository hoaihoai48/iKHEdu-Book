# Tổng Cửa Sổ Cố Định K

## Bối cảnh
Một thiết bị quan trắc lượng mưa tự động ghi nhận lượng nước mưa rơi xuống trong N giờ liên tiếp, ký hiệu là A1, A2, ..., An. Trung tâm khí tượng thủy văn cần đánh giá nguy cơ sạt lở bằng cách tìm ra giai đoạn mưa lớn nhất kéo dài đúng K giờ liên tục (tổng lượng mưa lớn nhất trong K giờ liên tiếp) và xác định chỉ số giờ bắt đầu của đợt mưa đó.

## Nhiệm vụ
Cho dãy N số nguyên và số nguyên dương K (K <= N). Hãy tìm đoạn con gồm K phần tử liên tiếp có tổng lớn nhất. In ra tổng lớn nhất và chỉ số bắt đầu (1-indexed) của đoạn con đó. Nếu có nhiều đoạn cùng đạt tổng lớn nhất, in ra chỉ số bắt đầu nhỏ nhất.

## Input
- Dòng 1: Chứa 2 số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra 2 số nguyên trên một dòng cách nhau bởi khoảng trắng: tổng lớn nhất và vị trí bắt đầu.

## Sample 1
### Input
```text
7 3
2 1 5 1 3 2 4
```
### Output
```text
9 3
```
### Giải thích
Các cửa sổ độ dài K = 3 gồm: [2, 1, 5] (tổng 8), [1, 5, 1] (tổng 7), [5, 1, 3] (tổng 9 tại vị trí 3), [1, 3, 2] (tổng 6), [3, 2, 4] (tổng 9 tại vị trí 5). Tổng lớn nhất là 9, đạt được sớm nhất tại vị trí bắt đầu 3. Kết quả in ra: 9 3.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
