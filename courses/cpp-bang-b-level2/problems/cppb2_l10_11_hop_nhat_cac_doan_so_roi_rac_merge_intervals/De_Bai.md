# Hợp nhất các đoạn số rời rạc (merge intervals)

## Bối cảnh

Phòng kỹ thuật của khu công nghiệp nhận được $N$ yêu cầu cắt điện để bảo trì, mỗi yêu cầu chiếm một khoảng thời gian $[l_i, r_i]$ trong ngày. Nhiều khung giờ của các đơn vị khác nhau giao nhau nên phòng muốn gộp tất cả thành các khung cắt điện liên tục không giao nhau để thông báo một lần duy nhất cho toàn khu, tránh tình trạng thông báo chập chờn khiến các nhà máy không kịp chuẩn bị máy phát dự phòng.

## Nhiệm vụ

Cho $N$ đoạn số $[l_i, r_i]$. Hai đoạn giao nhau hoặc chạm nhau (có điểm chung) được gộp thành một. Hãy lập trình gộp tất cả rồi in ra các đoạn rời nhau còn lại theo thứ tự tăng dần của điểm đầu.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số yêu cầu.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $l_i, r_i$ ($0 \le l_i \le r_i \le 10^9$), là một khoảng thời gian.

## Output

- In ra các đoạn sau khi gộp theo thứ tự tăng dần, mỗi đoạn một dòng dạng `l r`.

## Sample 1

### Input

```text
4
1 3
2 6
8 10
15 18
```

### Output

```text
1 6
8 10
15 18
```

### Giải thích

- Sắp xếp bốn đoạn theo điểm đầu: $[1, 3]$, $[2, 6]$, $[8, 10]$, $[15, 18]$.
- Đoạn $[1, 3]$ và $[2, 6]$ giao nhau nên gộp thành $[1, 6]$.
- Đoạn $[8, 10]$ rời hẳn với $[1, 6]$ nên giữ nguyên; đoạn $[15, 18]$ cũng rời hẳn nên giữ nguyên.
- Kết quả còn ba đoạn $[1, 6]$, $[8, 10]$, $[15, 18]$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le l_i \le r_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
