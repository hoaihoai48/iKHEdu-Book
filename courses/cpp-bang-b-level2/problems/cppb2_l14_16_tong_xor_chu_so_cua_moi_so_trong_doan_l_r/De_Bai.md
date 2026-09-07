# Tổng XOR trên mọi cặp mảng

## Bối cảnh

Trung tâm an ninh mạng đánh giá độ phân tán của N khóa phiên trong hệ thống mã hóa đầu cuối bằng cách cộng giá trị XOR của mọi cặp khóa phân biệt để ước lượng mức độ khó đoán của toàn bộ phiên giao dịch. Vì số cặp lên tới hàng chục tỉ nên kỹ sư không thể duyệt từng cặp mà đếm số bit 1 theo từng vị trí bit rồi nhân tổ hợp, lấy phần dư cho 1 000 000 007 để ghi vào báo cáo kiểm định.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$. Hãy lập trình tính tổng $a_i \oplus a_j$ trên mọi cặp $i < j$, rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng 1: số nguyên $N$ ($1 \le N \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên không âm $a_i$ ($0 \le a_i < 2^{60}$).

## Output

- In ra một dòng duy nhất là tổng XOR trên mọi cặp theo modulo $1\,000\,000\,007$.

## Sample 1

### Input

```text
3
1 2 3
```

### Output

```text
6
```

### Giải thích

- Ba cặp phân biệt cho $1 \oplus 2 = 3$, $1 \oplus 3 = 2$ và $2 \oplus 3 = 1$.
- Tổng ba giá trị là $3 + 2 + 1 = 6$.
- Chương trình in ra $6$.

## Ràng buộc

- $1 \le N \le 2 \cdot 10^5$; $0 \le a_i < 2^{60}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
