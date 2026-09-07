# Đếm số có tổng chữ số bằng K

## Bối cảnh

Phòng quản lý thuê bao viễn thông triển khai gói cước phong thủy trong đó số điện thoại được coi là may mắn khi tổng các chữ số của nó đúng bằng con số K mà khách hàng yêu cầu. Mỗi ngày tổng đài nhận một đoạn số thuê bao liên tiếp và cần đếm có bao nhiêu số may mắn trong đoạn đó để báo giá lô sim cho đại lý. Vì đoạn số có thể dài tới hàng nghìn tỉ nên chương trình dùng quy hoạch động chữ số thay vì duyệt từng số.

## Nhiệm vụ

Cho ba số nguyên $L, R, K$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) có tổng các chữ số đúng bằng $K$, rồi in ra kết quả.

## Input

- Dòng duy nhất: ba số nguyên $L, R, K$ ($0 \le L \le R \le 10^{18}$, $0 \le K \le 162$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn.

## Sample 1

### Input

```text
1 20 2
```

### Output

```text
3
```

### Giải thích

- Các số từ $1$ đến $20$ có tổng chữ số bằng $2$ là $2$ (tổng $2$), $11$ (tổng $1+1=2$) và $20$ (tổng $2+0=2$).
- Không còn số nào khác thỏa mãn trong đoạn.
- Chương trình in ra $3$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$; $0 \le K \le 162$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
