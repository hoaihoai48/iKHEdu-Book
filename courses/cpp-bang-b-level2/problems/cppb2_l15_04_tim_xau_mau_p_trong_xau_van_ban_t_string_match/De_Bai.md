# Tìm mẫu P trong văn bản T (KMP)

## Bối cảnh

Bộ phận kiểm duyệt nội dung của mạng xã hội cần quét các bài đăng dài để tìm mọi vị trí xuất hiện của cụm từ vi phạm đã được ban pháp chế liệt kê trong danh sách đen. Mỗi bài đăng có thể dài tới hàng triệu ký tự nên việc tìm kiếm ngây thơ sẽ quá chậm, đội kỹ thuật triển khai thuật toán KMP duyệt văn bản đúng một lần. Kết quả là danh sách vị trí bắt đầu của mọi lần xuất hiện để chuyển cho kiểm duyệt viên xử lý.

## Nhiệm vụ

Cho xâu văn bản $T$ và xâu mẫu $P$ (chữ cái thường). Hãy lập trình tìm mọi vị trí bắt đầu (đánh số từ $1$) mà $P$ xuất hiện trong $T$ bằng thuật toán KMP, rồi in ra các vị trí (in ra $-1$ nếu không xuất hiện).

## Input

- Dòng 1: xâu $T$ ($1 \le |T| \le 10^6$).
- Dòng 2: xâu $P$ ($1 \le |P| \le |T|$).

## Output

- In ra một dòng duy nhất: các vị trí xuất hiện cách nhau bởi dấu cách, hoặc $-1$.

## Sample 1

### Input

```text
ababa
aba
```

### Output

```text
1 3```

### Giải thích

- Văn bản $ababa$ dài năm ký tự, mẫu $aba$ dài ba ký tự.
- Đặt mẫu tại vị trí $1$ được $aba$ khớp; trượt tới vị trí $2$ được $bab$ không khớp; tại vị trí $3$ được $aba$ khớp.
- Các vị trí thỏa mãn là $1$ và $3$ nên in ra $1\ 3$.

## Ràng buộc

- $1 \le |P| \le |T| \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
