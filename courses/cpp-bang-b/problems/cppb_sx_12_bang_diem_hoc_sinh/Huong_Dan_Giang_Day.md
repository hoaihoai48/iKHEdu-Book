# Hướng Dẫn Giảng Dạy: Bảng Điểm Học Sinh Đa Trường
Chuyên đề: **Bài 01: Thuật toán sắp xếp**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách $N$ học sinh cùng điểm số của hai môn thi. Hãy sắp xếp danh sách học sinh theo các quy tắc ưu tiên sau:
1. Tổng điểm hai môn ($Math + Info$) giảm dần.
2. Nếu bằng tổng điểm, thí sinh có điểm môn Tin học ($Info$) cao hơn sẽ đứng trước.
3. Nếu vẫn bằng nhau cả về điểm Tin học, thí sinh có mã số định danh $ID$ nhỏ hơn sẽ đứng trước.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 101 8 9 102 9 8 103 10 )
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 101 8 9 102 9 8 103 10 10` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Thống kê điểm của 3 thí sinh: - Thí sinh $103$: Điểm Toán = $10$, Điểm Tin = $10 \implies$ Tổng điểm = $20$. - Thí sinh ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `103 10 10 101 8 9 102 9 8` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Thống kê điểm của 3 thí sinh:

- Thí sinh $103$: Điểm Toán = $10$, Điểm Tin = $10 \implies$ Tổng điểm = $20$.
- Thí sinh $101$: Điểm Toán = $8$, Điểm Tin = $9 \implies$ Tổng điểm = $17$.
- Thí sinh $102$: Điểm Toán = $9$, Điểm Tin = $8 \implies$ Tổng điểm = $17$.

Xếp hạng theo các tiêu chí:

- Thí sinh $103$ có tổng điểm cao nhất ($20$) nên đứng vị trí số 1.
- Giữa hai thí sinh $101$ và $102$ có cùng tổng điểm là $17$: xét tiêu chí phụ điểm Tin học, thí sinh $101$ có điểm Tin $9 > 8$ của thí sinh $102$, do đó thí sinh $101$ xếp trước thí sinh $102$.

Kết quả in ra đúng thứ tự: `103 10 10`, tiếp theo là `101 8 9`, và cuối cùng là `102 9 8`.

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
    long long total_a = a[1] + a[2];
    long long total_b = b[1] + b[2];
    if (total_a != total_b) return total_a > total_b;
    if (a[2] != b[2]) return a[2] > b[2];
    return a[0] < b[0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(3));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0] >> a[i][1] >> a[i][2];
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << " " << a[i][2] << "\n";
    }
    return 0;
}
```
