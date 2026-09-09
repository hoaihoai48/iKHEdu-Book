# Kiểm tra năm nhuận theo dương lịch

## Bối cảnh
Theo Dương lịch, một năm thông thường có 365 ngày, riêng năm nhuận có 366 ngày với tháng Hai có 29 ngày thay vì 28 ngày. Quy tắc xác định năm nhuận là: Năm đó phải chia hết cho 400, HOẶC chia hết cho 4 nhưng KHÔNG chia hết cho 100. Bạn hãy lập trình giúp xác định xem một năm có phải là năm nhuận hay không và cho biết tháng Hai của năm đó có bao nhiêu ngày.

## Nhiệm vụ
Cho một số nguyên dương $Y$ là năm cần kiểm tra. Hãy lập trình:

- Nếu $Y$ là năm nhuận: In ra `NHUAN 29`.
- Nếu $Y$ không phải năm nhuận: In ra `KHONG NHUAN 28`.

## Input
- Một dòng duy nhất chứa số nguyên dương $Y$ ($1 \le Y \le 10^5$).

## Output
- In ra một dòng duy nhất theo định dạng yêu cầu của đề bài.

## Sample 1
### Input
```text
2024
```
### Output
```text
NHUAN 29
```

### Giải thích
Năm 2024 chia hết cho 4 và không chia hết cho 100, do đó là năm nhuận và tháng Hai có 29 ngày.

## Sample 2
### Input
```text
1900
```
### Output
```text
KHONG NHUAN 28
```

### Giải thích
Năm 1900 chia hết cho 4 và chia hết cho 100, nhưng không chia hết cho 400 nên không phải năm nhuận. Tháng Hai có 28 ngày.

## Sample 3
### Input
```text
2000
```
### Output
```text
NHUAN 29
```

### Giải thích
Năm 2000 chia hết cho 400 nên là năm nhuận.

## Ràng buộc
- $100\%$ số test có $1 \le Y \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
