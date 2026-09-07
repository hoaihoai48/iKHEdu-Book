# Đếm cây khung của đồ thị đầy đủ (công thức Cayley)

## Bối cảnh

Tổng công ty viễn thông dự định nối N trạm phát sóng trên quần đảo bằng cáp quang sao cho mọi trạm đều liên thông với nhau mà tổng số tuyến cáp là ít nhất để giảm chi phí bảo trì đường biển. Mỗi phương án đi dây như vậy tạo thành một cây khung của mạng đầy đủ, và hội đồng quản trị cần biết có bao nhiêu phương án để đấu thầu vật tư. Con số này rất lớn nên chỉ cần phần dư cho 1 000 000 007.

## Nhiệm vụ

Cho số nguyên $N$ là số đỉnh của đồ thị đầy đủ. Hãy lập trình tính số cây khung của đồ thị đầy đủ $N$ đỉnh theo công thức Cayley $N^{N-2}$, rồi in ra phần dư khi chia cho $1\,000\,000\,007$ (quy ước đáp án bằng $1$ khi $N \le 2$).

## Input

- Dòng duy nhất: số nguyên $N$ ($1 \le N \le 10^9$).

## Output

- In ra một dòng duy nhất là $N^{N-2} \bmod 1\,000\,000\,007$ (với $N \le 2$ in ra $1$).

## Sample 1

### Input

```text
4
```

### Output

```text
16```

### Giải thích

- Với $N = 4$: công thức Cayley cho $4^{4-2} = 4^2 = 16$.
- Liệt kê tay: mỗi cây khung là một cây có $4$ đỉnh và $3$ cạnh, đếm đủ được $16$ cây phân biệt theo tập cạnh.
- Chương trình in ra $16$.

## Ràng buộc

- $1 \le N \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
