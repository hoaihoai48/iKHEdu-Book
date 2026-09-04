# Sinh Tất Cả Tập Con Của Tập N Phần Tử

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Hội đồng thẩm định dự án khởi nghiệp công nghệ đang xem xét danh mục $N$ gói giải pháp số được đánh số thứ tự từ $1$ đến $N$. Mỗi phương án đầu tư khả thi thực chất là một tập con các gói giải pháp được chọn phối hợp với nhau (bao gồm cả trường hợp không chọn gói nào). Để chuẩn bị ma trận đánh giá rủi ro cho nhà đầu tư, chuyên viên phân tích cần liệt kê toàn bộ mọi tổ hợp tập con của danh mục này.

## Nhiệm vụ
Cho tập hợp gồm $N$ phần tử $\{1, 2, \dots, N\}$. Hãy sử dụng thuật toán Quay lui mô hình nhị phân (ở mỗi bước quyết định chọn hoặc không chọn phần tử hiện tại) để sinh và in ra tất cả các tập con theo đúng thứ tự từ điển.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 16$).

## Output
- In ra các tập con, mỗi tập con trên một dòng. Các phần tử trong tập con cách nhau bởi dấu cách. Tập rỗng in một dòng trống.

## Sample 1
### Input
```text
3
```
### Output
```text

3
2
2 3
1
1 3
1 2
1 2 3
```
### Giải thích
Với $N = 3$, tập $\{1, 2, 3\}$ có tổng cộng $2^3 = 8$ tập con. Theo thứ tự duyệt quay lui với bit 0 (không chọn) đứng trước bit 1 (chọn), tập rỗng được sinh đầu tiên và tập đầy đủ $\{1, 2, 3\}$ sinh cuối cùng.

## Ràng buộc
- 100% số test có $1 \le N \le 16$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
