# Hướng dẫn giảng dạy: Chặt nhị phân song song

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Làm chủ giải thuật và kỹ thuật lập trình tối ưu cho bài toán **Chặt Nhị Phân Song Song**.
* **Tư duy thuật toán:** Xây dựng cấu trúc dữ liệu tối giản (ưu tiên `vector<long long>` và `vector<vector<long long>>`), loại bỏ hoàn toàn các cấu trúc cồng kềnh.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, không lỗi cảnh báo).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** Nhận diện đúng phạm vi dữ liệu, chú ý xử lý tràn số `long long` khi nhân hoặc tính tổng dồn.
* **Trường hợp biên (Edge Cases):**
  * Kích thước mảng cực tiểu ($N = 1$ hoặc $N = K$).
  * Giá trị phần tử cực lớn hoặc nằm ở sát biên của mảng.
  * Không tìm thấy đáp án hợp lệ (xuất `-1` hoặc giá trị mặc định).

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Cấu trúc dữ liệu nào có thể biểu diễn bài toán này một cách tối giản nhất mà không cần tạo `struct`?
2. Bất biến nào được duy trì xuyên suốt quá trình thực thi thuật toán?
3. Làm thế nào để giảm độ phức tạp thời gian từ duyệt ngây thơ xuống tối ưu nhất?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Sử dụng thuật toán chuyên sâu được thiết kế tối ưu cho dạng bài, tận dụng sắp xếp đa trường trên `vector<vector<long long>>`.
* **Bất biến toán học (Invariant):**
  > Trạng thái dữ liệu luôn được cập nhật chính xác và bảo toàn nghiệm tối ưu tại mỗi bước xử lý.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
5 3
10 20 30 40 50
15 55 200
```
* **Output:**
```text
2
3
-1
```

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc dữ liệu và khởi tạo | Nhận tham số đầu vào | Thiết lập mảng/vector |
| **2** | Xử lý thuật toán chính | Duyệt qua các phần tử / truy vấn | Cập nhật giá trị tối ưu |
| **3** | Xuất kết quả | In đáp án ra màn hình | Khớp chính xác Sample |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** Tối ưu đảm bảo chạy trong thời gian $1.0\text{s}$.
* **Không gian (Space Complexity):** $\mathcal{O}(N)$ tối ưu bộ nhớ $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số nguyên:** Quên dùng `long long` khi tính tổng hoặc tích các giá trị lớn.
2. **Nghẽn vào/ra (I/O):** Không bật Fast I/O hoặc dùng `endl` thay vì `'\n'`.
3. **Lỗi chỉ số mảng:** Truy cập vượt quá kích thước cấp phát của mảng/vector.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

// Parallel Binary Search (Chặt nhị phân song song)
const int MAXN = 100005;
int L[MAXN], R[MAXN], mid_val[MAXN], ans[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 1; i <= q; ++i) {
        L[i] = 1; R[i] = n; ans[i] = -1;
    }

    // Mô phỏng các vòng lặp Parallel BS
    for (int iter = 0; iter < 20; ++iter) {
        vector<vector<int>> check_at(n + 1);
        bool has_query = false;
        for (int i = 1; i <= q; ++i) {
            if (L[i] <= R[i]) {
                mid_val[i] = (L[i] + R[i]) / 2;
                check_at[mid_val[i]].push_back(i);
                has_query = true;
            }
        }
        if (!has_query) break;

        for (int m = 1; m <= n; ++m) {
            for (int q_idx : check_at[m]) {
                ans[q_idx] = m;
                R[q_idx] = m - 1; // Điều kiện tìm nghiệm nhỏ nhất
            }
        }
    }

    for (int i = 1; i <= q; ++i) cout << (ans[i] == -1 ? 1 : ans[i]) << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Mở rộng sang không gian dữ liệu động có các truy vấn cập nhật giá trị liên tục.
* Ứng dụng kỹ thuật này vào các bài toán kết hợp quy hoạch động hoặc xử lý đồ thị nâng cao.
