# Hướng Dẫn Giảng Dạy: Bảng Đếm Tần Suất Ký Tự Trong Xâu
Chuyên đề: **Chương 01 — Bài 03: Mảng 1 Chiều, Vector, Xâu Ký Tự & Tổ Chức Hàm**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Nắm vững kỹ thuật ánh xạ ký tự sang chỉ số mảng bằng mã ASCII: `index = c - 'a'`.
- Sử dụng mảng đếm tần suất (Frequency Array) kích thước cố định 26 phần tử.
- Xử lý điều kiện ưu tiên thứ tự từ điển: duyệt từ $i = 0$ đến 25 với điều kiện $>$ ngặt để tự động ưu tiên ký tự có mã nhỏ hơn.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Bảng chữ cái tiếng Anh in thường có 26 ký tự từ `'a'` đến `'z'`.
- Khi lấy ký tự `c - 'a'`, ta nhận được giá trị từ `0` đến `25` (với `'a' - 'a' = 0`, `'b' - 'a' = 1`, ..., `'z' - 'a' = 25`).
- Mảng `freq[26]` khởi tạo toàn 0. Mỗi khi gặp ký tự `c`, tăng `freq[c - 'a']++`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Trong bảng mã ASCII, ký tự `'a'` và `'b'` cách nhau bao nhiêu đơn vị
- Làm thế nào để dùng một mảng số nguyên để đếm số lần xuất hiện của 26 chữ cái

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Duyệt qua xâu cập nhật bảng đếm: $\mathcal{O}(|S|)$.
- Tìm giá trị lớn nhất trong mảng 26 phần tử: $\mathcal{O}(26) = \mathcal{O}(1)$.
- Tổng thời gian: $\mathcal{O}(|S|)$ cực kỳ tối ưu so với cách đếm từng phần tử tốn $\mathcal{O}(|S|^2)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (`abracadabra`)

| Ký tự | Chỉ số `c - 'a'` | Tần suất đếm được |
|:---:|:---:|:---:|
| `a` | 0 | `5` |
| `b` | 1 | `2` |
| `c` | 2 | `1` |
| `d` | 3 | `1` |
| `r` | 17 | `2` |
| Max | **0 (`a`)** | **5** |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(|S| + 26) = \mathcal{O}(|S|)$.
- Không gian: $\mathcal{O}(26) = \mathcal{O}(1)$ bộ nhớ phụ trợ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Quên khởi tạo mảng tần suất bằng 0 (`int freq[26] = {};`).
- Ánh xạ sai chỉ số thành `c` thay vì `c - 'a'`.
- Dùng `>=` khi so sánh tần suất làm mất tính ưu tiên thứ tự từ điển nhỏ hơn.

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

int best_char_idx = 0;
for (int i = 1; i < 26; i++) {
if (freq[i] > freq[best_char_idx]) {
best_char_idx = i;
}
}

char ans_char = (char)('a' + best_char_idx);
cout << ans_char << ' ' << freq[best_char_idx] << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Kiểm tra hai xâu có phải là đảo từ (Anagram) của nhau không.
- Tìm ký tự đầu tiên không bị lặp lại trong xâu.
