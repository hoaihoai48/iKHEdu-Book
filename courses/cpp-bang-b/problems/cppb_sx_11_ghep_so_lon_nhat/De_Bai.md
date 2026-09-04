# Ghép Chuỗi Tạo Số Lớn Nhất

## Bối cảnh
Tại một triển lãm công nghệ robot tương tác, một thiết bị điều khiển cần thiết lập mã khóa bảo mật cấp cao bằng cách ghép $N$ mảnh thẻ từ chứa các chữ số $S_1, S_2, \dots, S_N$. Mỗi mảnh thẻ là một chuỗi ký tự số không âm. Để hệ thống đạt mức bảo mật tối đa, mã số cuối cùng thu được sau khi ghép toàn bộ $N$ mảnh thẻ lại với nhau thành một con số duy nhất phải là số có giá trị lớn nhất có thể.

## Nhiệm vụ
Cho danh sách $N$ chuỗi số nguyên không âm. Hãy tìm cách sắp xếp và ghép nối toàn bộ $N$ chuỗi số này lại với nhau để tạo thành một số có giá trị lớn nhất.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^4$) — số lượng chuỗi số.
- Dòng 2: $N$ chuỗi số $S_1, S_2, \dots, S_N$ (độ dài mỗi chuỗi không quá 10 ký tự).

## Output
- In ra chuỗi số lớn nhất có thể tạo được. Nếu kết quả chỉ gồm toàn các chữ số $0$, chỉ cần in ra đúng một chữ số `0`.

## Sample 1
### Input
```text
4
3 30 34 5
```
### Output
```text
534330
```
### Giải thích
Xét 4 mảnh thẻ: `"3"`, `"30"`, `"34"`, `"5"`.
- Khi so sánh giữa `"3"` và `"30"`, ghép `"3" + "30" = "330"`, còn `"30" + "3" = "303"`. Vì `"330" > "303"` nên `"3"` phải đứng trước `"30"`.
- Tương tự, `"34" + "3" = "343"` lớn hơn `"3" + "34" = "334"`, nên `"34"` phải đứng trước `"3"`.
- Mảnh `"5"` khi ghép với bất kỳ mảnh nào khác ở đầu luôn tạo ra tiền tố $5...$ lớn nhất.

Thứ tự ghép tối ưu từ trước ra sau là: `"5"`, `"34"`, `"3"`, `"30"`.
Chuỗi kết quả thu được là `534330`.

## Ràng buộc
- $100\%$ số test có $N \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
