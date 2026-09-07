# Fenwick 2D tổng hình chữ nhật

## Bối cảnh

Trung tâm điều phối taxi công nghệ phủ sóng khu vực N hàng M cột với mật độ cuốc xe thay đổi liên tục theo từng ô bản đồ số. Mỗi khi có thêm cuốc xe tại một ô, hệ thống cộng dồn vào ô đó, và điều phối viên cần biết tổng số cuốc trong bất kỳ hình chữ nhật nào để điều xe tăng cường kịp thời. Cây Fenwick hai chiều giúp cập nhật điểm và hỏi tổng chữ nhật đều trong thời gian logarit nhân logarit.

## Nhiệm vụ

Cho lưới $N \times M$ (ban đầu toàn $0$) và $Q$ thao tác. Hãy lập trình xử lý: loại $1$ cộng $val$ vào ô $(r,c)$; loại $2$ in ra tổng các ô trong hình chữ nhật $[r_1,r_2] \times [c_1,c_2]$.

## Input

- Dòng 1: ba số nguyên $N, M, Q$ ($1 \le N, M \le 1000$, $1 \le Q \le 2 \cdot 10^5$).
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ r\ c\ val$; loại $2$ gồm $2\ r_1\ c_1\ r_2\ c_2$ ($|val| \le 10^9$).

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là tổng hình chữ nhật yêu cầu.

## Sample 1

### Input

```text
3 3 4
1 1 1 5
1 2 2 7
2 1 1 2 2
2 1 1 3 3
```

### Output

```text
12
12
```

### Giải thích

- Cộng $5$ vào ô $(1,1)$ và $7$ vào ô $(2,2)$.
- Hình chữ nhật $[1,2] \times [1,2]$ chứa cả hai ô nên tổng là $5 + 7 = 12$.
- Hình chữ nhật toàn lưới cũng chỉ chứa hai ô này nên tổng vẫn là $12$.

## Ràng buộc

- $1 \le N, M \le 1000$; $1 \le Q \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
