# TÀI LIỆU GỐC — CHƯƠNG 4: ĐẾM PHÂN PHỐI VÀ NGUYÊN LÝ DIRICHLET (FREQUENCY COUNT)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Chuyển đổi tư duy từ so sánh từng cặp ($\mathcal{O}(N^2)$) sang mảng tần suất trực tiếp ($\mathcal{O}(N)$), áp dụng nguyên lý Dirichlet để giải các bài toán tồn tại, đa số và thống kê dữ liệu trong tin học |
| Kiến thức cần có | Mảng 1 chiều (`vector<int>`), chỉ số mảng, vòng lặp, khởi tạo mảng `0` |
| Phạm vi | Mảng tần suất trực tiếp, tìm Max/Min tần suất, đếm giá trị phân biệt, đếm cặp phần tử trong $\mathcal{O}(N)$, nguyên lý Dirichlet (nguyên lý chuồng bồ câu) |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Xây dựng và cập nhật bảng đếm tần suất các giá trị trong thời gian $\mathcal{O}(N)$ — `LO-01`.
2. Tìm phần tử xuất hiện nhiều nhất, ít nhất hoặc xuất hiện đúng $K$ lần trong một dãy — `LO-02`.
3. Đếm số lượng cặp phần tử thỏa mãn điều kiện tổng/hiệu/bằng nhau trong $\mathcal{O}(N)$ mà không cần 2 vòng lặp lồng nhau — `LO-03`.
4. Vận dụng nguyên lý Dirichlet để chứng minh và giải các bài toán tồn tại phần tử trùng lặp — `LO-04`.
5. Phân biệt được giới hạn của mảng tần suất trực tiếp ($A_i \le 10^6$) và khi nào cần dùng nén số — `LO-05`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để biết một mảng có bao nhiêu giá trị khác nhau hoặc giá trị nào xuất hiện nhiều nhất chỉ qua MỘT lần duyệt duy nhất?**

---

### Bài 4.1 — Mảng tần suất (Frequency Array) là gì?

#### 1. Khái niệm & Tư duy chuyển giá trị thành chỉ số
- **Ý tưởng cốt lõi:** Thay vì duyệt qua mảng nhiều lần để đếm từng số, ta tạo một mảng đếm `cnt` được khởi tạo toàn số `0`. Mỗi khi đọc vào một giá trị `v`, ta xem `v` chính là **chỉ số (index)** của mảng `cnt` và tăng giá trị tại vị trí đó lên 1:
  $$\text{cnt}[v] = \text{cnt}[v] + 1 \quad (\text{hoặc } \text{cnt}[v]\text{++})$$
- **Điều kiện áp dụng:** Giá trị $A_i$ phải là số nguyên không âm và có độ lớn vừa phải ($0 \le A_i \le 10^6$).
- **Độ phức tạp:** Duyệt $N$ phần tử hết $\mathcal{O}(N)$, nhanh hơn gấp hàng nghìn lần so với phương pháp duyệt 2 vòng lặp $\mathcal{O}(N^2)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 4.1: Kiểm Kê Mã Vạch Siêu Thị WinMart**  
> **Bối cảnh:** Tại quầy thu ngân chuỗi siêu thị WinMart+, hệ thống máy quét ghi nhận $N$ lượt quét mã vạch sản phẩm được mua trong ngày. Mỗi mã sản phẩm là một số nguyên không âm $A_i \le 10^5$.  
> **Nhiệm vụ:** Là chuyên viên dữ liệu chuỗi bán lẻ, em hãy đếm xem có bao nhiêu loại mặt hàng khác nhau đã được bán và in ra số lượng bán của từng mặt hàng theo thứ tự mã số tăng dần.  
> 
> **Input:**  
> - Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).  
> - Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^5$).  
> 
> **Output:**  
> - Dòng 1: Ghi số lượng mã sản phẩm phân biệt đã bán.  
> - Các dòng tiếp theo: Ghi `[Mã] xuat hien [Số lần] lan` cho các sản phẩm có lượt bán $> 0$.  
> 
> **Sample:**  
> - **Input:**  
>   `6`  
>   `3 1 3 2 1 3`  
> - **Output:**  
>   `3`  
>   `1 xuat hien 2 lan`  
>   `2 xuat hien 1 lan`  
>   `3 xuat hien 3 lan`

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> cnt(MAX_VAL + 1, 0);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cnt[x]++;
    }

    int distinctCount = 0;
    for (int v = 0; v <= MAX_VAL; v++) {
        if (cnt[v] > 0) distinctCount++;
    }

    cout << distinctCount << "\n";
    for (int v = 0; v <= MAX_VAL; v++) {
        if (cnt[v] > 0) {
            cout << v << " xuat hien " << cnt[v] << " lan\n";
        }
    }

    return 0;
}
```

---

#### 3. Bẫy lỗi thường gặp
| Lỗi | Hậu quả | Cách tự kiểm tra |
|---|---|---|
| Kích thước mảng `cnt` nhỏ hơn $\max(A_i)$ | Gây lỗi bộ nhớ `Segmentation Fault` | Luôn khai báo `MAX_VAL >= max(A_i)` |
| Giá trị $A_i$ bị âm | Không dùng số âm làm chỉ số | Tịnh tiến: `cnt[x + OFFSET]++` |

---

#### 4. Bài tập thực hành Bài 4.1

##### Bài 4.1.1 — Mã Định Danh Duy Nhất Thẻ Học Sinh
- **Bối cảnh:** Trường học phát hành $N$ thẻ từ, mỗi thẻ mang mã số $A_i$. Do lỗi in ấn, một số thẻ bị trùng mã. Hãy in ra danh sách các mã thẻ chỉ xuất hiện đúng 1 lần theo thứ tự tăng dần.
- **Input:** Dòng 1 ghi $N \le 10^5$. Dòng 2 ghi $N$ số $A_i \le 10^5$.
- **Output:** Dãy các mã thẻ độc nhất.
- **Sample:** `6` \ `4 2 7 2 4 9` $\implies$ **Output:** `7 9`

##### Bài 4.1.2 — Ký Tự Phổ Biến Nhất Trong Tin Nhắn Zalo
- **Bối cảnh:** Bộ lọc từ khóa Zalo phân tích xâu $S$ gồm các chữ cái in thường để tìm chữ cái xuất hiện nhiều lần nhất.
- **Input:** Xâu ký tự $S$ ($1 \le |S| \le 10^5$).
- **Output:** Chữ cái xuất hiện nhiều nhất (nếu có nhiều chữ cái, in chữ cái có thứ tự từ điển nhỏ nhất).
- **Sample:** `ikheducppprogramming` $\implies$ **Output:** `p`

---

### Bài 4.2 — Tìm phần tử đa số và Thống kê dữ liệu

#### 1. Khái niệm & Thuật toán
- **Phần tử đa số (Majority Element):** Là phần tử xuất hiện nhiều hơn $\lfloor N / 2 \rfloor$ lần trong tập hợp $N$ phần tử.
- Dùng mảng tần suất kiểm tra điều kiện `cnt[v] > N / 2` trong $\mathcal{O}(N)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 4.2: Bỏ Phiếu Bầu Ban Cán Sự Lớp**  
> **Bối cảnh:** Lớp học tổ chức bầu lớp trưởng từ danh sách $N$ phiếu bầu. Phiếu bầu ghi số báo danh ứng viên $A_i$. Ứng viên chỉ trúng cử nếu đạt được đa số tuyệt đối (số phiếu $> N/2$).  
> **Nhiệm vụ:** Tìm số báo danh của người trúng cử. Nếu không có ai đạt đa số, in `-1`.  
> **Input:** `7` \ `3 3 4 2 3 3 5` $\implies$ **Output:** `3` (ứng viên số 3 đạt 4/7 phiếu).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> cnt(MAX_VAL + 1, 0);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cnt[x]++;
    }

    int majority = -1;
    for (int v = 0; v <= MAX_VAL; v++) {
        if (cnt[v] > n / 2) {
            majority = v;
            break;
        }
    }

    cout << majority << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 4.2

##### Bài 4.2.1 — Khôi Phục Vé Xe Bị Thất Lạc
- **Bối cảnh:** Bến xe miền Đông phát hành $N$ vé xe có mã từ $1$ đến $N$. Cuối ngày thu gom được $N - 1$ vé phân biệt. Hãy tìm mã số của chiếc vé bị thất lạc.
- **Input:** `5` \ `1 2 4 5` $\implies$ **Output:** `3`

##### Bài 4.2.2 — Mặt Hàng Bán Chạy Nhất Ngày Tết
- **Bối cảnh:** Tìm mã hàng có doanh số bán ra cao nhất và số lượng bán tương ứng.
- **Input:** `5` \ `10 20 10 30 10` $\implies$ **Output:** `10 3`

---

### Bài 4.3 — Kỹ thuật đếm cặp bằng Bảng tần suất $\mathcal{O}(N)$

#### 1. Khái niệm & Thuật toán
- Đếm số cặp $(i, j)$ ($i < j$) có $A_i + A_j = S$ trong $\mathcal{O}(N)$:
  - Với mỗi $A_j$, số phần tử đứng trước có giá trị bù $S - A_j$ là `cnt[S - A_j]`.
  - Cộng `cnt[S - A_j]` vào tổng kết quả rồi mới gọi `cnt[A_j]++`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 4.3: Ghép Đôi Container Cân Bằng Trọng Tải**  
> **Bối cảnh:** Xe kéo rơ-moóc chuyên dụng vận chuyển đúng 2 container cùng lúc. Xe chỉ được phép lưu thông nếu tổng trọng tải của 2 container đúng bằng tải trọng chuẩn $S$.  
> **Nhiệm vụ:** Cho $N$ container tại bãi có trọng lượng $A_1, A_2, \dots, A_N$. Hãy đếm số cách ghép cặp 2 container $(i, j)$ có $i < j$ và $A_i + A_j = S$.  
> **Input:** `5 6` \ `1 5 3 3 5` $\implies$ **Output:** `3` (các cặp ghép được: cont 1 với cont 2, cont 1 với cont 5, và cont 3 với cont 4).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;

    vector<int> cnt(MAX_VAL + 1, 0);
    long long totalPairs = 0;

    for (int j = 0; j < n; j++) {
        int x;
        cin >> x;
        int comp = s - x;
        if (comp >= 0 && comp <= MAX_VAL) {
            totalPairs += cnt[comp];
        }
        cnt[x]++;
    }

    cout << totalPairs << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 4.3

##### Bài 4.3.1 — Ghép Đôi Đèn Trang Trí Cùng Loại
- **Bối cảnh:** Đếm số cặp bóng đèn có cùng mã công suất ($A_i = A_j$ với $i < j$).
- **Input:** `4` \ `1 2 1 1` $\implies$ **Output:** `3`

##### Bài 4.3.2 — Ghép Đôi Cùng Pha Đèn Giao Thông
- **Bối cảnh:** Đếm số cặp cảm biến $(i, j)$ có cùng số dư khi chia cho $K$ ($(A_i - A_j) \% K == 0$).
- **Input:** `5 3` \ `1 4 7 2 5` $\implies$ **Output:** `4`

---

### Bài 4.4 — Nguyên lý Dirichlet trong Tin học

#### 1. Khái niệm & Ứng dụng
- Nếu nhốt $N + 1$ con chim vào $N$ cái chuồng thì có ít nhất một chuồng chứa $\ge 2$ con chim.
- **Ứng dụng:** Mảng $N$ phần tử luôn tồn tại ít nhất một đoạn con liên tiếp có tổng chia hết cho $N$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 4.4: Lô Hàng Khuyến Mãi Chia Đều Cho N Cửa Hàng**  
> **Bối cảnh:** Xe chở $N$ kiện quà liên tiếp. Cần chọn một dãy các kiện quà liên tiếp từ vị trí $L$ đến $R$ sao cho tổng số quà chia đều được cho $N$ cửa hàng đại lý. Đề bài đảm bảo luôn tìm được ít nhất một đoạn thỏa mãn theo nguyên lý Dirichlet.  
> **Input:** `5` \ `2 3 7 1 4` $\implies$ **Output:** `2 4` (đoạn $[3, 7, 1]$ có tổng 11... đoạn $[3, 7]$ tổng 10 chia hết cho 5).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n + 1);
    vector<int> firstPos(n, -1);
    firstPos[0] = 0;

    long long currentPrefix = 0;
    int ansL = -1, ansR = -1;

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        currentPrefix += a[i];
        int rem = (currentPrefix % n + n) % n;

        if (firstPos[rem] != -1) {
            ansL = firstPos[rem] + 1;
            ansR = i;
            break;
        } else {
            firstPos[rem] = i;
        }
    }

    cout << ansL << " " << ansR << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 4.4

##### Bài 4.4.1 — Tìm Đoạn Con Có Tổng Chia Hết Cho K
- **Bối cảnh:** Cho mảng $N$ phần tử. Tìm một đoạn con liên tiếp có tổng chia hết cho $K$ ($K \le N$). In ra vị trí $L, R$ đầu tiên tìm được.
- **Input:** `4 3` \ `1 2 4 5` $\implies$ **Output:** `1 2` (đoạn [1, 2] có tổng 3 chia hết cho 3).

##### Bài 4.4.2 — Đếm Số Đoạn Con Có Tổng Chia Hết Cho 3
- **Bối cảnh:** Đếm số lượng đoạn con liên tiếp $[L, R]$ ($L \le R$) có tổng chia hết cho 3 bằng mảng đếm tần suất số dư tiền tố.
- **Input:** `3` \ `3 3 3` $\implies$ **Output:** `6`

---

### Bài 4.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 4.5.1 — Phổ Điểm Kỳ Thi Học Sinh Giỏi Tin Học Trẻ
- **Bối cảnh:** Tổng kết điểm của $N$ thí sinh thang điểm $0..10$. In số thí sinh đạt từng mức điểm.
- **Sample:** `5` \ `8 9 8 10 8` $\implies$ In phổ điểm từ 0 đến 10.

##### Bài 4.5.2 — Mã Khách Hàng Thân Thiết Độc Nhất
- **Bối cảnh:** Tìm mã khách hàng nhỏ nhất chỉ mua hàng đúng 1 lần duy nhất trong ngày.
- **Giới hạn:** $N \le 10^5, A_i \le 10^5$.

##### Bài 4.5.3 — Ký Tự Hiếm Nhất Trong Tệp Cấu Hình Máy Chủ
- **Bối cảnh:** Tìm chữ cái xuất hiện ít nhất một lần nhưng có tần suất thấp nhất trong xâu văn bản.

##### Bài 4.5.4 — Thống Kê Độ Tuổi Lao Động Khu Công Nghiệp
- **Bối cảnh:** Đếm số công nhân có độ tuổi trong khoảng $[L, R]$ bằng bảng tần suất.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 4.5.5 — Cặp Giao Dịch Bù Trừ Ngân Hàng Vietcombank
- **Bối cảnh:** Đếm số cặp giao dịch chuyển tiền $(i, j)$ có $A_i + A_j = K$ khi số tiền lên tới $10^6$.

##### Bài 4.5.6 — Cặp Chênh Lệch Tải Trọng Cầu Treo
- **Bối cảnh:** Đếm số cặp xe tải $(i, j)$ có độ chênh lệch trọng lượng đúng bằng $D$ ($A_i - A_j = D$).

##### Bài 4.5.7 — Ban Lãnh Đạo Đa Số 1/3
- **Bối cảnh:** Tìm tất cả các ứng viên nhận được nhiều hơn $\lfloor N / 3 \rfloor$ phiếu bầu.

##### Bài 4.5.8 — Ghép Đôi Giày Thể Thao Bitis Hunter
- **Bối cảnh:** Kiểm tra xem $2N$ chiếc giày có thể ghép thành $N$ đôi giày hoàn chỉnh cùng kích cỡ không.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 4.5.9 — Bộ Ba Đơn Hàng Cân Bằng Tài Chính (3-SUM $\mathcal{O}(N^2)$)
- **Bối cảnh:** Đếm số bộ ba $(i, j, k)$ có $A_i + A_j + A_k = S$ kết hợp vòng lặp và mảng tần suất.

##### Bài 4.5.10 — Đoạn Phim Quảng Cáo Chia Hết Cho K Khung Hình
- **Bối cảnh:** Đếm tổng số đoạn con liên tiếp có tổng độ dài chia hết cho $K$ bằng mảng đếm tần suất số dư.

##### Bài 4.5.11 — Ghép Đôi Bạn Cùng Tiến Cuộc Thi Robocon
- **Bối cảnh:** Có $N$ học sinh nam và $M$ học sinh nữ với kỹ năng lập trình $1..K$. Đếm số cách ghép 1 nam và 1 nữ cùng mức kỹ năng.

##### Bài 4.5.12 — Kiểm Tra Hai Chuỗi ADN Đảo Mã (Anagram)
- **Bối cảnh:** Kiểm tra hai xâu ký tự sinh học có cùng bảng tần suất các nucleotide hay không trong $\mathcal{O}(N)$.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Khởi tạo kích thước bảng đếm quá nhỏ gây tràn bộ nhớ | `MAX_VAL` luôn $\ge$ giá trị lớn nhất trong đề |
| Tràn số biến đếm cặp khi $N = 10^5$ | Biến đếm cặp `ans` bắt buộc phải là kiểu `long long` (vì $C_N^2 \approx 5 \times 10^9$) |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Sử dụng thành thạo mảng `cnt` đếm phân phối và tìm Max/Min tần suất. |
| **Vận dụng (Tầng B)** | Đếm cặp bằng nhau và cặp tổng bằng $S$ trong $\mathcal{O}(N)$ không lỗi tràn số. |
| **Thành thạo (Tầng C)** | Vận dụng nguyên lý Dirichlet và mảng đếm số dư giải bài toán đoạn con chia hết. |
