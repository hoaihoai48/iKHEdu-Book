# Hướng Dẫn Giảng Dạy: Độ Dài Đoạn Ngoặc Đúng Liên Tiếp Dài Nhất

Chuyên đề: **Cấu Trúc Dữ Liệu Ngăn Xếp (Stack) & Monotonic Stack**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho chuỗi $S$ chỉ gồm các ký tự `(` và `)`. Hãy lập trình tìm độ dài lớn nhất của một đoạn con liên tiếp là dãy ngoặc đúng.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý hoạt động:** Vào sau Ra trước (LIFO). Thích hợp giải quyết các bài toán cặp ngoặc lồng nhau, khử đệ quy và tính toán biểu thức hậu tố.
- **Kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack):**
* Duy trì các phần tử trong stack luôn tăng dần hoặc giảm dần nghiêm ngặt.
* Trước khi đưa phần tử mới $A_i$ vào, liên tục đẩy các phần tử vi phạm tính đơn điệu ra khỏi stack (`pop()`).
* Mỗi phần tử chỉ được đưa vào và lấy ra khỏi stack đúng 1 lần, giúp tổng độ phức tạp đạt $\mathcal{O}(N)$ tối ưu tuyệt đối.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `)()())` $\implies$ Đầu ra kỳ vọng: `4`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `)()())` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với chuỗi $S = \text{")()())"}$: Đoạn con liên tiếp bắt đầu từ vị trí 1 đến vị trí 4 là "()()" tạo thành dãy ngoặc đúng hoàn chỉnh có đ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `4` |

*Giải thích chi tiết:* Với chuỗi $S = \text{")()())"}$:
Đoạn con liên tiếp bắt đầu từ vị trí 1 đến vị trí 4 là "()()" tạo thành dãy ngoặc đúng hoàn chỉnh có độ dài bằng 4. Đây là đoạn ngoặc đúng dài nhất.

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

string s;
if (!(cin >> s)) return 0;

stack<int> st;
st.push(-1);
int max_len = 0;

for (int i = 0; i < (int)s.size(); ++i) {
if (s[i] == '(') {
st.push(i);
} else {
st.pop();
if (st.empty()) {
st.push(i);
} else {
max_len = max(max_len, i - st.top());
}
}
}

cout << max_len << "\n";
return 0;
}
```
