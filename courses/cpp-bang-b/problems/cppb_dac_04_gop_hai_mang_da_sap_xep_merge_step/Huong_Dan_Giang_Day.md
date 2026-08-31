# Hướng Dẫn Giảng Dạy: Gộp Hai Mảng Đã Sắp Xếp (Merge Step)
Chuyên đề: **Kỹ Thuật Chia Để Trị (Divide and Conquer)**

**Phân loại chuyên đề:** `Core Foundation`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Gộp Hai Mảng Đã Sắp Xếp (Merge Step).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân rã bài toán thành 3 pha chuẩn mực: `Divide` $\to$ `Solve` $\to$ `Combine`.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, tối ưu bộ nhớ đệm).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: Hai số nguyên $N, M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ đã sắp xếp tăng dần ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên $B_1, \dots, B_M$ đã sắp xếp tăng dần ($|B_j| \le 10^9$).
* **Yêu cầu cốt lõi:** Cho 2 dãy số nguyên $A$ (gồm $N$ phần tử) và $B$ (gồm $M$ phần tử) đều đã được sắp xếp tăng dần. Hãy cài đặt bước gộp `merge()` bằng kỹ thuật 2 con trỏ trong $\mathcal{O}(N + M)$ để gộp $A$ và $B$ thành một dãy số tăng dần duy nhất.
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
3 4
1 5 8
2 3 6 9
```
* **Output:**
```text
1 2 3 5 6 8 9
```
* **Phân tích thực thi:** Mảng sau khi gộp tăng dần: 1 2 3 5 6 8 9.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** $\Theta(N + M)$
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\mathcal{O}(1)$ (Độ sâu tối đa: $1$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\mathcal{O}(1)$
* **Ghi chú phân tích:** Nền tảng của bước Combine trong Merge Sort bằng 2 con trỏ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số 32-bit khi đếm nghịch thế hoặc tính tổng:** Luôn sử dụng kiểu dữ liệu `long long`.
2. **Bẫy bỏ sót trường hợp vắt ngang (Crossing):** Phải xét đầy đủ mọi khả năng giữa 2 nửa mảng.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int j = 0; j < m; ++j) cin >> b[j];

    int i = 0, j = 0;
    bool first = true;
    while (i < n && j < m) {
        if (!first) cout << " ";
        if (a[i] <= b[j]) {
            cout << a[i++];
        } else {
            cout << b[j++];
        }
        first = false;
    }
    while (i < n) {
        if (!first) cout << " ";
        cout << a[i++];
        first = false;
    }
    while (j < m) {
        if (!first) cout << " ";
        cout << b[j++];
        first = false;
    }
    cout << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Vận dụng tư duy phân rã không gian tìm kiếm sang các bài toán hình học và chuẩn bị bước đệm cho Quay lui & Nhánh cận (Lesson 12).
