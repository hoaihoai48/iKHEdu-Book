# SOS DP Tổng Trên Tập Con (Ưu Đãi Theo Giỏ Hàng)

## Bối cảnh

Siêu thị trong khu dân cư phát hành nhiều gói combo ưu đãi, mỗi combo áp dụng cho một tập mặt hàng nhất định và được đánh dấu bằng một dãy bit cho biết gồm những món nào trong $N$ món của siêu thị. Khi khách mang giỏ hàng ra quầy thanh toán, máy tính tiền cần cộng dồn giá trị ưu đãi của mọi combo nằm gọn trong giỏ. Siêu thị cần một chương trình tính sẵn các tổng cộng dồn cho mọi giỏ hàng có thể để việc thanh toán không bị chờ đợi.

## Nhiệm vụ

Cho số nguyên $N$ và $2^N$ số nguyên $f$, trong đó $f[mask]$ là giá trị ưu đãi của combo có mặt nạ bit $mask$. Hãy lập trình tính, với mỗi giỏ hàng $mask$, tổng ưu đãi của mọi combo nằm gọn trong giỏ, rồi in ra $2^N$ tổng đó theo thứ tự mặt nạ tăng dần.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 20$), là số mặt hàng.
- Dòng thứ hai chứa $2^N$ số nguyên $f_i$ ($0 \le f_i \le 10^6$), là giá trị ưu đãi của từng combo theo thứ tự mặt nạ từ $0$ đến $2^N - 1$.

## Output

- In ra $2^N$ số nguyên trên một dòng, số thứ $mask$ là tổng ưu đãi của mọi combo nằm trong giỏ $mask$.

## Sample 1

### Input

```text
2
1 2 3 4
```

### Output

```text
1 3 4 10
```

### Giải thích

- Bốn combo ứng với bốn mặt nạ $00$, $01$, $10$, $11$ có ưu đãi lần lượt $1, 2, 3, 4$.
- Giỏ $00$ chỉ chứa combo $00$ nên tổng là $1$.
- Giỏ $01$ chứa combo $00$ và $01$ nên tổng là $1 + 2 = 3$.
- Giỏ $10$ chứa combo $00$ và $10$ nên tổng là $1 + 3 = 4$.
- Giỏ $11$ chứa cả bốn combo nên tổng là $1 + 2 + 3 + 4 = 10$.

## Ràng buộc

- $1 \le N \le 20$, $0 \le f_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
