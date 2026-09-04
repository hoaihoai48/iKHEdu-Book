# Căn Bậc Hai Số Nguyên Lớn

## Bối cảnh
Để giải mã mật mã RSA khi biết giá trị tích hai số nguyên tố N = p * q xấp xỉ nhau, việc tính phần nguyên căn bậc hai của số nguyên lớn A là bước then chốt.

## Nhiệm vụ
Cho số nguyên dương lớn A (có tới 1000 chữ số). Hãy tìm phần nguyên căn bậc hai floor(sqrt(A)).

## Input
- Một dòng duy nhất chứa chuỗi số $A$ ($1 \le |A| \le 1000$).

## Output
- In ra phần nguyên căn bậc hai của $A$.

## Sample 1
### Input
```text
17
```
### Output
```text
4
```
### Giải thích
sqrt(17) = 4.123... Phần nguyên là 4.

## Ràng buộc
- $100\%$ số test có $|A| \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
