# Tính giai thừa N cho N tới 1000

## Bối cảnh

Câu lạc bộ toán học của trường chuẩn bị tài liệu về các số khổng lồ cho buổi sinh hoạt chuyên đề hoán vị và chỉnh hợp với học sinh khối chuyên. Thầy chủ nhiệm cần in chính xác giá trị của N giai thừa với N lên tới một nghìn để treo lên bảng triển lãm, con số này có tới hàng nghìn chữ số nên kiểu dữ liệu thông thường không thể chứa nổi. Chương trình nhân số lớn liên tiếp từ 1 đến N cho ra kết quả chính xác tuyệt đối.

## Nhiệm vụ

Cho số nguyên $N$. Hãy lập trình tính $N! = 1 \times 2 \times \dots \times N$ với độ chính xác tuyệt đối, rồi in ra kết quả.

## Input

- Dòng duy nhất: số nguyên $N$ ($0 \le N \le 1000$).

## Output

- In ra một dòng duy nhất là $N!$ (quy ước $0! = 1$).

## Sample 1

### Input

```text
10
```

### Output

```text
3628800```

### Giải thích

- Tính tay $10! = 1 \times 2 \times \dots \times 10$: tích tới $5$ được $120$, nhân tiếp $6$ được $720$, nhân $7$ được $5040$, nhân $8$ được $40320$, nhân $9$ được $362880$, nhân $10$ được $3628800$.
- Kết quả có bảy chữ số và vừa khít kiểu số thường nhưng chương trình phải đúng tới $N = 1000$.
- In ra $3628800$.

## Ràng buộc

- $0 \le N \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
