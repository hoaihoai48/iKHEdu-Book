# Xếp Loại Học Lực

## Bối cảnh
Cuối năm, nhà trường cần xếp loại học lực cho học sinh dựa trên điểm trung bình. Quy tắc xếp loại: từ $8.0$ trở lên là "Gioi", từ $6.5$ đến dưới $8.0$ là "Kha", từ $5.0$ đến dưới $6.5$ là "Trung binh", dưới $5.0$ là "Yeu".

## Nhiệm vụ
Cho điểm trung bình $D$ của một học sinh (số thực). Hãy lập trình in ra xếp loại học lực tương ứng.

## Input
- Một dòng duy nhất chứa số thực $D$ ($0.0 \le D \le 10.0$).

## Output
- In ra một chuỗi ký tự: `Gioi`, `Kha`, `Trung binh` hoặc `Yeu`.

## Sample 1
### Input
```text
8.5
```
### Output
```text
Gioi
```

### Giải thích
Điểm $D = 8.5 \ge 8.0$ nên xếp loại "Gioi".

## Sample 2
### Input
```text
4.9
```
### Output
```text
Yeu
```

### Giải thích
Điểm $D = 4.9 < 5.0$ nên xếp loại "Yeu".

## Ràng buộc
- $100\%$ số test có $0.0 \le D \le 10.0$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
