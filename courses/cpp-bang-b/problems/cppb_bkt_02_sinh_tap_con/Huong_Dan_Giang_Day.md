# Hướng Dẫn Giảng Dạy: Sinh Tất Cả Tập Con Của Tập N Phần Tử
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho tập hợp gồm $N$ phần tử $\{1, 2, \dots, N\}$. Hãy sử dụng thuật toán Quay lui mô hình nhị phân (ở mỗi bước quyết định chọn hoặc không chọn phần tử hiện tại) để sinh và in ra tất cả các tập con theo đúng thứ tự từ điển.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
  - Xây dựng không gian trạng thái dạng cây tìm kiếm.
  - Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với $N = 3$, tập $\{1, 2, 3\}$ có tổng cộng $2^3 = 8$ tập con. Theo thứ tự duyệt quay lui với bit 0 (không chọn) đứng tr... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3 2 2 3 1 1 3 1 2 1 2 3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với $N = 3$, tập $\{1, 2, 3\}$ có tổng cộng $2^3 = 8$ tập con. Theo thứ tự duyệt quay lui với bit 0 (không chọn) đứng trước bit 1 (chọn), tập rỗng được sinh đầu tiên và tập đầy đủ $\{1, 2, 3\}$ sinh cuối cùng.

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

int n;
vector<int> cur;

void backtrack(int step) {
    if (step > n) {
        for (int i = 0; i < (int)cur.size(); ++i) cout << cur[i] << (i + 1 == (int)cur.size() ? "" : " ");
        cout << "\n";
        return;
    }
    // Không chọn step
    backtrack(step + 1);
    // Chọn step
    cur.push_back(step);
    backtrack(step + 1);
    cur.pop_back();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    backtrack(1);
    return 0;
}
```
