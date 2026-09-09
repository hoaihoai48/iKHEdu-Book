# Hướng Dẫn Giảng Dạy: Mô Phỏng Hai Con Trỏ Đối Đầu
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên đã được sắp xếp tăng dần và một số nguyên S. Hãy kiểm tra xem trong mảng có tồn tại cặp chỉ số (i, j) với i < j sao cho A[i] + A[j] = S hay không. Nếu có in ra YES, ngược lại in ra NO.

- **Chiến lược tiếp cận & tối ưu:**
- Sắp xếp mảng để tạo tính đơn điệu.
- Đặt 2 con trỏ $L$ ở đầu và $R$ ở cuối mảng (đối đầu), hoặc cùng chạy từ đầu mảng.
- Tại mỗi bước, dựa vào mối quan hệ giữa tổng/hiệu hiện tại và mục tiêu để quyết định tăng $L$ hay giảm $R$ một cách đơn điệu.

**Bất biến:** > Nếu $A[L] + A[R] > S$, vì mảng tăng dần nên $\forall k \ge L, A[k] + A[R] > S \implies$ phần tử $A[R]$ không thể ghép với bất kỳ số nào từ $L \dots R-1$, việc giảm $R$ là an toàn tuyệt đối và không bỏ sót nghiệm.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Thao tác thực hiện | Dữ liệu biến đổi | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu vào | Input: `5 20 2 5 8 12 19` | Nạp dữ liệu vào các biến/mảng |
| 2 | Thực thi thuật toán theo từng bước | Phân tích biến: Xét mảng đã sắp xếp: [2, 5, 8, 12, 19] và S = 20. Khởi tạo hai con trỏ L trỏ vào 2 (chỉ số 1) và R trỏ vào 19 (chỉ số 5). Tổng 2 + 19 = 21 > 20 -> giảm R xuống trỏ vào 12. Tiếp tục tính tổng 2 + 12 = 14 < 20 -> tăng L trỏ vào 5. Tổng 5 + 12 = 17 < 20 -> tăng L trỏ vào 8. Khi L trỏ vào 8 và R trỏ vào 12, tổng 8 + 12 = 20 đúng bằng S. Do đó in ra YES. | Cập nhật trạng thái tối ưu |
| 3 | Xuất kết quả chuẩn ra màn hình | Kết quả cuối cùng: `YES` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Xét mảng đã sắp xếp: [2, 5, 8, 12, 19] và S = 20. Khởi tạo hai con trỏ L trỏ vào 2 (chỉ số 1) và R trỏ vào 19 (chỉ số 5). Tổng 2 + 19 = 21 > 20 -> giảm R xuống trỏ vào 12. Tiếp tục tính tổng 2 + 12 = 14 < 20 -> tăng L trỏ vào 5. Tổng 5 + 12 = 17 < 20 -> tăng L trỏ vào 8. Khi L trỏ vào 8 và R trỏ vào 12, tổng 8 + 12 = 20 đúng bằng S. Do đó in ra YES.

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

int l = 0, r = n - 1;
bool found = false;

while (l < r) {
long long sum = a[l] + a[r];
if (sum == s) {
found = true;
break;
} else if (sum < s) {
++l;
} else {
--r;
}
}

if (found) cout << "YES\n";
else cout << "NO\n";
return 0;
}
```
