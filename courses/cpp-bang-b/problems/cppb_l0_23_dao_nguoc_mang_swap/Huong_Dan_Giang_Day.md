# Hướng Dẫn Giảng Dạy: Đảo Ngược Mảng Bằng Kỹ Thuật Hoán Đổi
Chuyên đề: **Chương 01 — Bài 03: Mảng 1 Chiều, Vector, Xâu Ký Tự & Tổ Chức Hàm**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Thành thạo hàm hoán đổi `swap(x, y)`.
- Hiểu sâu sắc cơ chế truyền tham chiếu `vector<int>& a` (thay đổi giá trị thực của mảng sau khi gọi hàm).
- Làm quen với mô hình tư duy Hai con trỏ (Two Pointers) cơ bản nhất để chuẩn bị cho Chương 02.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Hai con trỏ: $l = 0$ (đầu mảng) và $r = n - 1$ (cuối mảng).
- Chừng nào $l < r$, ta hoán đổi giá trị của $a[l]$ và $a[r]$, sau đó tăng $l++$ và giảm $r--$.
- Khi $l \ge r$, toàn bộ mảng đã được đảo ngược đối xứng hoàn hảo.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Nếu hàm viết `void reverseArray(vector<int> a)` (thiếu dấu `&`) thì mảng ở hàm `main` có bị thay đổi không (Không, vì chỉ thay đổi trên bản sao).
- Vì sao điều kiện lặp lại là $l < r$ mà không phải $l \le r$

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đảo ngược tại chỗ (in-place) với $\mathcal{O}(1)$ bộ nhớ phụ trội và $\mathcal{O}(N/2) = \mathcal{O}(N)$ phép toán.

---

## 5. Mô Phỏng Từng Bước Trên Sample ($[1, 2, 3, 4, 5]$)

| Bước | Con trỏ $l$ | Con trỏ $r$ | Cặp hoán đổi | Mảng sau hoán đổi |
|:---:|:---:|:---:|:---:|:---:|
| 1 | `0` (gt: 1) | `4` (gt: 5) | `swap(a[0], a[4])` | `[5, 2, 3, 4, 1]` |
| 2 | `1` (gt: 2) | `3` (gt: 4) | `swap(a[1], a[3])` | `[5, 4, 3, 2, 1]` |
| 3 | `2` (gt: 3) | `2` (gt: 3) | $l = r$ (Dừng) | `[5, 4, 3, 2, 1]` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(N)$.
- Không gian: $\mathcal{O}(1)$ bộ nhớ phụ trợ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Quên dấu tham chiếu `&` trong tham số hàm.
- Cho hai con trỏ chạy quá đà (chạy từ $0$ đến $n-1$ dẫn đến hoán đổi hai lần khiến mảng quay trở lại như cũ).

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

void reverseArray(vector<int>& a) {
int l = 0;
int r = (int)a.size() - 1;
while (l < r) {
swap(a[l], a[r]);
l++;
r--;
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;

vector<int> a(n);
for (int i = 0; i < n; i++) {
cin >> a[i];
}

reverseArray(a);

for (int i = 0; i < n; i++) {
cout << a[i] << (i == n - 1 '\n' : ' ');
}

return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Đảo ngược một đoạn con từ vị trí $L$ đến vị trí $R$ trong mảng.
- Thuật toán xoay mảng sang phải $K$ vị trí bằng 3 lần đảo ngược mảng.
