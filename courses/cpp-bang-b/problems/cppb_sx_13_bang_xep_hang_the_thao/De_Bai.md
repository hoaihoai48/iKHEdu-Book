# Bảng Xếp Hạng Giải Đấu Thể Thao

## Bối cảnh
Vòng bảng giải bóng đá thanh thiếu niên quy tụ $N$ đội tuyển tranh tài vừa kết thúc. Ban tổ chức đã tổng hợp đầy đủ các thông số kỹ thuật của từng đội bóng để xác định thứ hạng vào vòng loại trực tiếp, bao gồm: Mã đội $ID$, Điểm số tích lũy $Points$, Hiệu số bàn thắng bại $GoalDiff$ (bàn thắng trừ bàn thua), và Tổng số bàn thắng ghi được $Goals$. Theo điều lệ thi đấu chuẩn quốc tế, bảng xếp hạng phải được phân định dựa trên một chuỗi các chỉ số phụ công bằng.

## Nhiệm vụ
Cho thông số thi đấu của $N$ đội bóng. Hãy xếp hạng các đội theo thứ tự ưu tiên sau:

1. Điểm số tích lũy ($Points$) giảm dần.
2. Nếu bằng điểm số, đội có Hiệu số bàn thắng bại ($GoalDiff$) lớn hơn sẽ đứng trước.
3. Nếu vẫn bằng cả điểm số và hiệu số, đội ghi được Tổng số bàn thắng ($Goals$) nhiều hơn sẽ đứng trước.
4. Nếu cả 3 chỉ số trên đều hoàn toàn bằng nhau, đội có Mã số định danh ($ID$) nhỏ hơn sẽ đứng trước.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$) — số lượng đội bóng.
- $N$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $ID, Points, GoalDiff, Goals$ ($1 \le ID \le 10^9, 0 \le Points, Goals \le 100, -100 \le GoalDiff \le 100$).

## Output
- In ra danh sách mã đội $ID$ sau khi đã sắp xếp hoàn tất thứ hạng từ cao xuống thấp trên một dòng, cách nhau bởi một khoảng trắng.

## Sample 1
### Input
```text
3
1 10 5 12
2 10 5 15
3 12 2 8
```
### Output
```text
3 2 1
```
### Giải thích
Xét thông số của 3 đội bóng:

- Đội 3: có $12$ điểm (cao nhất) $\implies$ xếp vị trí số 1.
- Đội 1 và Đội 2: đều có $10$ điểm và cùng có hiệu số bàn thắng bại là $5$.
- Xét chỉ số phụ số bàn thắng ghi được: Đội 2 ghi được $15$ bàn, trong khi Đội 1 chỉ ghi được $12$ bàn ($15 > 12$).
- Do đó Đội 2 xếp thứ nhì, Đội 1 xếp thứ ba.

Thứ tự mã đội trên bảng xếp hạng là: `3 2 1`.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
