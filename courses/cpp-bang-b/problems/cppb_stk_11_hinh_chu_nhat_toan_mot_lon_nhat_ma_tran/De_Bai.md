# Hình Chữ Nhật Toàn 1 Lớn Nhất Trong Ma Trận

## Bối cảnh
Một tấm tôn kích thước $N  × M$ ô vuông bị đục thủng một số vị trí (ô bị đục ký hiệu bằng số `0`, ô nguyên vẹn ký hiệu bằng số `1`). Người thợ cơ khí cần cắt ra từ tấm tôn một miếng hình chữ nhật nguyên vẹn (chỉ chứa toàn số `1`) sao cho diện tích của miếng tôn cắt ra là lớn nhất có thể.

## Nhiệm vụ
Cho ma trận nhị phân $N  × M$. Hãy lập trình tìm diện tích lớn nhất của hình chữ nhật con chỉ chứa toàn số `1`.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên `0` hoặc `1` cách nhau bởi khoảng trắng.

## Output
- In ra trên một dòng duy nhất diện tích lớn nhất của hình chữ nhật tìm được.

## Sample 1
### Input
```text
4 5
10100
10111
11111
10010
```
### Output
```text
6
```

### Giải thích
Với ma trận kích thước $4  × 5$:
Hình chữ nhật con toàn số 1 lớn nhất có kích thước $2 × 3$ (chiều cao 2, chiều rộng 3) gồm 6 ô số 1. Diện tích lớn nhất đạt được là 6.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
