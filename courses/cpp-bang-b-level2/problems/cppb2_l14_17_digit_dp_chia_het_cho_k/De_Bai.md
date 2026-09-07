# Đếm số chia hết cho K trong đoạn

## Bối cảnh

Kho bạc nhà nước in séc du lịch theo dải số liên tiếp và quy định séc mệnh giá đặc biệt phải có số sê ri chia hết cho đúng K để máy kiểm đếm tự động phân loại vào khay riêng. Mỗi đợt phát hành xét một đoạn số và cần đếm có bao nhiêu sê ri đạt chuẩn nhằm chuẩn bị đủ khay đựng và tem niêm phong. Chương trình quy hoạch động ghi nhớ số dư theo mô-đun K giúp đếm nhanh đoạn dài tới hàng nghìn tỉ.

## Nhiệm vụ

Cho ba số nguyên $L, R, K$. Hãy lập trình đếm các số $x$ ($L \le x \le R$, $x > 0$) chia hết cho $K$, rồi in ra kết quả.

## Input

- Dòng duy nhất: ba số nguyên $L, R, K$ ($0 \le L \le R \le 10^{18}$, $1 \le K \le 100$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn.

## Sample 1

### Input

```text
1 20 3
```

### Output

```text
6
```

### Giải thích

- Các số từ $1$ đến $20$ chia hết cho $3$ là $3, 6, 9, 12, 15, 18$.
- Đếm được sáu số, số $0$ không nằm trong đoạn nên không ảnh hưởng.
- Chương trình in ra $6$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$; $1 \le K \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
