# Hướng Dẫn Giảng Dạy: Tìm Kiếm Nhị Phân Bằng Đệ Quy (Cầu Nối Sang D&C)
Chuyên đề: **Kỹ Thuật Chia Để Trị (Divide and Conquer)**

**Phân loại chuyên đề:** `Core Foundation`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Chia Đôi Mảng & Tìm Kiếm Nhị Phân D&C.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân rã bài toán thành 3 pha chuẩn mực: `Divide` $\to$ `Solve` $\to$ `Combine`.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, tối ưu bộ nhớ đệm).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: Hai số nguyên $N, X$ ($1 \le N \le 10^5, |X| \le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ đã sắp xếp tăng dần ($|A_i| \le 10^9$).
* **Yêu cầu cốt lõi:** Cho mảng số nguyên $A$ gồm $N$ phần tử đã được sắp xếp tăng dần và số nguyên $X$. Hãy sử dụng hàm đệ quy Chia Để Trị `binarySearchDac(l, r, x)` để tìm vị trí xuất hiện đầu tiên của $X$ trong mảng (chỉ số 1-based). Nếu không tìm thấy, in ra `-1`.
* **Phân tích trường hợp biên:** Xử lý chính xác Base Case khi kích thước mảng thu nhỏ về $\le 1$ phần tử.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Làm thế nào để chia bài toán hiện tại thành các bài toán con độc lập có kích thước $N/2$?
2. Bước gộp (Combine) kết quả từ 2 nửa đòi hỏi những thao tác gì và độ phức tạp là bao nhiêu?
3. Tại sao kỹ thuật Chia Để Trị lại giúp giảm độ phức tạp so với duyệt vét cạn tuần tự?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Divide & Combine Invariant:** Đảm bảo tính đúng đắn được bảo toàn qua từng tầng gộp mảng.
* **Bộ nhớ đệm tái sử dụng:** Tránh cấp phát động liên tục trong hàm đệ quy để chống tràn bộ nhớ và TLE.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
5 7
1 3 5 7 9
```
* **Output:**
```text
4
```
* **Phân tích thực thi:** Số 7 xuất hiện tại vị trí thứ 4 trong mảng.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** $\Theta(\log N)$
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\Theta(\log N)$ (Độ sâu tối đa: $\log_2 N$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\mathcal{O}(1)$
* **Ghi chú phân tích:** D&C đơn nhánh (Single-branch), chỉ giải 1 nửa không gian tìm kiếm.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số 32-bit khi đếm nghịch thế hoặc tính tổng:** Luôn sử dụng kiểu dữ liệu `long long`.
2. **Bẫy bỏ sót trường hợp vắt ngang (Crossing):** Phải xét đầy đủ mọi khả năng giữa 2 nửa mảng.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

int binarySearchDac(const vector<long long> &a, int l, int r, long long x) {
    if (l > r) return -1;
    int mid = l + (r - l) / 2;
    if (a[mid] == x) {
        int left_res = binarySearchDac(a, l, mid - 1, x);
        if (left_res != -1) return left_res;
        return mid;
    }
    if (a[mid] > x) return binarySearchDac(a, l, mid - 1, x);
    return binarySearchDac(a, mid + 1, r, x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    int ans = binarySearchDac(a, 0, n - 1, x);
    if (ans != -1) ans += 1;
    cout << ans << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Vận dụng tư duy phân rã không gian tìm kiếm sang các bài toán hình học và chuẩn bị bước đệm cho Quay lui & Nhánh cận (Lesson 12).
