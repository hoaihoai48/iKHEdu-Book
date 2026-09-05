# Diện tích bồn hoa chữ thập


## Bối cảnh

Trong công viên xanh mát có một bồn hoa hình chữ thập (dấu cộng) rất đẹp được tạo thành bởi hai luống hoa hình chữ nhật đặt chồng lên nhau:
 * Một luống hoa nằm ngang có kích thước $a \times b$ ($a$ là chiều dài, $b$ là chiều rộng).
 * Một luống hoa nằm dọc có kích thước $b \times a$ ($b$ là chiều rộng, $a$ là chiều dài).
 * Hai luống hoa giao nhau ở chính giữa tạo thành một hình vuông kích thước $b \times b$.
Cô công nhân muốn biết diện tích thật để gieo hạt, vì phần giao nhau ở giữa không được tính hai lần. Hãy giúp cô tính diện tích bồn hoa.
## Nhiệm vụ

Hãy tính diện tích thực tế của toàn bộ bồn hoa chữ thập này (không được tính trùng lặp phần diện tích giao nhau ở chính giữa).
## Input

Nhập 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$) trên 2 dòng.
## Output

Diện tích thực tế của bồn hoa.
## Sample 1

### Input
```text
10
3
```
### Output
```text
51
```
### Giải thích

- Luống ngang: $10 \times 3 = 30$.
- Luống dọc: $3 \times 10 = 30$.
- Phần giao nhau ở giữa: $3 \times 3 = 9$.
- Diện tích bồn hoa: $30 + 30 - 9 = 51$.
## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
