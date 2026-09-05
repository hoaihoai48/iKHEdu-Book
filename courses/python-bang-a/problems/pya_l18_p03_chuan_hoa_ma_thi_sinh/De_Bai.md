# Chuẩn hóa mã thí sinh


## Bối cảnh

Trường em tổ chức hội thi vẽ tranh nên mỗi người dùng được phát một mã thí sinh gồm 2 phần: chữ cái viết tắt của tỉnh và số báo danh (ví dụ: `HN025`, `DN007`). Hôm nay, cô văn thư nhập liệu vội quá nên gõ nhầm chữ thường và để sót các khoảng trắng thừa như thế này: ` hn 25 `. Cô đang lo các thẻ dự thi bị xấu, hãy cô sửa lại các mã thí sinh cho thật ngay ngắn.
## Nhiệm vụ

Cho chuỗi nhập liệu gồm chữ viết tắt và số. Hãy chuẩn hóa thành chuỗi viết hoa, bỏ mọi khoảng trắng và nếu phần số có ít hơn 3 chữ số thì thêm các chữ số 0 vào trước để phần số luôn đủ 3 chữ số.
## Input

Một dòng văn bản gồm chữ cái và số nguyên $K$.
## Output

Mã thí sinh chuẩn hóa.
## Sample 1

### Input
```text
hn 5
```
### Output
```text
HN005
```
### Giải thích

Với dữ liệu đầu vào là `hn 5`, kết quả thu được tương ứng là `HN005`.

## Sample 2

### Input
```text
HCM 12
```
### Output
```text
HCM012
```


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
