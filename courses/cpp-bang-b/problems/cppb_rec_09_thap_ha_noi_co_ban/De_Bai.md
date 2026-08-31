# Bài Toán Tháp Hà Nội (Tower of Hanoi)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho $N$ đĩa có kích thước từ $1$ đến $N$ đặt trên cọc $A$. Hãy in ra số bước di chuyển tối thiểu và các bước di chuyển từng đĩa từ cọc $A$ sang cọc $C$ dùng cọc $B$ làm trung gian theo quy tắc kinh điển.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 15$).

## Output
- Dòng 1: Số bước di chuyển $K = 2^N - 1$.
- $K$ dòng tiếp theo: Mỗi dòng in theo định dạng `A -> C` (chuyển đĩa từ cọc nguồn sang cọc đích).

## Sample 1
### Input
```text
3
```
### Output
```text
7
A -> C
A -> B
C -> B
A -> C
B -> A
B -> C
A -> C
```
### Giải thích
Với N = 3 đĩa, cần đúng 2^3 - 1 = 7 bước.

## Ràng buộc
- 100% số test có $1 \le N \le 15$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
