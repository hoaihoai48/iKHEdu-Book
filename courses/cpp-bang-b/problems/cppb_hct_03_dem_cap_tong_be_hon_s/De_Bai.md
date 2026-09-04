# Đếm Cặp Có Tổng Không Quá S

## Bối cảnh
Một phòng thí nghiệm vật lý tổ chức ghép cặp 2 hạt mang điện tích khác nhau trong chùm gồm N hạt để thực hiện phản ứng va chạm trong buồng từ trường. Để phản ứng diễn ra an toàn và không phá hủy thành buồng chứa, tổng mức năng lượng kích hoạt của hai hạt được ghép không được vượt quá ngưỡng giới hạn an toàn S. Các nhà khoa học cần đếm xem có tổng cộng bao nhiêu cặp hạt thỏa mãn tiêu chí an toàn này.

## Nhiệm vụ
Cho mảng gồm N số nguyên và một số nguyên S. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N thỏa mãn: A[i] + A[j] <= S.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 2 \cdot 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

## Sample 1
### Input
```text
5 8
2 5 1 4 3
```
### Output
```text
9
```
### Giải thích
Sắp xếp mảng tăng dần: [1, 2, 3, 4, 5] và S = 8. Tổng số cặp phân biệt từ 5 phần tử là 5*4/2 = 10 cặp. Cặp duy nhất có tổng lớn hơn 8 là (4, 5) với tổng 4 + 5 = 9 > 8. Còn lại tất cả 9 cặp khác đều có tổng <= 8: (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5). Vì vậy kết quả là 9.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
