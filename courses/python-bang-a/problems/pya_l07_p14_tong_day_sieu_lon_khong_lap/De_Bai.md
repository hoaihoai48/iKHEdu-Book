# Tổng Dãy Siêu Lớn Không Lặp


## Bối cảnh

Trong hội thi Tin học trẻ của trường, ban giám khảo đố cả lớp một số $N$ cực lớn lên tới $10^9$ ($1$ tỷ) bạn nào cũng tròn mắt ngạc nhiên. Cô giáo dặn rằng nếu em dùng vòng lặp `for i in range(1, N + 1):` thì chương trình sẽ bị chạy quá thời gian quy định (Time Limit Exceeded - TLE) vì máy tính phải lặp 1 tỷ lần mất hơn 10 giây! Cả lớp đang loay hoay chưa biết làm sao cho nhanh. Em hãy giúp cả lớp tìm cách tính thật nhanh nhé!
## Nhiệm vụ

Hãy tính tổng $S = 1 + 2 + \dots + N$ với thời gian chạy tức thì ($< 0.001$ giây) bằng công thức toán học.
## Input

Một số nguyên $N$ ($1 \le N \le 10^9$).
## Output

Giá trị tổng $S$.
## Sample 1

### Input
```text
1000000000
```
### Output
```text
500000000500000000
```
## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$