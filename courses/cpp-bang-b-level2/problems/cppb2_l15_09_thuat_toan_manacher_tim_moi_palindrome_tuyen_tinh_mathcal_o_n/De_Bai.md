# Đếm mọi xâu con đối xứng (Manacher)

## Bối cảnh

Xưởng sản xuất tem nhãn dán lên bao bì cần thống kê mọi đoạn mã đối xứng trong mã vạch sản phẩm để chọn ra các đoạn đẹp làm tem chống giả cho dòng hàng cao cấp. Mỗi mã vạch là một xâu ký tự và mọi xâu con liên tiếp đọc xuôi ngược giống nhau đều được tính, kể cả các đoạn chỉ dài một ký tự hay các đoạn giao nhau. Thuật toán Manacher đếm toàn bộ trong thời gian tuyến tính nhờ tận dụng tính đối xứng đã tính được.

## Nhiệm vụ

Cho xâu $S$. Hãy lập trình đếm tổng số xâu con liên tiếp của $S$ đọc xuôi ngược giống nhau bằng thuật toán Manacher, rồi in ra kết quả.

## Input

- Dòng duy nhất: xâu $S$ ($1 \le |S| \le 10^6$).

## Output

- In ra một dòng duy nhất là tổng số xâu con đối xứng (dùng số nguyên 64-bit).

## Sample 1

### Input

```text
aaa
```

### Output

```text
6```

### Giải thích

- Xâu $aaa$: ba xâu con độ dài một là $a$ ở mỗi vị trí đều đối xứng.
- Hai xâu con độ dài hai là $aa$ (vị trí $1$-$2$ và $2$-$3$) đều đối xứng.
- Một xâu con độ dài ba là $aaa$ cũng đối xứng, tổng $3+2+1 = 6$ nên in ra $6$.

## Ràng buộc

- $1 \le |S| \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
