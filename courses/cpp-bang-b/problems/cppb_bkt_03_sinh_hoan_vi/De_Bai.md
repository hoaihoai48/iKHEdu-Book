# Sinh Tất Cả Hoán Vị 1..N

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Tại cuộc thi trình diễn drone nghệ thuật mừng lễ hội ánh sáng, một đội bay gồm $N$ chiếc drone được đánh số từ $1$ đến $N$ cần thay đổi vị trí xuất phát theo các thứ tự khác nhau để tạo ra các hiệu ứng biến hình đặc sắc. Ban tổ chức lập trình một bộ điều khiển trung tâm để thử nghiệm mọi kịch bản đổi chỗ các drone sao cho mỗi vị trí chỉ có duy nhất một drone đảm nhiệm.

## Nhiệm vụ
Cho số nguyên dương $N$. Hãy áp dụng thuật toán Quay lui với kỹ thuật đánh dấu mảng `visited[]` để sinh và in ra tất cả các hoán vị của tập hợp $\{1, 2, \dots, N\}$ theo đúng thứ tự từ điển tăng dần.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 8$).

## Output
- In ra tất cả $N!$ hoán vị, mỗi hoán vị trên một dòng, các phần tử trong mỗi dòng cách nhau bởi dấu cách.

## Sample 1
### Input
```text
3
```
### Output
```text
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```
### Giải thích
Tập $\{1, 2, 3\}$ có đúng $3! = 6$ hoán vị khác nhau. Hoán vị đầu tiên theo thứ tự từ điển là `1 2 3` và hoán vị cuối cùng là `3 2 1`.

## Ràng buộc
- 100% số test có $1 \le N \le 8$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
