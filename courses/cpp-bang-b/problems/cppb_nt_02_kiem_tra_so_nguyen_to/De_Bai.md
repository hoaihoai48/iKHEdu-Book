# Kiểm Tra Số Nguyên Tố Cơ Bản

## Bối cảnh
Trong hệ thống xác thực bảo mật tài khoản ngân hàng, mã khóa OTP được coi là đạt chuẩn an toàn nếu nó là một số nguyên tố (chỉ có đúng 2 ước số dương là 1 và chính nó). Hệ thống cần xác định nhanh xem số nguyên dương N có phải là số nguyên tố hay không.

## Nhiệm vụ
Cho một số nguyên dương N. Hãy kiểm tra xem N có phải là số nguyên tố hay không. In YES nếu đúng, ngược lại in NO.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{12}$).

## Output
- In ra `YES` nếu $N$ là số nguyên tố, ngược lại in `NO`.

## Sample 1
### Input
```text
29
```
### Output
```text
YES
```
### Giải thích
Số 29 chỉ chia hết cho 1 và 29, do đó 29 là số nguyên tố -> in YES.

## Ràng buộc
- $100\%$ số test có $N \le 10^{12}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
