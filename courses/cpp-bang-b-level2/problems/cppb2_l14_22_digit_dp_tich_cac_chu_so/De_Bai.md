# Đếm số có tích chữ số bằng P

## Bối cảnh

Nhà máy khóa số điện tử kiểm định từng mã khóa với yêu cầu tích các chữ số khác không của mã phải đúng bằng hằng số P thì mạch điện mới đóng trơn tru khi người dùng xoay núm vặn. Mỗi lô kiểm định xét mọi mã từ 1 đến N và cần đếm có bao nhiêu mã đạt chuẩn để dán tem xuất xưởng. Chương trình quy hoạch động ghi nhớ tích hiện tại và cắt tỉa nhánh vượt quá P giúp đếm nhanh cả lô hàng triệu mã.

## Nhiệm vụ

Cho hai số nguyên $N, P$. Hãy lập trình đếm các số $x$ ($1 \le x \le N$) có tích các chữ số đúng bằng $P$, rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $N, P$ ($1 \le N \le 10^{18}$, $1 \le P \le 10^9$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn.

## Sample 1

### Input

```text
30 6
```

### Output

```text
3
```

### Giải thích

- Số $6$ có tích chữ số là $6$; số $16$ có tích $1 \times 6 = 6$; số $23$ có tích $2 \times 3 = 6$.
- Mọi số còn lại tới $30$ đều có tích khác $6$.
- Đếm được $3$ số nên chương trình in ra $3$.

## Ràng buộc

- $1 \le N \le 10^{18}$; $1 \le P \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
