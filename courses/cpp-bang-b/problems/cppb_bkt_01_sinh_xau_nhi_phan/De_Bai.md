# Sinh Tất Cả Xâu Nhị Phân Độ Dài N

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Trong hệ thống truyền tin mật mã của trạm nghiên cứu lượng tử iKH-Quantum, mỗi khóa chuyển trạng thái điều khiển được mã hóa thành một chuỗi nhị phân gồm các bit `0` và `1`. Để kiểm thử tính an toàn và khả năng bao phủ toàn diện của giao thức, hệ thống kiểm toán tự động cần sinh ra toàn bộ các chuỗi tín hiệu có thể có với độ dài $N$, đồng thời yêu cầu các chuỗi phải được kiểm tra lần lượt theo đúng thứ tự từ điển chuẩn mực.

## Nhiệm vụ
Cho số nguyên dương $N$. Hãy áp dụng mô hình thuật toán Quay lui chuẩn mực (`Choose` $\to$ `Explore` $\to$ `Unchoose`) để sinh và in ra tất cả các xâu nhị phân độ dài $N$ theo thứ tự từ điển tăng dần.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 16$).

## Output
- In ra tất cả các xâu nhị phân độ dài $N$, mỗi xâu trên một dòng theo đúng thứ tự từ điển tăng dần.

## Sample 1
### Input
```text
3
```
### Output
```text
000
001
010
011
100
101
110
111
```
### Giải thích
Với độ dài $N = 3$, không gian trạng thái nhị phân gồm $2^3 = 8$ xâu. Bắt đầu từ cấu hình nhỏ nhất theo từ điển là `000` và kết thúc ở cấu hình lớn nhất là `111`.

## Ràng buộc
- 100% số test có $1 \le N \le 16$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
