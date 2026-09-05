# Số đặc biệt chia hết cho tổng chữ số (Harshad number)


## Bối cảnh

Bạn Tí rất thích sưu tầm các con số kỳ lạ trong cuốn sổ tay toán học của mình. Hôm nay, bạn phát hiện một loại số đặc biệt: một số tự nhiên $N$ được gọi là số Harshad nếu nó chia hết cho chính tổng các chữ số của nó. Ví dụ: số 18 có tổng các chữ số là $1 + 8 = 9$. Vì 18 chia hết cho 9 nên 18 là số Harshad. Bạn Tí đố cả lớp tìm thêm các số như vậy, hãy cả lớp kiểm tra.
## Nhiệm vụ

Cho số $N$. In `YES` nếu $N$ là số Harshad, ngược lại in `NO`.
## Input

Số nguyên $N$ ($1 \le N \le 10^9$).
## Output

`YES` hoặc `NO`.
## Sample 1

### Input
```text
18
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `18`, kết quả thu được tương ứng là `YES`.

## Sample 2

### Input
```text
19
```
### Output
```text
`NO` ($1+9=10$, 19 không chia hết cho 10)
```


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
