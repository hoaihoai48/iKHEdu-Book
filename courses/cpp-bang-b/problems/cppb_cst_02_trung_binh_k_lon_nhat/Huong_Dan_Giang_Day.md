# Hướng Dẫn Giảng Dạy: Giá Trị Trung Bình Lớn Nhất Của Đoạn K
Chuyên đề: **Kỹ Thuật Cửa Sổ Trượt (Sliding Window)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ phương pháp giải quyết bài toán bằng kỹ thuật thuộc chuyên đề Kỹ Thuật Cửa Sổ Trượt (Sliding Window).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các vòng lặp lồng nhau $\mathcal{O}(N^2)$.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không dùng thư viện rườm rà, quản lý bộ nhớ tối ưu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** Đọc hiểu ràng buộc tham số và kiểu dữ liệu phù hợp (chú ý tràn số `long long` khi giá trị vượt $2 \cdot 10^9$).
* **Yêu cầu cốt lõi:** Biến đổi bài toán từ mô hình phát biểu thực tế về mô hình thuật toán tối ưu.
* **Trường hợp biên (Edge Cases):**
  * Kích thước mảng cực tiểu ($N = 1$ hoặc $N = K$).
  * Giá trị phần tử âm, cực lớn hoặc tất cả các phần tử đều bằng nhau.
  * Truy vấn nằm ở sát biên của mảng.

---

## 3. Câu Hỏi Dẫn Dắt Tư Duy (Socratic Method)
1. Độ dài cửa sổ là cố định hay biến thiên?
2. Khi cửa sổ trượt từ $[i-K \dots i-1]$ sang $[i-K+1 \dots i]$, giá trị tổng thay đổi như thế nào?
3. Tất cả các phần tử trong mảng có đều không âm ($A_i \ge 0$) để đảm bảo tính đơn điệu không?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Duy trì một đoạn con liên tiếp $[L \dots R]$ trên mảng.
- Khi mở rộng $R$, nạp phần tử $A_R$ vào trạng thái cửa sổ trong $\mathcal{O}(1)$.
- Khi điều kiện vi phạm hoặc cần tối ưu kích thước, tăng con trỏ $L$ để nhả phần tử $A_L$ trong $\mathcal{O}(1)$.

### 4.2. Bất biến toán học (Invariant):
> Mỗi phần tử đi vào cửa sổ đúng 1 lần (qua $R$) và ra khỏi cửa sổ tối đa 1 lần (qua $L$). Tổng số thao tác di chuyển con trỏ không bao giờ vượt quá $2N$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
4 2
1 12 -5 6
```
* **Output:**
```text
6.500
```
* **Phân tích quá trình thực thi:**
  Đoạn $[1, 12]$ có trung bình $(1 + 12)/2 = 6.5$.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(N)$ tuyến tính tuyệt đối, mỗi phần tử được xét đúng 2 lần.
- **Không gian (Space Complexity):** $\mathcal{O}(1)$ bộ nhớ phụ trợ ngoài mảng lưu trữ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. Áp dụng Sliding Window cho mảng có số âm khi bài toán yêu cầu tính tổng đoạn con (tính đơn điệu bị phá vỡ).
2. Quên khởi tạo giá trị ban đầu cho cửa sổ cố định $K$ đầu tiên.
3. Xử lý sai biên khi cửa sổ trượt qua vị trí cuối cùng của mảng.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long cur_sum = 0;
    for (int i = 0; i < k; ++i) cur_sum += a[i];

    long long max_sum = cur_sum;
    for (int i = k; i < n; ++i) {
        cur_sum += a[i] - a[i - k];
        max_sum = max(max_sum, cur_sum);
    }

    double ans = (double)max_sum / k;
    cout << fixed << setprecision(3) << ans << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Thử thách học sinh giải bài toán khi dữ liệu cập nhật động liên tục (Online Queries).
* **Mở rộng 2:** Áp dụng thuật toán trên không gian nhiều chiều (Ma trận 2D hoặc đồ thị).
* **Tự giải thích:** Yêu cầu học sinh giải thích tại sao không thể dùng thuật toán ngây thơ và chứng minh độ phức tạp tối ưu trước lớp.
