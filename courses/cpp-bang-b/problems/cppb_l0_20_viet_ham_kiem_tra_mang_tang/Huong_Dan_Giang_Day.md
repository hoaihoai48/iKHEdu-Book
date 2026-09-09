# Hướng Dẫn Giảng Dạy: Viết Hàm Kiểm Tra Mảng Tăng Dần
Chuyên đề: **Chương 01 — Bài 03: Mảng 1 Chiều, Vector, Xâu Ký Tự & Tổ Chức Hàm**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Học cách tổ chức mã nguồn sạch bằng cách tách bài toán thành Hàm con (`function`).
- Hiểu và áp dụng kỹ thuật truyền tham chiếu hằng `const vector<int>& a` để tránh sao chép tốn bộ nhớ.
- Nắm vững tư duy phản chứng (Early Exit): chỉ cần tìm thấy 1 cặp $a[i] > a[i+1]$ vi phạm là lập tức `return false`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Mảng tăng dần (không giảm) khi và chỉ khi mọi cặp phần tử kề nhau đều thỏa mãn $a[i] \le a[i+1]$.
- Nếu tồn tại bất kỳ chỉ số $i$ nào mà $a[i] > a[i+1]$, mảng chắc chắn không tăng dần.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Để biết một mảng có tăng dần không, ta cần so sánh bao nhiêu cặp phần tử kề nhau ($N - 1$ cặp).
- Khi phát hiện một cặp vi phạm, có cần kiểm tra tiếp các phần tử phía sau không (Không, dừng và trả về `false` ngay).
- Tại sao nên viết `const vector<int>&` thay vì `vector<int>`

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Viết hàm `isSorted(const vector<int>& a)`.
- Duyệt từ $i = 0$ đến $n - 2$. Nếu $a[i] > a[i+1]$ thì `return false`. Nếu duyệt hết mà không vi phạm thì `return true`.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Cặp kề nhau $(a[i], a[i+1])$ | Kiểm tra $a[i] > a[i+1]$ | Hành động |
|:---:|:---:|:---:|
| `(2, 4)` | $2 > 4$ (Sai) | Tiếp tục duyệt |
| `(4, 4)` | $4 > 4$ (Sai, vì bằng nhau vẫn thỏa mãn không giảm) | Tiếp tục duyệt |
| `(4, 7)` | $4 > 7$ (Sai) | Tiếp tục duyệt |
| `(7, 9)` | $7 > 9$ (Sai) | Hết mảng $\implies$ `return true` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(N)$ trong trường hợp xấu nhất, trung bình dừng sớm hơn.
- Không gian: $\mathcal{O}(1)$ phụ trội nhờ truyền tham chiếu `&`.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Duyệt vòng lặp đến $i < n$ và kiểm tra $a[i] > a[i+1]$ dẫn đến lỗi truy cập `a[n]` ngoài phạm vi.
- Viết nhầm điều kiện bằng nhau `a[i] == a[i+1]` là vi phạm (đề bài cho phép các phần tử bằng nhau).

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isSorted(const vector<int>& a) {
int n = a.size();
for (int i = 0; i < n - 1; i++) {
if (a[i] > a[i + 1]) {
return false;
}
}
return true;
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

if (isSorted(a)) {
cout << "YES\n";
} else {
cout << "NO\n";
}

return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Kiểm tra mảng giảm dần hoặc kiểm tra mảng cấp số cộng.
