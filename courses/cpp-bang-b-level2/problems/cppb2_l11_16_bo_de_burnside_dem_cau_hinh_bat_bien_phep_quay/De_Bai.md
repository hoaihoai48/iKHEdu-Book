# Bổ đề Burnside đếm vòng cổ theo phép quay

## Bối cảnh

Làng nghề làm vòng tay chuẩn bị ra mắt bộ sưu tập mới gồm những chiếc vòng tròn đính N hạt, mỗi hạt được nhuộm một trong K màu có sẵn trong kho. Hai chiếc vòng được xem là giống nhau nếu chiếc này xoay được thành chiếc kia quanh tâm vòng tròn. Chủ xưởng cần đếm có bao nhiêu mẫu vòng thực sự khác nhau để đăng ký bản quyền từng mẫu, lấy dư cho 1 000 000 007 vì số mẫu tăng rất nhanh.

## Nhiệm vụ

Cho hai số nguyên $N, K$. Hãy lập trình đếm số cách tô màu vòng cổ $N$ hạt bằng $K$ màu, hai cách tô xem là một nếu xoay được thành nhau (bổ đề Burnside cho nhóm quay), rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng duy nhất: hai số nguyên $N, K$ ($1 \le N, K \le 10^6$).

## Output

- In ra một dòng duy nhất là số mẫu vòng phân biệt theo modulo $1\,000\,000\,007$.

## Sample 1

### Input

```text
3 2
```

### Output

```text
4```

### Giải thích

- Vòng $3$ hạt với $2$ màu trắng đen, xét theo phép quay.
- Liệt kê tay: ba hạt cùng trắng; ba hạt cùng đen; hai trắng một đen; hai đen một trắng (mọi vị trí hạt lẻ đều xoay được về nhau).
- Có $4$ mẫu phân biệt nên chương trình in ra $4$.

## Ràng buộc

- $1 \le N, K \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
