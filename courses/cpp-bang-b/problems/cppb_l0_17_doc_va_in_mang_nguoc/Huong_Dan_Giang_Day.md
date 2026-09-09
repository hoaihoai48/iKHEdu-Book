# Hướng Dẫn Giảng Dạy: Đọc Và In Mảng Theo Thứ Tự Ngược Lại
Chuyên đề: **Chương 01 — Bài 03: Mảng 1 Chiều, Vector, Xâu Ký Tự & Tổ Chức Hàm**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Làm quen với cấu trúc dữ liệu mảng động `vector<int> a(n)`.
- Nắm vững quy tắc chỉ số trong C++: bắt đầu từ `0` đến `n - 1`.
- Thành thạo vòng lặp duyệt ngược: `for (int i = n - 1; i >= 0; i--)`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Mảng có $N$ phần tử: phần tử đầu tiên nằm tại chỉ số `0`, phần tử cuối cùng nằm tại chỉ số `n - 1`.
- Để duyệt ngược, ta cho biến chỉ số $i$ chạy từ `n - 1` giảm dần về `0` với bước nhảy `i--`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Nếu mảng có 5 phần tử thì phần tử cuối cùng mang chỉ số mấy (Chỉ số 4).
- Vòng lặp duyệt ngược bắt đầu từ đâu và điều kiện dừng là gì

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Khởi tạo `vector<int> a(n)`.
- Đọc từng phần tử qua vòng lặp.
- Duyệt ngược từ `n - 1` về `0` và in ra. Độ phức tạp $\mathcal{O}(N)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample ($N = 5$)

| Chỉ số $i$ | `4` | `3` | `2` | `1` | `0` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Giá trị $a[i]$ | `9` | `7` | `5` | `3` | `1` |
| Thứ tự in | 1 | 2 | 3 | 4 | 5 |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(N)$.
- Không gian: $\mathcal{O}(N)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Bẫy truy cập ngoài phạm vi (Out of bounds): Bắt đầu duyệt từ $i = n$ (phần tử `a[n]` không tồn tại, gây lỗi bộ nhớ).
- Viết điều kiện dừng `i > 0` thay vì `i >= 0` (bỏ quên phần tử đầu tiên `a[0]`).

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
for (int i = 0; i < n; i++) {
cin >> a[i];
}

for (int i = n - 1; i >= 0; i--) {
cout << a[i] << (i == 0 '\n' : ' ');
}

return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Đảo ngược mảng trực tiếp bằng hàm `reverse(a.begin(), a.end())` hoặc kỹ thuật hoán đổi 2 con trỏ `swap(a[l], a[r])`.
