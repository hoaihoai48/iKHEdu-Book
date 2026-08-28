# TÀI LIỆU GỐC — CHƯƠNG 6: MẢNG TIỀN TỐ VÀ MẢNG HIỆU (PREFIX SUM & DIFFERENCE ARRAY)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững kỹ thuật tiền xử lý dữ liệu để trả lời truy vấn tổng đoạn tĩnh trong $\mathcal{O}(1)$ (Prefix Sum) và thực hiện các thao tác cộng trên đoạn trong $\mathcal{O}(1)$ (Difference Array); mở rộng tính toán trên ma trận 2D |
| Kiến thức cần có | Mảng 1D, 2D, quy ước chỉ số 1-based, phép toán XOR |
| Phạm vi | Mảng tiền tố 1D (Prefix Sum), Prefix XOR, Mảng hiệu 1D (Difference Array), Mảng tiền tố 2 chiều (2D Prefix Sum) |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Xây dựng mảng tiền tố 1D trong $\mathcal{O}(N)$ và tính tổng đoạn bất kỳ $[L, R]$ trong $\mathcal{O}(1)$.
2. Áp dụng Prefix XOR để kiểm tra và trả lời truy vấn XOR đoạn trong $\mathcal{O}(1)$.
3. Cài đặt mảng hiệu 1D thực hiện $Q$ thao tác cộng đoạn $[L, R]$ trong $\mathcal{O}(1)$ mỗi thao tác.
4. Xây dựng mảng tiền tố 2D tính tổng hình chữ nhật con bất kỳ trên ma trận trong $\mathcal{O}(1)$.

### Câu hỏi trung tâm của chương

> **Làm thế nào để tính tổng các số trong một đoạn hoặc trong một hình chữ nhật con ngay lập tức trong $1$ bước tính?**

---

### Bài 6.1 — Mảng tiền tố 1D (1D Prefix Sum)

#### 1. Khái niệm & Công thức tính tổng đoạn trong $\mathcal{O}(1)$
- **Mảng tiền tố $P$:** Định nghĩa $P[i]$ là tổng của tất cả các phần tử từ vị trí đầu tiên $1$ đến vị trí $i$:
  $$P[0] = 0, \quad P[i] = P[i - 1] + A[i] \quad (1 \le i \le N)$$
- **Công thức tính tổng đoạn $[L, R]$:**
  $$\text{Sum}(L, R) = A[L] + A[L+1] + \dots + A[R] = P[R] - P[L - 1]$$
- **Ý nghĩa:** Tiền xử lý $\mathcal{O}(N)$, sau đó mỗi truy vấn chỉ tốn đúng $\mathcal{O}(1)$ thời gian.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 6.1: Thống Kê Doanh Thu Chuỗi Cửa Hàng Bán Lẻ WinMart**  
> **Bối cảnh:** Tập đoàn WinCommerce quản lý chuỗi $N$ siêu thị mini trải dọc tuyến phố. Siêu thị thứ $i$ có doanh thu trong ngày là $A_i$ triệu đồng ($1 \le i \le N$). Ban giám đốc gửi $Q$ yêu cầu báo cáo doanh thu của các khu vực từ siêu thị $L$ đến siêu thị $R$.  
> **Nhiệm vụ:** Em hãy tính và in ra tổng doanh thu của khu vực $[L, R]$ trong $\mathcal{O}(1)$ thời gian cho mỗi truy vấn.  
> 
> **Input:**  
> - Dòng 1: Hai số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).  
> - Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).  
> - $Q$ dòng tiếp theo: Mỗi dòng chứa hai số nguyên $L, R$ ($1 \le L \le R \le N$).  
> 
> **Output:**  
> - Ghi $Q$ dòng, mỗi dòng là tổng doanh thu của đoạn tương ứng.  
> 
> **Sample:**  
> - **Input:**  
>   `5 3`  
>   `2 4 1 7 3`  
>   `1 3`  
>   `2 4`  
>   `3 5`  
> - **Output:**  
>   `7`  
>   `12`  
>   `11`  
> - **Giải thích:** Tổng từ siêu thị 1 đến 3 là $2 + 4 + 1 = 7$. Tổng từ 2 đến 4 là $4 + 1 + 7 = 12$.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> pref(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        pref[i] = pref[i - 1] + x;
    }

    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << pref[r] - pref[l - 1] << "\n";
    }

    return 0;
}
```

---

#### 3. Bẫy lỗi thường gặp
| Lỗi | Hậu quả | Cách tự kiểm tra |
|---|---|---|
| Dùng chỉ số 0-based gây lỗi khi $L = 0$ (phải truy cập `pref[-1]`) | Gây lỗi bộ nhớ `Segmentation Fault` | **Bắt buộc dùng quy ước chỉ số 1-based** ($1 \le i \le N$) và khởi tạo `pref[0] = 0` |
| Dùng kiểu `int` cho mảng `pref` | Khi tổng các phần tử vượt quá $2 \times 10^9$ sẽ bị tràn số âm | Luôn khai báo `vector<long long> pref` |

---

#### 4. Bài tập thực hành Bài 6.1

##### Bài 6.1.1 — Đếm Lượng Điện Tiêu Thụ Vượt Ngưỡng Khu Dân Cư
- **Bối cảnh:** Cho $N$ hộ gia đình với lượng điện tiêu thụ $A_1.A_N$. Đếm số hộ dùng điện vượt mức trung bình trong đoạn $[L, R]$ bằng cách chuyển đổi mảng sang nhị phân và tính Prefix Sum.
- **Input:** `5 2` \ `1 2 4 5 6` \ `1 3` \ `2 4` $\implies$ **Output:** `2` \ `2`

##### Bài 6.1.2 — Đoạn Phố Thương Mại Sầm Uất Nhất Độ Dài K
- **Bối cảnh:** Tìm đoạn $K$ cửa hàng liên tiếp có tổng doanh thu lớn nhất.
- **Input:** `5 3` \ `1 4 2 10 3` $\implies$ **Output:** `16` (đoạn $[4, 2, 10]$).

---

### Bài 6.2 — Prefix XOR và ứng dụng

#### 1. Khái niệm & Thuật toán
- **Tính chất:** $X \oplus X = 0, X \oplus 0 = X$.
- **XOR đoạn $[L, R]$:** $A[L] \oplus \dots \oplus A[R] = P_{\text{xor}}[R] \oplus P_{\text{xor}}[L - 1]$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 6.2: Giải Mã Tín Hiệu Bảo Mật VinaPhone**  
> **Bối cảnh:** Trạm thu phát sóng viễn thông VinaPhone mã hóa luồng dữ liệu $N$ gói tin bằng toán tử XOR.  
> **Nhiệm vụ:** Trả lời $Q$ truy vấn tính tổng XOR của các gói tin từ vị trí $L$ đến $R$.  
> **Input:** `4 2` \ `3 2 5 7` \ `1 3` \ `2 4` $\implies$ **Output:** `4` \ `0`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> prefXor(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        prefXor[i] = prefXor[i - 1] ^ x;
    }

    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << (prefXor[r] ^ prefXor[l - 1]) << "\n";
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 6.2

##### Bài 6.2.1 — Đoạn Tín Hiệu Cân Bằng Parity
- **Bối cảnh:** Đếm số đoạn con $[L, R]$ có tổng XOR bằng $0$ (tức $P_{\text{xor}}[R] = P_{\text{xor}}[L - 1]$).
- **Input:** `4` \ `1 2 3 0` $\implies$ **Output:** `3`

##### Bài 6.2.2 — Khôi Phục Dãy Tín Hiệu Bằng XOR Tiền Tố
- **Bối cảnh:** Cho $N$ số. Thực hiện $Q$ truy vấn tính XOR các phần tử từ $L$ đến $R$.
- **Input:** `4 1` \ `1 2 3 4` \ `2 4` $\implies$ **Output:** `5`

---

### Bài 6.3 — Mảng hiệu 1D (Difference Array)

#### 1. Khái niệm & Kỹ thuật cộng đoạn trong $\mathcal{O}(1)$
- **Mục tiêu:** Cộng thêm giá trị $V$ vào tất cả phần tử từ vị trí $L$ đến $R$.
- **Mảng hiệu $D$:** $D[L] += V, D[R + 1] -= V$. Mảng ban đầu là Prefix Sum của $D$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 6.3: Phân Bổ Điện Năng Lưới Điện Quốc Gia EVN**  
> **Bối cảnh:** Tập đoàn Điện lực Việt Nam (EVN) quản lý $N$ trạm biến áp, ban đầu mức tải bổ sung đều là $0$. Có $Q$ lịch điều phối điện áp, lần thứ $j$ tăng cường $V_j$ Megawatt cho các trạm từ $L_j$ đến $R_j$.  
> **Nhiệm vụ:** In ra mức điện tải cuối cùng của $N$ trạm biến áp sau $Q$ lần điều phối.  
> **Input:** `5 3` \ `1 3 2` \ `2 5 3` \ `4 5 1` $\implies$ **Output:** `2 5 5 4 4`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> diff(n + 2, 0);
    while (q--) {
        int l, r;
        long long v;
        cin >> l >> r >> v;
        diff[l] += v;
        diff[r + 1] -= v;
    }

    long long current = 0;
    for (int i = 1; i <= n; i++) {
        current += diff[i];
        cout << current << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 6.3

##### Bài 6.3.1 — Điểm Nút Giao Thông Quá Tải Nhất Giờ Cao Điểm
- **Bối cảnh:** Cho $N$ tuyến xe bus có lộ trình chạy từ trạm $L_i$ đến $R_i$. Tìm trạm đón nhiều lượt xe nhất và số lượt xe qua trạm đó.
- **Input:** `3` \ `1 4` \ `2 5` \ `3 6` $\implies$ **Output:** `3 3`

##### Bài 6.3.2 — Tưới Nước Ruộng Vườn Tự Động
- **Bối cảnh:** $N$ bồn cây, $Q$ lượt tưới nước cho đoạn $[L, R]$ thêm $V$ lít nước. In lượng nước cuối cùng ở từng bồn.
- **Input:** `3 1` \ `0 0 0` \ `1 2 5` $\implies$ **Output:** `5 5 0`

---

### Bài 6.4 — Mảng tiền tố 2 chiều (2D Prefix Sum)

#### 1. Khái niệm & Công thức ma trận
- $P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + A[i][j]$.
- Tổng hình chữ nhật con: $P[x_2][y_2] - P[x_1-1][y_2] - P[x_2][y_1-1] + P[x_1-1][y_1-1]$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 6.4: Quy Hoạch Vùng Nông Nghiệp Công Nghệ Cao**  
> **Bối cảnh:** Bản đồ nông nghiệp $N \times M$ ô, ô $(i, j)$ cho sản lượng $A[i][j]$ tấn lúa. Trả lời $Q$ truy vấn tính sản lượng của vùng quy hoạch hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$.  
> **Input:**  
> `3 3 1`  
> `1 2 3`  
> `4 5 6`  
> `7 8 9`  
> `2 2 3 3`  
> **Output:** `28` ($5 + 6 + 8 + 9 = 28$).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> pref(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            long long val;
            cin >> val;
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + val;
        }
    }

    while (q--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        long long sum = pref[x2][y2] - pref[x1 - 1][y2] - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1];
        cout << sum << "\n";
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 6.4

##### Bài 6.4.1 — Vùng Trồng Cây Cà Phê Hình Vuông $K \times K$
- **Bối cảnh:** Tìm ô vuông $K \times K$ có tổng sản lượng cà phê lớn nhất trên nông trường $N \times M$.
- **Input:** `3 3 2` \ `1 1 1` \ `1 9 9` \ `1 9 9` $\implies$ **Output:** `36`

##### Bài 6.4.2 — Tổng Doanh Thu Lô Đất 2D
- **Bối cảnh:** Tính tổng doanh thu của khu vực hình chữ nhật con từ ô $(x_1, y_1)$ đến $(x_2, y_2)$ trên ma trận $N \times M$.
- **Input:** `2 2 1` \ `1 2` \ `3 4` \ `1 1 2 2` $\implies$ **Output:** `10`

---

### Bài 6.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)
##### Bài 6.5.1 — Tổng Lượng Mưa Đoạn Tuyến Bắc Nam
- **Bối cảnh:** $Q$ truy vấn tính tổng lượng mưa các trạm $[L, R]$.
##### Bài 6.5.2 — Đếm Ngày Nhiệt Độ Dưới 0 Độ C
- **Bối cảnh:** Trả lời số lượng ngày rét đậm rét hại trong $[L, R]$.
##### Bài 6.5.3 — Cấp Nước Sinh Hoạt Đô Thị Bằng Mảng Hiệu
- **Bối cảnh:** $Q$ đợt bơm nước vào các đoạn đường ống.
##### Bài 6.5.4 — Thống Kê Doanh Thu Quầy Hàng 2D
- **Bối cảnh:** Tính tổng doanh thu gian hàng chợ đầu mối.

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)
##### Bài 6.5.5 — Đoạn Giao Dịch Cân Bằng Thu Chi
- **Bối cảnh:** Tìm khoảng thời gian liên tiếp dài nhất có tổng thu trừ tổng chi bằng $0$.
##### Bài 6.5.6 — Cân Bằng Số Lượng Xe Điện Và Xe Xăng
- **Bối cảnh:** Cho mảng nhị phân. Tìm đoạn dài nhất có số xe điện bằng số xe xăng.
##### Bài 6.5.7 — Vùng Phủ Sóng Trạm Ra-đa Thời Tiết Hình Vuông K
- **Bối cảnh:** Tìm vị trí đặt trạm ra-đa $K \times K$ phủ được nhiều dân cư nhất.
##### Bài 6.5.8 — Điều Phối Nước Ruộng Bậc Thang 2D Difference
- **Bối cảnh:** $Q$ lần xả nước vào các ô hình chữ nhật trên đồng ruộng.

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)
##### Bài 6.5.9 — Đếm Vùng Đất Có Năng Suất Đúng Bằng K
- **Bối cảnh:** Đếm số ma trận con có tổng đúng bằng $K$ ($N, M \le 400$).
##### Bài 6.5.10 — Kiểm Tra Mật Mã Đối Xứng Trong Đoạn Con
- **Bối cảnh:** $Q$ truy vấn kiểm tra ký tự $S[L.R]$ có thể đảo thành Palindrome không bằng 26 mảng tiền tố ký tự.
##### Bài 6.5.11 — Quét Đoạn Tuyến Giao Thông Line Sweep
- **Bối cảnh:** Tính tổng chiều dài phần đường được sửa chữa từ $N$ đoạn đường thi công.
##### Bài 6.5.12 — Quảng Trường Hình Vuông Lát Đá Hoa Cương Lớn Nhất
- **Bối cảnh:** Tìm kích thước hình vuông toàn số 1 lớn nhất trên ma trận nhị phân.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Khai báo mảng hiệu kích thước $N$ (bị tràn khi ghi `diff[r + 1]`) | Luôn khai báo `vector<long long> diff(n + 2, 0)` |
| Sai dấu trong công thức 2D Prefix Sum | Nhớ nguyên tắc: Trừ 2 phần giao và Cộng lại phần góc bị trừ 2 lần |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Cài đặt chính xác 1D/2D Prefix Sum và Difference Array không lỗi lệch chỉ số. |
| **Vận dụng (Tầng B)** | Kết hợp mảng tiền tố với bảng băm giải các bài toán đoạn con tổng bằng 0 và mảng nhị phân. |
| **Thành thạo (Tầng C)** | Làm chủ 2D Prefix Sum trong các bài toán đếm ma trận con và kiểm tra xâu đối xứng. |
