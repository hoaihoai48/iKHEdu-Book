# Xếp gạch lát sàn kích thước $3 \times n$

## Bối cảnh

Gia đình bác Hùng vừa xây xong căn bếp dài và muốn lát sàn gạch men cho sạch sẽ. Mặt sàn là hình chữ nhật rộng đúng $3$ mét và dài $n$ mét, còn cửa hàng vật liệu chỉ bán một loại gạch hình chữ nhật $2 \times 1$ (được xoay dọc hay ngang tùy ý). Bác muốn biết có bao nhiêu cách lát kín mặt sàn bằng loại gạch này để còn chọn mẫu hoa văn ưng ý nhất, vì mỗi cách lát cho một họa tiết khác nhau mà giá tiền công thợ không đổi.

## Nhiệm vụ

Cho số nguyên $n$ là chiều dài của mặt sàn $3 \times n$. Hãy lập trình đếm số cách lát kín mặt sàn bằng các viên gạch $2 \times 1$ (được xoay tùy ý), rồi in ra số cách đó theo modulo $1\,000\,000\,007$.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 10^6$), là chiều dài mặt sàn.

## Output

- In ra số cách lát kín theo modulo $1\,000\,000\,007$ (sàn lẻ mét thì không lát được, in ra $0$).

## Sample 1

### Input

```text
4
```

### Output

```text
11
```

### Giải thích

- Mặt sàn $3 \times 4$ lát được bằng gạch $2 \times 1$ theo đúng $11$ cách.
- Với sàn $3 \times 2$ có $3$ cách: ba viên đặt đứng, hoặc hai viên nằm ngang xếp chồng theo hai tầng đảo nhau.
- Mở rộng từng cột từ trái sang phải, mỗi trạng thái khuyết của cột đang lát đều được lấp đầy theo đúng các mẫu trên, cộng dồn lại được $11$ cách cho sàn $3 \times 4$.

## Ràng buộc

- $1 \le n \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
