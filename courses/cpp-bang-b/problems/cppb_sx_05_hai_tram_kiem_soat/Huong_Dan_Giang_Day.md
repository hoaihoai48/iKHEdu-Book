# Hướng Dẫn Giảng Dạy: Hai Trạm Kiểm Soát Gần Nhau Nhất
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ phương pháp giải quyết bài toán bằng kỹ thuật thuộc chuyên đề Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting).
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
1. Nếu mảng chưa có thứ tự, ta phải tốn bao nhiêu chi phí để kiểm tra mọi cặp phần tử?
2. Khi sắp xếp mảng tăng dần, các phần tử có khoảng cách nhỏ nhất sẽ nằm ở đâu?
3. Ta có thể gom nhóm hoặc loại bỏ các phần tử trùng lặp trong thời gian tuyến tính sau khi sắp xếp không?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Tận dụng tính chất lân cận của mảng sau khi sắp xếp: các phần tử có giá trị gần nhau nhất luôn nằm kề nhau.
- Sử dụng hàm `sort` kết hợp Comparator chuẩn Strict Weak Ordering để định hình lại cấu trúc dữ liệu trong $\mathcal{O}(N \log N)$.

### 4.2. Bất biến toán học (Invariant):
> Sau khi sắp xếp, $\forall i < j \implies A_i \le A_j$. Mọi cặp phần tử tối ưu khoảng cách luôn có dạng $(A_k, A_{k+1})$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
6
1500 300 2800 800 1200 3150
```
* **Output:**
```text
300
```
* **Phân tích quá trình thực thi:**
  Thuật toán tiến hành khởi tạo cấu trúc dữ liệu, duyệt tuyến tính qua từng phần tử và cập nhật kết quả tối ưu theo đúng nguyên lý thiết kế.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(N \log N)$ cho bước sắp xếp và $\mathcal{O}(N)$ cho bước duyệt tuyến tính $\implies$ Tổng thời gian: $\mathcal{O}(N \log N)$, chạy mượt mà dưới $0.1\text{s}$ với $N = 10^5$.
- **Không gian (Space Complexity):** $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$ phụ thuộc vào việc xử lý mảng tại chỗ (in-place).

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. Sử dụng dấu `<=` trong hàm so sánh dẫn đến vi phạm tiên đề Strict Weak Ordering gây Runtime Error / Crash.
2. Tràn số khi nhân hoặc cộng các phần tử vượt giới hạn $2 \cdot 10^9$ (cần dùng `long long`).
3. Quên lưu lại chỉ số gốc khi đề bài yêu cầu truy vết vị trí ban đầu.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    sort(x.begin(), x.end());

    long long min_dist = x[1] - x[0];
    for (int i = 1; i < n - 1; ++i) {
        min_dist = min(min_dist, x[i + 1] - x[i]);
    }

    cout << min_dist << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Thử thách học sinh giải bài toán khi dữ liệu cập nhật động liên tục (Online Queries).
* **Mở rộng 2:** Áp dụng thuật toán trên không gian nhiều chiều (Ma trận 2D hoặc đồ thị).
* **Tự giải thích:** Yêu cầu học sinh giải thích tại sao không thể dùng thuật toán ngây thơ và chứng minh độ phức tạp tối ưu trước lớp.
