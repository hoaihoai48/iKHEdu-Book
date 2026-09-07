# Hứng nước mưa đa chiều (trapping rain water)

## Bối cảnh

Sau cơn mưa lớn đầu mùa, con đường làng lồi lõm thành nhiều mô đất cao thấp khác nhau, mỗi đoạn cao một số mét nhất định. Nước mưa đọng lại trong các chỗ trũng giữa những mô đất cao mà không thoát đi được, tạo thành nhiều vũng nước lớn nhỏ. Đội thanh niên tình nguyện muốn ước tính tổng lượng nước đọng lại trên cả con đường để điều máy bơm đi hút, vì nước tù đọng lâu ngày sẽ sinh muỗi gây bệnh cho cả xóm.

## Nhiệm vụ

Cho $N$ số nguyên là chiều cao mặt đất của từng đoạn đường theo thứ tự. Sau cơn mưa, mỗi đoạn giữ lại lượng nước bằng độ cao mực nước chung quanh trừ đi chiều cao của nó (nếu dương). Hãy lập trình tính tổng lượng nước đọng lại trên toàn bộ con đường, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số đoạn đường.
- Dòng thứ hai chứa $N$ số nguyên $h_i$ ($0 \le h_i \le 10^6$), là chiều cao từng đoạn.

## Output

- In ra một số nguyên duy nhất là tổng lượng nước đọng lại.

## Sample 1

### Input

```text
6
4 2 0 3 2 5
```

### Output

```text
9
```

### Giải thích

- Hai mô cao $4$ và $5$ ở hai đầu giữ nước lại ở bốn đoạn giữa.
- Đoạn cao $2$ giữ được $4 - 2 = 2$; đoạn cao $0$ giữ được $4 - 0 = 4$.
- Đoạn cao $3$ giữ được $4 - 3 = 1$; đoạn cao $2$ giữ được $4 - 2 = 2$.
- Tổng lượng nước là $2 + 4 + 1 + 2 = 9$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le h_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
