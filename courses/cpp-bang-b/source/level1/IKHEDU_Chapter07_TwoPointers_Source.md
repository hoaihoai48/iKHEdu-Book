# TÀI LIỆU GỐC — CHƯƠNG 7: HAI CON TRỎ VÀ CỬA SỔ TRƯỢT (TWO POINTERS & SLIDING WINDOW)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững kỹ thuật Hai con trỏ (Two Pointers) và Cửa sổ trượt (Sliding Window); giảm độ phức tạp từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N)$ tuyến tính |
| Kiến thức cần có | Mảng một chiều, sắp xếp, vòng lặp `while`, tính đơn điệu |
| Phạm vi | Con trỏ ngược chiều (2-SUM trên mảng sắp xếp), Cửa sổ trượt độ dài cố định/co giãn, Kỹ thuật trộn 2 dãy, Cửa sổ trượt với bảng tần suất |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Nhận biết tính chất đơn điệu để áp dụng kỹ thuật Hai con trỏ thay vì vét cạn 2 vòng lặp — `LO-01`.
2. Cài đặt thành thạo Hai con trỏ ngược chiều giải bài toán 2-SUM trong thời gian $\mathcal{O}(N)$ — `LO-02`.
3. Cài đặt Cửa sổ trượt linh hoạt (nới rộng và thu hẹp) để tìm đoạn con tối ưu — `LO-03`.
4. Duy trì trạng thái cửa sổ trượt bằng mảng đếm tần suất 26 chữ cái hoặc bảng băm — `LO-04`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để duyệt qua tất cả các cặp phần tử hoặc đoạn con liên tiếp mà chỉ mất thời gian $\mathcal{O}(N)$ thay vì $\mathcal{O}(N^2)$?**

---

### Bài 7.1 — Hai con trỏ ngược chiều (Opposite Direction)

#### 1. Khái niệm & Thuật toán
- **Điều kiện áp dụng:** Mảng đã được sắp xếp tăng dần.
- Đặt `left = 0, right = N - 1`. Nếu $A[left] + A[right] == X$, tìm thấy nghiệm. Nếu tổng $< X$, tăng `left++`. Nếu tổng $> X$, giảm `right--`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 7.1: Ghép Năng Lượng Hai Robot Thám Hiểm**  
> **Bối cảnh:** Hai robot thám hiểm không gian cần được ghép đôi để hoạt động. Tổng mức năng lượng của hai robot phải đạt đúng giá trị $X$ để kích hoạt cổng dịch chuyển.  
> **Nhiệm vụ:** Cho danh sách năng lượng của $N$ robot $A_1, A_2, \dots, A_N$ đã được sắp xếp tăng dần. Hãy tìm chỉ số của 2 robot $(i, j)$ sao cho $A_i + A_j = X$.  
> 
> **Input:**  
> - Dòng 1: Hai số nguyên $N$ và $X$ ($2 \le N \le 10^5, 1 \le X \le 10^9$).  
> - Dòng 2: $N$ số nguyên tăng dần $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).  
> 
> **Output:**  
> - Ghi 2 số nguyên là chỉ số (1-based) của 2 robot. Nếu không có cặp nào, in `-1 -1`.  
> 
> **Sample:**  
> - **Input:**  
>   `5 10`  
>   `1 2 4 7 9`  
> - **Output:** `1 5`  
> - **Giải thích:** Robot 1 có năng lượng 1 và robot 5 có năng lượng 9, tổng là $1 + 9 = 10$.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int left = 0, right = n - 1;
    int ansL = -1, ansR = -1;

    while (left < right) {
        long long sum = a[left] + a[right];
        if (sum == x) {
            ansL = left + 1;
            ansR = right + 1;
            break;
        } else if (sum < x) {
            left++;
        } else {
            right--;
        }
    }

    if (ansL != -1) {
        cout << ansL << " " << ansR << "\n";
    } else {
        cout << "-1 -1\n";
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 7.1

##### Bài 7.1.1 — Cặp Tàu Thuyền Vượt Cầu Trọng Tải K
- **Bối cảnh:** Cho danh sách $N$ sà lan chở hàng đã sắp xếp trọng lượng tăng dần. Đếm số cách chọn 2 sà lan $(i, j)$ có tổng trọng tải $< K$.
- **Input:** `4 8` \ `1 3 5 7` $\implies$ **Output:** `4`

##### Bài 7.1.2 — Ghép Đôi Xe Tải Tối Đa Tải Trọng
- **Bối cảnh:** Tìm 2 xe tải có tổng tải trọng gần $X$ nhất nhưng không vượt quá $X$.
- **Input:** `4 10` \ `2 4 7 9` $\implies$ **Output:** `9` (chọn 2 và 7)

---

### Bài 7.2 — Cửa sổ trượt (Sliding Window / Two Pointers cùng chiều)

#### 1. Khái niệm & Nguyên tắc nới rộng - thu hẹp
- Nới rộng biên phải $R$ để thêm phần tử $A[R]$.
- Thu hẹp biên trái $L$ bằng cách trừ $A[L]$ và tăng $L\text{++}$ khi điều kiện bị vi phạm.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 7.2: Chuyến Xe Buýt Tiếp Vận Nông Sản Dài Nhất**  
> **Bối cảnh:** Xe tải nông sản thu mua dưa hấu dọc tuyến đường liên xã gồm $N$ vựa nông sản. Vựa thứ $i$ có sản lượng $A_i$ tấn. Sức chứa tối đa của thùng xe là $S$ tấn. Xe chỉ được thu mua tại một dãy các vựa liên tiếp nhau.  
> **Nhiệm vụ:** Tìm số lượng vựa nông sản liên tiếp nhiều nhất mà xe có thể thu mua trọn vẹn mà không vượt quá tải trọng $S$.  
> **Input:** `5 7` \ `2 1 4 3 2` $\implies$ **Output:** `3` (thu mua 3 vựa $[2, 1, 4]$ có tổng 7 tấn $\le 7$).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int left = 0;
    long long currentSum = 0;
    int maxLen = 0;

    for (int right = 0; right < n; right++) {
        currentSum += a[right];
        while (currentSum > s && left <= right) {
            currentSum -= a[left];
            left++;
        }
        if (currentSum <= s) {
            maxLen = max(maxLen, right - left + 1);
        }
    }

    cout << maxLen << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 7.2

##### Bài 7.2.1 — Đoạn Đê Xung Yếu Ngắn Nhất Cần Gia Cố
- **Bối cảnh:** Tìm độ dài đoạn đê ngắn nhất có tổng mức độ xói mòn $\ge S$.
- **Input:** `6 15` \ `5 1 3 5 10 7` $\implies$ **Output:** `2` (đoạn $[10, 7]$).

##### Bài 7.2.2 — Đoạn Con Dài Nhất Có Tổng Nhỏ Hơn S
- **Bối cảnh:** Tìm độ dài của đoạn con liên tiếp dài nhất có tổng $\le S$.
- **Input:** `4 6` \ `1 2 3 4` $\implies$ **Output:** `3` (đoạn [1, 2, 3])

---

### Bài 7.3 — Kỹ thuật trộn hai dãy đã sắp xếp

#### 1. Khái niệm & Thuật toán
- Trộn 2 dãy tăng dần kích thước $N$ và $M$ thành 1 dãy tăng dần trong $\mathcal{O}(N + M)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 7.3: Hợp Nhất Dữ Liệu Cảm Biến Khí Tượng**  
> **Bối cảnh:** Hai trạm khí tượng thu thập dữ liệu nhiệt độ theo thứ tự tăng dần.  
> **Nhiệm vụ:** Hợp nhất 2 luồng dữ liệu thành một dòng thời gian duy nhất theo thứ tự tăng dần.  
> **Input:** `3 3` \ `1 4 7` \ `2 3 8` $\implies$ **Output:** `1 2 3 4 7 8`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n), b(m);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];

    int i = 0, j = 0;
    while (i < n && j < m) {
        if (a[i] <= b[j]) {
            cout << a[i++] << " ";
        } else {
            cout << b[j++] << " ";
        }
    }
    while (i < n) cout << a[i++] << " ";
    while (j < m) cout << b[j++] << " ";
    cout << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 7.3

##### Bài 7.3.1 — Hợp Nhất Hai Danh Sách Khách Hàng
- **Bối cảnh:** Trộn 2 danh sách số điện thoại tăng dần thành 1 danh sách tăng dần.
- **Input:** `2 2` \ `1 3` \ `2 4` $\implies$ **Output:** `1 2 3 4`

##### Bài 7.3.2 — Tìm Phần Tử Chung Của Hai Danh Sách Đã Sắp Xếp
- **Bối cảnh:** In các phần tử xuất hiện ở cả hai danh sách $A$ và $B$ trong $\mathcal{O}(N + M)$.
- **Input:** `3 3` \ `1 2 3` \ `2 3 4` $\implies$ **Output:** `2 3`

---

### Bài 7.4 — Cửa sổ trượt với Bảng tần suất

#### 1. Khái niệm & Thuật toán
- Dùng mảng tần suất hoặc `map` kết hợp mở rộng con trỏ phải `r` và thu hẹp con trỏ trái `l` để duy trì điều kiện có tối đa $K$ phần tử khác nhau.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 7.4: Gói Đăng Ký Xem Phim Truyền Hình Trả Tiền**  
> **Bối cảnh:** Nhà mạng cung cấp danh sách $N$ kênh truyền hình liên tiếp. Người dùng muốn chọn gói xem nhiều kênh nhất nhưng chỉ chứa tối đa $K$ thể loại nội dung khác nhau.  
> **Input:** `5 2` \ `1 2 1 2 3` $\implies$ **Output:** `4` (đoạn $[1, 2, 1, 2]$).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    unordered_map<int, int> freq;
    int left = 0, maxLen = 0;

    for (int right = 0; right < n; right++) {
        freq[a[right]]++;
        while ((int)freq.size() > k) {
            freq[a[left]]--;
            if (freq[a[left]] == 0) {
                freq.erase(a[left]);
            }
            left++;
        }
        maxLen = max(maxLen, right - left + 1);
    }

    cout << maxLen << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 7.4

##### Bài 7.4.1 — Đoạn Con Có Nhiều Nhất K Ký Tự Phân Biệt
- **Bối cảnh:** Tìm độ dài xâu con dài nhất chứa không quá $K$ ký tự khác nhau.
- **Input:** `eceba 2` $\implies$ **Output:** `3` ("ece")

##### Bài 7.4.2 — Đếm Số Đoạn Con Chứa Đủ K Loại Trái Cây
- **Bối cảnh:** Đếm số lượng đoạn con liên tiếp chứa đúng $K$ loại trái cây khác nhau.
- **Input:** `4 2` \ `1 2 1 3` $\implies$ **Output:** `4`

---

### Bài 7.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)
##### Bài 7.5.1 — Ghép Đôi Xe Tải Cân Bằng
- **Bối cảnh:** Tìm 2 xe có tổng tải trọng bằng $X$.
##### Bài 7.5.2 — Trộn Danh Sách Khách Hàng
- **Bối cảnh:** Hợp nhất 2 danh sách số điện thoại tăng dần.
##### Bài 7.5.3 — Tổng Doanh Thu Cửa Sổ K Ngày
- **Bối cảnh:** Tìm tổng lớn nhất của $K$ ngày liên tiếp.
##### Bài 7.5.4 — Đếm Chuyến Xe Tải Trọng Hợp Lệ
- **Bối cảnh:** Đếm số đoạn có tổng $\le S$.

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)
##### Bài 7.5.5 — Cân Bằng Tài Chính Bộ Ba 3-SUM $\mathcal{O}(N^2)$
- **Bối cảnh:** Tìm bộ ba $(i, j, k)$ có tổng bằng 0.
##### Bài 7.5.6 — Đoạn Phim Quảng Cáo Đa Dạng K Thể Loại
- **Bối cảnh:** Đếm số đoạn chứa tối đa $K$ thể loại phân biệt.
##### Bài 7.5.7 — Hứng Nước Mưa Khe Núi - Trapping Rain Water
- **Bối cảnh:** Tính thể tích nước mưa giữ lại giữa các dãy núi trong $\mathcal{O}(N)$.
##### Bài 7.5.8 — Chênh Lệch Nhỏ Nhất Giữa Hai Lô Đất
- **Bối cảnh:** Tìm cặp $(A_i, B_j)$ có $|A_i - B_j|$ nhỏ nhất.

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)
##### Bài 7.5.9 — Bộ Tứ Cân Bằng 4-SUM $\mathcal{O}(N^3)$
- **Bối cảnh:** Tìm 4 số có tổng bằng $X$.
##### Bài 7.5.10 — Giám Sát Lưu Lượng Mạng Cực Đại Cửa Sổ Trượt
- **Bối cảnh:** Tìm Max trong cửa sổ độ dài $K$ bằng Deque trong $\mathcal{O}(N)$.
##### Bài 7.5.11 — Đoạn Cổ Phiếu Dao Động Nhỏ Hơn D
- **Bối cảnh:** Đếm số đoạn có $\max - \min \le D$.
##### Bài 7.5.12 — Khôi Phục Bản Tin Đối Xứng Khi Xóa 1 Ký Tự
- **Bối cảnh:** Kiểm tra tạo Palindrome bằng xóa tối đa 1 ký tự.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Dùng Two Pointers khi dãy có số âm (làm mất tính đơn điệu của tổng) | Two Pointers chỉ áp dụng cho mảng số không âm hoặc mảng đã sắp xếp |
| Điều kiện dừng vòng lặp `while (left < right)` bị nhầm thành `left <= right` | Bài toán tìm 2 phần tử khác nhau bắt buộc dùng `left < right` |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Cài đặt chính xác 2-SUM và Sliding Window độ dài cố định. |
| **Vận dụng (Tầng B)** | Cài đặt Sliding Window co giãn và thuật toán Trapping Rain Water $\mathcal{O}(N)$. |
| **Thành thạo (Tầng C)** | Giải bài toán 3-SUM, 4-SUM và Sliding Window Max bằng Deque $\mathcal{O}(N)$. |
