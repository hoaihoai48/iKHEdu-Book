# Hướng Dẫn Giảng Dạy: Sinh Xâu Nhị Phân Không Chứa Hai Số 1 Liền Kề
Chuyên đề: **Bài 10: Thuật toán đệ quy & cây gọi hàm**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N (1 <= N <= 20). Hãy sinh tất cả các xâu nhị phân độ dài N không chứa chuỗi '11' theo thứ tự từ điển.

- **Phương pháp tiếp cận — Thuật toán đệ quy & Cây gọi hàm:**
  - Xác định trường hợp cơ sở (Base Case) để chặn đệ quy vô hạn.
  - Thiết lập công thức truy hồi và theo dõi luồng thực thi trên cây gọi hàm.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các xâu nhị phân độ dài 3 không có '11' gồm: 000, 001, 010, 100, 101. Tổng cộng có 5 xâu.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `000 001 010 100 101` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các xâu nhị phân độ dài 3 không có '11' gồm: 000, 001, 010, 100, 101. Tổng cộng có 5 xâu.

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

vector<string> results;

void genRec(int n, string &cur, char last_char) {
    if ((int)cur.size() == n) {
        results.push_back(cur);
        return;
    }
    // Luôn có thể thêm '0'
    cur.push_back('0');
    genRec(n, cur, '0');
    cur.pop_back();

    // Chỉ thêm '1' nếu ký tự trước không phải '1'
    if (last_char != '1') {
        cur.push_back('1');
        genRec(n, cur, '1');
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    string cur = "";
    genRec(n, cur, '0');
    cout << results.size() << "\n";
    for (const string &s : results) cout << s << "\n";
    return 0;
}
```
