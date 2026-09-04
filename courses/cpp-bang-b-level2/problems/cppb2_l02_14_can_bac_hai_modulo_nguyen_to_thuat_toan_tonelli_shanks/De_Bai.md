# Căn bậc hai modulo nguyên tố (thuật toán tonelli-shanks)

## Bối cảnh
Ổ khóa số của phòng dụng cụ mở ra khi nhập đúng số $x$ mà bình phương của nó chia cho số nguyên tố $p$ còn dư đúng $n$. Có những con số $n$ mà không chiếc chìa nào mở được, khi đó người trực phải báo $-1$ để đổi ổ khác.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ cặp $(n, p)$ với $p$ nguyên tố. Hãy lập trình tìm $x$ sao cho $x^2 \equiv n \pmod p$; in `-1` nếu không tồn tại.

## Input
- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

## Output
- In ra kết quả trên một dòng.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Căn Bậc Hai Modulo Nguyên Tố (Thuật Toán Tonelli-Shanks).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
