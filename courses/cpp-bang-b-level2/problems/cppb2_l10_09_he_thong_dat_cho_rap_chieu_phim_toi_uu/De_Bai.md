# Hệ thống đặt chỗ rạp chiếu phim tối ưu

## Bối cảnh

Liên hoan phim quốc tế nhận được $N$ hồ sơ đăng ký tham dự từ các đoàn làm phim, mỗi hồ sơ ghi ba thông tin: năm sản xuất, thời lượng và kinh phí của bộ phim. Để lập danh sách chiếu theo thứ tự công bằng, ban tổ chức quyết định sắp xếp toàn bộ hồ sơ theo thứ tự từ điển của bộ ba thông tin (so sánh năm sản xuất trước, rồi đến thời lượng, cuối cùng là kinh phí). Danh sách sau sắp xếp sẽ được dán công khai.

## Nhiệm vụ

Cho $N$ bộ ba số nguyên $(x_i, y_i, z_i)$. Hãy lập trình sắp xếp chúng theo thứ tự từ điển tăng dần (so $x$ trước, $x$ bằng nhau thì so $y$, $y$ bằng nhau thì so $z$), rồi in ra $N$ bộ theo thứ tự đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số hồ sơ.
- $N$ dòng tiếp theo, mỗi dòng chứa ba số nguyên $x_i, y_i, z_i$ ($-10^9 \le x_i, y_i, z_i \le 10^9$), là thông tin một bộ phim.

## Output

- In ra $N$ dòng theo thứ tự đã sắp xếp, mỗi dòng một bộ ba.

## Sample 1

### Input

```text
3
2 1 3
1 5 2
2 1 1
```

### Output

```text
1 5 2
2 1 1
2 1 3
```

### Giải thích

- So sánh ba bộ theo thành phần đầu tiên: $(1, 5, 2)$ có $1$ nhỏ nhất nên đứng đầu.
- Hai bộ còn lại cùng có thành phần đầu là $2$ và thành phần thứ hai là $1$, xét tiếp thành phần thứ ba: $1$ nhỏ hơn $3$ nên $(2, 1, 1)$ đứng trước $(2, 1, 3)$.

## Ràng buộc

- $1 \le N \le 10^5$, $-10^9 \le x_i, y_i, z_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
