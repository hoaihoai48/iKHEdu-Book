# Hệ phương trình đồng dư (chinese remainder theorem)

## Bối cảnh
Ba lớp trực nhật đếm số ghế trong hội trường theo ba cách khác nhau: lớp thì đếm dư theo nhóm $m_1$, lớp thì theo nhóm $m_2$, lớp thì theo nhóm $m_3$. Từ các số dư $r_1, r_2, r_3$ đó, ban tổ chức muốn suy ra tổng số ghế nhỏ nhất khớp với cả ba cách đếm.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho hệ $k$ phương trình đồng dư $x \equiv r_i \pmod{m_i}$. Hãy lập trình tìm nghiệm $x$ nhỏ nhất không âm thỏa mãn cả hệ.

## Input
- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

## Output
- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hệ Phương Trình Đồng Dư (Chinese Remainder Theorem).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
