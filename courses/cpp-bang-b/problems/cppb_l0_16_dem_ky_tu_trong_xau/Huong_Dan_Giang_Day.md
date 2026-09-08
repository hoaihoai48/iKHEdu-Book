# Hướng Dẫn Giảng Dạy: Đếm Ký Tự Trong Xâu
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Duyệt xâu ký tự.
- Mảng tần suất 26 phần tử.
- Tìm max trong mảng tần suất.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Mảng `freq[26]` đếm tần suất từng chữ cái.
- Chỉ số: `c - 'a'` chuyển ký tự thành số 0–25.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Làm sao chuyển `'a'` thành $0$, `'b'` thành $1$?
- Tại sao cần mảng 26 phần tử?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Đếm tần suất $\mathcal{O}(|S|)$, tìm max trong 26 phần tử $\mathcal{O}(26)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Ký tự | a | b | c | d | r |
|---|---|---|---|---|---|
| Tần suất | 5 | 2 | 1 | 1 | 2 |

Max = `a` với $5$ lần.

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(|S| + 26) = \mathcal{O}(|S|)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Quên khởi tạo `freq[26] = {}` (mảng rác).
- **Bẫy 2:** Nếu duyệt tìm max bằng `>` (strict), tự động chọn ký tự nhỏ nhất khi bằng nhau.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int freq[26] = {};
    for (char c : s) {
        freq[c - 'a']++;
    }

    int best = 0;
    for (int i = 1; i < 26; i++) {
        if (freq[i] > freq[best]) best = i;
    }
    cout << (char)('a' + best) << ' ' << freq[best] << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Đếm nguyên âm, phụ âm.
- Kiểm tra xâu palindrome.
- Nén RLE (Run-Length Encoding).
