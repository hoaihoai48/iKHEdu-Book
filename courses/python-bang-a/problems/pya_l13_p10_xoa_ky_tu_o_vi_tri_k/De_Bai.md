# Xóa ký tự ở vị trí K


## Bối cảnh

Bạn Tí viết tên mình lên bảng rồi lỡ viết thừa một chữ cái ở giữa. Tí nhớ rằng chuỗi trong Python là bất biến (không thể dùng lệnh xóa trực tiếp `del s[k]`). Vì vậy Tí phải dùng kỹ thuật cắt lát ghép chuỗi để bỏ chữ thừa đi. Hãy giúp Tí viết chương trình xóa chữ thừa thật gọn.
## Nhiệm vụ

Cho chuỗi $S$ và chỉ số nguyên $K$ ($0 \le K < |S|$). Hãy xóa ký tự tại vị trí $K$ và in ra chuỗi còn lại.
## Input

Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số nguyên $K$.
## Output

Chuỗi sau khi xóa ký tự thứ $K$.
## Sample 1

### Input
```text
PYTHON
2
```
### Output
```text
PYHON
```
### Giải thích

Xóa ký tự tại index 2 là chữ 'T'.
