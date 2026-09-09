# Hướng Dẫn Giảng Dạy: Next Greater Element Trên Mảng Vòng Tròn

Chuyên đề: **Cấu Trúc Dữ Liệu Ngăn Xếp (Stack) & Monotonic Stack**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng tròn $A$ gồm $N$ phần tử. Với mỗi phần tử, hãy tìm phần tử lớn hơn đầu tiên tiếp theo trên mảng vòng tròn. Nếu không có, in ra `-1`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý hoạt động:** Vào sau Ra trước (LIFO). Thích hợp giải quyết các bài toán cặp ngoặc lồng nhau, khử đệ quy và tính toán biểu thức hậu tố.
- **Kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack):**
* Duy trì các phần tử trong stack luôn tăng dần hoặc giảm dần nghiêm ngặt.
* Trước khi đưa phần tử mới $A_i$ vào, liên tục đẩy các phần tử vi phạm tính đơn điệu ra khỏi stack (`pop()`).
* Mỗi phần tử chỉ được đưa vào và lấy ra khỏi stack đúng 1 lần, giúp tổng độ phức tạp đạt $\mathcal{O}(N)$ tối ưu tuyệt đối.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `3 1 2 1` $\implies$ Đầu ra kỳ vọng: `2 -1 2`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 1 2 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng tròn gồm 3 phần tử $[1, 2, 1]$: - Phần tử 1 (đầu): Nhìn tiếp theo gặp số 2 lớn hơn 1 $\to$ in ra 2. - Phần tử 2 (giữa): Nhìn t... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `2 -1 2` |

*Giải thích chi tiết:* Với mảng tròn gồm 3 phần tử $[1, 2, 1]$:

- Phần tử 1 (đầu): Nhìn tiếp theo gặp số 2 lớn hơn 1 $\to$ in ra 2.
- Phần tử 2 (giữa): Nhìn tiếp theo gặp 1, rồi vòng lại đầu gặp 1, không có số nào lớn hơn 2 $\to$ in ra -1.
- Phần tử 1 (cuối): Vòng lại đầu mảng gặp 1, tiếp tục gặp 2 lớn hơn 1 $\to$ in ra 2.
Kết quả in ra: 2 -1 2.

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

vector<long long> nge(n, -1);
stack<int> st;

// Duyệt vòng tròn 2 vòng (2N)
for (int i = 0; i < 2 * n; ++i) {
while (!st.empty() && a[i % n] > a[st.top()]) {
nge[st.top()] = a[i % n];
st.pop();
}
if (i < n) st.push(i);
}

for (int i = 0; i < n; ++i) {
cout << nge[i] << (i + 1 == n "" : " ");
}
cout << "\n";
return 0;
}
```
