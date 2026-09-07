# Chu trình Euler (Hierholzer)

## Bối cảnh

Đội kiểm tra cáp treo cần đi qua toàn bộ M đoạn cáp nối N trụ tháp trong khu du lịch núi, mỗi đoạn đi đúng một lần rồi quay về trạm xuất phát để hoàn thành biên bản nghiệm thu. Kỹ sư trưởng kiểm tra bậc của từng trụ tháp trước rồi dùng thuật toán Hierholzer để vạch hành trình cụ thể bắt đầu từ trụ số 1. Nếu điều kiện bậc chẵn hoặc tính liên thông không thỏa thì đợt nghiệm thu phải dời sang tuần sau.

## Nhiệm vụ

Cho đồ thị vô hướng gồm $N$ đỉnh và $M$ cạnh. Hãy lập trình tìm một chu trình Euler bắt đầu tại đỉnh $1$ bằng thuật toán Hierholzer, rồi in ra dãy đỉnh của chu trình (in ra $IMPOSSIBLE$ nếu không tồn tại).

## Input

- Dòng 1: hai số nguyên $N, M$ ($1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v$ là một cạnh hai chiều.

## Output

- In ra một dòng duy nhất là dãy $M+1$ đỉnh của chu trình Euler, hoặc $IMPOSSIBLE$.

## Sample 1

### Input

```text
3 3
1 2
2 3
3 1
```

### Output

```text
1 3 2 1
```

### Giải thích

- Ba trụ tháp nối thành vòng tròn nên mọi đỉnh đều bậc chẵn, chu trình Euler tồn tại.
- Xuất phát từ $1$: thuật toán Hierholzer luôn rẽ sang đỉnh kề nhỏ nhất, hành trình sâu dần rồi quay lui ghi nhận đỉnh vào đáp án.
- Dãy đỉnh thu được là $1\ 3\ 2\ 1$ tạo thành vòng khép kín dùng mỗi đoạn cáp đúng một lần.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
