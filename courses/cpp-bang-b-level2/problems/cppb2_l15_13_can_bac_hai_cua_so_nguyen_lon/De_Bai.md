# Căn bậc hai của số nguyên lớn

## Bối cảnh

Viện đo lường quốc gia hiệu chuẩn thiết bị laser với yêu cầu tính cạnh của hình vuông có diện tích cho trước chính xác tới từng đơn vị, trong đó diện tích có thể là số nguyên khổng lồ tới hàng trăm chữ số. Mỗi phép đo gửi một diện tích và máy tính nhúng cần trả về phần nguyên của căn bậc hai để điều chỉnh tiêu cự kính ngắm. Thuật toán chặt nhị phân trên số lớn cho ra đáp án chính xác mà không cần tới số thực dấu chấm động.

## Nhiệm vụ

Cho số nguyên không âm $A$ rất lớn (tới $1000$ chữ số). Hãy lập trình tính phần nguyên của $\sqrt{A}$, tức số nguyên lớn nhất $X$ sao cho $X^2 \le A$, rồi in ra kết quả.

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
123456789```

### Giải thích

- Kiểm tra $123456789^2 = 15241578750190521$ khớp đúng với số đã cho.
- Số tiếp theo $123456790^2$ đã vượt quá nên phần nguyên của căn đúng bằng $123456789$.
- Chương trình in ra $123456789$.

## Ràng buộc

- $A$ có tối đa $1000$ chữ số.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
