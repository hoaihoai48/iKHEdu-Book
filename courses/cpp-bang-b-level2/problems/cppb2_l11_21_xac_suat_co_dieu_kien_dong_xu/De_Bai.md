# Xác suất có điều kiện khi tung đồng xu

## Bối cảnh

Trạm khí tượng thủy văn dùng mô hình tung đồng xu công bằng để mô phỏng chuỗi N ngày nắng mưa trong bản tin dự báo mùa vụ cho bà con nông dân. Sau khi vệ tinh báo đã có ít nhất M ngày nắng trong chuỗi, bà con muốn biết xác suất để chuỗi đó có đúng K ngày nắng là bao nhiêu để quyết định lịch xuống giống. Đài khí tượng cần chương trình in xác suất với sáu chữ số thập phân cho từng bản tin phát sóng.

## Nhiệm vụ

Cho ba số nguyên $N, K, M$. Hãy lập trình tính xác suất để có đúng $K$ mặt ngửa khi tung $N$ đồng xu công bằng, với điều kiện đã biết có ít nhất $M$ mặt ngửa, rồi in ra với đúng sáu chữ số thập phân.

## Input

- Dòng duy nhất: ba số nguyên $N, K, M$ ($1 \le M \le N \le 100$).

## Output

- In ra một dòng duy nhất là xác suất cần tính với đúng sáu chữ số sau dấu chấm thập phân ($0.000000$ khi $K < M$).

## Sample 1

### Input

```text
4 3 2
```

### Output

```text
0.363636
```

### Giải thích

- Tung $4$ đồng xu, biết có ít nhất $2$ mặt ngửa, hỏi xác suất có đúng $3$ mặt ngửa.
- Số kết quả thuận lợi cho đúng $3$ mặt ngửa là $C(4,3) = 4$; số kết quả thuộc điều kiện là $C(4,2)+C(4,3)+C(4,4) = 6+4+1 = 11$.
- Tỉ số $4/11 = 0.363636$ nên chương trình in ra $0.363636$.

## Ràng buộc

- $1 \le M \le N \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
