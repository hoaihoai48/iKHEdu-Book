# Hướng Dẫn Giảng Dạy: Đoạn Con Chứa Tối Đa K Số 0 (Lật Bit)
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho một mảng nhị phân A gồm N phần tử (Ai thuộc {0, 1}) và số nguyên không âm K. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp chỉ toàn bit 1 sau khi lật tối đa K số 0 thành số 1.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 11 2 1 1 1 0 0 0 1 1 1 1 )
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `11 2 1 1 1 0 0 0 1 1 1 1 0` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Xét đoạn từ vị trí 5 đến vị trí 10: [0, 0, 1, 1, 1, 1]. Đoạn này có độ dài 6 và chứa đúng hai số 0. Khi lật 2 số 0 này t... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Xét đoạn từ vị trí 5 đến vị trí 10: [0, 0, 1, 1, 1, 1]. Đoạn này có độ dài 6 và chứa đúng hai số 0. Khi lật 2 số 0 này thành 1, ta thu được chuỗi 6 số 1 liên tiếp. Đây là độ dài dài nhất có thể tạo được.

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

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int l = 0;
    int zero_cnt = 0;
    int max_len = 0;

    for (int r = 0; r < n; ++r) {
        if (a[r] == 0) ++zero_cnt;

        while (zero_cnt > k) {
            if (a[l] == 0) --zero_cnt;
            ++l;
        }

        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}
```
