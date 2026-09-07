# Hình chữ nhật lớn nhất dưới biểu đồ cột (histogram)

## Bối cảnh

Khu hội chợ xuân dựng một dãy các gian hàng san sát nhau với chiều cao mái che khác nhau. Ban tổ chức muốn căng một tấm bạt quảng cáo hình chữ nhật lớn nhất có thể nằm gọn dưới các mái che này, với cạnh đáy đặt trên mặt đất và không được vượt quá chiều cao của bất kỳ gian hàng nào mà nó che phủ. Tấm bạt càng to thì logo nhà tài trợ càng nổi bật, nên ban tổ chức cần tính chính xác diện tích lớn nhất.

## Nhiệm vụ

Cho $N$ số nguyên là chiều cao của từng gian hàng theo thứ tự. Một hình chữ nhật hợp lệ gồm một đoạn gian hàng liên tiếp với chiều cao bằng chiều cao của gian thấp nhất trong đoạn. Hãy lập trình tính diện tích lớn nhất, rồi in ra diện tích đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số gian hàng.
- Dòng thứ hai chứa $N$ số nguyên $h_i$ ($1 \le h_i \le 10^6$), là chiều cao từng gian.

## Output

- In ra một số nguyên duy nhất là diện tích lớn nhất.

## Sample 1

### Input

```text
6
2 1 5 6 2 3
```

### Output

```text
10
```

### Giải thích

- Xét các hình chữ nhật ứng với từng gian làm chiều cao giới hạn.
- Lấy chiều cao $5$ phủ hai gian $5, 6$ được diện tích $5 \times 2 = 10$.
- Lấy chiều cao $2$ của gian thứ năm phủ bốn gian $5, 6, 2, 3$ được $2 \times 4 = 8$; lấy chiều cao $1$ phủ cả sáu gian được $1 \times 6 = 6$.
- Mọi hình chữ nhật hợp lệ khác đều có diện tích không vượt quá $10$, nên đáp án là $10$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le h_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
