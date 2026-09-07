# Hướng Dẫn Giảng Dạy: Ghép Cặp Trẻ Em Và Bánh Quy
Chuyên đề: **Bài 02: Kỹ thuật hai con trỏ**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mức độ thèm ăn của N đứa trẻ và kích thước của M chiếc bánh quy. Hãy tính số lượng đứa trẻ tối đa có thể được thỏa mãn.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 2 1 2 3 1 1)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 2 1 2 3 1 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Có 3 đứa trẻ với mức độ thèm ăn là [1, 2, 3] và 2 chiếc bánh quy kích thước [1, 1]. Chiếc bánh đầu tiên kích thước 1 phá... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Có 3 đứa trẻ với mức độ thèm ăn là [1, 2, 3] và 2 chiếc bánh quy kích thước [1, 1]. Chiếc bánh đầu tiên kích thước 1 phát cho đứa trẻ có mức thèm ăn 1 (thỏa mãn 1 trẻ). Chiếc bánh thứ hai cũng có kích thước 1, nhưng hai đứa trẻ còn lại yêu cầu bánh kích thước tối thiểu là 2 và 3, nên chiếc bánh này không thể làm hài lòng thêm đứa trẻ nào. Do đó số đứa trẻ tối đa được thỏa mãn là 1.

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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> g(n), s(m);
    for (int i = 0; i < n; ++i) cin >> g[i];
    for (int i = 0; i < m; ++i) cin >> s[i];

    sort(g.begin(), g.end());
    sort(s.begin(), s.end());

    int i = 0, j = 0;
    int satisfied = 0;

    while (i < n && j < m) {
        if (s[j] >= g[i]) {
            ++satisfied;
            ++i;
            ++j;
        } else {
            ++j;
        }
    }

    cout << satisfied << "\n";
    return 0;
}
```
