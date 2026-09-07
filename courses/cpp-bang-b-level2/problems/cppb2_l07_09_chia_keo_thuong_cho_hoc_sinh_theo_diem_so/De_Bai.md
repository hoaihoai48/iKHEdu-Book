# Chia kẹo thưởng cho học sinh theo điểm số

## Bối cảnh

Cuối năm học, cô giáo chủ nhiệm mua một túi kẹo lớn để thưởng cho cả lớp theo kết quả thi đua. Lớp có $N$ bạn ngồi thành một hàng dài, mỗi bạn có một điểm thi đua khác nhau đã được tổng kết. Để các bạn đều vui vẻ, cô đặt ra quy tắc: mỗi bạn đều được ít nhất một viên kẹo, và bạn nào có điểm cao hơn bạn ngồi ngay cạnh thì phải được nhiều kẹo hơn bạn đó. Cô muốn dùng càng ít kẹo càng tốt mà vẫn giữ đúng quy tắc công bằng này.

## Nhiệm vụ

Cho $N$ số nguyên là điểm thi đua của từng bạn theo thứ tự chỗ ngồi. Hãy lập trình chia cho mỗi bạn một số viên kẹo (ít nhất một viên) sao cho bạn điểm cao hơn bạn kề bên luôn được nhiều kẹo hơn, tổng số kẹo ít nhất, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số học sinh.
- Dòng thứ hai chứa $N$ số nguyên $r_i$ ($1 \le r_i \le 10^6$), là điểm thi đua của từng bạn.

## Output

- In ra một số nguyên duy nhất là tổng số kẹo ít nhất cần dùng.

## Sample 1

### Input

```text
5
1 2 3 4 5
```

### Output

```text
15
```

### Giải thích

- Điểm của năm bạn tăng dần từ trái sang phải nên mỗi bạn đều phải nhiều kẹo hơn bạn bên trái.
- Bạn đầu hàng được $1$ viên, bạn thứ hai được $2$ viên, rồi $3$, $4$ viên cho hai bạn tiếp theo.
- Bạn cuối hàng có điểm cao nhất nên được $5$ viên, nhiều hơn $4$ viên của bạn kề bên.
- Tổng số kẹo là $1 + 2 + 3 + 4 + 5 = 15$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le r_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
