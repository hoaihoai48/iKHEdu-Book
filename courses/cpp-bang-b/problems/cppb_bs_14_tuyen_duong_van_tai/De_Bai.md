# Tối Ưu Hóa Tuyến Đường Vận Tải Đa Điểm

## Bối cảnh
Có $N$ thành phố xếp liên tiếp từ $1$ đến $N$. Tại thành phố thứ $i$ có $A_i$ tấn hàng cần vận chuyển. Có $M$ xe tải giống hệt nhau, mỗi xe có bình nhiên liệu cho phép chạy tối đa một quãng đường $D$ (tức chỉ có thể gom hàng trong một cụm các thành phố liên tiếp có độ dài không vượt quá $D$ thành phố). Mỗi xe tải có sức chứa tối đa là $C$ tấn hàng.

## Nhiệm vụ
Biết trước danh sách hàng hóa tại $N$ thành phố và số lượng xe $M$. Hãy tìm sức chứa tối thiểu $C$ của mỗi xe tải sao cho toàn bộ hàng hóa được gom hết về kho mà không xe nào phải gom quá cự ly $D$ thành phố.

## Input
- Dòng 1: Gồm 3 số nguyên $N, M, D$ ($1 \le N \le 2 \cdot 10^5, 1 \le M \le N, 1 \le D \le N$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là sức chứa $C$ nhỏ nhất.

## Sample 1
### Input
```text
5 2 3
4 2 3 5 1
```
### Output
```text
9
```

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
