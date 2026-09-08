# Hướng Dẫn Giảng Dạy: Sắp Xếp Lưu Vị Trí Ban Đầu
Chuyên đề: **Bài 01: Thuật toán sắp xếp**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho một dãy gồm $N$ số nguyên $A_1, A_2, \dots, A_N$. Hãy sắp xếp các phần tử theo thứ tự giá trị tăng dần, đồng thời in ra giá trị và vị trí ban đầu (chỉ số 1-indexed) của mỗi phần tử trong mảng gốc. Nếu hai phần tử có cùng giá trị, phần tử xuất hiện trước trong mảng gốc sẽ đứng trước.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 40 10 20 10 30)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 40 10 20 10 30` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Dãy ban đầu cùng vị trí gốc (1-indexed) là: - Vị trí 1: $40$ - Vị trí 2: $10$ - Vị trí 3: $20$ - Vị trí 4: $10$ - Vị trí... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `10 2 10 4 20 3 30 5 40 1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Dãy ban đầu cùng vị trí gốc (1-indexed) là:

- Vị trí 1: $40$
- Vị trí 2: $10$
- Vị trí 3: $20$
- Vị trí 4: $10$
- Vị trí 5: $30$

Sau khi sắp xếp theo giá trị tăng dần:

- Giá trị $10$: có ở vị trí 2 và vị trí 4. Vì $2 < 4$ nên in `10 2` trước, sau đó in `10 4`.
- Giá trị $20$: ở vị trí 3 $\implies$ in `20 3`.
- Giá trị $30$: ở vị trí 5 $\implies$ in `30 5`.
- Giá trị $40$: ở vị trí 1 $\implies$ in `40 1`.

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
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(2));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0];
        a[i][1] = i + 1;
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << "\n";
    }
    return 0;
}
```
