# Nối dây tiết kiệm bằng priority queue

## Bối cảnh

Công ty viễn thông cần nối các đoạn cáp quang rời rạc dưới đáy biển thành một tuyến cáp liên tục duy nhất để truyền tín hiệu ra đảo. Mỗi lần hàn nối hai đoạn cáp tốn chi phí đúng bằng tổng độ dài của hai đoạn đem nối, và đoạn cáp tạo thành có thể đem hàn tiếp với các đoạn khác. Giám đốc kỹ thuật muốn chọn thứ tự hàn nối sao cho tổng chi phí sau tất cả các lần hàn là thấp nhất.

## Nhiệm vụ

Cho $N$ số nguyên là độ dài của từng đoạn cáp ban đầu. Mỗi lần được hàn nối hai đoạn thành một với chi phí bằng tổng độ dài của chúng. Hãy lập trình tính tổng chi phí nhỏ nhất để nối tất cả thành một đoạn duy nhất, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số đoạn cáp.
- Dòng thứ hai chứa $N$ số nguyên $x_i$ ($1 \le x_i \le 10^6$), là độ dài từng đoạn.

## Output

- In ra một số nguyên duy nhất là tổng chi phí hàn nối nhỏ nhất.

## Sample 1

### Input

```text
4
4 3 2 6
```

### Output

```text
29
```

### Giải thích

- Hàn hai đoạn ngắn nhất $2$ và $3$ tốn $2 + 3 = 5$, còn lại các đoạn $4, 5, 6$.
- Hàn hai đoạn $4$ và $5$ tốn $4 + 5 = 9$, còn lại các đoạn $6, 9$.
- Hàn hai đoạn cuối $6$ và $9$ tốn $6 + 9 = 15$, chỉ còn một tuyến cáp duy nhất.
- Tổng chi phí là $5 + 9 + 15 = 29$, và mọi thứ tự hàn khác đều tốn từ $29$ trở lên.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le x_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
