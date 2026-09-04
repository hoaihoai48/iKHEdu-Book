# Tháp Hà Nội Có Ràng Buộc Nước Đi

## Bối cảnh
Trong một biến thể nâng cao của trò chơi Tháp Hà Nội, giữa cọc A và cọc C có một vách ngăn ngăn cách: cấm tuyệt đối mọi nước đi trực tiếp giữa cọc A và cọc C. Mọi chiếc đĩa muốn chuyển từ A sang C hoặc ngược lại bắt buộc phải đi trung chuyển qua cọc B (A <-> B <-> C).

## Nhiệm vụ
Cho N đĩa trên cọc A với quy tắc chuyển qua cọc trung gian B. Hãy tính số bước di chuyển tối thiểu và in ra danh sách các bước đi để chuyển hết N đĩa từ A sang C.

## Input
- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10$).

## Output
- Dòng 1: In số bước chuyển tối thiểu $3^N - 1$.
- Các dòng tiếp theo: Mỗi dòng in một bước chuyển dạng `X -> Y`.

## Sample 1
### Input
```text
1
```
### Output
```text
2
A -> B
B -> C
```
### Giải thích
Với 1 đĩa không được đi trực tiếp A -> C nên phải đi qua B: A -> B rồi B -> C. Tổng cộng 2 bước.

## Ràng buộc
- $100\%$ số test có $N \le 10$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
