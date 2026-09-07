# Ma trận toàn số 1 lớn nhất (maximal rectangle 2d)

## Bối cảnh

Ban quản lý chợ đầu mối muốn dành ra một khu đất hình chữ nhật lớn nhất mà toàn bộ các lô trong khu đều còn trống để làm bãi đỗ xe tạm trong dịp Tết. Mặt bằng khu chợ được chia thành lưới ô vuông, mỗi ô được đánh dấu $1$ nếu đang trống và $0$ nếu đã có sạp chiếm chỗ. Khu đất chọn ra phải là một hình chữ nhật gồm toàn ô trống, càng rộng càng tốt để chứa được nhiều xe tải chở hàng hóa về chợ trong những ngày cao điểm.

## Nhiệm vụ

Cho lưới $N \times M$ chỉ gồm các số $0$ và $1$. Hãy lập trình tìm hình chữ nhật con có diện tích lớn nhất mà mọi ô trong đó đều bằng $1$, rồi in ra diện tích đó.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, M$ ($1 \le N, M \le 500$), là số hàng và số cột của mặt bằng.
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên $0$ hoặc $1$, trong đó $1$ là ô trống.

## Output

- In ra một số nguyên duy nhất là diện tích lớn nhất (bằng $0$ nếu không có ô trống nào).

## Sample 1

### Input

```text
3 3
1 0 1
1 1 1
0 1 1
```

### Output

```text
4
```

### Giải thích

- Bốn ô ở góc dưới bên phải gồm hai hàng cuối và hai cột cuối đều bằng $1$ nên tạo thành hình chữ nhật $2 \times 2$ diện tích $4$.
- Hàng giữa có ba ô $1$ liên tiếp tạo thành hình $1 \times 3$ diện tích $3$.
- Mọi hình chữ nhật toàn số $1$ khác đều có diện tích không vượt quá $4$, nên đáp án là $4$.

## Ràng buộc

- $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
