# Tối ưu hóa mua bán cổ phiếu không giới hạn lần giao dịch

## Bối cảnh

Anh Tuấn làm nghề môi giới chứng khoán và theo dõi giá một mã cổ phiếu trong $N$ ngày liên tiếp. Anh được phép mua đi bán lại nhiều lần tùy ý, mỗi lần nắm giữ tối đa một cổ phiếu và phải bán ra trước khi mua lượt mới. Anh muốn biết với lịch sử giá đã biết trước này thì khoản lãi lớn nhất có thể kiếm được là bao nhiêu, để rút kinh nghiệm chọn thời điểm vào lệnh cho những đợt sóng sau và báo cáo lại với nhóm khách hàng thân thiết.

## Nhiệm vụ

Cho $N$ số nguyên là giá cổ phiếu mỗi ngày. Được thực hiện bao nhiêu lượt mua bán tùy ý (mua trước bán sau, không nắm giữ quá một cổ phiếu tại một thời điểm). Hãy lập trình tính tổng lợi nhuận lớn nhất có thể đạt được, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số ngày.
- Dòng thứ hai chứa $N$ số nguyên $p_i$ ($1 \le p_i \le 10^6$), là giá cổ phiếu mỗi ngày.

## Output

- In ra một số nguyên duy nhất là lợi nhuận lớn nhất.

## Sample 1

### Input

```text
6
7 1 5 3 6 4
```

### Output

```text
7
```

### Giải thích

- Ngày giá $7$ xuống $1$ thì đứng ngoài thị trường, chưa mua gì.
- Mua ở giá $1$ rồi bán ở giá $5$, lãi $5 - 1 = 4$.
- Giá xuống $3$ thì mua vào, rồi bán ở giá $6$, lãi thêm $6 - 3 = 3$.
- Ngày cuối giá $4$ thấp hơn giá bán nên không mua nữa.
- Tổng lãi là $4 + 3 = 7$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le p_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
