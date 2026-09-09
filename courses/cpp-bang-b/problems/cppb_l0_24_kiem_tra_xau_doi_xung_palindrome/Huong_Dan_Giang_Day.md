# Hướng Dẫn Giảng Dạy: Kiểm Tra Xâu Đối Xứng Palindrome
Chuyên đề: **Chương 01 — Bài 03: Mảng 1 Chiều, Vector, Xâu Ký Tự & Tổ Chức Hàm**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Áp dụng kỹ thuật hai con trỏ đối xứng trên cấu trúc `string`.
- Rèn luyện kỹ năng viết hàm trả về kiểu `bool` với kỹ thuật Early Exit (dừng ngay khi tìm thấy điểm sai lệch).
- Hiểu bản chất đối xứng: $s[i] == s[n - 1 - i]$ với mọi $0 \le i < n/2$.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Một xâu có độ dài $N$ là palindrome khi và chỉ khi:
$$s[i] = s[N - 1 - i] \quad \forall 0 \le i < \lfloor N / 2 \rfloor$$

- Bằng cách dùng hai con trỏ $l = 0$ và $r = N - 1$, ta so sánh từng cặp ký tự đối xứng. Nếu có bất kỳ cặp nào khác nhau thì kết luận `NO` ngay.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Một từ có 1 chữ cái (như `"a"`) có phải là xâu đối xứng không (Có, vì $l = r$ không vi phạm).
- Khi nào thì hai con trỏ sẽ dừng lại (Khi $l \ge r$).

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Sử dụng hai con trỏ quét từ ngoài vào trong: độ phức tạp thời gian $\mathcal{O}(|S| / 2) = \mathcal{O}(|S|)$, bộ nhớ phụ trợ $\mathcal{O}(1)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (`racecar`)

| Bước | Con trỏ $l$ | Con trỏ $r$ | So sánh $s[l]$ và $s[r]$ | Kết quả so sánh |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 (`'r'`) | 6 (`'r'`) | `'r' == 'r'` | Khớp |
| 2 | 1 (`'a'`) | 5 (`'a'`) | `'a' == 'a'` | Khớp |
| 3 | 2 (`'c'`) | 4 (`'c'`) | `'c' == 'c'` | Khớp |
| 4 | 3 (`'e'`) | 3 (`'e'`) | $l = r$ (Dừng) | Khớp toàn bộ $\implies$ `YES` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(|S|)$.
- Không gian: $\mathcal{O}(1)$ bộ nhớ phụ trợ nhờ truyền `const string&`.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Đảo ngược xâu bằng phép cộng chuỗi `t = s[i] + t` trong vòng lặp gây độ phức tạp $\mathcal{O}(|S|^2)$ dẫn đến lỗi chạy quá thời gian (TLE) khi $|S| = 10^5$.
- Không dùng tham chiếu `&` mà truyền tham trị cả xâu lớn $10^5$ làm giảm hiệu năng.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isPalindrome(const string& s) {
int l = 0;
int r = (int)s.size() - 1;
while (l < r) {
if (s[l] != s[r]) {
return false;
}
l++;
r--;
}
return true;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

string s;
if (!(cin >> s)) return 0;

if (isPalindrome(s)) {
cout << "YES\n";
} else {
cout << "NO\n";
}

return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Kiểm tra palindrome có bỏ qua dấu cách và dấu câu (Palindrome câu văn).
- Bài toán tìm xâu con đối xứng dài nhất (LPS - sẽ học trong Chương Quy hoạch động).
