# SOS DP Tổng Trên Tập Con (Ưu Đãi Theo Giỏ Hàng)

## Bối cảnh
Siêu thị phát hành nhiều combo ưu đãi, mỗi combo áp dụng cho một tập mặt hàng. Với mỗi giỏ hàng của khách, siêu thị cần cộng dồn ưu đãi của mọi combo nằm gọn trong giỏ.

Tổng ưu đãi phải được tính cho mọi giỏ hàng có thể, nên cần cách tính thật nhanh.

## Nhiệm vụ
Cho một hàm $F$ xác định trên mọi tập con của tập $N$ phần tử. Với mỗi mặt nạ $mask$, hãy lập trình tính tổng $F[sub]$ trên mọi tập con $sub$ của $mask$.

## Input
- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

## Output
- In ra kết quả trên một dòng.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán SOS DP (Sum Over Subsets Dynamic Programming).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
