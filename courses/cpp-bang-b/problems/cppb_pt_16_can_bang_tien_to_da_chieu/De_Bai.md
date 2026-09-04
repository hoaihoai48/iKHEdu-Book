# Cân Bằng Tiền Tố Đa Chiều

## Bối cảnh
Trong chuỗi mã hóa di truyền sinh học gồm N phân tử thuộc ba loại 'A', 'B', 'C', các nhà sinh học phân tử cần tìm một đoạn gen liên tiếp dài nhất mà trong đó số lượng các phân tử loại 'A', 'B' và 'C' xuất hiện hoàn toàn bằng nhau.

## Nhiệm vụ
Cho một chuỗi gồm N ký tự chỉ gồm các chữ cái 'A', 'B', 'C'. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp có số lượng ký tự 'A', 'B' và 'C' bằng nhau.

## Input
- Dòng 1: Chuỗi ký tự $S$ có độ dài $N$ ($1 \le N \le 10^5$).

## Output
- In ra độ dài lớn nhất của chuỗi con thỏa mãn, hoặc `0` nếu không có đoạn nào.

## Sample 1
### Input
```text
ABACBC
```
### Output
```text
6
```
### Giải thích
Chuỗi 'ABACBC' có độ dài 6 chứa đúng hai ký tự 'A', hai ký tự 'B' và hai ký tự 'C' (số lượng bằng nhau = 2). Vì vậy độ dài lớn nhất là 6.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
