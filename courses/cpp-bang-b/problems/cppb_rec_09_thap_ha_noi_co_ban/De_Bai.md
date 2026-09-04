# Bài Toán Tháp Hà Nội (Tower of Hanoi)

## Bối cảnh
Bài toán truyền thuyết cổ về các nhà sư chuyển N chiếc đĩa vàng giữa 3 cọc A, B, C tuân theo quy tắc: mỗi lần chỉ chuyển 1 đĩa và đĩa lớn hơn không bao giờ được đặt lên trên đĩa nhỏ hơn. Đây là bài toán mẫu mực kinh điển về tư duy đệ quy phân rã bài toán.

## Nhiệm vụ
Cho N đĩa đặt trên cọc A. Hãy in ra số bước chuyển tối thiểu và danh sách các bước di chuyển đĩa từ cọc này sang cọc khác để chuyển hết N đĩa từ cọc A sang cọc C (dùng cọc B làm trung gian).

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 15$).

## Output
- Dòng 1: In số bước di chuyển tối thiểu $2^N - 1$.
- Các dòng tiếp theo: Mỗi dòng in một bước chuyển dạng `X -> Y`.

## Sample 1
### Input
```text
2
```
### Output
```text
3
A -> B
A -> C
B -> C
```
### Giải thích
Với N = 2 cần 2^2 - 1 = 3 bước: chuyển đĩa 1 từ A sang B; chuyển đĩa 2 từ A sang C; chuyển đĩa 1 từ B sang C.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 15$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
