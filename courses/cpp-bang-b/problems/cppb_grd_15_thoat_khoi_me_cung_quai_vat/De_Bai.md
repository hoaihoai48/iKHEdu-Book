# Thoát Khỏi Mê Cung Quái Vật (Monsters Maze)

## Bối cảnh
Trong một trò chơi phiêu lưu sinh tồn trên lưới ô vuông $N × M$, một người thám hiểm xuất phát tại ô `A` và cần chạy thoát ra một ô biên bất kỳ của mê cung. Trong mê cung cũng có sự xuất hiện của một số quái vật tại các ô `M`. Tại mỗi giây, người thám hiểm và tất cả quái vật đều có thể di chuyển 1 bước sang ô kề cạnh. Nếu một con quái vật có thể tới một ô cùng lúc hoặc trước người thám hiểm, người thám hiểm sẽ bị bắt.

## Nhiệm vụ
Cho bản đồ mê cung. Hãy lập trình kiểm tra xem người thám hiểm có thể thoát thân thành công ra mép biên hay không. Nếu có in ra `YES` kèm số bước, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ ký tự (`.` là đường, `#` là tường, `A` là người, `M` là quái vật).

## Output
- Dòng 1: In ra `YES` nếu thoát được, ngược lại in ra `NO`.
- Nếu `YES`, dòng 2 in ra số bước đi ngắn nhất ra biên.

## Sample 1
### Input
```text
5 8
########
#M..A..#
#.#.M#.#
#M#..#..#
#.######
```
### Output
```text
YES
```

### Giải thích
Người thám hiểm chọn lộ trình nhanh nhất hướng về phía mép biên phía đông, đến được biên an toàn sau 2 bước trước khi bất kỳ quái vật nào kịp tiếp cận. Kết quả in ra YES.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
