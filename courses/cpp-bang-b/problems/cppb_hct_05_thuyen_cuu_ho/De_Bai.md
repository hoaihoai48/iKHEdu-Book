# Ghép Thuyền Cứu Hộ Tối Ưu

## Bối cảnh
Trong một đợt cứu hộ bão lụt khẩn cấp, đội cứu nạn tiếp cận một khu dân cư có N người dân cần di tản qua sông an toàn. Mỗi người thứ i có cân nặng Wi. Lực lượng cứu nạn trang bị loại xuồng cứu hộ chuyên dụng: mỗi chiếc xuồng chỉ có thể chở tối đa 2 người và tổng trọng lượng của hai người trên cùng một xuồng không được vượt quá tải trọng định mức C. Để tiết kiệm phương tiện và thời gian cứu nạn, chỉ huy cần tìm số lượng xuồng cứu hộ ít nhất cần dùng.

## Nhiệm vụ
Cho cân nặng của N người và tải trọng tối đa C của thuyền. Biết mỗi thuyền chở tối đa 2 người và tổng cân nặng không vượt quá C. Hãy tìm số lượng thuyền ít nhất để chở hết toàn bộ N người sang sông.

## Input
- Dòng 1: 2 số nguyên $N$ và $C$ ($1 \le N \le 10^5, 1 \le C \le 10^9$).
- Dòng 2: $N$ số nguyên $W_1, W_2, \dots, W_N$ ($1 \le W_i \le C$).

## Output
- In ra một số nguyên duy nhất là số thuyền ít nhất cần dùng.

## Sample 1
### Input
```text
4 50
30 20 40 50
```
### Output
```text
3
```
### Giải thích
Sắp xếp cân nặng 4 người tăng dần: [20, 30, 40, 50] với tải trọng C = 50. Người nặng 50 kg bắt buộc phải đi một mình 1 thuyền (tốn 1 thuyền). Người nặng 40 kg không thể ghép với ai (vì 40 + 20 = 60 > 50) nên cũng đi một mình 1 thuyền (tốn thêm 1 thuyền). Hai người còn lại có cân nặng 20 kg và 30 kg ghép chung 1 thuyền vì 20 + 30 = 50 <= 50 (tốn 1 thuyền). Tổng số thuyền ít nhất cần dùng là 1 + 1 + 1 = 3 thuyền.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, C \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
