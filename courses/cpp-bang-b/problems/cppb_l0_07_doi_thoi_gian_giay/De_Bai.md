# Đổi thời gian từ giờ phút sang giây

## Bối cảnh
Trong một giải chạy marathon quốc tế, thiết bị đo thời gian tự động của ban tổ chức ghi nhận thành tích của vận động viên dưới dạng tổng số giây kể từ thời điểm xuất phát. Để hiển thị lên bảng điện tử cho khán giả dễ theo dõi, ban tổ chức cần chuyển đổi tổng số giây này thành định dạng giờ, phút và giây.

## Nhiệm vụ
Cho một số nguyên không âm $T$ là tổng số giây. Hãy lập trình đổi $T$ thành $h$ giờ, $m$ phút và $s$ giây, in ra theo định dạng `h:m:s`.

## Input
- Một dòng duy nhất chứa số nguyên không âm $T$ ($0 \le T \le 10^9$).

## Output
- In ra một dòng duy nhất theo định dạng `h:m:s`.

## Sample 1
### Input
```text
3665
```
### Output
```text
1:1:5
```

### Giải thích
Ta có $1\text{ giờ} = 3600\text{ giây}$, $1\text{ phút} = 60\text{ giây}$:

- Số giờ: $3665 / 3600 = 1$ giờ.
- Số giây còn lại sau khi trừ giờ: $3665 \% 3600 = 65$ giây.
- Số phút: $65 / 60 = 1$ phút.
- Số giây còn lại: $65 \% 60 = 5$ giây.
Định dạng kết quả: `1:1:5`.

## Sample 2
### Input
```text
125
```
### Output
```text
0:2:5
```

### Giải thích
$125$ giây gồm $0$ giờ, $2$ phút và $5$ giây. Kết quả: `0:2:5`.

## Ràng buộc
- $100\%$ số test có $0 \le T \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
