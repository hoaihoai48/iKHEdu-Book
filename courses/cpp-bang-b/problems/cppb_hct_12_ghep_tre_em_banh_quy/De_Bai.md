# Ghép Cặp Trẻ Em Và Bánh Quy

## Bối cảnh
Tại một buổi tiệc sinh nhật thiếu nhi, cô giáo chuẩn bị M chiếc bánh quy với các kích thước S1, S2, ..., Sm để phát cho N đứa trẻ. Mỗi đứa trẻ thứ i có mức độ thèm ăn tối thiểu là Gi và chỉ cảm thấy hài lòng nếu nhận được một chiếc bánh có kích thước không nhỏ hơn Gi (Sj >= Gi). Để công bằng, mỗi đứa trẻ chỉ nhận tối đa 1 chiếc bánh và mỗi chiếc bánh chỉ chia cho đúng 1 đứa trẻ. Hãy tìm cách phân phát bánh sao cho số lượng đứa trẻ được thỏa mãn là nhiều nhất có thể.

## Nhiệm vụ
Cho mức độ thèm ăn của N đứa trẻ và kích thước của M chiếc bánh quy. Hãy tính số lượng đứa trẻ tối đa có thể được thỏa mãn.

## Input
- Dòng 1: 2 số nguyên $N$ và $M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên $G_1, G_2, \dots, G_N$ ($1 \le G_i \le 10^9$).
- Dòng 3: $M$ số nguyên $S_1, S_2, \dots, S_M$ ($1 \le S_j \le 10^9$).

## Output
- In ra số lượng đứa trẻ tối đa được thỏa mãn.

## Sample 1
### Input
```text
3 2
1 2 3
1 1
```
### Output
```text
1
```
### Giải thích
Có 3 đứa trẻ với mức độ thèm ăn là [1, 2, 3] và 2 chiếc bánh quy kích thước [1, 1]. Chiếc bánh đầu tiên kích thước 1 phát cho đứa trẻ có mức thèm ăn 1 (thỏa mãn 1 trẻ). Chiếc bánh thứ hai cũng có kích thước 1, nhưng hai đứa trẻ còn lại yêu cầu bánh kích thước tối thiểu là 2 và 3, nên chiếc bánh này không thể làm hài lòng thêm đứa trẻ nào. Do đó số đứa trẻ tối đa được thỏa mãn là 1.

## Ràng buộc
- $100\%$ số test có $N, M \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
