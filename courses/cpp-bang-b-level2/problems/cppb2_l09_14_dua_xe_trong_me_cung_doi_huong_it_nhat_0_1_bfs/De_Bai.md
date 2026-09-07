# Đua xe trong mê cung đổi hướng ít nhất (0-1 BFS)

## Bối cảnh

Câu lạc bộ xe địa hình tổ chức cuộc đua vượt mê cung trên một khu đất chia thành lưới ô vuông, trong đó một số ô là tường gạch không thể đi qua. Mỗi tay đua xuất phát từ ô `S` và phải về đích ở ô `T`, mỗi bước được đi sang một trong bốn ô kề cạnh còn trống. Vì xe chạy đà rất tốn nhiên liệu mỗi lần bẻ lái, ban tổ chức tính điểm bằng số lần đổi hướng của hành trình (đi thẳng không tốn điểm, mỗi lần rẽ tốn một điểm).

## Nhiệm vụ

Cho lưới $N \times M$ gồm các ký tự `.` (đường trống), `#` (tường), `S` (xuất phát), `T` (đích). Mỗi bước đi sang ô kề cạnh còn trống; lần đi đầu tiên chọn hướng tùy ý không tốn điểm, mỗi lần đổi hướng tốn một điểm. Hãy lập trình tính số điểm ít nhất để từ `S` tới `T`, rồi in ra số đó. Nếu không tới được thì in ra $-1$.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, M$ ($1 \le N, M \le 500$), là số hàng và số cột của mê cung.
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ ký tự mô tả mê cung, gồm đúng một ô `S` và một ô `T`.

## Output

- In ra số lần đổi hướng ít nhất, hoặc $-1$ nếu không tới được đích.

## Sample 1

### Input

```text
3 3
S..
...
..T
```

### Output

```text
1
```

### Giải thích

- Hành trình đi thẳng xuống hai ô tới $(2, 0)$ rồi rẽ phải đi tiếp hai ô tới đích $(2, 2)$.
- Cả hành trình chỉ đổi hướng đúng một lần tại ô $(2, 0)$ từ hướng xuống sang hướng phải.
- Mọi hành trình từ `S` tới `T` đều phải rẽ ít nhất một lần vì điểm xuất phát và đích không cùng hàng cũng không cùng cột, nên đáp án là $1$.

## Ràng buộc

- $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
