# Cặp Số Có Tổng Bằng S (Two Sum)

## Bối cảnh
Tại một trung tâm phân phối năng lượng, người điều hành cần ghép nối đúng 2 bình ắc-quy dự phòng trong kho lưu trữ gồm N bình chưa được sắp xếp sao cho tổng dung lượng tích trữ của hai bình được chọn đạt đúng công suất yêu cầu S. Nếu có nhiều cặp bình thỏa mãn, người điều hành muốn chọn một cặp bất kỳ và in ra dung lượng của 2 bình theo thứ tự tăng dần.

## Nhiệm vụ
Cho một mảng gồm N số nguyên và một số nguyên S. Hãy tìm hai phần tử ở hai vị trí khác nhau trong mảng có tổng đúng bằng S. Nếu có nhiều cặp thỏa mãn, in ra một cặp bất kỳ theo thứ tự tăng dần. Nếu không tồn tại bất kỳ cặp nào, in ra -1.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra 2 số nguyên là giá trị của 2 phần tử tìm được theo thứ tự tăng dần, hoặc `-1` nếu không có nghiệm.

## Sample 1
### Input
```text
5 20
19 2 8 12 5
```
### Output
```text
8 12
```
### Giải thích
Danh sách dung lượng các bình ắc-quy là: 19, 2, 8, 12, 5. Sau khi sắp xếp tăng dần: [2, 5, 8, 12, 19]. Cặp phần tử có giá trị 8 và 12 có tổng là 8 + 12 = 20 đúng bằng S. Kết quả in ra theo thứ tự tăng dần là: 8 12.

## Ràng buộc
- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
