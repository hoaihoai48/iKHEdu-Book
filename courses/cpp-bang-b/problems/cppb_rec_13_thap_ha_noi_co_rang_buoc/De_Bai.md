# Tháp Hà Nội Có Ràng Buộc Nước Đi

**Phân loại bài toán:** `Advanced Challenge`

## Bối cảnh
Cho $N$ đĩa trên cọc $A$. Quy tắc: **Cấm tuyệt đối mọi nước đi trực tiếp giữa cọc A và cọc C** (mọi đĩa muốn đi từ $A \to C$ hoặc $C \to A$ bắt buộc phải đi qua cọc trung gian $B$). Hãy in ra số bước di chuyển tối thiểu $K = 3^N - 1$ và danh sách các bước di chuyển hợp lệ.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10$).

## Output
- Dòng 1: Số bước di chuyển tối thiểu $K = 3^N - 1$.
- $K$ dòng tiếp theo: Mỗi dòng in theo định dạng `X -> Y`.

## Sample 1
### Input
```text
2
```
### Output
```text
8
A -> B
B -> C
A -> B
C -> B
B -> A
B -> C
A -> B
B -> C
```
### Giải thích
Với N = 2 đĩa và cấm A <-> C trực tiếp, cần đúng 3^2 - 1 = 8 bước.

## Ràng buộc
- 100% số test có $1 \le N \le 10$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
