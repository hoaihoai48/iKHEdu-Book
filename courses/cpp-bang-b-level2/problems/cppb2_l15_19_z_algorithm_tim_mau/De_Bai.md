# Mảng Z (Z-algorithm)

## Bối cảnh

Phòng nghiên cứu ngôn ngữ cổ cần tiền xử lý văn bản bia đá bằng mảng Z để phục vụ hàng loạt truy vấn tìm kiếm mẫu tự động trong dự án số hóa di sản. Với mỗi vị trí trong văn bản, mảng Z ghi lại độ dài của tiền tố dài nhất khớp tại vị trí đó, giúp mọi tìm kiếm mẫu sau này chạy trong thời gian tuyến tính. Thuật toán duy trì khung khớp hiện tại nên toàn bộ quá trình chỉ duyệt văn bản đúng một lần.

## Nhiệm vụ

Cho xâu $S$. Hãy lập trình tính mảng $Z$ bằng Z-algorithm, trong đó $Z[1] = 0$ và $Z[i]$ là độ dài của tiền tố dài nhất của $S$ khớp tại vị trí $i$, rồi in ra $n$ số trên một dòng.

## Input

- Dòng duy nhất: xâu $S$ ($1 \le |S| \le 10^6$).

## Output

- In ra một dòng duy nhất gồm $|S|$ số là mảng $Z$ (đánh số từ $1$).

## Sample 1

### Input

```text
aabaa
```

### Output

```text
0 1 0 2 1
```

### Giải thích

- Vị trí $2$ khớp tiền tố được một ký tự $a$ rồi dừng ở $b$ nên $Z[2] = 1$.
- Vị trí $3$ bắt đầu bằng $b$ khác $a$ nên $Z[3] = 0$; vị trí $4$ khớp $aa$ nên $Z[4] = 2$; vị trí $5$ khớp $a$ nên $Z[5] = 1$.

## Ràng buộc

- $1 \le |S| \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
