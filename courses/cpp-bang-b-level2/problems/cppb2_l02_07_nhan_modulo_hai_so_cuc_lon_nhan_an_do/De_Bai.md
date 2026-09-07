# Nhân modulo hai số cực lớn (nhân ấn độ)

## Bối cảnh
Hai kho hàng điện tử cần đối soát số lượng linh kiện: mỗi bên có một con số cực lớn, và hệ thống chỉ lưu được phần dư của tích hai số đó khi chia cho $m$. Phép nhân trực tiếp sẽ làm tràn bộ nhớ máy quét cũ, nên người ta nhân từng phần rồi cộng dồn phần dư — giống cách nhân đặt cột mà học sinh vẫn làm trên giấy.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ bộ $(a, b, m)$. Hãy lập trình tính $(a \cdot b) \bmod m$ mà không để xảy ra tràn số.

## Input

- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$) — số lượng truy vấn.
- $T$ dòng tiếp theo, mỗi dòng chứa ba số nguyên không âm $a, b, m$ ($0 \le a, b \le 10^{18}$, $1 \le m \le 10^{18}$), cách nhau bởi dấu cách.

## Output

- Với mỗi truy vấn, in ra một dòng là giá trị $(a \cdot b) \bmod m$. Phép nhân phải được thực hiện mà không để xảy ra tràn số $64$ bit.

## Sample 1
### Input
```text
2
1000000000000000000 1000000000000000000 1000000007
5 7 13
```
### Output
```text
2401
9
```
### Giải thích

* Truy vấn thứ nhất: $10^{18}$ chia cho $1000000007$ dư $49$ (vì $10^9$ dư $-7$ nên $(10^9)^2$ dư $49$). Do đó tích dư $49 \cdot 49 = 2401$, mà $2401 < 1000000007$ nên đáp án là $2401$.
* Truy vấn thứ hai: $5 \cdot 7 = 35 = 2 \cdot 13 + 9$, chia $13$ dư $9$.

## Ràng buộc

- $1 \le T \le 10^5$, $0 \le a, b \le 10^{18}$, $1 \le m \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
