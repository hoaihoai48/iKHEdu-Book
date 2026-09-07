# Hướng Dẫn Giảng Dạy: Hình Chữ Nhật Lớn Nhất Trên Histogram

Chuyên đề: **Cấu Trúc Dữ Liệu Ngăn Xếp (Stack) & Monotonic Stack**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách chiều cao của $N$ cột. Hãy lập trình tìm diện tích lớn nhất của một hình chữ nhật nằm gọn bên trong biểu đồ cột.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý hoạt động:** Vào sau Ra trước (LIFO). Thích hợp giải quyết các bài toán cặp ngoặc lồng nhau, khử đệ quy và tính toán biểu thức hậu tố.
- **Kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack):**
  * Duy trì các phần tử trong stack luôn tăng dần hoặc giảm dần nghiêm ngặt.
  * Trước khi đưa phần tử mới $A_i$ vào, liên tục đẩy các phần tử vi phạm tính đơn điệu ra khỏi stack (`pop()`).
  * Mỗi phần tử chỉ được đưa vào và lấy ra khỏi stack đúng 1 lần, giúp tổng độ phức tạp đạt $\mathcal{O}(N)$ tối ưu tuyệt đối.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `6 2 1 5 6 2 3` $\implies$ Đầu ra kỳ vọng: `10`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `6 2 1 5 6 2 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với biểu đồ có chiều cao các cột là $[2, 1, 5, 6, 2, 3]$: Hình chữ nhật lớn nhất được tạo thành bởi hai cột có chiều cao 5 và 6. Chiều ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `10` |

*Giải thích chi tiết:* Với biểu đồ có chiều cao các cột là $[2, 1, 5, 6, 2, 3]$:
Hình chữ nhật lớn nhất được tạo thành bởi hai cột có chiều cao 5 và 6. Chiều cao của hình chữ nhật này là $\min(5, 6) = 5$, chiều rộng là 2 cột. Diện tích lớn nhất đạt được là $5 \times 2 = 10$.

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

    h.push_back(0); // Cột lính canh
    stack<int> st;
    long long max_area = 0;

    for (int i = 0; i <= n; ++i) {
        while (!st.empty() && h[i] < h[st.top()]) {
            long long height = h[st.top()];
            st.pop();
            long long width = st.empty() ? i : (i - st.top() - 1);
            max_area = max(max_area, height * width);
        }
        st.push(i);
    }

    cout << max_area << "\n";
    return 0;
}
```
