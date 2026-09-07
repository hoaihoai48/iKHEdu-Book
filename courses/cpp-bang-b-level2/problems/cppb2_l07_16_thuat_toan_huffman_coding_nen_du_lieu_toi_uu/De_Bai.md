# Thuật toán huffman coding nén dữ liệu tối ưu

## Bối cảnh

Trung tâm dữ liệu của tỉnh cần lưu trữ hồ sơ của $N$ loại văn bản, mỗi loại xuất hiện với một tần suất khác nhau. Để tiết kiệm ổ cứng, trung tâm muốn gán cho mỗi loại một mã nhị phân (dãy các bit $0$ và $1$) sao cho không mã nào là tiền tố của mã khác, và tổng số bit phải lưu (tần suất nhân với độ dài mã, cộng trên mọi loại) là nhỏ nhất. Loại văn bản xuất hiện càng nhiều càng nên được gán mã ngắn.

## Nhiệm vụ

Cho $N$ số nguyên là tần suất xuất hiện của từng loại văn bản. Hãy lập trình tính tổng số bit nhỏ nhất của một bộ mã tiền tố tối ưu, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số loại văn bản.
- Dòng thứ hai chứa $N$ số nguyên $f_i$ ($1 \le f_i \le 10^6$), là tần suất của từng loại.

## Output

- In ra một số nguyên duy nhất là tổng số bit nhỏ nhất.

## Sample 1

### Input

```text
4
1 2 3 4
```

### Output

```text
19
```

### Giải thích

- Bắt đầu với bốn nhóm tần suất $1, 2, 3, 4$.
- Gộp hai nhóm nhỏ nhất $1$ và $2$ thành nhóm $3$, các lá $1$ và $2$ nằm sâu thêm một tầng.
- Gộp hai nhóm $3$ và $3$ thành nhóm $6$, các lá trong hai nhóm này nằm sâu thêm một tầng.
- Gộp nhóm $4$ với nhóm $6$ thành gốc $10$ hoàn tất cây mã.
- Tổng số bit là $1 \times 3 + 2 \times 3 + 3 \times 2 + 4 \times 1 = 3 + 6 + 6 + 4 = 19$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le f_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
