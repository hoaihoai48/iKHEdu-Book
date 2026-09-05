# Xếp loại học lực


## Bối cảnh

Cuối học kỳ, cô giáo cần xếp loại học lực cho từng học sinh dựa vào điểm trung bình. Hãy giúp cô giáo viết chương trình xếp loại tự động.

## Nhiệm vụ

Nhập vào điểm trung bình môn Tin học của một người dùng (số thực $0.0 \le diem \le 10.0$).
 * Điểm $\ge 9.0$: in `XUAT SAC`.
 * Điểm $\ge 8.0$ và $< 9.0$: in `GIOI`.
 * Điểm $\ge 6.5$ và $< 8.0$: in `KHA`.
 * Điểm $< 6.5$: in `CAN CO GANG`.
## Input

Một số thực $diem$.
## Output

Xếp loại tương ứng.

## Sample 1

### Input
```text
8.5
```
### Output
```text
GIOI
```
### Giải thích
Điểm 8.5 thuộc thang điểm giỏi (từ 8.0 trở lên).

## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
