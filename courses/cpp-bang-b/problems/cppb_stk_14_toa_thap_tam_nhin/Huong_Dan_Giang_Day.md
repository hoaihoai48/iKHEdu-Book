# Hướng Dẫn Giảng Dạy: Tầm Nhìn Tòa Tháp (Stock Span)

Chuyên đề: **Cấu Trúc Dữ Liệu Ngăn Xếp (Stack) & Monotonic Stack**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách chiều cao của $N$ tòa tháp. Hãy lập trình tính tầm nhìn cho từng tòa tháp trong dãy.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý hoạt động:** Vào sau Ra trước (LIFO). Thích hợp giải quyết các bài toán cặp ngoặc lồng nhau, khử đệ quy và tính toán biểu thức hậu tố.
- **Kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack):**
  * Duy trì các phần tử trong stack luôn tăng dần hoặc giảm dần nghiêm ngặt.
  * Trước khi đưa phần tử mới $A_i$ vào, liên tục đẩy các phần tử vi phạm tính đơn điệu ra khỏi stack (`pop()`).
  * Mỗi phần tử chỉ được đưa vào và lấy ra khỏi stack đúng 1 lần, giúp tổng độ phức tạp đạt $\mathcal{O}(N)$ tối ưu tuyệt đối.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `7 100 80 60 70 60 75 85` $\implies$ Đầu ra kỳ vọng: `1 1 1 2 1 4 6`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `7 100 80 60 70 60 75 85` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với chiều cao các tháp $[100, 80, 60, 70, 60, 75, 85]$: - Tháp 1 (100): tầm nhìn 1 (chính nó). - Tháp 2 (80): tầm nhìn 1. - Tháp 3 (60)... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `1 1 1 2 1 4 6` |

*Giải thích chi tiết:* Với chiều cao các tháp $[100, 80, 60, 70, 60, 75, 85]$:

- Tháp 1 (100): tầm nhìn 1 (chính nó).
- Tháp 2 (80): tầm nhìn 1.
- Tháp 3 (60): tầm nhìn 1.
- Tháp 4 (70): bao trùm tháp 60 và chính nó $\to$ tầm nhìn 2.
- Tháp 5 (60): tầm nhìn 1.
- Tháp 6 (75): bao trùm tháp 60, 70, 60 và chính nó $\to$ tầm nhìn 4.
- Tháp 7 (85): bao trùm tất cả các tháp trừ tháp 100 $\to$ tầm nhìn 6.
Kết quả in ra: 1 1 1 2 1 4 6.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Lỗi `Runtime Error (SIGSEGV)` khi gọi `stk.top()` hoặc `stk.pop()` trên ngăn xếp rỗng. Bắt buộc kiểm tra `!stk.empty()` trước mọi thao tác truy cập đỉnh.
* Quên xử lý các phần tử còn sót lại trong stack sau khi duyệt hết mảng dữ liệu (đặc biệt trong bài toán tìm hình chữ nhật lớn nhất trong biểu đồ cột).
* Khi kiểm tra dãy ngoặc đúng, nếu gặp ngoặc đóng mà stack rỗng thì dãy ngoặc không hợp lệ ngay lập tức.

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
    if (n <= 0) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    vector<int> span(n);
    stack<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && h[st.top()] <= h[i]) {
            st.pop();
        }
        span[i] = st.empty() ? (i + 1) : (i - st.top());
        st.push(i);
    }

    for (int i = 0; i < n; ++i) {
        cout << span[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
