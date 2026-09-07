# Hướng Dẫn Giảng Dạy: Tổng Giá Trị Nhỏ Nhất Của Mọi Đoạn Con

Chuyên đề: **Cấu Trúc Dữ Liệu Ngăn Xếp (Stack) & Monotonic Stack**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình tính tổng giá trị nhỏ nhất của tất cả các đoạn con, lấy dư cho $10^9 + 7$.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý hoạt động:** Vào sau Ra trước (LIFO). Thích hợp giải quyết các bài toán cặp ngoặc lồng nhau, khử đệ quy và tính toán biểu thức hậu tố.
- **Kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack):**
  * Duy trì các phần tử trong stack luôn tăng dần hoặc giảm dần nghiêm ngặt.
  * Trước khi đưa phần tử mới $A_i$ vào, liên tục đẩy các phần tử vi phạm tính đơn điệu ra khỏi stack (`pop()`).
  * Mỗi phần tử chỉ được đưa vào và lấy ra khỏi stack đúng 1 lần, giúp tổng độ phức tạp đạt $\mathcal{O}(N)$ tối ưu tuyệt đối.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `4 3 1 2 4` $\implies$ Đầu ra kỳ vọng: `17`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 3 1 2 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng gồm 4 phần tử $[3, 1, 2, 4]$: Các đoạn con có giá trị nhỏ nhất tương ứng: - Độ dài 1: [3] -> 3, [1] -> 1, [2] -> 2, [4] -> 4 (... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `17` |

*Giải thích chi tiết:* Với mảng gồm 4 phần tử $[3, 1, 2, 4]$:
Các đoạn con có giá trị nhỏ nhất tương ứng:
- Độ dài 1: [3] -> 3, [1] -> 1, [2] -> 2, [4] -> 4 (tổng = 10).
- Độ dài 2: [3,1] -> 1, [1,2] -> 1, [2,4] -> 2 (tổng = 4).
- Độ dài 3: [3,1,2] -> 1, [1,2,4] -> 1 (tổng = 2).
- Độ dài 4: [3,1,2,4] -> 1 (tổng = 1).
Tổng cộng toàn bộ là $10 + 4 + 2 + 1 = 17$.

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

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> left_bound(n), right_bound(n);
    stack<int> st;

    // Tìm biên trái nghiêm ngặt nhỏ hơn
    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.top()] > a[i]) st.pop();
        left_bound[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }

    while (!st.empty()) st.pop();

    // Tìm biên phải nhỏ hơn hoặc bằng
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.top()] >= a[i]) st.pop();
        right_bound[i] = st.empty() ? n : st.top();
        st.push(i);
    }

    long long total_sum = 0;
    for (int i = 0; i < n; ++i) {
        long long count = (1LL * (i - left_bound[i]) * (right_bound[i] - i)) % MOD;
        total_sum = (total_sum + a[i] * count) % MOD;
    }

    cout << total_sum << "\n";
    return 0;
}
```
