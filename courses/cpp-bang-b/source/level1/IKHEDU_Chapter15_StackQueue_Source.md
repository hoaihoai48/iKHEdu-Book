# TÀI LIỆU GỐC — CHƯƠNG 15: CẤU TRÚC STACK VÀ QUEUE (STACK, QUEUE & MONOTONIC STACK)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững cấu trúc Ngăn xếp (Stack - LIFO) và Hàng đợi (Queue - FIFO); làm chủ kỹ thuật Ngăn xếp đơn điệu (Monotonic Stack) giải bài toán tìm phần tử lớn hơn đầu tiên và Hình chữ nhật lớn nhất trong Histogram trong $\mathcal{O}(N)$ |
| Kiến thức cần có | `std::stack`, `std::queue`, `std::deque`, mảng, vòng lặp |
| Phạm vi | Stack (LIFO), Kiểm tra dãy ngoặc đúng, Queue (FIFO), Deque hai đầu, Ngăn xếp đơn điệu (Monotonic Stack $\mathcal{O}(N)$), Hình chữ nhật lớn nhất trong biểu đồ Histogram |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Sử dụng `stack` để kiểm tra tính hợp lệ của biểu thức chứa nhiều loại dấu ngoặc — `LO-01`.
2. Sử dụng `queue` và `deque` quản lý luồng dữ liệu FIFO và hai đầu — `LO-02`.
3. Cài đặt Ngăn xếp đơn điệu (Monotonic Stack) tìm phần tử lớn hơn/nhỏ hơn đầu tiên bên phải trong $\mathcal{O}(N)$ — `LO-03`.
4. Giải bài toán kinh điển Hình chữ nhật lớn nhất trong Histogram trong $\mathcal{O}(N)$ — `LO-04`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để tìm phần tử lớn hơn gần nhất cho TẤT CẢ $N$ phần tử trong mảng chỉ trong $1$ lần duyệt duy nhất?**

---

### Bài 15.1 — Ngăn xếp (Stack): LIFO và Dãy ngoặc đúng

#### 1. Khái niệm & Cơ chế LIFO
- Ngăn xếp (Stack): Last In, First Out (LIFO). `push`, `pop`, `top`, `empty`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 15.1: Kiểm Tra Cú Pháp Trình Biên Dịch iKHEDU IDE**  
> **Bối cảnh:** Trình biên dịch mã nguồn C++ cần kiểm tra tính đóng mở hợp lệ của các cặp dấu ngoặc `()`, `[]`, `{}` trong tệp mã nguồn $S$.  
> **Input:** `{[()()]}` $\implies$ **Output:** `YES`.  
> **Input:** `{[(])}` $\implies$ **Output:** `NO`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isValid(const string &s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if (st.empty()) return false;
            char topChar = st.top();
            if ((c == ')' && topChar != '(') ||
                (c == ']' && topChar != '[') ||
                (c == '}' && topChar != '{')) {
                return false;
            }
            st.pop();
        }
    }
    return st.empty();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    cout << (isValid(s) ? "YES\n" : "NO\n");
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 15.1

##### Bài 15.1.1 — Xóa Các Cặp Ký Tự Kề Nhau Giống Nhau
- **Bối cảnh:** Cho xâu ký tự $S$. Liên tục xóa các cặp ký tự liền kề giống nhau cho đến khi không thể xóa được nữa. In xâu kết quả.
- **Input:** `abbaca` $\implies$ **Output:** `ca`

##### Bài 15.1.2 — Đếm Số Dấu Ngoặc Cần Thêm Để Tạo Dãy Đúng
- **Bối cảnh:** Cho xâu ngoặc. Tìm số lượng dấu ngoặc ít nhất cần chèn thêm để xâu thành hợp lệ.
- **Input:** `())` $\implies$ **Output:** `1`

---

### Bài 15.2 — Hàng đợi (Queue) và Hàng đợi hai đầu (Deque)

#### 1. Khái niệm & Cơ chế FIFO
- `queue` (FIFO) và `deque` hai đầu $\mathcal{O}(1)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 15.2: Mô Phỏng Vận Hành Hàng Đợi In Tài Liệu**  
> **Bối cảnh:** Máy in văn phòng nhận $Q$ lệnh in. Mỗi lệnh gồm ID tài liệu hoặc lệnh in tài liệu đến trước nhất (FIFO).  
> **Input:** `4` \ `1 101` \ `1 102` \ `2` (in) \ `2` (in) $\implies$ **Output:** `101` \ `102`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    queue<int> taskQueue;
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int id;
            cin >> id;
            taskQueue.push(id);
        } else {
            if (!taskQueue.empty()) {
                cout << taskQueue.front() << "\n";
                taskQueue.pop();
            } else {
                cout << "EMPTY\n";
            }
        }
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 15.2

##### Bài 15.2.1 — Trò Chơi Vòng Tròn Đếm Số Josephus
- **Bối cảnh:** $N$ người đứng thành vòng tròn, lần lượt đếm đến người thứ $K$ thì loại khỏi vòng bằng `queue`. Tìm người cuối cùng còn lại.
- **Input:** `5 2` $\implies$ **Output:** `3`

##### Bài 15.2.2 — Đảo Ngược Hàng Đợi Bằng Ngăn Xếp
- **Bối cảnh:** Sử dụng một cấu trúc Stack để đảo ngược thứ tự các phần tử trong Queue.
- **Input:** `3` \ `1 2 3` $\implies$ **Output:** `3 2 1`

---

### Bài 15.3 — Ngăn xếp đơn điệu (Monotonic Stack $\mathcal{O}(N)$)

#### 1. Khái niệm & Bài toán Next Greater Element
- Tìm phần tử lớn hơn đầu tiên bên phải trong $\mathcal{O}(N)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 15.3: Giám Sát Cột Tín Hiệu Cao Hơn Gần Nhất**  
> **Bối cảnh:** $N$ trạm phát sóng có độ cao $A_1, A_2, \dots, A_N$. Tìm trạm đầu tiên bên phải có độ cao lớn hơn để chuyển tiếp chùm sóng vi ba.  
> **Input:** `4` \ `4 5 2 25` $\implies$ **Output:** `5 25 25 -1`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    vector<int> nge(n, -1);
    stack<int> st;

    for (int i = n - 1; i >= 0; i--) {
        while (!st.empty() && st.top() <= a[i]) st.pop();
        if (!st.empty()) nge[i] = st.top();
        st.push(a[i]);
    }

    for (int i = 0; i < n; i++) cout << nge[i] << (i + 1 == n ? "" : " ");
    cout << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 15.3

##### Bài 15.3.1 — Tìm Phần Tử Nhỏ Hơn Đầu Tiên Bên Trái (Previous Smaller Element)
- **Bối cảnh:** Cho mảng $N$ số. Tìm phần tử nhỏ hơn đầu tiên nằm bên trái của từng vị trí trong $\mathcal{O}(N)$.
- **Input:** `4` \ `4 5 2 10` $\implies$ **Output:** `-1 4 -1 2`

##### Bài 15.3.2 — Tầm Nhìn Xa Của Tòa Tháp Chọc Trời
- **Bối cảnh:** Mỗi tòa tháp nhìn thấy các tòa nhà thấp hơn liên tiếp bên trái. Tính số tòa tháp mỗi vị trí nhìn thấy.
- **Input:** `4` \ `10 4 6 8` $\implies$ **Output:** `1 1 2 3`

---

### Bài 15.4 — Ứng dụng: Hình chữ nhật lớn nhất trong Histogram

#### 1. Khái niệm & Thuật toán
- Tìm cận trái $L[i]$ và cận phải $R[i]$ trong $\mathcal{O}(N)$. Diện tích: $H_i \times (R[i] - L[i] - 1)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 15.4: Thiết Kế Tấm Pin Năng Lượng Mặt Trời Diện Tích Lớn Nhất**  
> **Bối cảnh:** Mái nhà gồm $N$ khối kiến trúc liền kề có chiều cao $H_1, H_2, \dots, H_N$. Tìm diện tích hình chữ nhật lớn nhất có thể lắp đặt tấm pin mặt trời.  
> **Input:** `6` \ `2 1 5 6 2 3` $\implies$ **Output:** `10` ($5 \times 2 = 10$).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; i++) cin >> h[i];

    vector<int> leftLess(n), rightLess(n);
    stack<int> st;

    for (int i = 0; i < n; i++) {
        while (!st.empty() && h[st.top()] >= h[i]) st.pop();
        leftLess[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }

    while (!st.empty()) st.pop();

    for (int i = n - 1; i >= 0; i--) {
        while (!st.empty() && h[st.top()] >= h[i]) st.pop();
        rightLess[i] = st.empty() ? n : st.top();
        st.push(i);
    }

    long long maxArea = 0;
    for (int i = 0; i < n; i++) {
        long long width = rightLess[i] - leftLess[i] - 1;
        maxArea = max(maxArea, h[i] * width);
    }

    cout << maxArea << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 15.4

##### Bài 15.4.1 — Tấm Bạt Phủ Hàng Nông Sản Hình Vuông Lớn Nhất
- **Bối cảnh:** Tìm diện tích hình vuông lớn nhất (cạnh $K \le H_i$ và $K \le \text{width}$) nằm hoàn toàn bên trong biểu đồ Histogram.
- **Input:** `4` \ `3 3 3 3` $\implies$ **Output:** `9` ($3 \times 3$).

##### Bài 15.4.2 — Ma Trận Con Toàn Số 1 Lớn Nhất
- **Bối cảnh:** Tìm diện tích hình chữ nhật lớn nhất toàn số 1 trên ma trận nhị phân $N \times M$.
- **Input:** `2 2` \ `1 1` \ `1 1` $\implies$ **Output:** `4`

---

### Bài 15.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 15.5.1 — Kiểm Tra Cặp Ngoặc Tròn Đơn Giản
- **Bối cảnh:** Kiểm tra xâu chỉ gồm các ký tự `(` và `)` có phải là dãy ngoặc đúng không.

##### Bài 15.5.2 — Mô Phỏng Hàng Đợi Khách Hàng Viettel Store
- **Bối cảnh:** Thực hiện các thao tác thêm khách hàng vào hàng đợi và phục vụ khách hàng đầu tiên.

##### Bài 15.5.3 — Tìm Trạm Cao Hơn Bên Phải (Next Greater Element)
- **Bối cảnh:** Cho mảng $N$ phần tử, tìm phần tử lớn hơn đầu tiên bên phải cho từng vị trí.

##### Bài 15.5.4 — Đảo Ngược Từ Trong Đoạn Tin Nhắn
- **Bối cảnh:** Dùng cấu trúc Stack để đảo ngược thứ tự các chữ cái trong từng từ của câu văn.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 15.5.5 — Diện Tích Kho Bãi Lớn Nhất Trong Histogram
- **Bối cảnh:** Cài đặt bài toán Histogram tìm diện tích hình chữ nhật lớn nhất trong $\mathcal{O}(N)$.

##### Bài 15.5.6 — Khu Vực Đất Trống Hình Chữ Nhật Toàn Số 1 Lớn Nhất
- **Bối cảnh:** Tìm diện tích hình chữ nhật toàn số 1 lớn nhất trên ma trận nhị phân $N \times M$ bằng cách quy về $N$ bài toán Histogram.

##### Bài 15.5.7 — Tạo Mã Định Danh Nhỏ Nhất Bằng Cách Xóa K Chữ Số
- **Bối cảnh:** Cho số nguyên lớn dưới dạng xâu, xóa đúng $K$ chữ số để số còn lại đạt giá trị nhỏ nhất có thể (dùng Monotonic Stack).

##### Bài 15.5.8 — Tính Giá Trị Biểu Thức Tính Toán Hậu Tố (Reverse Polish Notation)
- **Bối cảnh:** Đánh giá biểu thức toán học dạng hậu tố (Postfix) bằng Stack.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 15.5.9 — Tổng Mức Tiêu Thụ Điện Tối Thiểu Mọi Khoảng Thời Gian
- **Bối cảnh:** Tính tổng $\sum_{1 \le i \le j \le N} \min(A[i..j])$ trong thời gian $\mathcal{O}(N)$ bằng Monotonic Stack.

##### Bài 15.5.10 — Hàng Đợi Trượt Giám Sát Min/Max Bằng Deque
- **Bối cảnh:** Tìm giá trị nhỏ nhất và lớn nhất trong mọi cửa sổ trượt độ dài $K$ bằng Deque trong $\mathcal{O}(N)$.

##### Bài 15.5.11 — Đoạn Mã Lập Trình Hợp Lệ Dài Nhất
- **Bối cảnh:** Tìm độ dài của đoạn con liên tiếp dài nhất là một dãy ngoặc đúng.

##### Bài 15.5.12 — Xây Dựng Cây Nhị Phân Biểu Diễn Mảng (Cartesian Tree)
- **Bối cảnh:** Xây dựng Cartesian Tree cho mảng $N$ phần tử trong $\mathcal{O}(N)$ bằng Monotonic Stack.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Gọi `st.top()` hoặc `st.pop()` khi `st.empty() == true` | Luôn kiểm tra `!st.empty()` trước khi truy cập đỉnh stack |
| Tràn số khi tính diện tích Histogram ($H_i \times \text{width}$) | Ép kiểu `long long` cho diện tích |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Kiểm tra dãy ngoặc đúng và sử dụng Stack/Queue thành thạo. |
| **Vận dụng (Tầng B)** | Cài đặt Monotonic Stack tìm NGE và diện tích Histogram $\mathcal{O}(N)$. |
| **Thành thạo (Tầng C)** | Áp dụng Monotonic Stack tính tổng min các đoạn con và tìm ma trận 1 lớn nhất. |
