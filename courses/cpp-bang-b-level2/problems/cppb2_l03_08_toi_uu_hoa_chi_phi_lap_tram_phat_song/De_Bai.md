# Tối ưu hóa chi phí lắp trạm phát sóng

## Bối cảnh

Ủy ban xã muốn dựng một trạm phát sóng sao cho tổng chi phí kéo dây tới các hộ dân là thấp nhất. Vị trí trạm càng gần khu dân cư đông thì càng tiết kiệm, nhưng mặt bằng mỗi nơi lại có giá khác nhau.

Cán bộ địa chính vẽ bản đồ các hộ dân rồi tính xem đặt trạm ở đâu thì tổng chi phí nhỏ nhất.

## Nhiệm vụ

Cho vị trí các hộ dân và hàm chi phí lắp trạm. Hãy lập trình tìm vị trí đặt trạm phát sóng sao cho tổng chi phí là nhỏ nhất.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 10^5$) — số khu dân cư.
- $n$ dòng tiếp theo, mỗi dòng chứa hai số thực $x_i, cost_i$ ($|x_i| \le 10^9$, $cost_i > 0$) là vị trí và chi phí kéo cáp trên mỗi đơn vị khoảng cách của từng khu.

## Output

- In ra một dòng duy nhất là tổng chi phí kéo cáp nhỏ nhất khi đặt trạm tại vị trí tối ưu $p$ (chi phí là $\sum cost_i \cdot |x_i - p|$), làm tròn tới $4$ chữ số thập phân.

## Sample 1
### Input
```text
3
1 10
2 1
3 1
```
### Output
```text
3.0000
```
### Giải thích

Thử đặt trạm tại $p = 1$: chi phí $10 \cdot 0 + 1 \cdot 1 + 1 \cdot 2 = 3$. Thử $p = 2$: $10 \cdot 1 + 0 + 1 \cdot 1 = 11$. Thử $p = 3$: $10 \cdot 2 + 1 \cdot 1 + 0 = 21$. Vị trí $p = 1$ cho chi phí nhỏ nhất là $3$ (dịch trạm sang phải chỉ làm chi phí phía khu thứ nhất tăng nhanh hơn mức giảm của hai khu còn lại).

## Ràng buộc

- $1 \le n \le 10^5$, $|x_i| \le 10^9$, $cost_i > 0$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
