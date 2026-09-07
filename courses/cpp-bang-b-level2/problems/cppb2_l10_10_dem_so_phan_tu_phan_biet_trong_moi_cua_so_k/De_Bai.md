# Đếm số phần tử phân biệt trong mọi cửa sổ k

## Bối cảnh

Nhà máy sản xuất linh kiện ghi lại mã lỗi của từng sản phẩm chạy trên dây chuyền theo đúng thứ tự thời gian, mỗi sản phẩm có thể mắc một trong nhiều loại lỗi khác nhau. Để giám sát chất lượng theo từng ca sản xuất, tổ trưởng muốn biết trong mỗi khung $K$ sản phẩm liên tiếp có bao nhiêu loại lỗi khác nhau xuất hiện, vì khung nào có quá nhiều loại lỗi thì toàn bộ khung đó phải đưa đi kiểm tra lại từ đầu trước khi đóng gói xuất xưởng.

## Nhiệm vụ

Cho $N$ số nguyên là mã lỗi từng sản phẩm và độ dài cửa sổ $K$. Với mỗi cửa sổ gồm $K$ sản phẩm liên tiếp (trượt từ đầu đến cuối dãy), hãy lập trình đếm số giá trị phân biệt trong cửa sổ đó, rồi in ra $N - K + 1$ kết quả theo thứ tự.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, K$ ($1 \le K \le N \le 10^5$), là số sản phẩm và độ dài cửa sổ.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^6$), là mã lỗi từng sản phẩm.

## Output

- In ra $N - K + 1$ số nguyên trên một dòng là số giá trị phân biệt của từng cửa sổ.

## Sample 1

### Input

```text
7 4
1 2 1 3 4 2 3
```

### Output

```text
3 4 4 3
```

### Giải thích

- Cửa sổ $[1, 2, 1, 3]$ gồm ba loại lỗi khác nhau là $1, 2, 3$.
- Cửa sổ $[2, 1, 3, 4]$ gồm bốn loại khác nhau là $1, 2, 3, 4$.
- Cửa sổ $[1, 3, 4, 2]$ gồm bốn loại khác nhau là $1, 2, 3, 4$.
- Cửa sổ $[3, 4, 2, 3]$ gồm ba loại khác nhau là $2, 3, 4$.

## Ràng buộc

- $1 \le K \le N \le 10^5$, $1 \le a_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
