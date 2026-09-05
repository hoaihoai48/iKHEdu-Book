# Tam giác sao cân


## Bối cảnh

Vẽ tam giác cân bằng dấu sao `*` với chiều cao $N$. Mỗi hàng cần tính số khoảng trắng và số sao phù hợp để hình tam giác cân đối.

## Nhiệm vụ

In ra một tháp sao tam giác cân đối xứng có độ cao $N$.
* **Quy luật:** Dòng thứ $i$ (từ 1 đến $N$) có $(N - i)$ dấu cách phía trước, tiếp theo là $(2i - 1)$ dấu sao `*`.
## Input

Độ cao $N$ của tam giác ($1 \le N \le 20$).
## Output

Tháp sao tam giác cân có $N$ dòng đúng quy luật trên.
## Sample 1

### Input
```text
3
```
### Output
```text
  *
 ***
*****
```
### Giải thích

Với dữ liệu đầu vào là `3`, kết quả thu được tương ứng là `*
 ***
*****`.



## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
