# Hướng Dẫn Giảng Dạy: Đếm Số Đoạn Con Tổng Trong Đoạn [L, R]
Chuyên đề: **Kỹ Thuật Chia Để Trị (Divide and Conquer)**

**Phân loại chuyên đề:** `Advanced`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Đếm Số Đoạn Con Tổng Trong Đoạn [L, R].
* **Tư duy thuật toán:** Rèn luyện phản xạ phân rã bài toán thành 3 pha chuẩn mực: `Divide` $\to$ `Solve` $\to$ `Combine`.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, tối ưu bộ nhớ đệm).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: 3 số nguyên $N, Lower, Upper$ ($1 \le N \le 10^5, -10^{14} \le Lower \le Upper \le 10^{14}$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).
* **Yêu cầu cốt lõi:** Cho mảng số nguyên $A$ gồm $N$ phần tử và hai số nguyên $Lower, Upper$. Hãy đếm số lượng đoạn con liên tiếp khác rỗng $A[i..j]$ ($1 \le i \le j \le N$) có tổng $\sum_{k=i}^j A_k$ nằm trong đoạn $[Lower, Upper]$ bằng Chia Để Trị trên mảng tiền tố (Prefix Sum Merge Count) trong $\mathcal{O}(N \log N)$.
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
3 -2 2
0 -3 1
```
* **Output:**
```text
3
```
* **Phân tích thực thi:** Các đoạn con thỏa mãn: [0] (tổng 0), [1] (tổng 1), [0, -3, 1] (tổng -2).

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** $\Theta(N \log N)$
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\Theta(\log N)$ (Độ sâu tối đa: $\log_2 N$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\Theta(N)$
* **Ghi chú phân tích:** Chia để trị trên mảng tổng tiền tố (Prefix Sum Merge Count).

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số 32-bit khi đếm nghịch thế hoặc tính tổng:** Luôn sử dụng kiểu dữ liệu `long long`.
2. **Bẫy bỏ sót trường hợp vắt ngang (Crossing):** Phải xét đầy đủ mọi khả năng giữa 2 nửa mảng.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

long long countSubarraysDac(vector<long long> &prefix, vector<long long> &temp, int l, int r, long long lower, long long upper) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long cnt = 0;
    cnt += countSubarraysDac(prefix, temp, l, mid, lower, upper);
    cnt += countSubarraysDac(prefix, temp, mid + 1, r, lower, upper);

    int j1 = mid + 1, j2 = mid + 1;
    for (int i = l; i <= mid; ++i) {
        while (j1 <= r && prefix[j1] - prefix[i] < lower) j1++;
        while (j2 <= r && prefix[j2] - prefix[i] <= upper) j2++;
        cnt += (j2 - j1);
    }

    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        if (prefix[i] <= prefix[j]) temp[k++] = prefix[i++];
        else temp[k++] = prefix[j++];
    }
    while (i <= mid) temp[k++] = prefix[i++];
    while (j <= r) temp[k++] = prefix[j++];
    for (int idx = l; idx <= r; ++idx) prefix[idx] = temp[idx];

    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long lower, upper;
    if (!(cin >> n >> lower >> upper)) return 0;
    vector<long long> a(n);
    vector<long long> prefix(n + 1, 0), temp(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        prefix[i + 1] = prefix[i] + a[i];
    }
    cout << countSubarraysDac(prefix, temp, 0, n, lower, upper) << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Vận dụng tư duy phân rã không gian tìm kiếm sang các bài toán hình học và chuẩn bị bước đệm cho Quay lui & Nhánh cận (Lesson 12).
