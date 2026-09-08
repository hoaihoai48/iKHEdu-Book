# Hướng Dẫn Giảng Dạy: Đảo Ngược Mảng
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Đọc mảng vào `vector`.
- Duyệt ngược mảng.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- In từ $a[n-1]$ về $a[0]$.
- Hoặc dùng `reverse(a.begin(), a.end())` rồi in.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Duyệt ngược thì vòng `for` viết thế nào?
- Có cách nào không cần lưu mảng không? (Nếu $N$ lớn?)

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Đọc vào vector, in ngược. $\mathcal{O}(N)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $i$ | $a[i]$ | Output |
|---|---|---|
| 4 | 5 | 5 |
| 3 | 4 | 5 4 |
| 2 | 3 | 5 4 3 |
| 1 | 2 | 5 4 3 2 |
| 0 | 1 | 5 4 3 2 1 |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(N)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Dùng `int i = n; i >= 0` → truy cập `a[n]` ngoài mảng.
- **Bẫy 2:** In dấu cách thừa ở cuối dòng.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    for (int i = n - 1; i >= 0; i--) {
        cout << a[i] << (i == 0 ? "" : " ");
    }
    cout << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Đảo mảng tại chỗ bằng swap (hai con trỏ).
- Đảo một đoạn con $[l, r]$.
