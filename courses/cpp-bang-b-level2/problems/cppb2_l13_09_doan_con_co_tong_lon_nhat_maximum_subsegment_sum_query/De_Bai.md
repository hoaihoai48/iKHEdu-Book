# Tổng đoạn con lớn nhất trên đoạn truy vấn (static)

## Bối cảnh

Sở kế hoạch đầu tư rà soát N dự án xếp theo tiến độ với mức đóng góp lợi nhuận có thể âm hoặc dương vào ngân sách tỉnh. Mỗi kỳ họp, hội đồng chọn một đoạn các dự án liên tiếp để đánh giá và cần biết tổng lớn nhất của một chuỗi con liên tiếp nằm trong đoạn đó nhằm quyết định có tiếp tục rót vốn hay không. Cây đoạn hợp nhất bốn thông tin mỗi nút giúp trả lời từng truy vấn trong thời gian logarit.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ cố định và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(l,r)$, tổng lớn nhất của một đoạn con liên tiếp nằm trong $[l,r]$, rồi in ra đáp án.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $l, r$ ($1 \le l \le r \le N$).

## Output

- Gồm $Q$ dòng, mỗi dòng là tổng đoạn con lớn nhất trong đoạn tương ứng.

## Sample 1

### Input

```text
9 1
-2 1 -3 4 -1 2 1 -5 4
1 9
```

### Output

```text
6```

### Giải thích

- Dãy gồm $-2\ 1\ -3\ 4\ -1\ 2\ 1\ -5\ 4$: xét đoạn $4, -1, 2, 1$ cho tổng $6$.
- Mọi cách mở rộng đoạn này sang trái đều cộng thêm số âm, sang phải gặp $-5$ kéo tổng xuống nên $6$ là lớn nhất.
- Truy vấn duy nhất in ra $6$.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
