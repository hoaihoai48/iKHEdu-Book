# Duy trì trung vị động (running median)

## Bối cảnh

Trạm cân của hợp tác xã ghi lại khối lượng từng bao lúa mà bà con chở đến nhập kho trong ngày, các bao đến nối tiếp nhau không ngừng từ sáng đến tối. Sau mỗi bao lúa vừa cân, kế toán muốn biết ngay trung vị của tất cả các bao đã cân từ đầu ngày: trung vị là giá trị đứng giữa khi xếp mọi bao theo thứ tự (với số lượng bao chẵn thì lấy giá trị nhỏ hơn trong hai giá trị giữa).

## Nhiệm vụ

Cho $N$ số nguyên đến lần lượt theo thời gian. Sau mỗi số vừa đến, xét toàn bộ các số đã thấy và tìm trung vị của chúng (sắp xếp tăng dần; số lượng lẻ lấy phần tử giữa, số lượng chẵn lấy phần tử nhỏ hơn trong hai phần tử giữa). Hãy lập trình in ra trung vị sau mỗi lần thêm một số.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số bao lúa.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^9$), là khối lượng từng bao theo thứ tự.

## Output

- In ra $N$ dòng, dòng thứ $i$ là trung vị của $i$ số đầu tiên.

## Sample 1

### Input

```text
4
5 15 1 3
```

### Output

```text
5
5
5
3
```

### Giải thích

- Sau bao đầu $5$: chỉ có một số nên trung vị là $5$.
- Sau hai bao $5, 15$: xếp lại $5, 15$, số lượng chẵn nên lấy giá trị nhỏ hơn trong hai giữa là $5$.
- Sau ba bao $5, 15, 1$: xếp lại $1, 5, 15$, phần tử giữa là $5$.
- Sau bốn bao $5, 15, 1, 3$: xếp lại $1, 3, 5, 15$, hai giá trị giữa là $3$ và $5$ nên lấy $3$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
