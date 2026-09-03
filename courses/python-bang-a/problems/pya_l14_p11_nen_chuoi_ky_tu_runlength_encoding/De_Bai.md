# Nén Chuỗi Ký Tự (Run-Length Encoding)


*(Đề thi Tin học trẻ Bảng A)*

## Bối cảnh

Thuật toán nén chuỗi đơn giản thay thế một dãy các ký tự giống nhau liên tiếp bằng ký tự đó kèm theo số lần lặp lại.
  Ví dụ: `AAABBC` nén thành `A3B2C1`.
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


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
