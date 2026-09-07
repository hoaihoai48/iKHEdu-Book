# Tối ưu hóa quy hoạch động bằng monotonic deque

## Bối cảnh

Cửa hàng điện máy ghi lại doanh số bán hàng của $N$ ngày liên tiếp trong tháng khuyến mãi lớn nhất năm. Với mỗi khoảng thời gian liên tục, cửa hàng quan tâm đến ngày ế ẩm nhất trong khoảng đó, vì đó chính là điểm yếu cần khắc phục của chiến dịch quảng cáo. Tổng doanh số thấp nhất của tất cả các khoảng thời gian cho thấy toàn cảnh những ngày bán chậm, giúp giám đốc quyết định có nên kéo dài chương trình giảm giá thêm một tuần nữa hay không.

## Nhiệm vụ

Cho $N$ số nguyên là doanh số mỗi ngày. Với mỗi đoạn liên tục, lấy giá trị nhỏ nhất trong đoạn. Hãy lập trình tính tổng các giá trị nhỏ nhất này trên mọi đoạn liên tục theo modulo $1\,000\,000\,007$, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số ngày.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^6$), là doanh số mỗi ngày.

## Output

- In ra tổng các giá trị nhỏ nhất trên mọi đoạn liên tục theo modulo $1\,000\,000\,007$.

## Sample 1

### Input

```text
4
3 1 2 4
```

### Output

```text
17
```

### Giải thích

- Liệt kê cả $10$ đoạn liên tục cùng giá trị nhỏ nhất của từng đoạn.
- Bốn đoạn một ngày cho $3, 1, 2, 4$; ba đoạn hai ngày $[3, 1]$, $[1, 2]$, $[2, 4]$ cho $1, 1, 2$.
- Hai đoạn ba ngày $[3, 1, 2]$, $[1, 2, 4]$ cho $1, 1$; đoạn bốn ngày cho $1$.
- Tổng là $3 + 1 + 2 + 4 + 1 + 1 + 2 + 1 + 1 + 1 = 17$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le a_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
