# SOS DP Tổng Trên Tập Con (Cộng Dồn Theo Nhóm)

## Bối cảnh

Phòng khảo sát thị trường của thành phố lưu điểm đánh giá cho từng nhóm đối tượng, mỗi nhóm được đánh dấu bằng một dãy bit cho biết gồm những đặc điểm nào trong $N$ đặc điểm khảo sát. Khi cần báo cáo cho một nhóm lớn, phòng phải cộng dồn điểm của mọi nhóm nhỏ nằm gọn trong nó, tức mọi nhóm mà tập đặc điểm là tập con của nhóm lớn. Vì số nhóm lên tới hàng chục nghìn, phòng cần một chương trình tính sẵn toàn bộ các tổng cộng dồn này để tra cứu tức thì.

## Nhiệm vụ

Cho số nguyên $N$ và $2^N$ số nguyên $f$, trong đó $f[mask]$ là điểm của nhóm có mặt nạ bit $mask$. Hãy lập trình tính, với mỗi mặt nạ $mask$, tổng điểm của mọi nhóm con $sub$ nằm gọn trong $mask$, rồi in ra $2^N$ tổng đó theo thứ tự mặt nạ tăng dần.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 20$), là số đặc điểm khảo sát.
- Dòng thứ hai chứa $2^N$ số nguyên $f_i$ ($0 \le f_i \le 10^6$), là điểm của từng nhóm theo thứ tự mặt nạ từ $0$ đến $2^N - 1$.

## Output

- In ra $2^N$ số nguyên trên một dòng, số thứ $mask$ là tổng điểm của mọi nhóm con nằm trong $mask$.

## Sample 1

### Input

```text
2
5 1 4 2
```

### Output

```text
5 6 9 12
```

### Giải thích

- Bốn nhóm ứng với bốn mặt nạ $00$, $01$, $10$, $11$ có điểm lần lượt $5, 1, 4, 2$.
- Nhóm $00$ chỉ chứa chính nó nên tổng là $5$.
- Nhóm $01$ chứa $00$ và $01$ nên tổng là $5 + 1 = 6$.
- Nhóm $10$ chứa $00$ và $10$ nên tổng là $5 + 4 = 9$.
- Nhóm $11$ chứa cả bốn nhóm nên tổng là $5 + 1 + 4 + 2 = 12$.

## Ràng buộc

- $1 \le N \le 20$, $0 \le f_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
