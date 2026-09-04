# Dãy Con Liên Tiếp Tăng Dài Nhất


*(Bài toán phân loại Huy chương Vàng Bảng A toàn quốc)*

## Bối cảnh

Các bạn nhỏ lớp 4A đang chơi trò xếp thẻ số thành một hàng dài gồm $N$ số nguyên. Các bạn phát hiện một trò rất vui gọi là "dãy con liên tiếp tăng": đó là một đoạn các phần tử đứng cạnh nhau mà phần tử đứng sau luôn lớn hơn phần tử đứng ngay trước nó ($A_i < A_{i+1} < A_{i+2} \dots$). Ai tìm được đoạn dài nhất sẽ thắng, em hãy giúp các bạn tìm xem đoạn dài nhất có bao nhiêu thẻ số nhé!
## Nhiệm vụ

Hãy tìm độ dài của dãy con liên tiếp tăng dài nhất trong dãy số đã cho.
## Input

  * Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($|A_i| \le 10^9$).
## Output

Một số nguyên duy nhất là độ dài lớn nhất tìm được.
## Sample 1

### Input
```text
6
1 3 5 2 4 7
```
### Output
```text
3
```
### Giải thích

Dãy con tăng dài nhất có độ dài 3 (đoạn `1 3 5` hoặc `2 4 7`).

## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
