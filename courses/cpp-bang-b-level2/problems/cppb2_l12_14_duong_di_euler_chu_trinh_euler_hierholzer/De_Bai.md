# Chu trình Euler (Hierholzer)

## Bối cảnh

Hội xe đạp thành phố tổ chức giải chinh phục toàn bộ M con đường nối N giao lộ, yêu cầu mỗi con đường đi qua đúng một lần và quay về điểm xuất phát để nhận huy chương vàng. Ban trọng tài cần kiểm tra xem thử thách này có khả thi không và đưa ra một hành trình cụ thể cho vận động viên xuất phát từ giao lộ số 1. Nếu bậc của giao lộ nào đó lẻ hoặc mạng bị chia cắt thì giải đấu phải đổi thể thức thi đấu.

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
1 3 2 1```

### Giải thích

- Ba giao lộ nối thành vòng tròn nên mọi đỉnh đều bậc chẵn, chu trình Euler tồn tại.
- Xuất phát từ $1$: thuật toán Hierholzer duyệt cạnh nhỏ trước nên đi $1 \to 3 \to 2 \to 1$, dùng mỗi con đường đúng một lần.
- Dãy in ra là $1\ 3\ 2\ 1$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
