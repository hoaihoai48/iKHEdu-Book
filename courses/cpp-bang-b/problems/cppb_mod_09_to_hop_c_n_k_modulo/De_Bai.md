# Tính Số Tổ Hợp C(N, K) mod M

## Bối cảnh
Tại một giải đấu cờ vua quốc tế, ban tổ chức cần chọn ra K kỳ thủ từ danh sách N người tham gia để lập đội tuyển. Số cách chọn chính là số tổ hợp C(N, K). Vì số cách chọn rất lớn, ban tổ chức cần tính C(N, K) mod (10^9 + 7) cho Q câu hỏi truy vấn độc lập.

## Nhiệm vụ
Cho Q truy vấn, mỗi truy vấn chứa 2 số N và K. Hãy tính C(N, K) mod (10^9 + 7) bằng phương pháp tiền xử lý giai thừa và nghịch đảo giai thừa.

## Input
- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số nguyên $N$ và $K$ ($0 \le K \le N \le 10^6$).

## Output
- In ra $Q$ dòng, mỗi dòng là giá trị $C(N, K) \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
2
5 2
10 3
```
### Output
```text
10
120
```
### Giải thích
- C(5, 2) = 5! / (2! * 3!) = 10.
- C(10, 3) = 10! / (3! * 7!) = 120.

## Ràng buộc
- $100\%$ số test có $Q \le 10^5, N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
