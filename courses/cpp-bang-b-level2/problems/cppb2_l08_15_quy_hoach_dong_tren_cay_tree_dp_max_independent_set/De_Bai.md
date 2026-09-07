# Quy hoạch động trên cây (Tree dp: max independent set)

## Bối cảnh

Công ty tổ chức sự kiện muốn mời một nhóm khách mời từ danh sách bạn bè của giám đốc, mà mối quan hệ bạn bè giữa họ tạo thành một cấu trúc cây không có vòng tròn. Mỗi người có một mức độ ảnh hưởng khác nhau đã được phòng truyền thông chấm điểm, nhưng hai người là bạn trực tiếp của nhau không thể cùng mời. Công ty muốn chọn ra nhóm khách đôi một không phải bạn trực tiếp sao cho tổng điểm ảnh hưởng là lớn nhất.

## Nhiệm vụ

Cho một cây gồm $N$ đỉnh (đánh số từ $1$ đến $N$), mỗi đỉnh có giá trị $val_i$, và $N - 1$ cạnh. Hãy lập trình chọn một tập đỉnh đôi một không kề nhau có tổng giá trị lớn nhất, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số người.
- Dòng thứ hai chứa $N$ số nguyên $val_i$ ($1 \le val_i \le 10^6$), là điểm ảnh hưởng của từng người.
- $N - 1$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u, v$ ($1 \le u, v \le N$), là một cặp bạn trực tiếp.

## Output

- In ra một số nguyên duy nhất là tổng giá trị lớn nhất.

## Sample 1

### Input

```text
5
10 20 30 40 50
1 2
1 3
3 4
3 5
```

### Output

```text
110
```

### Giải thích

- Người $1$ bạn với $2$ và $3$; người $3$ bạn với $4$ và $5$.
- Chọn nhóm $\{2, 4, 5\}$: không ai là bạn trực tiếp của ai trong nhóm, tổng điểm $20 + 40 + 50 = 110$.
- Mọi nhóm hợp lệ khác đều có tổng không vượt quá $110$, ví dụ nhóm $\{1, 4, 5\}$ chỉ được $10 + 40 + 50 = 100$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le val_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
