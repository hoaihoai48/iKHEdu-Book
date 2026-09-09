# Hướng Dẫn Giảng Dạy: Tìm Giá Trị Lớn Nhất & Vị Trí Xuất Hiện
Chuyên đề: **Chương 01 — Bài 03: Mảng 1 Chiều, Vector, Xâu Ký Tự & Tổ Chức Hàm**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Thành thạo mẫu tích lũy Cực trị (Finding Maximum Pattern).
- Biết cách khởi tạo biến `max_val` an toàn bằng chính phần tử đầu tiên `a[0]`.
- Nắm vững kỹ thuật chuyển đổi chỉ số giữa $0$-based (nội bộ C++) và $1$-based (yêu cầu đề bài).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Khởi tạo: Gán `max_val = a[0]` và `best_pos = 1`.
- Duyệt từ $i = 1$ đến $N - 1$: Nếu gặp $a[i] > \text{max\_val}$ thì cập nhật `max_val = a[i]` và `best_pos = i + 1`.
- Chú ý: Dùng dấu $>$ ngặt (chứ không dùng $\ge$) để đảm bảo giữ nguyên vị trí xuất hiện đầu tiên khi có nhiều phần tử bằng nhau.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Nếu tất cả các phần tử đều là số âm, khởi tạo `max_val = 0` có đúng không (Sai hoàn toàn vì 0 lớn hơn mọi số âm).
- Để lưu vị trí xuất hiện đầu tiên, ta dùng điều kiện so sánh `>` hay `>=`

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Khởi tạo giá trị lớn nhất bằng `a[0]`.
- Duyệt tuyến tính $\mathcal{O}(N)$ cập nhật cực trị.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Chỉ số $i$ | Giá trị $a[i]$ | So sánh với `max_val` | Cập nhật `max_val` | Cập nhật `best_pos` |
|:---:|:---:|:---:|:---:|:---:|
| 0 | `3` | Khởi tạo ban đầu | `3` | `1` |
| 1 | `7` | $7 > 3$ (Đúng) | `7` | `2` |
| 2 | `2` | $2 > 7$ (Sai) | `7` | `2` |
| 3 | `7` | $7 > 7$ (Sai, vì dấu $>$ ngặt) | `7` | `2` |
| 4 | `5` | $5 > 7$ (Sai) | `7` | `2` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(N)$.
- Không gian: $\mathcal{O}(N)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Khởi tạo `max_val = 0` thay vì `a[0]` (sai với mảng toàn số âm).
- Dùng `>=` khiến vị trí bị cập nhật thành vị trí xuất hiện cuối cùng.
- In ra chỉ số $0$-based thay vì $1$-based.

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

vector<long long> a(n);
for (int i = 0; i < n; i++) {
cin >> a[i];
}

long long max_val = a[0];
int best_pos = 1;

for (int i = 1; i < n; i++) {
if (a[i] > max_val) {
max_val = a[i];
best_pos = i + 1;
}
}

cout << max_val << ' ' << best_pos << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tìm giá trị lớn thứ nhì trong mảng.
- Tìm giá trị nhỏ nhất và khoảng cách giữa vị trí nhỏ nhất và lớn nhất.
