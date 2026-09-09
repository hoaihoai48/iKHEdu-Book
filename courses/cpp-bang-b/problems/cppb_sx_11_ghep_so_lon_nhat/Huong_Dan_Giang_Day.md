# Hướng Dẫn Giảng Dạy: Ghép Chuỗi Tạo Số Lớn Nhất
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách $N$ số nguyên không âm. Ghép toàn bộ các số này lại thành một số nguyên lớn nhất có thể.
- **Tại sao so sánh thông thường bị sai**
- Nếu so sánh theo thứ tự từ điển thông thường (`"9" > "34"` đúng, nhưng `"3" > "30"` thì `"30"` lại dài hơn `"3"`). Nếu xếp `"30"` trước `"3"` ta được `"303"`, trong khi `"3"` trước `"30"` cho `"330"` lớn hơn!
- **Tính chất bắc cầu của phép ghép (Greedy Comparator):**
- Để quyết định giữa hai chuỗi $u$ và $v$ chuỗi nào nên đứng trước, ta so sánh trực tiếp kết quả của hai cách ghép:
$$\text{Nếu } u + v > v + u \implies u \text{ phải đứng trước } v.$$

- Quan hệ này thỏa mãn tính chất phản đối xứng và bắc cầu (Strict Weak Ordering), cho phép hàm `sort` định hình đúng toàn bộ dãy ghép.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử: Danh sách gồm 4 chuỗi `["3", "30", "34", "5", "9"]`.

| Cặp so sánh $(u, v)$ | Ghép $u + v$ | Ghép $v + u$ | Quyết định |
|---|---|---|---|
| `"9"` và `"5"` | `"95"` | `"59"` | `"9"` đứng trước `"5"` |
| `"34"` và `"3"` | `"343"` | `"334"` | `"34"` đứng trước `"3"` |
| `"3"` và `"30"` | `"330"` | `"303"` | `"3"` đứng trước `"30"` |

Sau khi sắp xếp: `["9", "5", "34", "3", "30"]`.
Ghép lại được số lớn nhất: `9534330`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Toàn số 0:** Nếu input gồm các số `[0, 0, 0]`, kết quả ghép sẽ là `"000"`. Đáp số hợp lệ của bài toán khi đó chỉ là một số `"0"`. Cần kiểm tra nếu phần tử đầu tiên sau khi sắp xếp là `"0"` thì in ngay `"0"` và kết thúc.
- **Bẫy 2 — Dùng dấu `>=` trong comparator:** Viết `return u + v >= v + u;` sẽ gây lỗi vi phạm Strict Weak Ordering dẫn đến crash chương trình khi gặp hai số giống hệt nhau.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

bool cmp(const string &u, const string &v) {
return u + v > v + u;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;

vector<string> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

sort(a.begin(), a.end(), cmp);

if (a[0] == "0") {
cout << "0\n";
return 0;
}

for (int i = 0; i < n; ++i) {
cout << a[i];
}
cout << "\n";
return 0;
}
```