# Kiểm Tra Số Hoàn Hảo

## Bối cảnh
Từ thời Hy Lạp cổ đại, các nhà toán học đã tôn vinh các 'số hoàn hảo' — những số nguyên dương có tổng tất cả các ước số thực sự (không kể chính nó) bằng đúng con số đó (ví dụ 6 = 1 + 2 + 3). Hãy kiểm tra xem số N có phải là số hoàn hảo hay không.

## Nhiệm vụ
Cho số nguyên dương N. Hãy kiểm tra xem N có phải là số hoàn hảo hay không. In YES nếu đúng, ngược lại in NO.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
28
```
### Output
```text
YES
```
### Giải thích
Các ước số thực sự của 28 là {1, 2, 4, 7, 14}. Tổng của chúng là 1 + 2 + 4 + 7 + 14 = 28. Vì vậy 28 là số hoàn hảo -> in YES.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
