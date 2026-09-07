# Đếm số cặp $(a_i, a_j)$ có tích and bằng 0

## Bối cảnh

Thủ thư của một thư viện lớn đánh số mỗi cuốn sách bằng một mã nhị phân ghi trên gáy sách để quản lý kho. Hai cuốn sách được gọi là không chồng lấn nếu phép AND hai mã của chúng bằng $0$, nghĩa là không có vị trí bit nào mà cả hai cuốn cùng bật. Cuối mỗi quý, thủ thư muốn thống kê có bao nhiêu cặp sách có thứ tự trong kho là không chồng lấn nhau, để sắp xếp chúng lên cùng một kệ mà không sợ nhầm lẫn khi quét mã.

## Nhiệm vụ

Cho $N$ số nguyên là mã sách. Hãy lập trình đếm số cặp có thứ tự $(i, j)$ (hai vị trí có thể trùng nhau) sao cho $a_i \mathrel{\&} a_j = 0$, rồi in ra số lượng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số cuốn sách.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($0 \le a_i < 2^{20}$), là mã của từng cuốn.

## Output

- In ra một số nguyên duy nhất là số cặp có thứ tự có phép AND bằng $0$.

## Sample 1

### Input

```text
4
1 2 3 4
```

### Output

```text
8
```

### Giải thích

- Viết bốn mã dưới dạng nhị phân: $1 = 001_2$, $2 = 010_2$, $3 = 011_2$, $4 = 100_2$.
- Kiểm tra từng cặp hai cuốn khác nhau: $1 \mathrel{\&} 2 = 0$, $1 \mathrel{\&} 4 = 0$, $2 \mathrel{\&} 4 = 0$, $3 \mathrel{\&} 4 = 0$; còn $1 \mathrel{\&} 3 = 1$ và $2 \mathrel{\&} 3 = 2$ nên loại.
- Bốn cặp không thứ tự đạt yêu cầu, mỗi cặp cho hai thứ tự $(i, j)$ và $(j, i)$, tổng cộng $4 \times 2 = 8$ cặp có thứ tự.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le a_i < 2^{20}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
