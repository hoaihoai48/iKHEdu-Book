# Chia kẹo theo nguyên lý Euler (stars and bars)

## Bối cảnh

Nhân dịp Trung thu, phường đoàn chuẩn bị N viên kẹo giống hệt nhau để phát cho K em nhỏ trong khu phố cổ. Có em đến muộn nên ban tổ chức cho phép một em nhận không viên nào mà chương trình văn nghệ vẫn bắt đầu đúng giờ. Các anh chị phụ trách muốn biết có bao nhiêu cách chia khác nhau, chỉ tính phần dư khi chia cho 1 000 000 007 để ghi nhanh vào sổ theo dõi quà tặng của phường.

## Nhiệm vụ

Cho hai số nguyên $N$ (số kẹo) và $K$ (số em nhỏ). Hãy lập trình tính số cách chia $N$ viên kẹo giống nhau cho $K$ em (mỗi em có thể nhận không viên nào), rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng duy nhất: hai số nguyên $N, K$ ($1 \le K \le N \le 10^6$).

## Output

- In ra một dòng duy nhất là số cách chia theo modulo $1\,000\,000\,007$.

## Sample 1

### Input

```text
5 2
```

### Output

```text
6
```

### Giải thích

- Cần chia $5$ viên kẹo giống nhau cho $2$ em, em nào cũng có thể nhận không viên nào.
- Liệt kê theo số kẹo của em thứ nhất: $0, 1, 2, 3, 4, 5$ (em thứ hai nhận phần còn lại $5, 4, 3, 2, 1, 0$).
- Có tất cả $6$ cách nên chương trình in ra $6$.

## Ràng buộc

- $1 \le K \le N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
