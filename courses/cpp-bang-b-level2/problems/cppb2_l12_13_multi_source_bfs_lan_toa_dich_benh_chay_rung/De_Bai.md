# BFS đa nguồn lan tỏa cháy rừng

## Bối cảnh

Chi cục kiểm lâm theo dõi khu rừng hình chữ nhật R hàng C cột, trong đó một số ô đang bốc cháy được vệ tinh phát hiện vào buổi sáng. Mỗi giờ ngọn lửa lan sang bốn ô kề cạnh chưa cháy và không phải là hồ nước cản lửa. Ban chỉ huy cần biết sau bao nhiêu giờ toàn bộ khu rừng sẽ cháy hết để điều xe cứu hỏa, hoặc xác định có vùng rừngicho an toàn không bao giờ bị cháy tới.

## Nhiệm vụ

Cho lưới $R \times C$ gồm các ô $.$ (rừng), $\#$ (hồ nước), $F$ (đang cháy). Hãy lập trình tính, bằng BFS đa nguồn, thời gian để lửa lan hết các ô rừng; in ra $-1$ nếu có ô rừng không bao giờ cháy tới.

## Input

- Dòng 1: hai số nguyên $R, C$ ($1 \le R, C \le 1000$).
- $R$ dòng tiếp theo, mỗi dòng là một chuỗi $C$ ký tự thuộc $\{., \#, F\}$.

## Output

- In ra một dòng duy nhất là số giờ lan hết lửa, hoặc $-1$.

## Sample 1

### Input

```text
3 3
...
.F.
...
```

### Output

```text
2```

### Giải thích

- Lửa khởi phát tại ô giữa $(2,2)$, giờ đầu lan ra bốn ô kề cạnh.
- Giờ thứ hai lan tiếp ra bốn ô góc, toàn bộ tám ô rừng còn lại đều đã cháy.
- Tổng thời gian là $2$ giờ nên chương trình in ra $2$.

## Ràng buộc

- $1 \le R, C \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
