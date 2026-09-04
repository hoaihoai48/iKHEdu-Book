# Bài Toán Cái Túi 0/1 Nhánh Cận (B&B Knapsack)

**Phân loại bài toán:** `Advanced`

## Bối cảnh
Một nhà thám hiểm địa chất lạc bước vào một hang động cổ xưa chứa $N$ mẫu khoáng thạch quý hiếm. Mỗi mẫu vật $i$ được xác định có khối lượng $W_i$ và giá trị thương mại là $V_i$. Chiếc ba lô chuyên dụng mang theo chỉ chịu được tải trọng tối đa là $M$. Để tối ưu hóa lợi ích thu được từ chuyến thám hiểm, nhà nghiên cứu cần lựa chọn một tập hợp các mẫu vật cho vào ba lô sao cho không bị quá tải trọng và đạt tổng giá trị lớn nhất.

## Nhiệm vụ
Cho $N$ đồ vật với trọng lượng $W_i$ và giá trị $V_i$ tương ứng, cùng sức chứa tối đa $M$ của ba lô. Hãy áp dụng thuật toán Nhánh Cận (Branch and Bound) sử dụng hàm cận trên Fractional Knapsack (sắp xếp theo tỷ lệ đơn giá $\frac{V_i}{W_i}$ giảm dần) để tìm giá trị tài sản lớn nhất có thể mang về.

## Input
- Dòng 1: Hai số nguyên dương $N, M$ ($1 \le N \le 25, 1 \le M \le 10^9$).
- $N$ dòng tiếp theo: Mỗi dòng gồm hai số nguyên dương $W_i, V_i$ ($1 \le W_i, V_i \le 10^7$).

## Output
- In ra một số nguyên duy nhất là tổng giá trị lớn nhất đạt được.

## Sample 1
### Input
```text
4 10
3 40
4 50
5 60
6 70
```
### Output
```text
120
```
### Giải thích
Chọn đồ vật thứ 2 (trọng lượng 4, giá trị 50) và đồ vật thứ 4 (trọng lượng 6, giá trị 70). Tổng trọng lượng là $4 + 6 = 10 \le 10$ và tổng giá trị đạt được là $50 + 70 = 120$, là giá trị lớn nhất có thể đạt được.

## Ràng buộc
- 100% số test có $1 \le N \le 25, 1 \le M \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
