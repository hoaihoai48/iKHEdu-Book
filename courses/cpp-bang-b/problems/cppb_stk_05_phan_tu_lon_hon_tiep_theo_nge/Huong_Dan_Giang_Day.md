# Hướng Dẫn Giảng Dạy: Phần Tử Lớn Hơn Tiếp Theo (Next Greater Element)

Chuyên đề: **Cấu Trúc Dữ Liệu Ngăn Xếp (Stack) & Monotonic Stack**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho dãy số nguyên $A$ gồm $N$ phần tử. Với mỗi phần tử trong mảng, hãy tìm phần tử đầu tiên nằm bên phải nó có giá trị lớn hơn nó. Nếu không có, gán giá trị `-1`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý hoạt động:** Vào sau Ra trước (LIFO). Thích hợp giải quyết các bài toán cặp ngoặc lồng nhau, khử đệ quy và tính toán biểu thức hậu tố.
- **Kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack):**
  * Duy trì các phần tử trong stack luôn tăng dần hoặc giảm dần nghiêm ngặt.
  * Trước khi đưa phần tử mới $A_i$ vào, liên tục đẩy các phần tử vi phạm tính đơn điệu ra khỏi stack (`pop()`).
  * Mỗi phần tử chỉ được đưa vào và lấy ra khỏi stack đúng 1 lần, giúp tổng độ phức tạp đạt $\mathcal{O}(N)$ tối ưu tuyệt đối.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `4 4 5 2 25` $\implies$ Đầu ra kỳ vọng: `5 25 25 -1`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 4 5 2 25` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng gồm 4 phần tử $[4, 5, 2, 25]$: - Phần tử 4: Bên phải phần tử đầu tiên lớn hơn 4 là 5. - Phần tử 5: Bên phải phần tử đầu tiên l... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `5 25 25 -1` |

*Giải thích chi tiết:* Với mảng gồm 4 phần tử $[4, 5, 2, 25]$:
- Phần tử 4: Bên phải phần tử đầu tiên lớn hơn 4 là 5.
- Phần tử 5: Bên phải phần tử đầu tiên lớn hơn 5 là 25.
- Phần tử 2: Bên phải phần tử đầu tiên lớn hơn 2 là 25.
- Phần tử 25: Bên phải không còn số nào lớn hơn 25 $\to$ in ra -1.
Kết quả in ra: 5 25 25 -1.

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

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[i] > a[st.top()]) {
            nge[st.top()] = a[i];
            st.pop();
        }
        st.push(i);
    }

    for (int i = 0; i < n; ++i) {
        cout << nge[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
