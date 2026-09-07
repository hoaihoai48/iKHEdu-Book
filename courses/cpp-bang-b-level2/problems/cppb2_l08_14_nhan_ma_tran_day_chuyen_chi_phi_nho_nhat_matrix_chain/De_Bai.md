# Nhân ma trận dây chuyền chi phí nhỏ nhất (matrix chain)

## Bối cảnh

Phòng thí nghiệm trí tuệ nhân tạo cần nhân một dây chuyền $N$ ma trận liên tiếp nhau để huấn luyện mô hình mới, và thứ tự đặt dấu ngoặc khi nhân ảnh hưởng rất lớn đến tổng số phép tính phải thực hiện. Máy chủ của phòng thì cũ kỹ nên mỗi phép nhân thừa đều tốn thêm hàng giờ chạy. Nhóm kỹ sư cần tìm cách đặt dấu ngoặc sao cho tổng số phép nhân vô hướng là ít nhất.

## Nhiệm vụ

Cho $N$ ma trận $A_1, A_2, \dots, A_N$, trong đó ma trận $A_i$ có kích thước $p_{i-1} \times p_i$. Hãy lập trình tìm cách đặt dấu ngoặc để nhân toàn bộ dây chuyền với tổng số phép nhân ít nhất, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 200$), là số ma trận.
- Dòng thứ hai chứa $N + 1$ số nguyên $p_0, p_1, \dots, p_N$ ($1 \le p_i \le 100$), mô tả kích thước các ma trận.

## Output

- In ra một số nguyên duy nhất là tổng số phép nhân ít nhất.

## Sample 1

### Input

```text
3
1 2 3 4
```

### Output

```text
18
```

### Giải thích

- Ba ma trận có kích thước $1 \times 2$, $2 \times 3$ và $3 \times 4$.
- Cách $(A_1 \times A_2) \times A_3$: nhân hai ma trận đầu tốn $1 \times 2 \times 3 = 6$, ma trận kết quả $1 \times 3$ nhân tiếp tốn $1 \times 3 \times 4 = 12$, tổng $18$.
- Cách $A_1 \times (A_2 \times A_3)$: nhân hai ma trận sau tốn $2 \times 3 \times 4 = 24$, nhân tiếp tốn $1 \times 2 \times 4 = 8$, tổng $32$.
- Cách rẻ nhất tốn $18$ phép nhân.

## Ràng buộc

- $1 \le N \le 200$, $1 \le p_i \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
