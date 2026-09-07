# Lũy thừa nhanh cơ bản

## Bối cảnh

Câu lạc bộ tin học của trường vừa nhận dự án nhỏ cho phòng thí nghiệm mật mã. Mỗi bản tin thử nghiệm mang hai con số: cơ số $A$ tượng trưng cho khóa gốc và số mũ $B$ tượng trưng cho số vòng mã hóa lặp lại. Nhóm cần tính $A^B$ rồi chỉ giữ phần dư khi chia cho $1\,000\,000\,007$. Vì số mũ có thể rất lớn nên phép nhân trực tiếp từng bước sẽ không kịp giờ nộp báo cáo.

## Nhiệm vụ

Cho $T$ cặp số $(A, B)$. Hãy lập trình tính $A^B \bmod 1\,000\,000\,007$ cho mỗi cặp và in kết quả trên một dòng riêng.

## Input

- Dòng đầu tiên chứa số nguyên $T$ ($1 \le T \le 10^5$), là số cặp cần tính.
- $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $A, B$ ($0 \le A, B \le 10^{18}$).

## Output

- Với mỗi cặp $(A, B)$, in ra một dòng là giá trị $A^B \bmod 1\,000\,000\,007$.
- Quy ước $0^0 = 1$.

## Sample 1

### Input

```text
2
2 10
3 13
```

### Output

```text
1024
1594323
```

### Giải thích

- Cặp thứ nhất: $2^{10} = 1024$. Vì $1024$ nhỏ hơn $1\,000\,000\,007$ nên phần dư vẫn là $1024$.
- Cặp thứ hai: tính nháp từng chặng $3^2 = 9$, $3^4 = 9 \times 9 = 81$, $3^8 = 81 \times 81 = 6561$. Từ đó $3^{10} = 3^8 \times 3^2 = 6561 \times 9 = 59049$, và $3^{13} = 3^{10} \times 3^3 = 59049 \times 27 = 1\,594\,323$. Vì kết quả này cũng nhỏ hơn $1\,000\,000\,007$ nên đáp án dòng hai là $1594323$.

## Ràng buộc

- $0 \le A, B \le 10^{18}$, $1 \le T \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
