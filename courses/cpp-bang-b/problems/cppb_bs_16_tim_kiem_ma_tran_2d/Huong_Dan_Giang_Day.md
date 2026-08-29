# Hướng Dẫn Giảng Dạy: Tìm Kiếm Trên Ma Trận 2D Đã Sắp Xếp (Matrix Search)
Chuyên đề: **Thuật Toán Tìm Kiếm Nhị Phân (Binary Search)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ phương pháp giải quyết bài toán bằng kỹ thuật thuộc chuyên đề Thuật Toán Tìm Kiếm Nhị Phân (Binary Search).
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
1. Hàm mục tiêu có tính chất đơn điệu (tăng/giảm một chiều) khi biến đổi giá trị nghiệm giả định không?
2. Khi `check(mid) == true`, đáp án tối ưu hơn có thể nằm ở nửa trái hay nửa phải?
3. Giá trị nhỏ nhất và lớn nhất khả dĩ của nghiệm ($low, high$) là bao nhiêu?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Nhận diện tính chất đơn điệu của không gian tìm kiếm hoặc hàm kiểm tra `check(mid)`.
- Thiết lập không gian tìm kiếm $[low, high]$.
- Tại mỗi bước lặp, tính $mid = low + (high - low) / 2$, gọi `check(mid)` và thu hẹp $50\%$ không gian tìm kiếm.

### 4.2. Bất biến toán học (Invariant):
> Nghiệm tối ưu luôn được bảo toàn nằm trọn vẹn trong khoảng $[low, high]$ sau mỗi bước thu hẹp.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
3 4 2
1 3 5 7
10 11 16 20
23 30 34 60
3
13
```
* **Output:**
```text
YES
NO
```
* **Phân tích quá trình thực thi:**
  Thuật toán tiến hành khởi tạo cấu trúc dữ liệu, duyệt tuyến tính qua từng phần tử và cập nhật kết quả tối ưu theo đúng nguyên lý thiết kế.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(\log(\text{Range}) \times \text{Cost}(\text{check}))$. Với Range $= 10^{18}$, chỉ mất tối đa $\approx 60$ lần lặp chia đôi không gian.
- **Không gian (Space Complexity):** $\mathcal{O}(1)$ hoặc $\mathcal{O}(N)$ phụ thuộc vào cấu trúc dữ liệu của hàm `check`.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. Tràn số khi tính `mid = (low + high) / 2` với $low, high \ge 2 \cdot 10^9$ (phải dùng `low + (high - low) / 2`).
2. Vòng lặp vô tận khi không gian còn 2 phần tử do làm tròn số hoặc cập nhật sai biên ($low = mid$ thay vì $low = mid + 1$).
3. Đặt biên $high$ quá nhỏ dẫn đến bỏ sót nghiệm tối ưu, hoặc $low = 0$ gây chia cho 0 trong hàm `check`.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    while (q--) {
        long long target;
        cin >> target;

        int low = 0, high = n * m - 1;
        bool found = false;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int r = mid / m;
            int c = mid % m;

            if (a[r][c] == target) {
                found = true;
                break;
            } else if (a[r][c] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        cout << (found ? "YES\n" : "NO\n");
    }

    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Thử thách học sinh giải bài toán khi dữ liệu cập nhật động liên tục (Online Queries).
* **Mở rộng 2:** Áp dụng thuật toán trên không gian nhiều chiều (Ma trận 2D hoặc đồ thị).
* **Tự giải thích:** Yêu cầu học sinh giải thích tại sao không thể dùng thuật toán ngây thơ và chứng minh độ phức tạp tối ưu trước lớp.
