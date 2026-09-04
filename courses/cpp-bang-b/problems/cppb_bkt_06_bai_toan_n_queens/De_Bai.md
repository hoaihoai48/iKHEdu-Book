# Bài Toán N-Queens (Đếm Số Cách)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Trên một mạng lưới trạm tiếp sóng an ninh vệ tinh được mô phỏng dưới dạng bàn cờ kích thước $N \times N$, trung tâm chỉ huy cần bố trí $N$ ăng-ten phát sóng siêu cao tần (được biểu diễn như những quân Hậu trong cờ vua). Để các chùm sóng không gây nhiễu chéo lẫn nhau, không được có bất kỳ hai trạm phát nào nằm trên cùng một hàng ngang, cùng một cột dọc hoặc cùng một đường chéo.

## Nhiệm vụ
Cho số nguyên dương $N$. Hãy áp dụng thuật toán Quay lui kết hợp các mảng đánh dấu cột, đường chéo chính và đường chéo phụ để đếm tổng số cách đặt $N$ quân hậu hợp lệ lên bàn cờ $N \times N$.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 12$).

## Output
- In ra một số nguyên duy nhất là tổng số cách xếp $N$ quân hậu thỏa mãn yêu cầu.

## Sample 1
### Input
```text
4
```
### Output
```text
2
```
### Giải thích
Trên bàn cờ kích thước $4 \times 4$, có đúng 2 cấu hình hợp lệ không quân hậu nào khống chế nhau: hàng 1 đặt ở cột 2, hàng 2 cột 4, hàng 3 cột 1, hàng 4 cột 3 (tức `[2, 4, 1, 3]`) và cấu hình đối xứng qua gương `[3, 1, 4, 2]`.

## Ràng buộc
- 100% số test có $1 \le N \le 12$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
