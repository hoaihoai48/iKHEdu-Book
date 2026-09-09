# Hình Vuông Toàn 1 Lớn Nhất (Maximal Square)

## Bối cảnh
Một cảm biến vệ tinh chụp bức ảnh mặt đất độ phân giải cao dạng ma trận nhị phân $N × M$ điểm ảnh. Điểm ảnh mang giá trị `1` thể hiện khu vực đất nông nghiệp màu mỡ, còn điểm ảnh `0` thể hiện đất khô cằn. Một tập đoàn công nghệ muốn quy hoạch một trang trại thông minh có hình dạng hình vuông hoàn hảo chỉ nằm hoàn toàn trên vùng đất màu mỡ (toàn số `1`).

## Nhiệm vụ
Cho ma trận nhị phân $N × M$. Hãy lập trình tìm độ dài cạnh lớn nhất của một hình vuông con chỉ chứa toàn số `1`.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ ký tự `0` hoặc `1` liền nhau hoặc cách nhau bởi khoảng trắng.

## Output
- In ra trên một dòng duy nhất độ dài cạnh của hình vuông toàn số `1` lớn nhất tìm được.

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
4
```

### Giải thích
Với ma trận kích thước $4 × 4$:
1 0 1 0
1 1 1 1
1 1 1 0
0 1 1 1
Hình vuông con toàn số 1 lớn nhất có kích thước $2 × 2$ (độ dài cạnh bằng 2). Kết quả in ra là 2.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
