# Hướng Dẫn Giảng Dạy: Đếm Số Phần Tử Chẵn Trong Vector
Chuyên đề: **Chương 01 — Bài 03: Mảng 1 Chiều, Vector, Xâu Ký Tự & Tổ Chức Hàm**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Kết hợp duyệt vector với kiểm tra điều kiện phần tử `a[i] % 2 == 0`.
- Rèn luyện kỹ thuật đếm trực tiếp ngay trong quá trình nhập dữ liệu (Stream processing) để tối ưu code.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Duyệt qua từng phần tử của mảng, nếu phần tử chia hết cho 2 (`x % 2 == 0`), tăng biến đếm `count_even++`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Khi một số âm chẵn (như -4) chia dư cho 2 thì kết quả là mấy (`-4 % 2 == 0`, điều kiện vẫn đúng).
- Ta có thể kiểm tra chẵn lẻ ngay lúc đọc `cin >> a[i]` mà không cần duyệt vòng lặp thứ hai được không

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Khởi tạo `count_even = 0`.
- Duyệt $N$ phần tử, kiểm tra `a[i] % 2 == 0`.
- In kết quả. Độ phức tạp thời gian $\mathcal{O}(N)$, bộ nhớ $\mathcal{O}(N)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Phần tử $a_i$ | `4` | `7` | `2` | `9` | `8` | `5` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `a[i] % 2 == 0` | Đúng | Sai | Đúng | Sai | Đúng | Sai |
| `count_even` | 1 | 1 | 2 | 2 | 3 | 3 |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(N)$.
- Không gian: $\mathcal{O}(N)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Kiểm tra số lẻ bằng `a[i] % 2 == 1` gây lỗi nếu có số âm lẻ (vì `-3 % 2 == -1`).
- Quên khởi tạo `count_even = 0`.

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
int count_even = 0;

for (int i = 0; i < n; i++) {
cin >> a[i];
if (a[i] % 2 == 0) {
count_even++;
}
}

cout << count_even << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính tổng các phần tử chẵn trong mảng.
- Tách mảng ban đầu thành hai vector: một vector chứa các số chẵn, một vector chứa các số lẻ.
