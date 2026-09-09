# Hướng Dẫn Giảng Dạy: Cân Bằng Tiền Tố Đa Chiều
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho một chuỗi gồm N ký tự chỉ gồm các chữ cái 'A', 'B', 'C'. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp có số lượng ký tự 'A', 'B' và 'C' bằng nhau.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
- Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
- Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `ABACBC` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Chuỗi 'ABACBC' có độ dài 6 chứa đúng hai ký tự 'A', hai ký tự 'B' và hai ký tự 'C' (số lượng bằng nhau = 2). Vì vậy độ d... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Chuỗi 'ABACBC' có độ dài 6 chứa đúng hai ký tự 'A', hai ký tự 'B' và hai ký tự 'C' (số lượng bằng nhau = 2). Vì vậy độ dài lớn nhất là 6.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Tràn số nguyên:** Khi tính toán tổng, tích hoặc lũy thừa lớn hơn $2 \cdot 10^9$, bắt buộc phải sử dụng kiểu dữ liệu `long long` (64-bit) để tránh tràn số âm.
- **Bẫy 2 — Chỉ số mảng & Giới hạn biên:** Chú ý giữa đánh chỉ số 0-based (`0 .. N-1`) và 1-based (`1 .. N`). Kiểm tra kỹ trường hợp $N = 1$ hoặc giá trị biên tối đa của đề bài.
- **Bẫy 3 — Tối ưu thời gian I/O:** Luôn sử dụng `ios::sync_with_stdio(false); cin.tie(nullptr);` ở đầu hàm `main()` để đọc ghi nhanh, tránh bị TLE khi số lượng testcase lớn.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
string s;
if (!(cin >> n >> s)) return 0;

int ca = 0, cb = 0, cc = 0;

// Lưu: {diff1, diff2, index}
vector<vector<int>> states;
states.reserve(n + 1);
states.push_back({0, 0, 0}); // Tại vị trí 0

for (int i = 1; i <= n; ++i) {
if (s[i - 1] == 'A') ca++;
else if (s[i - 1] == 'B') cb++;
else if (s[i - 1] == 'C') cc++;

states.push_back({ca - cb, cb - cc, i});
}

sort(states.begin(), states.end(), [](const vector<int>& u, const vector<int>& v) {
if (u[0] != v[0]) return u[0] < v[0];
if (u[1] != v[1]) return u[1] < v[1];
return u[2] < v[2];
});

int max_len = 0;
int i = 0;
while (i <= n) {
int j = i;
while (j <= n && states[j][0] == states[i][0] && states[j][1] == states[i][1]) {
j++;
}
max_len = max(max_len, states[j - 1][2] - states[i][2]);
i = j;
}

cout << max_len << "\n";
return 0;
}
```
