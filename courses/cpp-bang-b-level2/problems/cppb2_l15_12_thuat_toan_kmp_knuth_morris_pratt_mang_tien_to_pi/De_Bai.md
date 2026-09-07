# Mảng tiền tố PI của KMP

## Bối cảnh

Phòng thí nghiệm ngôn ngữ máy tính xây dựng công cụ gợi ý từ khóa cho trình soạn thảo văn bản với cốt lõi là hàm tiền tố của thuật toán KMP. Với mỗi vị trí trong từ khóa, công cụ cần biết độ dài của tiền tố dài nhất đồng thời cũng là hậu tố để khi gõ sai một ký tự thì con trỏ quay lui ít nhất có thể. Bảng PI này được tính trong thời gian tuyến tính và lưu lại để tái sử dụng cho mọi văn bản người dùng soạn thảo.

## Nhiệm vụ

Cho xâu $P$. Hãy lập trình tính mảng tiền tố $\pi$ của KMP, trong đó $\pi[i]$ là độ dài của tiền tố dài nhất đồng thời là hậu tố của $P[1 \dots i]$, rồi in ra $n$ số trên một dòng.

## Input

- Dòng duy nhất: xâu $P$ gồm chữ cái thường ($1 \le |P| \le 10^6$).

## Output

- In ra một dòng duy nhất gồm $|P|$ số là mảng $\pi$ (đánh số từ $1$).

## Sample 1

### Input

```text
aabaa
```

### Output

```text
0 1 0 1 2```

### Giải thích

- Tiền tố độ dài một $a$: không có khối vừa đầu vừa cuối nên $\pi[1] = 0$.
- Tiền tố $aa$: khối $a$ thỏa mãn nên $\pi[2] = 1$; tiền tố $aab$: không có khối nào nên $\pi[3] = 0$.
- Tiền tố $aaba$: khối $a$ thỏa mãn nên $\pi[4] = 1$; cả xâu $aabaa$: khối $aa$ thỏa mãn nên $\pi[5] = 2$.
- In ra $0\ 1\ 0\ 1\ 2$.

## Ràng buộc

- $1 \le |P| \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
