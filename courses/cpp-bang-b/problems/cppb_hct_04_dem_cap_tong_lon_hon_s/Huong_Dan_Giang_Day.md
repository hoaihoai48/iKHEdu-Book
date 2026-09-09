# Hướng Dẫn Giảng Dạy: Đếm Cặp Có Tổng Lớn Hơn Hoặc Bằng S
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên và một số nguyên S. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N thỏa mãn: A[i] + A[j] >= S.

- **Chiến lược tiếp cận & tối ưu:**
- Sắp xếp mảng để tạo tính đơn điệu.
- Đặt 2 con trỏ $L$ ở đầu và $R$ ở cuối mảng (đối đầu), hoặc cùng chạy từ đầu mảng.
- Tại mỗi bước, dựa vào mối quan hệ giữa tổng/hiệu hiện tại và mục tiêu để quyết định tăng $L$ hay giảm $R$ một cách đơn điệu.

**Bất biến:** > Nếu $A[L] + A[R] > S$, vì mảng tăng dần nên $\forall k \ge L, A[k] + A[R] > S \implies$ phần tử $A[R]$ không thể ghép với bất kỳ số nào từ $L \dots R-1$, việc giảm $R$ là an toàn tuyệt đối và không bỏ sót nghiệm.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Thao tác thực hiện | Dữ liệu biến đổi | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu vào | Input: `5 8 2 5 1 4 3` | Nạp dữ liệu vào các biến/mảng |
| 2 | Thực thi thuật toán theo từng bước | Phân tích biến: Sắp xếp dãy điểm chiến lực tăng dần: [1, 2, 3, 4, 5]. Các cặp có tổng >= 8 là: cặp (3, 5) có tổng 3 + 5 = 8 >= 8 và cặp (4, 5) có tổng 4 + 5 = 9 >= 8. Tổng cộng có đúng 2 cặp thỏa mãn. | Cập nhật trạng thái tối ưu |
| 3 | Xuất kết quả chuẩn ra màn hình | Kết quả cuối cùng: `2` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Sắp xếp dãy điểm chiến lực tăng dần: [1, 2, 3, 4, 5]. Các cặp có tổng >= 8 là: cặp (3, 5) có tổng 3 + 5 = 8 >= 8 và cặp (4, 5) có tổng 4 + 5 = 9 >= 8. Tổng cộng có đúng 2 cặp thỏa mãn.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
1. Quên sắp xếp mảng trước khi chạy Hai con trỏ đối đầu khiến điều kiện di chuyển $L/R$ bị sai logic.
2. Lỗi tràn số $A[L] + A[R] \ge 2 \cdot 10^9$ khi tính tổng hai số lớn.
3. Vòng lặp dừng không đúng (ví dụ $L \le R$ thay vì $L < R$ khi chọn 2 phần tử phân biệt).

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
long long s;
if (!(cin >> n >> s)) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

sort(a.begin(), a.end());

int l = 0, r = n - 1;
long long count = 0;

while (l < r) {
if (a[l] + a[r] >= s) {
count += (r - l);
--r;
} else {
++l;
}
}

cout << count << "\n";
return 0;
}
```
