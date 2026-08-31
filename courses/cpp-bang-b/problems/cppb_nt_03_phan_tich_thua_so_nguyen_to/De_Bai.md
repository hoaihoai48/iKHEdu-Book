# Phân Tích Thừa Số Nguyên Tố

## Bối cảnh
Cho số nguyên dương $N$. Hãy phân tích $N$ thành tích các thừa số nguyên tố theo dạng $p_1^{a_1} \times p_2^{a_2} \dots$.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($2 \le N \le 10^{12}$).

## Output
- In ra phân tích thừa số nguyên tố của $N$ theo thứ tự tăng dần của các ước nguyên tố theo định dạng `p^a`. Nếu $a=1$ vẫn in `p^1`.

## Sample 1
### Input
```text
60
```
### Output
```text
2^2 * 3^1 * 5^1
```
### Giải thích
60 = 4 * 3 * 5 = 2^2 * 3^1 * 5^1.

## Ràng buộc
- $100\%$ số test có $N \le 10^{12}$.\n- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
