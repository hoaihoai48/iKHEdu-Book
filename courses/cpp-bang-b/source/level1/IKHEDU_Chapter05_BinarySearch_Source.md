# TÀI LIỆU GỐC — CHƯƠNG 5: TÌM KIẾM NHỊ PHÂN (BINARY SEARCH)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững kỹ thuật chia đôi không gian tìm kiếm $\mathcal{O}(\log N)$, cài đặt tìm kiếm chính xác, tìm cận (Lower/Upper Bound) và Chặt nhị phân kết quả (Binary Search on Answer) để giải các bài toán tối ưu hóa trong tin học |
| Kiến thức cần có | Mảng đã sắp xếp (Sorting), vòng lặp `while`, hàm kiểm tra `bool check(long long mid)`, tính đơn điệu |
| Phạm vi | Tìm kiếm phần tử trên mảng đã sắp xếp, tìm vị trí biên Lower/Upper Bound, tìm căn bậc hai số lớn, chặt nhị phân kết quả tìm Min/Max tối ưu |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Giải thích nguyên lý chia đôi và cài đặt tìm kiếm nhị phân $\mathcal{O}(\log N)$ không bao giờ bị lặp vô hạn.
2. Tìm vị trí xuất hiện đầu tiên và cuối cùng của phần tử trùng nhau (Lower/Upper Bound).
3. Nhận diện tính chất đơn điệu của bài toán tối ưu và thiết kế hàm kiểm tra `bool check(mid)`.
4. Cài đặt thuật toán Chặt nhị phân kết quả tìm nghiệm tối ưu trong thời gian $\mathcal{O}(N \log(\text{range}))$.

### Câu hỏi trung tâm của chương

> **Làm thế nào để tìm được phương án tốt nhất trong một không gian có hàng tỷ khả năng mà chỉ cần kiểm tra tối đa $60$ lần**

---

### Bài 5.1 — Ý tưởng chia đôi và Tìm kiếm trên mảng đã sắp xếp

#### 1. Khái niệm & Nguyên lý chia đôi $\mathcal{O}(\log N)$
- **Điều kiện tiên quyết:** Dữ liệu bắt buộc phải được sắp xếp theo thứ tự tăng dần.
- **Nguyên lý:** Chia đôi đoạn tìm kiếm $[left, right]$ tại $mid = left + (right - left) / 2$. So sánh $A[mid]$ với $X$:
- Nếu $A[mid] == X$: Tìm thấy.
- Nếu $A[mid] < X$: Loại bỏ nửa trái, tìm bên phải ($left = mid + 1$).
- Nếu $A[mid] > X$: Loại bỏ nửa phải, tìm bên trái ($right = mid - 1$).
- **Độ phức tạp:** Giảm một nửa mỗi bước $\implies \mathcal{O}(\log N)$. Với $N = 10^9$ chỉ mất tối đa $\approx 30$ phép so sánh.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 5.1: Tra Cứu Điểm Thu Phí Tự Động VETC** 
> **Bối cảnh:** Trạm thu phí tự động không dừng VETC lưu trữ danh sách $N$ mã định danh thẻ RFID của các xe đã đăng ký tài khoản giao thông. Danh sách đã được sắp xếp tăng dần. 
> **Nhiệm vụ:** Khi một xe mang mã $X$ tiến vào làn thu phí, hệ thống cần kiểm tra xem mã $X$ có tồn tại trong cơ sở dữ liệu không và trả về vị trí chỉ số (0-based) để mở barrier trong thời gian dưới $0.001$ mili-giây. 
> 
> **Input:** 
> - Dòng 1: Hai số nguyên $N$ và $X$ ($1 \le N \le 10^6, -10^9 \le X \le 10^9$). 
> - Dòng 2: $N$ số nguyên đã sắp xếp tăng dần $A_0, A_1, \dots, A_{N-1}$ ($-10^9 \le A_i \le 10^9$). 
> 
> **Output:** 
> - Ghi chỉ số (0-based) của phần tử $X$. Nếu không tìm thấy, in `-1`. 
> 
> **Sample:** 
> - **Input:** 
> `6 7` 
> `1 3 5 7 9 11` 
> - **Output:** `3` 
> - **Giải thích:** Mã số $7$ nằm ở vị trí chỉ số 3 trong mảng.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int binarySearch(const vector<int> &a, int x) {
int left = 0, right = (int)a.size() - 1;
while (left <= right) {
int mid = left + (right - left) / 2;
if (a[mid] == x) {
return mid;
} else if (a[mid] < x) {
left = mid + 1;
} else {
right = mid - 1;
}
}
return -1;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, x;
if (!(cin >> n >> x)) return 0;

vector<int> a(n);
for (int i = 0; i < n; i++) cin >> a[i];

cout << binarySearch(a, x) << "\n";

return 0;
}
```

---

#### 3. Bẫy lỗi thường gặp
| Lỗi | Hậu quả | Cách tự kiểm tra |
|---|---|---|
| Tính `mid = (left + right) / 2` | Tràn số nguyên khi $left + right > 2 \times 10^9$ | Luôn dùng `mid = left + (right - left) / 2` |
| Quên `left = mid + 1` hoặc `right = mid - 1` | Vòng lặp bị lặp vô tận | Luôn tăng/giảm 1 đơn vị sau khi loại trừ `mid` |

---

#### 4. Bài tập thực hành Bài 5.1

##### Bài 5.1.1 — Tra Cứu Tài Khoản Ngân Hàng VietinBank
- **Bối cảnh:** Cơ sở dữ liệu chứa $N$ số tài khoản VIP đã sắp xếp. Có $Q$ giao dịch cần tra cứu xem số tài khoản $X$ có hợp lệ không.
- **Input:** Dòng 1 ghi $N, Q \le 10^5$. Dòng 2 ghi $N$ số tài khoản. $Q$ dòng tiếp theo mỗi dòng ghi số $X$.
- **Output:** Ghi `YES` nếu tìm thấy, ngược lại ghi `NO`.
- **Sample:** `5 2` \ `2 4 6 8 10` \ `6` \ `7` $\implies$ **Output:** `YES` \ `NO`

##### Bài 5.1.2 — Tìm Chuyến Bay Sớm Nhất Sau Giờ X
- **Bối cảnh:** Sân bay có $N$ chuyến bay khởi hành tại các mốc thời gian $A_1 < A_2 < \dots < A_N$. Tìm chuyến bay sớm nhất có giờ cất cánh $> X$.
- **Input:** `5 5` \ `1 3 5 7 9` $\implies$ **Output:** `7`

---

### Bài 5.2 — Tìm vị trí biên: Lower Bound và Upper Bound

#### 1. Khái niệm & Thuật toán
- **Lower Bound:** Vị trí đầu tiên có giá trị $\ge X$.
- **Upper Bound:** Vị trí đầu tiên có giá trị $> X$.
- **Đếm số lượng phần tử bằng $X$:** $\text{upper\_bound}(X) - \text{lower\_bound}(X)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 5.2: Thống Kê Số Lượng Vé Xem Ca Nhạc Theo Mệnh Giá** 
> **Bối cảnh:** Ban tổ chức liveshow bán $N$ vé xem ca nhạc với nhiều mệnh giá khác nhau, đã được sắp xếp tăng dần. 
> **Nhiệm vụ:** Em hãy đếm xem có bao nhiêu vé có đúng mệnh giá $X$ bằng thuật toán Lower Bound và Upper Bound. 
> **Input:** `7 5` \ `1 2 5 5 5 8 9` $\implies$ **Output:** `3` (có 3 vé mệnh giá 5).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int findLowerBound(const vector<int> &a, int x) {
int left = 0, right = (int)a.size() - 1, ans = a.size();
while (left <= right) {
int mid = left + (right - left) / 2;
if (a[mid] >= x) {
ans = mid;
right = mid - 1;
} else {
left = mid + 1;
}
}
return ans;
}

int findUpperBound(const vector<int> &a, int x) {
int left = 0, right = (int)a.size() - 1, ans = a.size();
while (left <= right) {
int mid = left + (right - left) / 2;
if (a[mid] > x) {
ans = mid;
right = mid - 1;
} else {
left = mid + 1;
}
}
return ans;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, x;
if (!(cin >> n >> x)) return 0;

vector<int> a(n);
for (int i = 0; i < n; i++) cin >> a[i];

cout << findUpperBound(a, x) - findLowerBound(a, x) << "\n";

return 0;
}
```

---

#### 3. Bài tập thực hành Bài 5.2

##### Bài 5.2.1 — Đếm Số Lô Hàng Trong Khoảng Trọng Tải $[L, R]$
- **Bối cảnh:** Đếm số kiện hàng có khối lượng trong đoạn $[L, R]$ từ danh sách $N$ kiện hàng đã sắp xếp.
- **Input:** `5 2` \ `1 3 5 7 9` \ `3 7` \ `4 6` $\implies$ **Output:** `3` \ `1`

##### Bài 5.2.2 — Tìm Vị Trí Đầu Tiên Và Cuối Cùng Của Cổ Phiếu X
- **Bối cảnh:** Tìm chỉ số 1-based xuất hiện đầu tiên và cuối cùng của mức giá $X$.
- **Input:** `5 3` \ `1 3 3 3 5` $\implies$ **Output:** `2 4`

---

### Bài 5.3 — Tìm căn bậc hai nguyên bằng Binary Search

#### 1. Khái niệm & Thuật toán
- Tìm số nguyên $K$ lớn nhất có $K^2 \le N$ với $N \le 10^{18}$ trên miền $[0, 10^9]$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 5.3: Quy Hoạch Công Viên Xanh Hình Vuông Ecopark** 
> **Bối cảnh:** Khu đô thị Ecopark dành quỹ đất $N$ mét vuông để xây dựng một quảng trường hình vuông có cạnh là số nguyên mét $K$. 
> **Nhiệm vụ:** Tìm độ dài cạnh $K$ lớn nhất sao cho diện tích $K \times K \le N$ ($N \le 10^{18}$). 
> **Input:** `20` $\implies$ **Output:** `4` (vì $4^2 = 16 \le 20 < 5^2 = 25$).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

long long integerSqrt(long long n) {
long long left = 0, right = 1000000000LL;
long long ans = 0;
while (left <= right) {
long long mid = left + (right - left) / 2;
if (mid * mid <= n) {
ans = mid;
left = mid + 1;
} else {
right = mid - 1;
}
}
return ans;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long n;
if (!(cin >> n)) return 0;

cout << integerSqrt(n) << "\n";

return 0;
}
```

---

#### 3. Bài tập thực hành Bài 5.3

##### Bài 5.3.1 — Kiểm Tra Lô Đất Chính Phương Lớn
- **Bối cảnh:** Kiểm tra xem diện tích lô đất $N \le 10^{18}$ có phải là số chính phương hoàn hảo không.
- **Input:** `1000000000000000000` $\implies$ **Output:** `YES`

##### Bài 5.3.2 — Dung Tích Bể Chứa Nước Lập Phương
- **Bối cảnh:** Tìm cạnh nguyên $K$ lớn nhất của bể nước lập phương có thể tích $K^3 \le N$ ($N \le 10^{18}$).
- **Input:** `30` $\implies$ **Output:** `3`

---

### Bài 5.4 — Chặt nhị phân kết quả (Binary Search on Answer)

#### 1. Dấu hiệu nhận biết & Thiết kế hàm `check(mid)`
- **Dấu hiệu:** Đề bài hỏi *"Tìm giá trị nhỏ nhất sao cho.."* hoặc *"Tìm giá trị lớn nhất thỏa mãn.."*.
- **Tính đơn điệu:** Nếu nghiệm $M$ thỏa mãn thì mọi $M' > M$ cũng thỏa mãn (hoặc ngược lại).

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 5.4: Khai Thác Gỗ Rừng Trồng Bền Vững (EKO)** 
> **Bối cảnh:** Công ty Lâm nghiệp Quốc gia quản lý $N$ cây gỗ có chiều cao $H_1, H_2, \dots, H_N$. Để chế biến theo hợp đồng xuất khẩu, công ty cần thu hoạch ít nhất $M$ mét gỗ. Máy cưa tự động được đặt ở độ cao $H$, mọi phần thân cây cao hơn $H$ sẽ bị cắt đứt để lấy gỗ. 
> **Nhiệm vụ:** Tìm độ cao đặt máy cưa $H$ lớn nhất có thể để vừa thu đủ ít nhất $M$ mét gỗ, vừa bảo tồn tối đa chiều cao phần thân cây còn lại. 
> 
> **Input:** 
> - Dòng 1: Hai số nguyên $N$ và $M$ ($1 \le N \le 10^6, 1 \le M \le 10^9$). 
> - Dòng 2: $N$ số nguyên $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^9$). 
> 
> **Output:** 
> - Ghi một số nguyên duy nhất là độ cao $H$ lớn nhất tìm được. 
> 
> **Sample:** 
> - **Input:** 
> `4 7` 
> `20 15 10 17` 
> - **Output:** `15` 
> - **Giải thích:** Cắt ở độ cao 15 thu được $(20-15) + (17-15) = 5 + 2 = 7$ mét gỗ $\ge 7$.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(const vector<int> &trees, long long m, int h) {
long long wood = 0;
for (int height : trees) {
if (height > h) {
wood += height - h;
}
}
return wood >= m;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
long long m;
if (!(cin >> n >> m)) return 0;

vector<int> trees(n);
int maxH = 0;
for (int i = 0; i < n; i++) {
cin >> trees[i];
maxH = max(maxH, trees[i]);
}

int left = 0, right = maxH, ans = 0;
while (left <= right) {
int mid = left + (right - left) / 2;
if (check(trees, m, mid)) {
ans = mid;
left = mid + 1;
} else {
right = mid - 1;
}
}

cout << ans << "\n";

return 0;
}
```

---

#### 3. Bài tập thực hành Bài 5.4

##### Bài 5.4.1 — Tải Trọng Tối Đa Tàu Container Cảng Quốc Tế
- **Bối cảnh:** Phân bổ $N$ kiện hàng liên tiếp vào tối đa $K$ chuyến tàu sao cho tải trọng của chuyến tàu nặng nhất là nhỏ nhất có thể.
- **Input:** `5 3` \ `1 2 3 4 5` $\implies$ **Output:** `6`

##### Bài 5.4.2 — Đặt Chuồng Bò An Toàn Tránh Dịch Bệnh (Aggressive Cows)
- **Bối cảnh:** Đặt $C$ con bò vào $N$ vị trí chuồng sao cho khoảng cách giữa hai con bò gần nhau nhất là lớn nhất.
- **Input:** `5 3` \ `1 2 8 4 9` $\implies$ **Output:** `3`

---

### Bài 5.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)
##### Bài 5.5.1 — Tra Cứu Mã Số Thuế Doanh Nghiệp
- **Bối cảnh:** Tìm kiếm mã $X$ trong danh sách đã sắp xếp.
##### Bài 5.5.2 — Điểm Trạm Dừng Xe Bus Gần Nhất
- **Bối cảnh:** Tìm vị trí trạm xe bus có tọa độ gần điểm $X$ nhất ($|A_i - X|$ nhỏ nhất).
##### Bài 5.5.3 — Căn Bậc Hai Số Lớn $10^{18}$
- **Bối cảnh:** Tính $\lfloor\sqrt{N}\rfloor$ bằng Binary Search.
##### Bài 5.5.4 — Đếm Số Học Sinh Trong Dải Điểm
- **Bối cảnh:** $Q$ truy vấn đếm số phần tử trong $[L, R]$.

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)
##### Bài 5.5.5 — Khai Thác Gỗ Rừng Trồng EKO
- **Bối cảnh:** Tìm độ cao cắt cây $H$ thu về tối thiểu $M$ mét gỗ.
##### Bài 5.5.6 — Phân Chia Dây Chuyền Sản Xuất VinFast
- **Bối cảnh:** Chia $N$ công đoạn cho $K$ kỹ sư sao cho thời gian làm việc nhiều nhất là nhỏ nhất.
##### Bài 5.5.7 — Bố Trí Trạm Tiếp Vận Cứu Hộ
- **Bối cảnh:** Đặt $C$ trạm cứu hộ vào $N$ vị trí tối đa hóa khoảng cách nhỏ nhất.
##### Bài 5.5.8 — Đếm Bộ Ba Cạnh Tam Giác
- **Bối cảnh:** Đếm số bộ ba $(A_i, A_j, A_k)$ tạo thành tam giác trong $\mathcal{O}(N^2 \log N)$.

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)
##### Bài 5.5.9 — Phân Phối Điện Năng Mặt Trời
- **Bối cảnh:** Chia mảng thành $K$ đoạn con liên tiếp sao cho tổng đoạn lớn nhất là nhỏ nhất.
##### Bài 5.5.10 — Phần Tử Thứ K Của Hai Danh Sách Giao Dịch
- **Bối cảnh:** Tìm phần tử nhỏ thứ $K$ của 2 mảng đã sắp xếp trong $\mathcal{O}(\log N)$.
##### Bài 5.5.11 — Bán Kính Phủ Sóng Trạm 5G Viettel
- **Bối cảnh:** Tìm bán kính phủ sóng nhỏ nhất để $M$ trạm 5G bao phủ toàn bộ $N$ hộ dân cư.
##### Bài 5.5.12 — Bảng Nhân Số Lớn $N \times M$
- **Bối cảnh:** Tìm số nhỏ thứ $K$ trong bảng cửu chương $N \times M$ ($N, M \le 10^5$).

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Lặp vô hạn do cập nhật `left = mid` | Luôn dùng `left = mid + 1` hoặc `right = mid - 1` |
| Giới hạn biến `right` trong chặt nhị phân kết quả quá nhỏ | Khởi tạo `right` đủ lớn (ví dụ tổng toàn mảng hoặc $10^{18}$) |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Cài đặt chính xác Binary Search và Lower/Upper Bound không lỗi lặp vô hạn. |
| **Vận dụng (Tầng B)** | Xác định đúng tính đơn điệu và cài đặt thành công Chặt nhị phân kết quả cho bài toán tối ưu. |
| **Thành thạo (Tầng C)** | Áp dụng Binary Search giải các bài toán trên bảng 2D và bài toán chia đoạn nâng cao. |
