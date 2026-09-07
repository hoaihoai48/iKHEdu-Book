# Đường đi hamilton đếm số cách

## Bối cảnh

Hướng dẫn viên du lịch của một công ty lữ hành muốn thiết kế những tour đi qua mỗi điểm tham quan trong thành phố đúng một lần, khởi hành từ bến xe trung tâm và kết thúc tại khu nghỉ dưỡng ven biển. Giữa các điểm chỉ có một số tuyến đường một chiều được phép lưu thông. Để in thành nhiều tờ gợi ý cho du khách lựa chọn, công ty cần biết chính xác có tất cả bao nhiêu lộ trình thỏa mãn điều kiện đi qua mọi điểm đúng một lần như vậy.

## Nhiệm vụ

Cho đồ thị có hướng gồm $N$ đỉnh (đỉnh $0$ là điểm xuất phát, đỉnh $N - 1$ là điểm kết thúc) và $M$ cạnh một chiều. Hãy lập trình đếm số đường đi từ đỉnh $0$ đến đỉnh $N - 1$ mà đi qua mỗi đỉnh đúng một lần, rồi in ra số lượng đó.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, M$ ($2 \le N \le 18$, $0 \le M \le N \times (N - 1)$), là số đỉnh và số cạnh một chiều.
- $M$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u, v$ ($0 \le u, v < N$, $u \ne v$), mô tả cạnh một chiều từ $u$ đến $v$.

## Output

- In ra một số nguyên duy nhất là số đường đi Hamilton từ đỉnh $0$ đến đỉnh $N - 1$.

## Sample 1

### Input

```text
4 5
0 1
0 2
1 2
1 3
2 3
```

### Output

```text
1
```

### Giải thích

- Liệt kê mọi đường đi từ đỉnh $0$ đến đỉnh $3$ trong đồ thị trên.
- Đường $0 \to 1 \to 3$ chỉ đi qua ba đỉnh nên không tính.
- Đường $0 \to 2 \to 3$ cũng chỉ đi qua ba đỉnh nên không tính.
- Đường $0 \to 1 \to 2 \to 3$ đi qua cả bốn đỉnh $0, 1, 2, 3$ đúng một lần nên được tính.
- Chỉ có đúng $1$ đường đi thỏa mãn.

## Ràng buộc

- $2 \le N \le 18$, $0 \le M \le N \times (N - 1)$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
