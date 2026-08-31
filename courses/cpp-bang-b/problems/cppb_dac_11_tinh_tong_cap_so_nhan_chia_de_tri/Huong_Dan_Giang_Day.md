# Hướng Dẫn Giảng Dạy: Tính Tổng Cấp Số Nhân D&C
Chuyên đề: **Kỹ Thuật Chia Để Trị (Divide and Conquer)**

**Phân loại chuyên đề:** `Core Foundation`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Tính Tổng Cấp Số Nhân D&C.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân rã bài toán thành 3 pha chuẩn mực: `Divide` $\to$ `Solve` $\to$ `Combine`.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, tối ưu bộ nhớ đệm).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Một dòng duy nhất chứa 3 số nguyên $A, N, M$ ($0 \le A, N \le 10^9, 1 \le M \le 10^9 + 7$).
* **Yêu cầu cốt lõi:** Cho 3 số nguyên $A, N, M$. Hãy tính tổng cấp số nhân $S(N) = A^0 + A^1 + A^2 + \dots + A^N \pmod M$ bằng kỹ thuật Chia Để Trị trong $\mathcal{O}(\log N)$ theo hệ thức $S(2k+1) = S(k) \times (1 + A^{k+1})$.
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
2 3 1000
```
* **Output:**
```text
15
```
* **Phân tích thực thi:** 2^0 + 2^1 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** $\Theta(\log N)$
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\Theta(\log N)$ (Độ sâu tối đa: $\log_2 N$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\mathcal{O}(1)$
* **Ghi chú phân tích:** S(2k+1) = S(k) * (1 + A^(k+1)) chia đôi độ dài chuỗi tổng.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số 32-bit khi đếm nghịch thế hoặc tính tổng:** Luôn sử dụng kiểu dữ liệu `long long`.
2. **Bẫy bỏ sót trường hợp vắt ngang (Crossing):** Phải xét đầy đủ mọi khả năng giữa 2 nửa mảng.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

long long powerMod(long long a, long long b, long long m) {
    long long res = 1 % m;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

long long sumGeoDac(long long a, long long n, long long m) {
    if (n == 0) return 1 % m;
    if (n % 2 == 1) {
        long long k = n / 2;
        long long half_sum = sumGeoDac(a, k, m);
        long long mult = (1 + powerMod(a, k + 1, m)) % m;
        return (half_sum * mult) % m;
    } else {
        long long prev = sumGeoDac(a, n - 1, m);
        return (prev + powerMod(a, n, m)) % m;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a, n, m;
    if (!(cin >> a >> n >> m)) return 0;
    cout << sumGeoDac(a, n, m) << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Vận dụng tư duy phân rã không gian tìm kiếm sang các bài toán hình học và chuẩn bị bước đệm cho Quay lui & Nhánh cận (Lesson 12).
