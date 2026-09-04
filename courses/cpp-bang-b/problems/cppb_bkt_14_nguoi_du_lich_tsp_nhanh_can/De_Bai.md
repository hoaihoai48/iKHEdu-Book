# Người Du Lịch (TSP) Nhánh Cận

**Phân loại bài toán:** `Advanced`

## Bối cảnh
Một đại diện thương mại quốc tế của tập đoàn công nghệ cần lên lịch trình công tác ghé thăm trực tiếp đối tác tại $N$ thành phố trọng điểm (được đánh số từ $1$ đến $N$). Doanh nhân bắt đầu chuyến đi từ trụ sở chính tại thành phố $1$, cần bay qua tất cả $N-1$ thành phố còn lại, mỗi thành phố đúng một lần duy nhất, rồi cuối cùng bay về lại thành phố $1$. Chi phí di chuyển giữa mỗi cặp thành phố đã được hãng bay niêm yết cố định.

## Nhiệm vụ
Cho số lượng thành phố $N$ và ma trận chi phí vận tải $C$ kích thước $N \times N$, trong đó $C_{i, j}$ là chi phí bay từ thành phố $i$ đến thành phố $j$. Hãy áp dụng thuật toán Nhánh Cận (Branch and Bound) với hàm cận dưới dựa trên cạnh có chi phí nhỏ nhất toàn đồ thị để tìm chu trình di chuyển có tổng chi phí thấp nhất.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 13$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $N$ số nguyên biểu diễn ma trận chi phí $C$ ($0 \le C_{i, j} \le 10^6, C_{i, i} = 0$).

## Output
- In ra một số nguyên duy nhất là tổng chi phí nhỏ nhất của chu trình Hamilton tìm được.

## Sample 1
### Input
```text
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```
### Output
```text
80
```
### Giải thích
Lộ trình tối ưu xuất phát từ thành phố 1 là: $1 \to 2 \to 4 \to 3 \to 1$. Tổng chi phí của hành trình là: $C_{1, 2} + C_{2, 4} + C_{4, 3} + C_{3, 1} = 10 + 25 + 30 + 15 = 80$.

## Ràng buộc
- 100% số test có $2 \le N \le 13$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
