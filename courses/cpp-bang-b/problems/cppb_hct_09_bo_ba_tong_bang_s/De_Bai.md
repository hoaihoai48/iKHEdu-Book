# Bộ Ba Số Có Tổng Bằng S (3-Sum)

## Bối cảnh
Trong một trò chơi tam giác ma thuật trên truyền hình, ban tổ chức đưa ra N viên xúc xắc khắc các số nguyên khác nhau. Người chơi cần chọn ra đúng 3 viên xúc xắc ở 3 vị trí phân biệt sao cho tổng các mặt số ghi trên 3 viên xúc xắc đúng bằng con số mục tiêu S do ban giám khảo chỉ định. Nếu có nhiều bộ ba thỏa mãn, người chơi chỉ cần công bố một bộ bất kỳ theo thứ tự giá trị tăng dần.

## Nhiệm vụ
Cho mảng gồm N số nguyên và một số nguyên S. Hãy tìm 3 phần tử ở 3 vị trí phân biệt trong mảng có tổng đúng bằng S. Nếu có nhiều bộ, in ra một bộ bất kỳ theo thứ tự tăng dần. Nếu không tồn tại, in ra -1.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($3 \le N \le 3000, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra 3 số nguyên theo thứ tự tăng dần, hoặc `-1`.

## Sample 1
### Input
```text
6 15
2 7 5 1 8 4
```
### Output
```text
2 5 8
```
### Giải thích
Sắp xếp mảng tăng dần: [1, 2, 4, 5, 7, 8] với mục tiêu S = 15. Cố định phần tử đầu tiên là 2, ta cần tìm hai phần tử còn lại có tổng là 15 - 2 = 13. Sử dụng hai con trỏ trên đoạn còn lại [4, 5, 7, 8], ta tìm được cặp (5, 8) có 5 + 8 = 13. Do đó bộ ba số tìm được là 2, 5, 8 thỏa mãn 2 + 5 + 8 = 15. Kết quả in ra: 2 5 8.

## Ràng buộc
- $100\%$ số test có $N \le 3000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
