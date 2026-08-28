# TÀI LIỆU GỐC — CHƯƠNG 11: TỔ HỢP CƠ BẢN VÀ CÁC QUY TẮC ĐẾM (BASIC COMBINATORICS)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững các quy tắc đếm cơ bản (Cộng, Nhân, Bù trừ), Hoán vị, Chỉnh hợp, Tổ hợp; áp dụng Tam giác Pascal và kỹ thuật tiền xử lý Giai thừa để giải các bài toán đếm cấu hình và phân phối trong tin học |
| Kiến thức cần có | Vòng lặp, mảng 2D, số học Modulo, lũy thừa nhanh |
| Phạm vi | Quy tắc cộng/nhân/bù trừ (PIE), Hoán vị $P_N$, Chỉnh hợp $A_N^K$, Tổ hợp $C_N^K$, Tam giác Pascal $\mathcal{O}(N^2)$, Bài toán chia kẹo Euler (Stars and Bars) |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Phân biệt và áp dụng đúng quy tắc cộng (các trường hợp rời nhau), quy tắc nhân (các bước liên tiếp) và nguyên lý bù trừ — `LO-01`.
2. Xây dựng Tam giác Pascal bằng quy hoạch động $\mathcal{O}(N^2)$ để tính $C_N^K$ khi không có nghịch đảo modulo — `LO-02`.
3. Áp dụng công thức Tổ hợp giải bài toán đếm đường đi trên lưới ô vuông — `LO-03`.
4. Vận dụng kỹ thuật "Đặt vách ngăn" (Stars and Bars) giải bài toán chia kẹo Euler phân phối đồ vật — `LO-04`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để đếm số lượng cách sắp xếp hoặc phân chia đồ vật có thể lên tới hàng tỷ trường hợp mà không cần phải sinh từng trường hợp?**

---

### Bài 11.1 — Các quy tắc đếm cơ bản: Cộng, Nhân và Bù trừ

#### 1. Khái niệm & Định lý
- **Quy tắc cộng:** Nếu công việc có thể thực hiện theo một trong 2 phương án rời nhau: phương án $A$ có $m$ cách, phương án $B$ có $n$ cách $\implies$ Tổng số cách là $m + n$.
- **Quy tắc nhân:** Nếu công việc gồm 2 công đoạn liên tiếp: công đoạn 1 có $m$ cách, ứng với mỗi cách đó công đoạn 2 có $n$ cách $\implies$ Tổng số cách là $m \times n$.
- **Nguyên lý bù trừ (PIE):** $|A \cup B| = |A| + |B| - |A \cap B|$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 11.1: Phân Luồng Xe Vận Tải Theo Biển Số**  
> **Bối cảnh:** Trạm kiểm soát giao thông có $N$ xe tải đi qua mang biển số từ $1$ đến $N$. Các xe có biển số chia hết cho $A$ hoặc chia hết cho $B$ được ưu tiên vào làn xanh.  
> **Nhiệm vụ:** Đếm số lượng xe tải được ưu tiên vào làn xanh trong đoạn $[1, N]$.  
> **Input:** `20 3 5` $\implies$ **Output:** `9` (các xe có biển số: 3, 5, 6, 9, 10, 12, 15, 18, 20).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

long long lcm(long long a, long long b) {
    return (a / gcd(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, a, b;
    if (!(cin >> n >> a >> b)) return 0;

    long long countA = n / a;
    long long countB = n / b;
    long long countAB = n / lcm(a, b);

    cout << countA + countB - countAB << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 11.1

##### Bài 11.1.1 — Đếm Số Vé Xe May Mắn Chia Hết Cho 3 Hoặc 7
- **Bối cảnh:** Đếm số lượng vé xe có số hiệu trong đoạn $[1, N]$ chia hết cho 3 hoặc 7 ($N \le 10^{12}$).
- **Input:** `30` $\implies$ **Output:** `13`

##### Bài 11.1.2 — Lựa Chọn Thực Đơn Dinh Dưỡng Bữa Sáng
- **Bối cảnh:** Căn tin trường học phục vụ $N$ món ăn chính và $M$ loại đồ uống. Mỗi học sinh chọn 1 món chính và 1 đồ uống. Tính số cách chọn thực đơn khác nhau.
- **Input:** `3 4` $\implies$ **Output:** `12`

---

### Bài 11.2 — Hoán vị, Chỉnh hợp và Tổ hợp

#### 1. Định nghĩa & Công thức
- **Hoán vị:** $P_N = N!$.
- **Chỉnh hợp chập $K$:** $A_N^K = \frac{N!}{(N-K)!}$.
- **Tổ hợp chập $K$:** $C_N^K = \frac{N!}{K!(N-K)!}$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 11.2: Bầu Chọn Ban Chấp Hành Đoàn Trường**  
> **Bối cảnh:** Từ danh sách $N$ ứng viên, cần chọn ra 1 Bí thư, 1 Phó bí thư và 1 Ủy viên thường vụ (3 vị trí có phân biệt vai trò $\implies$ Chỉnh hợp $A_N^3$).  
> **Input:** `5` $\implies$ **Output:** `60` ($A_5^3 = 5 \times 4 \times 3 = 60$).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    long long ans = 1;
    for (int i = 0; i < k; i++) {
        ans = (ans * (n - i)) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 11.2

##### Bài 11.2.1 — Xếp Hàng Chụp Ảnh Kỷ Yếu Lớp Học
- **Bối cảnh:** Có $N$ học sinh đứng thành một hàng dọc để chụp ảnh. Tính số cách xếp hàng khác nhau $N! \pmod{10^9+7}$.
- **Input:** `4` $\implies$ **Output:** `24`

##### Bài 11.2.2 — Chọn Đội Hình Thi Đấu Robocon 3 Thành Viên
- **Bối cảnh:** Chọn 3 học sinh từ $N$ ứng viên để tham gia giải Robocon (không phân biệt vai trò). Tính $C_N^3 \pmod{10^9+7}$.
- **Input:** `5` $\implies$ **Output:** `10`

---

### Bài 11.3 — Tam giác Pascal và Tiền xử lý Tổ hợp $\mathcal{O}(N^2)$

#### 1. Hệ thức Pascal
- $C_N^K = C_{N-1}^{K-1} + C_{N-1}^K$ với $C_N^0 = C_N^N = 1$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 11.3: Sinh Bảng Tổ Hợp Bằng Tam Giác Pascal**  
> **Bối cảnh:** Lập bảng tổ hợp $C_N^K$ modulo $10^9+7$ cho $N \le 2000$ khi thực hiện $Q$ truy vấn thời gian thực.  
> **Input:** `5 2` $\implies$ **Output:** `10`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 2000;
const int MOD = 1000000007;

int c[MAX_N + 1][MAX_N + 1];

void buildPascal() {
    for (int i = 0; i <= MAX_N; i++) {
        c[i][0] = 1;
        for (int j = 1; j <= i; j++) {
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    buildPascal();

    int n, k;
    if (!(cin >> n >> k)) return 0;

    cout << c[n][k] << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 11.3

##### Bài 11.3.1 — Tổng Các Hệ Số Khai Triển Nhị Thức Newton
- **Bối cảnh:** In tổng tất cả các phần tử trên hàng thứ $N$ của Tam giác Pascal: $\sum_{K=0}^N C_N^K = 2^N \pmod{10^9+7}$.
- **Input:** `3` $\implies$ **Output:** `8` ($1 + 3 + 3 + 1 = 8$).

##### Bài 11.3.2 — Truy Vấn Tổ Hợp Hàng Loạt Bằng Bảng Pascal
- **Bối cảnh:** Xây dựng bảng Pascal $2000 \times 2000$. Trả lời $Q$ truy vấn tính $C_N^K \pmod{10^9+7}$ trong $\mathcal{O}(1)$.
- **Input:** `1` \ `5 2` $\implies$ **Output:** `10`

---

### Bài 11.4 — Đếm đường đi trên lưới và Bài toán chia kẹo Euler (Stars and Bars)

#### 1. Khái niệm & Công thức kinh điển
- **Đường đi trên lưới:** Số đường đi từ $(0, 0)$ đến $(N, M)$ chỉ đi sang phải và lên trên: $C_{N+M}^N$.
- **Bài toán chia kẹo Euler:**
  - Chia $N$ cái kẹo cho $K$ đứa trẻ sao cho mỗi người có ít nhất $1$ cái: $C_{N-1}^{K-1}$.
  - Chia $N$ cái kẹo cho $K$ đứa trẻ sao cho mỗi người có thể nhận $\ge 0$ cái: $C_{N+K-1}^{K-1}$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 11.4: Phân Phối Suất Học Bổng Cho Các Trường THPT**  
> **Bối cảnh:** Quỹ học bổng iKHEDU phân bổ $N$ suất học bổng cho $K$ trường THPT chuyên, mỗi trường nhận ít nhất $1$ suất.  
> **Input:** `5 3` $\implies$ **Output:** `6` ($C_{5-1}^{3-1} = C_4^2 = 6$).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long ans = 1;
    for (int i = 1; i <= r; i++) {
        ans = ans * (n - i + 1) / i;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    cout << nCr(n - 1, k - 1) << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 11.4

##### Bài 11.4.1 — Phân Bổ Phòng Thí Nghiệm Cho K Nhóm Nghiên Cứu
- **Bối cảnh:** Phân phối $N$ bộ máy vi tính cho $K$ nhóm nghiên cứu (có nhóm có thể nhận 0 bộ máy). Tính số phương án $C_{N+K-1}^{K-1}$.
- **Input:** `4 2` $\implies$ **Output:** `5`

##### Bài 11.4.2 — Đếm Số Nghiệm Nguyên Dương
- **Bối cảnh:** Đếm số bộ nghiệm nguyên dương $(x_1, x_2, x_3)$ thỏa mãn $x_1 + x_2 + x_3 = N$: $C_{N-1}^2$.
- **Input:** `6` $\implies$ **Output:** `10`

---

### Bài 11.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 11.5.1 — Tính Giai Thừa Số Lượng Đội Thi Đấu
- **Bối cảnh:** Tính $N! \pmod{10^9+7}$ với $N \le 10^6$.

##### Bài 11.5.2 — In Tam Giác Pascal N Hàng Đầu Tiên
- **Bối cảnh:** Xuất ma trận tam giác Pascal ra màn hình.

##### Bài 11.5.3 — Chọn Đại Biểu Đoàn Vận Động Viên iKHEDU
- **Bối cảnh:** Có $N$ học sinh nam và $M$ học sinh nữ. Chọn ra đoàn gồm 2 nam và 1 nữ. Tính số cách chọn.

##### Bài 11.5.4 — Đường Đi Của Robot Trong Kho Hàng 2D
- **Bối cảnh:** Tính số đường đi từ $(0, 0)$ đến $(N, M)$ trên lưới ô vuông.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 11.5.5 — Phân Bổ Kẹo Bánh Trung Thu Cho Lớp Học
- **Bối cảnh:** Chia $N$ gói quà cho $K$ học sinh sao cho mỗi học sinh nhận ít nhất 1 gói ($N, K \le 10^5$).

##### Bài 11.5.6 — Xếp Hàng Hành Khách Không Đứng Cạnh Nhau
- **Bối cảnh:** Có $N$ nam và $M$ nữ xếp thành hàng ngang sao cho không có 2 học sinh nữ nào đứng cạnh nhau.

##### Bài 11.5.7 — Lọc Mã Số Không Chia Hết Cho 2, 3, 5
- **Bối cảnh:** Áp dụng nguyên lý bù trừ cho 3 tập hợp đếm số lượng số trong đoạn $[1, N]$ không chia hết cho 2, 3 và 5.

##### Bài 11.5.8 — Đếm Tam Giác Tạo Từ N Điểm Cảm Biến
- **Bối cảnh:** Cho $N$ điểm trên mặt phẳng, không có 3 điểm nào thẳng hàng. Tính số tam giác có 3 đỉnh là các điểm đã cho: $C_N^3$.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 11.5.9 — Đường Đi Trong Mê Cung Có Ô Chướng Ngại Vật
- **Bối cảnh:** Đếm số đường đi từ $(0, 0)$ đến $(N, M)$ nhưng không được đi qua ô chướng ngại vật $(X, Y)$: $C_{N+M}^N - C_{X+Y}^X \times C_{(N-X)+(M-Y)}^{N-X}$.

##### Bài 11.5.10 — Bốc Thăm Đổi Quà Không Trùng Nhau (Derangements)
- **Bối cảnh:** Tính số cách trao $N$ món quà sao cho không ai nhận lại đúng món quà của mình ($D_N = (N-1)(D_{N-1} + D_{N-2})$).

##### Bài 11.5.11 — Phân Tích Số N Thành Tổng Đúng K Số Nguyên Dương
- **Bối cảnh:** Áp dụng kỹ thuật Stars and Bars đếm số nghiệm nguyên dương của phương trình $x_1 + x_2 + \dots + x_K = N$.

##### Bài 11.5.12 — Tổ Hợp Lucas Cho Khóa Mật Mã Siêu Lớn
- **Bối cảnh:** Tính $C_N^K \pmod P$ với modulo $P = 13$ và $N, K \le 10^{18}$.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Dùng công thức $N! / (K! (N-K)!)$ khi Modulo $M$ không phải số nguyên tố | Dùng Tam giác Pascal quy hoạch động cộng dồn |
| Nhầm lẫn giữa dạng 1 và dạng 2 của bài toán chia kẹo Euler | Kiểm tra kỹ điều kiện: mỗi người $\ge 1$ cái kẹo ($C_{N-1}^{K-1}$) hay $\ge 0$ cái kẹo ($C_{N+K-1}^{K-1}$) |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Xây dựng Tam giác Pascal và tính $C_N^K$ chính xác. |
| **Vận dụng (Tầng B)** | Áp dụng chia kẹo Euler và đếm đường đi trên lưới thành thạo. |
| **Thành thạo (Tầng C)** | Giải bài toán lưới có ô cấm và hoán vị mất tiêu chuẩn. |
