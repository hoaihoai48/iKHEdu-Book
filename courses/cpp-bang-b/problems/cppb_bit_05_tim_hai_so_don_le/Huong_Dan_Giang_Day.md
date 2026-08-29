# Hướng Dẫn Giảng Dạy: Tìm Hai Số Xuất Hiện 1 Lần Duy Nhất
Chuyên đề: **Phép Toán Bit & Biểu Diễn Trạng Thái (Bitmask)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ phương pháp giải quyết bài toán bằng kỹ thuật thuộc chuyên đề Phép Toán Bit & Biểu Diễn Trạng Thái (Bitmask).
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
1. Số lượng phần tử $N$ có đủ nhỏ ($N \le 22$) để duyệt toàn bộ $2^N$ trạng thái không?
2. Làm sao để kiểm tra, bật, tắt hoặc đảo trạng thái của phần tử thứ $k$ trong $\mathcal{O}(1)$?
3. Làm thế nào để duyệt toàn bộ các tập con thực sự (submasks) của một mask trong $\mathcal{O}(3^N)$?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Biểu diễn trạng thái tập hợp $N$ phần tử bằng số nguyên $N$ bit ($0 \dots 2^N - 1$).
- Sử dụng các phép toán bitwise `&, |, ^, ~, <<, >>` và các hàm nội tại CPU `__builtin_popcountll`, `__builtin_clzll` để thực thi trong $\mathcal{O}(1)$ chu kỳ máy.

### 4.2. Bất biến toán học (Invariant):
> Bit thứ $k$ bằng 1 đại diện cho phần tử thứ $k$ được chọn vào tập hợp con, bit thứ $k$ bằng 0 đại diện cho phần tử bị loại bỏ.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
2
1 2 1 3 2 5
```
* **Output:**
```text
3 5
```
* **Phân tích quá trình thực thi:**
  Thuật toán tiến hành khởi tạo cấu trúc dữ liệu, duyệt tuyến tính qua từng phần tử và cập nhật kết quả tối ưu theo đúng nguyên lý thiết kế.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(N \times 2^N)$ cho bài toán duyệt tập con, hoặc $\mathcal{O}(1)$ cho mỗi thao tác bitwise.
- **Không gian (Space Complexity):** $\mathcal{O}(1)$ bộ nhớ phụ trợ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. Quên ép kiểu `1LL << k` khi dịch bit với $k \ge 31$ dẫn đến tràn số 32-bit (Undefined Behavior).
2. Độ ưu tiên của các toán tử bitwise (`&, |, ^`) thấp hơn toán tử so sánh (`==, !=, <, >`), bắt buộc phải đóng ngoặc: `((mask >> k) & 1) == 1`.
3. Vét cạn $2^N$ với $N > 25$ dẫn đến TLE (số phép tính vượt quá $10^8$).

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

    int total_elements = 2 * n + 2;
    vector<long long> a(total_elements);
    long long xor_sum = 0;
    for (int i = 0; i < total_elements; ++i) {
        cin >> a[i];
        xor_sum ^= a[i];
    }

    // Lấy bit 1 phân biệt
    long long diff_bit = xor_sum & (-xor_sum);

    long long num1 = 0, num2 = 0;
    for (long long val : a) {
        if (val & diff_bit) {
            num1 ^= val;
        } else {
            num2 ^= val;
        }
    }

    if (num1 > num2) swap(num1, num2);
    cout << num1 << " " << num2 << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Thử thách học sinh giải bài toán khi dữ liệu cập nhật động liên tục (Online Queries).
* **Mở rộng 2:** Áp dụng thuật toán trên không gian nhiều chiều (Ma trận 2D hoặc đồ thị).
* **Tự giải thích:** Yêu cầu học sinh giải thích tại sao không thể dùng thuật toán ngây thơ và chứng minh độ phức tạp tối ưu trước lớp.
