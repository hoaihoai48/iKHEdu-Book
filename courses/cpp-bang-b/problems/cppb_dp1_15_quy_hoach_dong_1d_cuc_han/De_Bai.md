# Tối Ưu Hóa Chuỗi Dự Án Năng Lượng

## Bối cảnh
Một quỹ đầu tư năng lượng tái tạo xem xét danh mục gồm $N$ dự án điện gió và điện mặt trời. Dự án thứ $i$ có quy mô công suất là $P_i$ (MW) và mang lại doanh thu kỳ vọng là $V_i$ (tỷ đồng). Để đảm bảo lộ trình mở rộng thị phần an toàn và bền vững, quỹ đầu tư chỉ được phép phê duyệt một chuỗi các dự án có quy mô công suất tăng dần nghiêm ngặt theo thời gian xét duyệt.

## Nhiệm vụ
Cho danh sách $N$ dự án với công suất $P_i$ và doanh thu $V_i$. Hãy lập trình chọn ra một chuỗi các dự án có công suất tăng nghiêm ngặt sao cho tổng doanh thu thu về là lớn nhất.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$) biểu diễn số lượng dự án.
- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $P_i$ và $V_i$ ($1 \le P_i \le 10^5, 1 \le V_i \le 10^9$) lần lượt là công suất và doanh thu của dự án thứ $i$.

## Output
- In ra trên một dòng duy nhất một số nguyên là tổng doanh thu lớn nhất có thể đạt được.

## Sample 1
### Input
```text
3
10 100
5 50
20 200
```
### Output
```text
350
```

### Giải thích
Với 3 dự án năng lượng có thông số $[(10, 100), (5, 50), (20, 200)]$:
Chuỗi dự án có công suất tăng dần nghiêm ngặt là chọn dự án 2 (công suất 5), sau đó dự án 1 (công suất 10), và cuối cùng là dự án 3 (công suất 20). Chuỗi công suất là $5 < 10 < 20$, mang lại tổng doanh thu tối đa là $50 + 100 + 200 = 350$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 2000, 1 \le V_i, C_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
