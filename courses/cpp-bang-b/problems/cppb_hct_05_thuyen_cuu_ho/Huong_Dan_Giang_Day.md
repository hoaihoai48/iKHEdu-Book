# Hướng Dẫn Giảng Dạy: Ghép Thuyền Cứu Hộ Tối Ưu
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho cân nặng của N người và tải trọng tối đa C của thuyền. Biết mỗi thuyền chở tối đa 2 người và tổng cân nặng không vượt quá C. Hãy tìm số lượng thuyền ít nhất để chở hết toàn bộ N người sang sông.

- **Chiến lược tiếp cận & tối ưu:**
- Sắp xếp mảng để tạo tính đơn điệu.
- Đặt 2 con trỏ $L$ ở đầu và $R$ ở cuối mảng (đối đầu), hoặc cùng chạy từ đầu mảng.
- Tại mỗi bước, dựa vào mối quan hệ giữa tổng/hiệu hiện tại và mục tiêu để quyết định tăng $L$ hay giảm $R$ một cách đơn điệu.

**Bất biến:** > Nếu $A[L] + A[R] > S$, vì mảng tăng dần nên $\forall k \ge L, A[k] + A[R] > S \implies$ phần tử $A[R]$ không thể ghép với bất kỳ số nào từ $L \dots R-1$, việc giảm $R$ là an toàn tuyệt đối và không bỏ sót nghiệm.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Thao tác thực hiện | Dữ liệu biến đổi | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu vào | Input: `4 50 30 20 40 50` | Nạp dữ liệu vào các biến/mảng |
| 2 | Thực thi thuật toán theo từng bước | Phân tích biến: Sắp xếp cân nặng 4 người tăng dần: [20, 30, 40, 50] với tải trọng C = 50. Người nặng 50 kg bắt buộc phải đi một mình 1 thuyền (tốn 1 thuyền). Người nặng 40 kg không thể ghép với ai (vì 40 + 20 = 60 > 50) nên cũng đi một mình 1 thuyền (tốn thêm 1 thuyền). Hai người còn lại có cân nặng 20 kg và 30 kg ghép chung 1 thuyền vì 20 + 30 = 50 <= 50 (tốn 1 thuyền). Tổng số thuyền ít nhất cần dùng là 1 + 1 + 1 = 3 thuyền. | Cập nhật trạng thái tối ưu |
| 3 | Xuất kết quả chuẩn ra màn hình | Kết quả cuối cùng: `3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Sắp xếp cân nặng 4 người tăng dần: [20, 30, 40, 50] với tải trọng C = 50. Người nặng 50 kg bắt buộc phải đi một mình 1 thuyền (tốn 1 thuyền). Người nặng 40 kg không thể ghép với ai (vì 40 + 20 = 60 > 50) nên cũng đi một mình 1 thuyền (tốn thêm 1 thuyền). Hai người còn lại có cân nặng 20 kg và 30 kg ghép chung 1 thuyền vì 20 + 30 = 50 <= 50 (tốn 1 thuyền). Tổng số thuyền ít nhất cần dùng là 1 + 1 + 1 = 3 thuyền.

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
long long c;
if (!(cin >> n >> c)) return 0;

vector<long long> w(n);
for (int i = 0; i < n; ++i) cin >> w[i];

sort(w.begin(), w.end());

int l = 0, r = n - 1;
int boats = 0;

while (l <= r) {
if (l == r) {
++boats;
break;
}
if (w[l] + w[r] <= c) {
++l;
--r;
} else {
--r;
}
++boats;
}

cout << boats << "\n";
return 0;
}
```
