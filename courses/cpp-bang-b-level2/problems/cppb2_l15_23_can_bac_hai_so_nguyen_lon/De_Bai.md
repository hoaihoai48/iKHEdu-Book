# Căn bậc hai nguyên của số lớn

## Bối cảnh

Phòng thí nghiệm vật liệu cần cắt tấm pin năng lượng mặt trời hình vuông có diện tích cho trước chính xác tới từng milimét, trong đó diện tích là số nguyên khổng lồ tới hàng trăm chữ số do ghép nhiều tấm nhỏ lại với nhau. Mỗi yêu cầu gửi một diện tích và hệ thống điều khiển máy cắt cần biết cạnh hình vuông lớn nhất có diện tích không vượt quá số đã cho. Thuật toán tìm căn theo từng chữ số cho ra đáp án chính xác mà không dùng tới số thực.

## Nhiệm vụ

Cho số nguyên không âm $A$ rất lớn (tới $1000$ chữ số). Hãy lập trình tính phần nguyên của $\sqrt{A}$, rồi in ra kết quả.

## Input

- Dòng duy nhất: số nguyên $A$ (không có số 0 vô nghĩa ở đầu, trừ chính số $0$).

## Output

- In ra một dòng duy nhất là $\lfloor\sqrt{A}\rfloor$.

## Sample 1

### Input

```text
15241578750190521
```

### Output

```text
123456789
```

### Giải thích

- Kiểm tra $123456789^2 = 15241578750190521$ khớp đúng với số đã cho.
- Số tiếp theo $123456790^2$ đã vượt quá nên phần nguyên của căn đúng bằng $123456789$.
- Chương trình in ra $123456789$.

## Ràng buộc

- $A$ có tối đa $1000$ chữ số.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
