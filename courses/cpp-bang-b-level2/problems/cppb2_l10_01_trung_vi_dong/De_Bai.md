# Duy trì trung vị động

## Bối cảnh

Một mạng lưới cảm biến gửi nhiệt độ về trung tâm theo từng lượt, mỗi lượt một số liệu mới được thêm vào sổ theo dõi. Sau mỗi lượt, người trực cần biết ngay giá trị ở giữa của toàn bộ số liệu đã nhận cho tới lúc đó để nắm mức nhiệt điển hình, tránh bị lệch bởi vài số liệu quá cao hay quá thấp. Vì số liệu đến dồn dập và sổ ngày càng dày, trung tâm cần một chương trình tự động in ra giá trị ở giữa sau mỗi lần ghi nhận số mới.

## Nhiệm vụ

Cho số nguyên $N$ và dãy $N$ số nguyên $A_1, A_2, \dots, A_N$ theo đúng thứ tự đó. Hãy lập trình in ra $N$ giá trị, trong đó giá trị thứ $i$ là trung vị của $i$ số đầu tiên $A_1, \dots, A_i$. Quy ước trung vị: sắp xếp các số đang có theo thứ tự không giảm; nếu số lượng là lẻ thì lấy số đứng chính giữa, nếu số lượng là chẵn thì lấy số nhỏ hơn trong hai số đứng giữa.

## Input

- Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$, các số cách nhau bởi dấu cách.

## Output

- In ra $N$ số nguyên trên cùng một dòng, cách nhau bởi dấu cách: số thứ $i$ là trung vị của $i$ số đầu tiên theo quy ước trên.

## Sample 1

### Input

```text
4
5 15 1 3
```

### Output

```text
5 5 5 3
```

### Giải thích

Thêm từng số và sắp xếp lại các số đã có để tìm số đứng giữa:

- Sau số thứ nhất: tập số là $\{5\}$, chỉ có một số nên kết quả là $5$.
- Sau số thứ hai: tập số là $\{5, 15\}$, xếp lại thành $5, 15$; có $2$ số nên lấy số nhỏ hơn trong hai số giữa, tức $5$.
- Sau số thứ ba: tập số là $\{5, 15, 1\}$, xếp lại thành $1, 5, 15$; có $3$ số nên lấy số chính giữa là $5$.
- Sau số thứ tư: tập số là $\{5, 15, 1, 3\}$, xếp lại thành $1, 3, 5, 15$; có $4$ số, hai số giữa là $3$ và $5$, lấy số nhỏ hơn là $3$.

Dãy kết quả theo từng bước là $5, 5, 5, 3$.

## Ràng buộc

- $1 \le N \le 10^5$; mỗi $A_i$ là một số nguyên.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
