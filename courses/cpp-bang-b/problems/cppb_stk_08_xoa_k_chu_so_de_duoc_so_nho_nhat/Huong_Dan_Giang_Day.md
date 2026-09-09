# Hướng Dẫn Giảng Dạy: Xóa K Chữ Số Để Được Số Nhỏ Nhất

Chuyên đề: **Cấu Trúc Dữ Liệu Ngăn Xếp (Stack) & Monotonic Stack**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho chuỗi số $S$ và số nguyên $K$. Hãy lập trình tìm số nguyên nhỏ nhất thu được sau khi xóa đúng $K$ chữ số.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý hoạt động:** Vào sau Ra trước (LIFO). Thích hợp giải quyết các bài toán cặp ngoặc lồng nhau, khử đệ quy và tính toán biểu thức hậu tố.
- **Kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack):**
* Duy trì các phần tử trong stack luôn tăng dần hoặc giảm dần nghiêm ngặt.
* Trước khi đưa phần tử mới $A_i$ vào, liên tục đẩy các phần tử vi phạm tính đơn điệu ra khỏi stack (`pop()`).
* Mỗi phần tử chỉ được đưa vào và lấy ra khỏi stack đúng 1 lần, giúp tổng độ phức tạp đạt $\mathcal{O}(N)$ tối ưu tuyệt đối.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `1432219 3` $\implies$ Đầu ra kỳ vọng: `1219`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `1432219 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với số ban đầu là "1432219" và cần xóa đi $K = 3$ chữ số: Ta xóa các chữ số 4, 3, 2 tại các vị trí đầu để giữ lại số "1219". Đây là số ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `1219` |

*Giải thích chi tiết:* Với số ban đầu là "1432219" và cần xóa đi $K = 3$ chữ số:
Ta xóa các chữ số 4, 3, 2 tại các vị trí đầu để giữ lại số "1219". Đây là số nguyên nhỏ nhất có thể tạo thành.

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

string num;
int k;
if (!(cin >> num >> k)) return 0;

string st = "";
for (char c : num) {
while (!st.empty() && k > 0 && st.back() > c) {
st.pop_back();
k--;
}
st.push_back(c);
}

while (k > 0 && !st.empty()) {
st.pop_back();
k--;
}

// Xóa các số 0 ở đầu
int start = 0;
while (start < (int)st.size() && st[start] == '0') start++;

string ans = st.substr(start);
if (ans.empty()) cout << "0\n";
else cout << ans << "\n";
return 0;
}
```
