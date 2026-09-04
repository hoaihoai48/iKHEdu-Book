# Giải Phương Trình Đồng Dư Tuyến Tính Ax = B mod M

## Bối cảnh
Trong kỹ thuật mã hóa và phá mã cổ điển Affine Cipher, việc giải mã đòi hỏi giải phương trình đồng dư tuyến tính dạng Ax = B mod M để tìm lại bản rõ ban đầu x.

## Nhiệm vụ
Cho 3 số nguyên A, B, M. Hãy tìm nghiệm nguyên không âm nhỏ nhất X của phương trình Ax = B mod M. Nếu vô nghiệm, in ra -1.

## Input
- Một dòng chứa 3 số nguyên $A, B, M$ ($1 \le A, B, M \le 10^9$).

## Output
- In ra nghiệm nguyên nhỏ nhất $X$ trong khoảng $[0, M - 1]$, hoặc `-1`.

## Sample 1
### Input
```text
2 4 6
```
### Output
```text
2
```
### Giải thích
Thay X = 2: 2 * 2 = 4 = 4 mod 6. Nghiệm không âm nhỏ nhất là 2.

## Ràng buộc
- $100\%$ số test có $A, B, M \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
