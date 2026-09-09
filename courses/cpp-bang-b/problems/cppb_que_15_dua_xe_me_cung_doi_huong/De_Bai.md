# Đua Xe Mê Cung Đổi Hướng Ít Nhất (0-1 BFS State)

## Bối cảnh
Trong một giải đua xe robot trong mê cung lưới ô vuông $N × M$, robot cần di chuyển từ ô xuất phát $S$ tới ô đích $D$. Mỗi lần robot đi thẳng theo hướng đang di chuyển thì hoàn toàn miễn phí (chi phí 0), nhưng mỗi khi robot phải bẻ lái đổi sang một trong các hướng vuông góc thì bánh lái sẽ tiêu hao 1 đơn vị năng lượng.

## Nhiệm vụ
Cho bản đồ mê cung $N × M$ và vị trí $S, D$. Hãy lập trình tìm số lần đổi hướng ít nhất để robot đi từ $S$ tới $D$. Nếu không có đường đi, in ra `-1`.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi $M$ ký tự biểu diễn mê cung (`.` là đường đi, `*` là vật cản, `S` là xuất phát, `D` là đích).

## Output
- In ra số lần đổi hướng ít nhất, hoặc `-1` nếu không có đường đi.

## Sample 1
### Input
```text
3 3
S..
.#.
..E
```
### Output
```text
1
```

### Giải thích
Với mê cung $3 × 3$ không vật cản từ góc $(1,1)$ tới $(3,3)$:
Robot chỉ cần đi thẳng hết hàng 1 sang phải, sau đó rẽ lái 1 lần duy nhất để đi thẳng xuống dưới tới đích. Số lần đổi hướng ít nhất là 1.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
