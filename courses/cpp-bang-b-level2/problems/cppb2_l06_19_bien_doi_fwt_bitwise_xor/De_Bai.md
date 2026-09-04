# Biến Đổi FWT với Phép XOR Bitwise

## Bối cảnh
Trung tâm mã hóa cần trộn hai bảng tín hiệu $A$ và $B$ thành bảng $C$, trong đó mỗi ô của bảng kết quả được tổng hợp từ các cặp ô có chỉ số XOR với nhau đúng bằng chỉ số đó. Cách trộn ngây thơ duyệt mọi cặp ô nên chạy quá chậm khi bảng rất dài.

Kỹ sư bèn đưa cả hai bảng qua một phép biến đổi nhanh theo từng bit, nhân từng cặp tương ứng rồi biến đổi ngược trở lại để thu được đúng bảng trộn cần tìm.

## Nhiệm vụ
Cho hai dãy số $A$ và $B$ có độ dài bằng nhau (là lũy thừa của $2$). Hãy lập trình tính tích chập XOR của chúng, tức dãy $C$ trong đó mỗi phần tử được tổng hợp từ các cặp có XOR chỉ số tương ứng.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Bien Doi Fwt Bitwise Xor.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
