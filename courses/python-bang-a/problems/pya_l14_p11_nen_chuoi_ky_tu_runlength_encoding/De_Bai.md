# Nén chuỗi ký tự (Run-Length encoding)


*(Đề thi lập trình)*

## Bối cảnh

Bạn Nam gấp thật nhiều ngôi sao giấy cùng màu rồi xếp chúng thành hàng dài trên bàn. Cô giáo dạy thuật toán nén chuỗi đơn giản thay thế một dãy các ký tự giống nhau liên tiếp bằng ký tự đó kèm theo số lần lặp lại.
 Ví dụ: `AAABBC` nén thành `A3B2C1`.
Nam muốn ghi lại hàng ngôi sao thật gọn vào sổ. Hãy giúp bạn Nam viết chương trình nén chuỗi thật gọn.
## Nhiệm vụ

Cho một chuỗi $S$ chỉ gồm các chữ cái in hoa. Hãy in ra dạng nén của chuỗi $S$.
## Input

Một chuỗi $S$ ($1 \le |S| \le 1000$).
## Output

Chuỗi sau khi nén.
## Sample 1

### Input
```text
AAABBCCCC
```
### Output
```text
A3B2C4
```
### Giải thích

Với dữ liệu đầu vào là `AAABBCCCC`, kết quả thu được tương ứng là `A3B2C4`.



## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
