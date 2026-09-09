# Hướng Dẫn Giảng Dạy: Phần Tử Nhỏ Hơn Gần Nhất Bên Trái (Previous Smaller Element)

Chuyên đề: **Cấu Trúc Dữ Liệu Ngăn Xếp (Stack) & Monotonic Stack**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ gồm $N$ số nguyên. Với mỗi phần tử $A_i$, hãy tìm phần tử đầu tiên nằm bên trái nó có giá trị nhỏ hơn nó. Nếu không có phần tử nào thỏa mãn, gán `-1`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý hoạt động:** Vào sau Ra trước (LIFO). Thích hợp giải quyết các bài toán cặp ngoặc lồng nhau, khử đệ quy và tính toán biểu thức hậu tố.
- **Kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack):**
* Duy trì các phần tử trong stack luôn tăng dần hoặc giảm dần nghiêm ngặt.
* Trước khi đưa phần tử mới $A_i$ vào, liên tục đẩy các phần tử vi phạm tính đơn điệu ra khỏi stack (`pop()`).
* Mỗi phần tử chỉ được đưa vào và lấy ra khỏi stack đúng 1 lần, giúp tổng độ phức tạp đạt $\mathcal{O}(N)$ tối ưu tuyệt đối.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `5 4 5 2 10 8` $\implies$ Đầu ra kỳ vọng: `-1 4 -1 2 2`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 4 5 2 10 8` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng $[4, 5, 2, 10, 8]$: - Số 4: Bên trái không có số nào $\to$ -1. - Số 5: Số đầu tiên bên trái nhỏ hơn 5 là 4. - Số 2: Bên trái k... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `-1 4 -1 2 2` |

*Giải thích chi tiết:* Với mảng $[4, 5, 2, 10, 8]$:

- Số 4: Bên trái không có số nào $\to$ -1.
- Số 5: Số đầu tiên bên trái nhỏ hơn 5 là 4.
- Số 2: Bên trái không có số nào nhỏ hơn 2 $\to$ -1.
- Số 10: Số đầu tiên bên trái nhỏ hơn 10 là 2.
- Số 8: Số đầu tiên bên trái nhỏ hơn 8 là 2.
Kết quả in ra: -1 4 -1 2 2.

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

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

vector<long long> pse(n, -1);
stack<long long> st;

for (int i = 0; i < n; ++i) {
while (!st.empty() && st.top() >= a[i]) {
st.pop();
}
if (!st.empty()) {
pse[i] = st.top();
}
st.push(a[i]);
}

for (int i = 0; i < n; ++i) {
cout << pse[i] << (i + 1 == n "" : " ");
}
cout << "\n";
return 0;
}
```
