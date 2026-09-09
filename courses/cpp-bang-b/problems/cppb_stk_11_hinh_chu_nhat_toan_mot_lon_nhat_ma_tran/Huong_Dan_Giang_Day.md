# Hướng Dẫn Giảng Dạy: Hình Chữ Nhật Toàn 1 Lớn Nhất Trong Ma Trận

Chuyên đề: **Cấu Trúc Dữ Liệu Ngăn Xếp (Stack) & Monotonic Stack**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho ma trận nhị phân $N × M$. Hãy lập trình tìm diện tích lớn nhất của hình chữ nhật con chỉ chứa toàn số `1`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý hoạt động:** Vào sau Ra trước (LIFO). Thích hợp giải quyết các bài toán cặp ngoặc lồng nhau, khử đệ quy và tính toán biểu thức hậu tố.
- **Kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack):**
* Duy trì các phần tử trong stack luôn tăng dần hoặc giảm dần nghiêm ngặt.
* Trước khi đưa phần tử mới $A_i$ vào, liên tục đẩy các phần tử vi phạm tính đơn điệu ra khỏi stack (`pop()`).
* Mỗi phần tử chỉ được đưa vào và lấy ra khỏi stack đúng 1 lần, giúp tổng độ phức tạp đạt $\mathcal{O}(N)$ tối ưu tuyệt đối.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `4 5 10100 10111 11111 10010` $\implies$ Đầu ra kỳ vọng: `6`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 5 10100 10111 11111 10010` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với ma trận kích thước $4 × 5$: Hình chữ nhật con toàn số 1 lớn nhất có kích thước $2 × 3$ (chiều cao 2, chiều rộng 3) gồm 6 ô số 1. D... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `6` |

*Giải thích chi tiết:* Với ma trận kích thước $4 × 5$:
Hình chữ nhật con toàn số 1 lớn nhất có kích thước $2 × 3$ (chiều cao 2, chiều rộng 3) gồm 6 ô số 1. Diện tích lớn nhất đạt được là 6.

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

int n, m;
if (!(cin >> n >> m)) return 0;
if (n <= 0 || m <= 0) return 0;

vector<string> grid(n);
for (int i = 0; i < n; ++i) cin >> grid[i];

vector<int> h(m, 0);
int max_area = 0;

for (int i = 0; i < n; ++i) {
for (int j = 0; j < m; ++j) {
if (grid[i][j] == '1') h[j]++;
else h[j] = 0;
}

// Monotonic stack on row histogram
vector<int> cur_h = h;
cur_h.push_back(0);
stack<int> st;

for (int j = 0; j <= m; ++j) {
while (!st.empty() && cur_h[j] < cur_h[st.top()]) {
int height = cur_h[st.top()];
st.pop();
int width = st.empty() j : (j - st.top() - 1);
max_area = max(max_area, height * width);
}
st.push(j);
}
}

cout << max_area << "\n";
return 0;
}
```
