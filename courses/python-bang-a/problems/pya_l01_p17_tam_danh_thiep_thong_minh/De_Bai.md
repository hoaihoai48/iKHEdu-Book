# Tấm danh thiếp thông minh


## Bối cảnh

Hệ thống quản lý thông tin hội thảo cần in thẻ danh thiếp tự động cho người tham dự sau khi nhập tên.

## Nhiệm vụ

Nhập vào tên của một người (chuỗi ký tự). Hãy in ra thông điệp chào mừng theo mẫu: `Xin chao ban [Ten]!`

## Input

Một dòng duy nhất chứa chuỗi ký tự tên của người dùng.
## Output

In ra dòng thông điệp: `Xin chao ban <Ten>!` (giữa chữ `ban` và tên cách nhau một dấu cách, cuối câu có dấu chấm than `!`).
## Sample 1

### Input
```text
Nam
```
### Output
```text
Xin chao ban Nam!
```
### Giải thích

Với tên nhập vào là `"Nam"`, chương trình ghép chuỗi `"Xin chao ban "` với `"Nam"` và thêm dấu chấm than `!` ở cuối, tạo thành dòng chữ `Xin chao ban Nam!`.

## Sample 2

### Input
```text
Bao Anh
```
### Output
```text
Xin chao ban Bao Anh!
```
## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
