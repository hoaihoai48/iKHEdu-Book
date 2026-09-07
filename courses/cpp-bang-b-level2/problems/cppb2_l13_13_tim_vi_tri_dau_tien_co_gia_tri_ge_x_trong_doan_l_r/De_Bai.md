# Vị trí đầu tiên có giá trị lớn hơn hoặc bằng X

## Bối cảnh

Hệ thống kho lạnh bảo quản N thùng vắc xin với nhiệt độ được ghi nhận theo từng vị trí kệ để đảm bảo dây chuyền lạnh không bị gián đoạn. Khi cảnh báo ngưỡng an toàn X được ban hành, nhân viên cần tìm thùng đầu tiên trong một đoạn kệ có nhiệt độ vượt ngưỡng để kiểm tra khẩn cấp trước khi cả lô bị ảnh hưởng. Cây đoạn lưu giá trị lớn nhất mỗi nút giúp nhảy tìm vị trí thỏa mãn trong thời gian logarit.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ cố định và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(l,r,x)$, vị trí nhỏ nhất $p$ trong $[l,r]$ sao cho $a_p \ge x$ (in ra $-1$ nếu không tồn tại).

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $l, r, x$.

## Output

- Gồm $Q$ dòng, mỗi dòng là vị trí cần tìm hoặc $-1$.

## Sample 1

### Input

```text
5 3
1 5 2 4 3
1 5 4
2 3 6
3 5 3
```

### Output

```text
2
-1
4```

### Giải thích

- Truy vấn $(1,5,4)$: duyệt từ trái thấy $a[2] = 5 \ge 4$ nên đáp án là $2$.
- Truy vấn $(2,3,6)$: hai giá trị $5$ và $2$ đều nhỏ hơn $6$ nên đáp án là $-1$.
- Truy vấn $(3,5,3)$: $a[3] = 2$ chưa đạt nhưng $a[4] = 4 \ge 3$ nên đáp án là $4$.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i|, |x| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
