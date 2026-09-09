# Xếp loại học lực theo điểm số

## Bối cảnh
Cuối năm học, nhà trường tiến hành phân loại danh hiệu cho học sinh dựa trên điểm trung bình tổng kết môn học $S$. Điểm số hợp lệ phải nằm trong thang điểm từ $0.0$ đến $10.0$. Bạn hãy lập trình tự động hóa việc kiểm tra điểm và xếp loại học sinh.

## Nhiệm vụ
Cho một số thực $S$ là điểm trung bình của học sinh:

- Nếu $S < 0.0$ hoặc $S > 10.0$: In ra `DIEM KHONG HOP LE`.
- Ngược lại, xếp loại theo thang điểm:
- Nếu $8.0 \le S \le 10.0$: In ra `GIOI`.
- Nếu $6.5 \le S < 8.0$: In ra `KHA`.
- Nếu $5.0 \le S < 6.5$: In ra `TRUNG BINH`.
- Nếu $S < 5.0$: In ra `CHUA DAT`.

## Input
- Một dòng duy nhất chứa số thực $S$ ($-10.0 \le S \le 20.0$).

## Output
- In ra một dòng duy nhất kết quả xếp loại tương ứng.

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
Điểm $S = 8.5$ nằm trong khoảng $[8.0, 10.0]$ nên đạt loại `GIOI`.

## Sample 2
### Input
```text
11.5
```
### Output
```text
DIEM KHONG HOP LE
```

### Giải thích
Điểm $11.5 > 10.0$ vượt quá thang điểm quy định, in ra `DIEM KHONG HOP LE`.

## Ràng buộc
- $100\%$ số test có $-10.0 \le S \le 20.0$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
