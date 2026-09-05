# Giải mã mật thư Caesar


## Bối cảnh

Mật mã Caesar là một trong những phương pháp mã hóa thay thế lâu đời nhất, hoạt động bằng cách dịch chuyển từng chữ cái trong bảng mã theo một bước nhảy cố định.

## Nhiệm vụ

Cho một bản mật mã $S$ (chỉ gồm các chữ cái in hoa) đã bị mã hóa Caesar với bước nhảy $K$. Hãy giải mã để tìm lại thông điệp ban đầu.
## Input

Dòng 1 chứa bản mật mã $S$. Dòng 2 chứa số nguyên $K$ ($1 \le K \le 25$).
## Output

Thông điệp ban đầu trước khi mã hóa.
## Sample 1

### Input
```text
DEFABC
3
```
### Output
```text
ABCXYZ
```
### Giải thích

Với dữ liệu đầu vào là `DEFABC
3`, kết quả thu được tương ứng là `ABCXYZ`.



## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
