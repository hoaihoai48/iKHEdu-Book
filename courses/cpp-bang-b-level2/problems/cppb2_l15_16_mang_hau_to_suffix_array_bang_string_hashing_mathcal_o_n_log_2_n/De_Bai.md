# Mảng hậu tố bằng hashing (n log^2 n)

## Bối cảnh

Thư viện số quốc gia lập chỉ mục tra cứu cho cuốn từ điển khổng lồ bằng cách xếp mọi hậu tố của văn bản theo thứ tự từ điển để tìm kiếm tiền tố trong thời gian logarit. Mỗi truy vấn tìm kiếm cần biết thứ hạng của từng hậu tố, tức mảng hậu tố của toàn bộ văn bản. Thuật toán tiền tố nhân đôi kết hợp hàm băm để so sánh nhanh giúp xây dựng mảng hậu tố trong thời gian N log bình phương N.

## Nhiệm vụ

Cho xâu $S$. Hãy lập trình xây dựng mảng hậu tố, tức dãy chỉ số bắt đầu (đánh số từ $0$) của các hậu tố khi xếp theo thứ tự từ điển, rồi in ra trên một dòng.

## Input

- Dòng duy nhất: xâu $S$ ($1 \le |S| \le 2 \cdot 10^5$).

## Output

- In ra một dòng duy nhất gồm $|S|$ số là mảng hậu tố.

## Sample 1

### Input

```text
banana
```

### Output

```text
5 3 1 0 4 2```

### Giải thích

- Sáu hậu tố của $banana$ xếp từ điển: $a$ (vị trí $5$), $ana$ (vị trí $3$), $anana$ (vị trí $1$), $banana$ (vị trí $0$), $na$ (vị trí $4$), $nana$ (vị trí $2$).
- Dãy chỉ số tương ứng là $5\ 3\ 1\ 0\ 4\ 2$.
- Chương trình in ra đúng dãy này.

## Ràng buộc

- $1 \le |S| \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
