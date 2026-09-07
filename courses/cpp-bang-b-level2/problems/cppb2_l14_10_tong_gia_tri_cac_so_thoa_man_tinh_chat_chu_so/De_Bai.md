# Tổng chữ số trên đoạn (digit sum range)

## Bối cảnh

Trung tâm dữ liệu căn cước kiểm tra tính toàn vẹn của lô hồ sơ mới bằng cách cộng toàn bộ các chữ số trong mã số của mọi hồ sơ thuộc đoạn liên tiếp rồi so với mã băm đã niêm phong từ trước. Nếu hai giá trị khớp nhau thì lô hồ sơ được duyệt tự động mà không cần mở từng bìa hồ sơ ra đối chiếu. Chương trình quy hoạch động chữ số cho ra tổng này gần như tức thì kể cả với đoạn dài hàng nghìn tỉ.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình tính tổng các chữ số của tất cả các số $x$ ($L \le x \le R$), rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($0 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là tổng cần tính (dùng số nguyên 64-bit).

## Sample 1

### Input

```text
1 13
```

### Output

```text
55
```

### Giải thích

- Tổng chữ số từ $1$ đến $9$ là $1+2+\dots+9 = 45$.
- Bốn số tiếp theo đóng góp $1 + 2 + 3 + 4 = 10$ (tổng chữ số của $10, 11, 12, 13$).
- Tổng chung $45 + 10 = 55$ nên chương trình in ra $55$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
