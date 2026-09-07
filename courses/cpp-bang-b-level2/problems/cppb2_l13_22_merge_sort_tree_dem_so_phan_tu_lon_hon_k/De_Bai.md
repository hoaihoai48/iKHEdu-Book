# Đếm số phần tử lớn hơn K (merge sort tree)

## Bối cảnh

Phòng nhân sự tập đoàn lưu mức lương của N nhân viên theo mã số để phục vụ các đợt xét tăng lương và thưởng Tết hằng năm. Mỗi đợt xét duyệt cần đếm trong một đoạn mã số có bao nhiêu người đang hưởng mức cao hơn ngưỡng K nhằm ước tính quỹ lương điều chỉnh. Cây hợp nhất sắp xếp lưu dãy đã xếp tại mỗi nút giúp đếm bằng tìm kiếm nhị phân trong thời gian logarit bình phương.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ cố định và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(l,r,k)$, số lượng phần tử trong $a_l, \dots, a_r$ lớn hơn $k$, rồi in ra đáp án.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $l, r, k$.

## Output

- Gồm $Q$ dòng, mỗi dòng là đáp án của truy vấn tương ứng.

## Sample 1

### Input

```text
5 2
1 5 2 4 3
1 5 3
2 4 4
```

### Output

```text
2
1
```

### Giải thích

- Truy vấn $(1,5,3)$: cả mảng có hai số lớn hơn $3$ là $5$ và $4$.
- Truy vấn $(2,4,4)$: đoạn $5\ 2\ 4$ chỉ có $5$ lớn hơn $4$.
- Hai truy vấn in ra $2$ rồi $1$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 10^5$; $|a_i|, |k| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
