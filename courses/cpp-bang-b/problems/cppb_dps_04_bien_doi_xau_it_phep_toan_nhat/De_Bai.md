# Chỉ Dùng Phép Xóa Biến Đổi Hai Xâu

## Bối cảnh
Tại một máy nén dữ liệu truyền thông, hệ thống chỉ hỗ trợ duy nhất một thao tác cơ học là xóa bỏ ký tự. Cho hai chuỗi văn bản $S$ và $T$. Kỹ sư cần đưa cả hai chuỗi về cùng một chuỗi hoàn toàn giống nhau bằng cách chỉ xóa bỏ các ký tự trên mỗi chuỗi.

## Nhiệm vụ
Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm tổng số lượng ký tự ít nhất cần phải xóa bỏ trên cả hai chuỗi để phần còn lại của chúng trở nên đồng nhất.

## Input
- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chứa chuỗi ký tự $T$ ($1 \le |T| \le 2000$).

## Output
- In ra trên một dòng duy nhất tổng số ký tự ít nhất cần xóa.

## Sample 1
### Input
```text
sea
eat
```
### Output
```text
2
```

### Giải thích
Với hai chuỗi $S = \text{"sea"}$ và $T = \text{"eat"}$:
Để hai chuỗi trở nên giống nhau, ta đưa cả hai về chuỗi chung là $\text{"ea"}$:
- Trên chuỗi $S$: Xóa ký tự 's' (1 ký tự).
- Trên chuỗi $T$: Xóa ký tự 't' (1 ký tự).
Tổng số ký tự cần xóa là $1 + 1 = 2$.

## Ràng buộc
- $100\%$ số test có $1 \le |S|, |T| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
