# Xóa Ký Tự Ở Vị Trí K


## Bối cảnh

Chuỗi trong Python là bất biến (không thể dùng lệnh xóa trực tiếp `del s[k]`). Ta phải dùng kỹ thuật cắt lát ghép chuỗi.
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


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
