# Hướng Dẫn Giảng Dạy: Tìm Hình Vuông K x K Có Tổng Lớn Nhất
Chuyên đề: **Mảng Tiền Tố & Mảng Hiệu (Prefix Sum & Difference Array)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ phương pháp giải quyết bài toán bằng kỹ thuật thuộc chuyên đề Mảng Tiền Tố & Mảng Hiệu (Prefix Sum & Difference Array).
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
1. Bài toán có bao nhiêu truy vấn $Q$? Nếu $Q, N \le 10^5$, thuật toán $\mathcal{O}(Q \times N)$ có bị TLE không?
2. Làm sao để tính tổng đoạn con trong $\mathcal{O}(1)$ sau một lần tiền xử lý duy nhất?
3. Với bài toán cộng đoạn, ta tác động vào những điểm biên nào để sau khi tính tiền tố mảng sẽ được cộng đều?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Xây dựng mảng tiền tố $P_i = P_{i-1} + A_i$ (1-based index) để trả lời truy vấn tổng đoạn $[L \dots R]$ qua công thức $P_R - P_{L-1}$ trong $\mathcal{O}(1)$.
- Sử dụng mảng hiệu $D[L] += V, D[R+1] -= V$ để thực hiện thao tác cộng dồn đoạn trong $\mathcal{O}(1)$, sau đó chạy tiền tố khôi phục mảng kết quả trong $\mathcal{O}(N)$.

### 4.2. Bất biến toán học (Invariant):
> $P[R] - P[L-1] = \sum_{k=1}^R A_k - \sum_{k=1}^{L-1} A_k = \sum_{k=L}^R A_k$. Đoạn thừa trước $L$ bị triệt tiêu hoàn toàn.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
3 3 2
1 1 1
1 2 2
1 2 2
```
* **Output:**
```text
8
```
* **Phân tích quá trình thực thi:**
  Thuật toán tiến hành khởi tạo cấu trúc dữ liệu, duyệt tuyến tính qua từng phần tử và cập nhật kết quả tối ưu theo đúng nguyên lý thiết kế.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(N)$ tiền xử lý + $\mathcal{O}(1)$ mỗi truy vấn $\implies$ Tổng thời gian $\mathcal{O}(N + Q)$, xử lý $10^5$ truy vấn trong dưới $0.05\text{s}$.
- **Không gian (Space Complexity):** $\mathcal{O}(N)$ (hoặc $\mathcal{O}(N \times M)$ cho bảng 2D) để lưu mảng tiền tố.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. Tràn số khi cộng dồn mảng tiền tố $P$ với $A_i \le 10^9$ (bắt buộc dùng `vector<long long>` hoặc `long long P[]`).
2. Lỗi truy cập ngoài mảng khi cập nhật $D[R+1]$ với $R = N$ (cần khai báo mảng kích thước $N + 2$).
3. Nhầm lẫn chỉ số 0-based và 1-based dẫn đến truy vấn $P[L-1]$ bị truy cập ô rác hoặc âm.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            long long val;
            cin >> val;
            p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + val;
        }
    }

    long long max_sum = -4e18; // Khởi tạo âm vô cùng
    for (int i = k; i <= n; ++i) {
        for (int j = k; j <= m; ++j) {
            long long current = p[i][j] - p[i - k][j] - p[i][j - k] + p[i - k][j - k];
            max_sum = max(max_sum, current);
        }
    }

    cout << max_sum << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Thử thách học sinh giải bài toán khi dữ liệu cập nhật động liên tục (Online Queries).
* **Mở rộng 2:** Áp dụng thuật toán trên không gian nhiều chiều (Ma trận 2D hoặc đồ thị).
* **Tự giải thích:** Yêu cầu học sinh giải thích tại sao không thể dùng thuật toán ngây thơ và chứng minh độ phức tạp tối ưu trước lớp.
