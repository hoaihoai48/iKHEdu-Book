# Tìm Nghiệm Nguyên Phương Trình Diophantine

## Bối cảnh
Phương trình Diophantine tuyến tính có dạng:
$$A \cdot x + B \cdot y = C$$
trong đó $A, B, C$ là các số nguyên cho trước, ta cần tìm cặp nghiệm nguyên $(x, y)$ hoặc kết luận vô nghiệm.

Theo **Định lý Bézout**, phương trình trên có nghiệm nguyên khi và chỉ khi $\gcd(A, B)$ chia hết $C$.

Cho $T$ bộ dữ liệu, mỗi bộ gồm ba số nguyên $A, B, C$. Hãy kiểm tra phương trình $Ax + By = C$ có nghiệm nguyên hay không. Nếu có, in ra một cặp nghiệm $(x_0, y_0)$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Tìm Nghiệm Nguyên Phương Trình Diophantine với độ phức tạp tối ưu nhất.

## Input
- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$).
- $T$ dòng tiếp theo, mỗi dòng chứa ba số nguyên $A$, $B$, $C$ ($-10^9 \le A, B, C \le 10^9$), cách nhau bởi dấu cách.

## Output
- Gồm $T$ dòng:
- Nếu phương trình vô nghiệm, in `NO`.
- Nếu có nghiệm, in `YES x0 y0` với $(x_0, y_0)$ là một cặp nghiệm nguyên bất kỳ.

## Sample 1
### Input
```text
3
2 3 7
4 6 3
0 0 0
```
### Output
```text
YES -7 7
NO
YES 0 0
```
### Giải thích
* $2x + 3y = 7$: $\gcd(2, 3) = 1 \mid 7 \implies$ có nghiệm. Nghiệm $(x_0, y_0) = (-7, 7)$: $2(-7) + 3(7) = -14 + 21 = 7$ ✓.
* $4x + 6y = 3$: $\gcd(4, 6) = 2 \nmid 3 \implies$ vô nghiệm.
* $0x + 0y = 0$: $0 = 0 \implies$ mọi $(x, y)$ đều là nghiệm, in $(0, 0)$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
