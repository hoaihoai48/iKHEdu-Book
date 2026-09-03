# Chuẩn Hóa Mã Thí Sinh


## Bối cảnh

Mã thí sinh trong kỳ thi gồm 2 phần: chữ cái viết tắt của tỉnh và số báo danh (ví dụ: `HN025`, `DN007`). Do sơ suất, người nhập liệu gõ nhầm chữ thường và các khoảng trắng thừa: `  hn  25  `.
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
