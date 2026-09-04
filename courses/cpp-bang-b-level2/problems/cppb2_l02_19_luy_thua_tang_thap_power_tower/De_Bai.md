# Lũy Thừa Tầng Tháp (Power Tower)

## Bối cảnh
Giải đấu cờ vua tính điểm thưởng theo "tháp lũy thừa" $a^{b^c}$: đội thắng nhận số điểm bằng phần dư của ngọn tháp khi chia cho $m$. Vì ngọn tháp phình to rất nhanh, trọng tài không thể tính trực tiếp mà phải rút gọn từng tầng một.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho bốn số $a, b, c, m$. Hãy lập trình tính tháp lũy thừa $a^{b^c} \bmod m$.

## Input
- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

## Output
- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Luy Thua Tang Thap Power Tower.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
