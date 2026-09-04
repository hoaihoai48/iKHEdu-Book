# Tam Giác Số Tổng Lớn Nhất (Triangle DP)

## Bối cảnh
Một kim tự tháp số có $N$ tầng được đánh số từ $1$ đến $N$. Tầng thứ $i$ chứa đúng $i$ số nguyên. Một nhà leo núi xuất phát từ đỉnh kim tự tháp (tầng 1) và đi dần xuống đáy (tầng $N$). Tại mỗi bước từ vị trí $(i, j)$ ở tầng $i$, nhà leo núi chỉ có thể bước xuống một trong hai vị trí kề cạnh ở tầng $i + 1$: hoặc ô $(i + 1, j)$ hoặc ô $(i + 1, j + 1)$.

## Nhiệm vụ
Cho cấu trúc kim tự tháp số $N$ tầng. Hãy lập trình tìm đường đi từ đỉnh xuống đáy sao cho tổng các số trên đường đi là lớn nhất.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$) biểu diễn số tầng của kim tự tháp.
- $N$ dòng tiếp theo, dòng thứ $i$ chứa $i$ số nguyên $A_{i,j}$ ($0 \le A_{i,j} \le 10^4$).

## Output
- In ra trên một dòng duy nhất tổng lớn nhất thu được.

## Sample 1
### Input
```text
4
2
3 4
6 5 7
4 1 8 3
```
### Output
```text
21
```

### Giải thích
Với tam giác số gồm 4 tầng:
  3
  7 4
  2 4 6
  8 5 9 3
Đường đi mang lại tổng lớn nhất là $3  × o 7  × o 4  × o 9$, cho tổng lớn nhất là $3 + 7 + 4 + 9 = 23$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 1000, 0 \le A_{i, j} \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
