# BẢN TIN TỔNG KẾT BUỔI HỌC VÀ BÀI TẬP THỰC HÀNH C++ (GỬI PHỤ HUYNH & HỌC SINH)
**Khóa học:** C++ Lập trình thi đấu iKHEDU - Bảng B  
**Bài 04:** Thuật toán sắp xếp & Hàm so sánh Comparator

---

## 🌟 PHẦN 1: HÌNH ẢNH TỔNG KẾT BUỔI HỌC (CHUẨN ĐỒ HỌA HD SẮC NÉT)

> Hình ảnh tổng kết chính thức buổi học hôm nay (chuẩn phong cách đồ họa iKHEDU, bố cục hài hòa, chữ và code nét 100%):

![Tổng kết buổi học hôm nay - Bài 04: Thuật toán sắp xếp](/Users/vu/Developer/ikhEdu_lessons/assets/Noi_dung_bai_hoc_Bai_04_Sap_Xep.png)

---

## 📚 PHẦN 2: TÓM TẮT TRỌNG TÂM KIẾN THỨC BÀI 04

### 1. Bản chất & Tính chất lân cận (Adjacency Property)
- **Sắp xếp** không chỉ để hiển thị mà là một **phép biến đổi cấu trúc dữ liệu** giúp tối ưu thuật toán từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N \log N)$.
- **Tính chất lân cận:** Trong một mảng đã được sắp xếp tăng dần, **khoảng cách nhỏ nhất giữa hai phần tử bất kỳ luôn rơi vào ít nhất một cặp phần tử liền kề nhau** $(A_i, A_{i+1})$. Nhờ đó ta chỉ cần duyệt qua $N-1$ cặp thay vì kiểm tra toàn bộ các cặp rời nhau.

---

### 2. Cú pháp hàm `sort` trong C++
- Thư viện: `#include <bits/stdc++.h>`
- Sắp xếp tăng dần:
  ```cpp
  sort(a.begin(), a.end());
  ```
- Sắp xếp giảm dần:
  ```cpp
  sort(a.rbegin(), a.rend());
  // Hoặc dùng: sort(a.begin(), a.end(), greater<long long>());
  ```
- Quy tắc nửa mở: Đoạn được sắp xếp là $[first, last)$ — bao gồm `first` nhưng **không bao gồm** vị trí `last`.

---

### 3. Hàm so sánh tự định nghĩa (Custom Comparator)
- Khi bài toán yêu cầu quy tắc sắp xếp đặc thù hoặc đa tiêu chí, ta tự viết hàm `cmp`:
  ```cpp
  sort(a.begin(), a.end(), cmp);
  ```
- **Nguyên lý Strict Weak Ordering (Tử huyệt lập trình):**
  - Hàm `cmp(u, v)` trả về `true` khi và chỉ khi `u` **bắt buộc phải đứng trước** `v`.
  - Khi hai phần tử bằng nhau ($u == v$), hàm so sánh **bắt buộc phải trả về `false`**.
  - ⚠️ **CẢNH BÁO TỬ HUYỆT:** Tuyệt đối **CẤM** dùng toán tử `<=` hoặc `>=` trong comparator. Viết `return u <= v;` sẽ vi phạm tiên đề toán học dẫn tới **Runtime Error / Crash tràn bộ nhớ** trong các bài thi!

---

## 🎯 PHẦN 3: ĐỀ BÀI & MÃ NGUỒN GIẢI CHUẨN 2 BÀI TẬP TRỌNG TÂM

### Bài 1: Khoảng Cách Nhỏ Nhất Giữa Hai Trạm Cảm Biến
- **Bối cảnh & Nhiệm vụ:** Cho $N$ trạm cảm biến môi trường có tọa độ $A_1, A_2, \dots, A_N$ ($2 \le N \le 10^5, A_i \le 10^9$). Tìm khoảng cách ngắn nhất giữa 2 trạm bất kỳ để chống can nhiễu tín hiệu vô tuyến.
- **Chiến lược giải thuật:** 
  1. Sắp xếp mảng tăng dần bằng `sort(a.begin(), a.end())` mất $\mathcal{O}(N \log N)$.
  2. Quét qua $N - 1$ cặp kề nhau $(A_i, A_{i+1})$ để tìm hiệu nhỏ nhất $\min(A_{i+1} - A_i)$ mất $\mathcal{O}(N)$.
- **Mã nguồn giải chuẩn C++:**
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long ans = a[1] - a[0];
    for (int i = 1; i < n - 1; ++i) {
        ans = min(ans, a[i + 1] - a[i]);
    }

    cout << ans << "\n";
    return 0;
}
```

---

### Bài 2: Sắp Xếp Theo Trị Tuyệt Đối & Ưu Tiên Số Âm
- **Bối cảnh & Nhiệm vụ:** Cho độ lệch nhiệt độ của $N$ mẫu khoáng thạch ($N \le 10^5, |A_i| \le 10^9$). Sắp xếp các mẫu theo giá trị tuyệt đối tăng dần. Nếu có cùng giá trị tuyệt đối, mẫu bị làm lạnh (số âm) phải đứng trước mẫu bị nóng lên (số dương).
- **Chiến lược giải thuật:**
  - Viết hàm so sánh hai tiêu chí `cmp(u, v)`:
    - Nếu $|u| \ne |v|$: ưu tiên $|u| < |v|$.
    - Nếu $|u| == |v|$: ưu tiên $u < v$ (vì số âm nhỏ hơn số dương nên sẽ tự động đứng trước).
- **Mã nguồn giải chuẩn C++:**
```cpp
#include <bits/stdc++.h>
using namespace std;

bool cmp(long long u, long long v) {
    if (abs(u) != abs(v)) return abs(u) < abs(v);
    return u < v; // Khi cùng trị tuyệt đối: số âm đứng trước số dương
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---
*Tài liệu học tập được chuẩn hóa theo tiêu chuẩn thi đấu iKHEDU - DKOJ.*
