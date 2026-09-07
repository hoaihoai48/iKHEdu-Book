# Hướng Dẫn Giảng Dạy: Hứng Nước Mưa (Trapping Rain Water)

Chuyên đề: **Cấu Trúc Dữ Liệu Ngăn Xếp (Stack) & Monotonic Stack**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách chiều cao của $N$ khối bê tông. Hãy lập trình tính tổng đơn vị thể tích nước mưa có thể đọng lại.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý hoạt động:** Vào sau Ra trước (LIFO). Thích hợp giải quyết các bài toán cặp ngoặc lồng nhau, khử đệ quy và tính toán biểu thức hậu tố.
- **Kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack):**
  * Duy trì các phần tử trong stack luôn tăng dần hoặc giảm dần nghiêm ngặt.
  * Trước khi đưa phần tử mới $A_i$ vào, liên tục đẩy các phần tử vi phạm tính đơn điệu ra khỏi stack (`pop()`).
  * Mỗi phần tử chỉ được đưa vào và lấy ra khỏi stack đúng 1 lần, giúp tổng độ phức tạp đạt $\mathcal{O}(N)$ tối ưu tuyệt đối.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `12 0 1 0 2 1 0 1 3 2 1 2 1` $\implies$ Đầu ra kỳ vọng: `6`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `12 0 1 0 2 1 0 1 3 2 1 2 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với độ cao địa hình là $[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]$: Nước mưa sẽ bị giữ lại ở các vùng trũng giữa các cột cao: - Tại vị trí 2... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `6` |

*Giải thích chi tiết:* Với độ cao địa hình là $[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]$:
Nước mưa sẽ bị giữ lại ở các vùng trũng giữa các cột cao:
- Tại vị trí 2: nước đọng 1 đơn vị.
- Tại vị trí 4: nước đọng 1 đơn vị.
- Tại vị trí 5: nước đọng 2 đơn vị.
- Tại vị trí 6: nước đọng 1 đơn vị.
- Tại vị trí 9: nước đọng 1 đơn vị.
Tổng lượng nước đọng lại là $1 + 1 + 2 + 1 + 1 = 6$ đơn vị.

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

    stack<int> st;
    long long total_water = 0;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && h[i] > h[st.top()]) {
            int top = st.top();
            st.pop();
            if (st.empty()) break;

            int dist = i - st.top() - 1;
            long long bounded_height = min(h[i], h[st.top()]) - h[top];
            total_water += dist * bounded_height;
        }
        st.push(i);
    }

    cout << total_water << "\n";
    return 0;
}
```
