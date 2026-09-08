# Hướng Dẫn Giảng Dạy: Bảng Xếp Hạng Giải Đấu Thể Thao
Chuyên đề: **Bài 01: Thuật toán sắp xếp**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho thông số thi đấu của $N$ đội bóng. Hãy xếp hạng các đội theo thứ tự ưu tiên sau:
1. Điểm số tích lũy ($Points$) giảm dần.
2. Nếu bằng điểm số, đội có Hiệu số bàn thắng bại ($GoalDiff$) lớn hơn sẽ đứng trước.
3. Nếu vẫn bằng cả điểm số và hiệu số, đội ghi được Tổng số bàn thắng ($Goals$) nhiều hơn sẽ đứng trước.
4. Nếu cả 3 chỉ số trên đều hoàn toàn bằng nhau, đội có Mã số định danh ($ID$) nhỏ hơn sẽ đứng trước.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 1 10 5 12 2 10 5 15 3 1)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 1 10 5 12 2 10 5 15 3 12 2 8` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Xét thông số của 3 đội bóng: - Đội 3: có $12$ điểm (cao nhất) $\implies$ xếp vị trí số 1. - Đội 1 và Đội 2: đều có $10$ ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3 2 1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Xét thông số của 3 đội bóng:

- Đội 3: có $12$ điểm (cao nhất) $\implies$ xếp vị trí số 1.
- Đội 1 và Đội 2: đều có $10$ điểm và cùng có hiệu số bàn thắng bại là $5$.
  - Xét chỉ số phụ số bàn thắng ghi được: Đội 2 ghi được $15$ bàn, trong khi Đội 1 chỉ ghi được $12$ bàn ($15 > 12$).
  - Do đó Đội 2 xếp thứ nhì, Đội 1 xếp thứ ba.

Thứ tự mã đội trên bảng xếp hạng là: `3 2 1`.

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

bool cmp(const vector<long long> &a, const vector<long long> &b) {
    if (a[1] != b[1]) return a[1] > b[1];
    if (a[2] != b[2]) return a[2] > b[2];
    if (a[3] != b[3]) return a[3] > b[3];
    return a[0] < b[0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(4));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0] >> a[i][1] >> a[i][2] >> a[i][3];
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
