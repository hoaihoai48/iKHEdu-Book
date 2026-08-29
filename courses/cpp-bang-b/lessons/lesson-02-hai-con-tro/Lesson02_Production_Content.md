# KỸ THUẬT HAI CON TRỎ
## Tối Ưu Hóa Tìm Kiếm Tuyến Tính O(N) Trong C++

---

## 1. Khái Niệm & Nguyên Lý Hoạt Động

**Kỹ thuật Hai con trỏ (Two Pointers Technique)** là phương pháp sử dụng hai biến chỉ số (thường ký hiệu là $L$ và $R$) duyệt trên cấu trúc dữ liệu tuyến tính (mảng hoặc chuỗi) nhằm thu hẹp không gian tìm kiếm từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N)$.

Trong mô hình **Hai con trỏ đối đầu (Opposite-direction Two Pointers)**:
* Con trỏ trái $L$ khởi tạo tại đầu mảng ($L = 0$).
* Con trỏ phải $R$ khởi tạo tại cuối mảng ($R = N - 1$).
* Dãy số bắt buộc phải có **tính đơn điệu** (thường là mảng đã sắp xếp tăng dần $A_0 \le A_1 \le \dots \le A_{N-1}$).

Tại mỗi bước, thuật toán tính toán một hàm mục tiêu trên cặp phần tử $(A_L, A_R)$ (ví dụ: $\text{Sum} = A_L + A_R$) và so sánh với giá trị đích $S$:
* **Nếu $\text{Sum} == S$:** Tìm thấy nghiệm hợp lệ.
* **Nếu $\text{Sum} < S$:** Tổng hiện tại nhỏ hơn mục tiêu $\implies$ Tăng con trỏ trái (`++L`) để tìm kiếm tổng lớn hơn.
* **Nếu $\text{Sum} > S$:** Tổng hiện tại lớn hơn mục tiêu $\implies$ Giảm con trỏ phải (`--R`) để tìm kiếm tổng nhỏ hơn.

---

## 2. Chứng Minh Bất Biến Lặp (Loop Invariant) & Tính Đúng Đắn

### 2.1. Phát biểu Bất biến lặp
> **Bất biến lặp:** Tại bất kỳ thời điểm nào trong quá trình thực thi, nếu tồn tại một cặp nghiệm $(i, j)$ thỏa mãn $A_i + A_j = S$ ($i < j$), thì cặp nghiệm đó chắc chắn nằm trọn vẹn trong đoạn chỉ số đang xét: $L \le i < j \le R$.

### 2.2. Chứng minh quy nạp toán học
1. **Khởi tạo:** Ban đầu $L = 0, R = N - 1$, đoạn $[L, R]$ bao phủ toàn bộ mảng, bất biến lặp hiển nhiên đúng.
2. **Duy trì:** Giả sử bất biến lặp đúng tại bước hiện tại $[L, R]$.
   * **Trường hợp 1: $A_L + A_R > S$ (Thao tác `--R`):**  
     Vì mảng tăng dần, với mọi chỉ số $k \in [L, R-1]$, ta luôn có $A_k \ge A_L \implies A_k + A_R \ge A_L + A_R > S$.  
     Do đó, phần tử $A_R$ không thể tạo thành tổng $S$ với bất kỳ phần tử nào trong đoạn $[L, R-1]$. Việc loại bỏ $R$ bằng cách giảm $R \to R - 1$ không làm mất bất kỳ nghiệm hợp lệ nào.
   * **Trường hợp 2: $A_L + A_R < S$ (Thao tác `++L`):**  
     Vì mảng tăng dần, với mọi chỉ số $k \in [L+1, R]$, ta luôn có $A_k \le A_R \implies A_L + A_k \le A_L + A_R < S$.  
     Do đó, phần tử $A_L$ không thể tạo thành tổng $S$ với bất kỳ phần tử nào trong đoạn $[L+1, R]$. Việc loại bỏ $L$ bằng cách tăng $L \to L + 1$ là an toàn $100\%$.
3. **Kết thúc:** Vòng lặp dừng khi $L \ge R$. Nếu không tìm thấy nghiệm, chứng tỏ không tồn tại cặp $(i, j)$ nào thỏa mãn $A_i + A_j = S$.

---

## 3. Các Mô Hình Bài Toán Đặc Trưng

### 3.1. Mô hình 1: Tìm cặp số có tổng đúng bằng $S$ (Two Sum)
* **Mục tiêu:** Tìm $i < j$ sao cho $A_i + A_j = S$.
* **Quy tắc di chuyển:**
  $$\begin{cases} L \leftarrow L + 1 & \text{khi } A_L + A_R < S \\ R \leftarrow R - 1 & \text{khi } A_L + A_R > S \\ \text{Dừng thuật toán} & \text{khi } A_L + A_R = S \end{cases}$$

### 3.2. Mô hình 2: Đếm số cặp có tổng thỏa mãn bất đẳng thức $A_i + A_j \le S$
* **Mục tiêu:** Đếm số lượng cặp $(i, j)$ với $i < j$ thỏa mãn $A_i + A_j \le S$.
* **Khai thác tổ hợp:**  
  Nếu tại bước $(L, R)$ ta có $A_L + A_R \le S$, thì do mảng tăng dần, mọi phần tử $A_k$ với $L < k \le R$ khi ghép với $A_L$ đều thỏa mãn:
  $$A_L + A_k \le A_L + A_R \le S$$
  Do đó, có đúng **$R - L$ cặp hợp lệ** xuất phát từ $L$: $(L, L+1), (L, L+2), \dots, (L, R)$.
* **Thao tác:** Cộng $(R - L)$ vào kết quả đếm, sau đó tăng $L \leftarrow L + 1$. Ngược lại, nếu $A_L + A_R > S$, giảm $R \leftarrow R - 1$.

### 3.3. Mô hình 3: Ghép cặp cực trị tham lam (Bài toán Thuyền cứu hộ / Xe chở hàng)
* **Bài toán:** Mỗi xe chở tối đa 2 kiện hàng có tổng trọng lượng $\le C$. Tìm số xe ít nhất để chở hết $N$ kiện hàng.
* **Chiến lược:** Sắp xếp mảng trọng lượng tăng dần. Đặt $L = 0, R = N - 1$.
  * Thử ghép kiện nặng nhất $A_R$ với kiện nhẹ nhất $A_L$.
  * Nếu $A_L + A_R \le C$: Cả hai kiện đi chung xe $\implies L \leftarrow L + 1, R \leftarrow R - 1$.
  * Nếu $A_L + A_R > C$: Kiện $A_R$ buộc phải đi xe riêng $\implies R \leftarrow R - 1$.
  * Mỗi lần lặp tốn 1 xe (`++ans`).

### 3.4. Mô hình 4: Khử chiều đa biến (Bài toán 3-Sum và 4-Sum)
* **Bài toán 3-Sum:** Tìm bộ ba $(i, j, k)$ có tổng $A_i + A_j + A_k = S$.
* **Chiến lược:** Sắp xếp mảng. Cố định phần tử thứ nhất $i$ từ $0$ đến $N - 3$, chuyển bài toán về tìm 2 số trong đoạn $[i+1 \dots N-1]$ có tổng bằng $S - A_i$ bằng Two Pointers.
* **Độ phức tạp:** Giảm từ $\mathcal{O}(N^3)$ xuống $\mathcal{O}(N^2)$.

---

## 4. Phân Tích Độ Phức Tạp Thời Gian & Không Gian

* **Thời gian (Time Complexity):**
  * Bước sắp xếp: $\mathcal{O}(N \log N)$.
  * Bước duyệt Hai con trỏ: $\mathcal{O}(N)$ (do tại mỗi phép so sánh, ít nhất một trong hai con trỏ di chuyển 1 bước, tổng số bước di chuyển tối đa là $N$).
  * Tổng thời gian: $\mathcal{O}(N \log N + N) = \mathcal{O}(N \log N)$.
* **Không gian bộ nhớ (Space Complexity):**
  * $\mathcal{O}(1)$ bộ nhớ phụ trợ khi xử lý trực tiếp trên mảng (in-place).

---

## 5. Mẫu Cài Đặt Chuẩn Thi Đấu (Competitive Template)

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
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    // Bước 1: Sắp xếp mảng tạo tính đơn điệu O(N log N)
    sort(a.begin(), a.end());

    // Bước 2: Khởi tạo Hai con trỏ đối đầu O(N)
    int l = 0, r = n - 1;
    bool found = false;

    while (l < r) {
        long long current_sum = a[l] + a[r];
        if (current_sum == s) {
            cout << a[l] << " " << a[r] << "\n";
            found = true;
            break;
        } else if (current_sum < s) {
            ++l; // Tổng nhỏ hơn mục tiêu -> tăng giá trị cận dưới
        } else {
            --r; // Tổng lớn hơn mục tiêu -> giảm giá trị cận trên
        }
    }

    if (!found) {
        cout << -1 << "\n";
    }

    return 0;
}
```

---

## 6. Các Bẫy Lỗi Kỹ Thuật Thường Gặp (Bug Traps)

1. **Bẫy điều kiện dừng `l <= r` thay vì `l < r`:** Khi $L = R$, phần tử $A_L$ tự cộng với chính nó ($2 \cdot A_L$), vi phạm yêu cầu chọn hai vị trí phân biệt ($i < j$).
2. **Bẫy tràn số nguyên 32-bit:** Khi các phần tử $A_i \approx 10^9$, tổng $A_L + A_R$ có thể đạt $2 \cdot 10^9$, suýt soát giới hạn kiểu `int` ($2^{31}-1$). Bắt buộc sử dụng `long long` cho biến tính tổng.
3. **Bẫy mảng chưa sắp xếp:** Áp dụng Hai con trỏ trên mảng chưa có trật tự đơn điệu sẽ dẫn đến sai lệch logic hoàn toàn.

---

# CÂU HỎI TRẮC NGHIỆM ĐO LƯỜNG TƯ DUY (CONCEPT QUIZ)

#### Câu 1 (Nhận diện — Recognize):
Kỹ thuật hai con trỏ đối đầu ($L = 0, R = N - 1$) có thể áp dụng trực tiếp trên dãy số nào sau đây?
* A. Dãy số ngẫu nhiên ban đầu chưa qua xử lý.
* B. **(Đáp án đúng)** Dãy số đã được sắp xếp tăng dần hoặc giảm dần đơn điệu.
* C. Dãy số có tổng các phần tử bằng 0.
* D. Dãy số chỉ gồm toàn các số nguyên dương lẻ.
> *Giải thích:* Tính chất đơn điệu là điều kiện tiên quyết để việc dịch chuyển con trỏ không bỏ sót nghiệm. Do đó mảng bắt buộc phải có thứ tự đơn điệu.

---

#### Câu 2 (Dự đoán — Predict):
Cho mảng đã sắp xếp $A = [3, 7, 11, 15, 20]$ và mục tiêu $S = 22$. Tại bước khởi đầu với $L = 0$ ($A[0]=3$) và $R = 4$ ($A[4]=20$), tổng là $3 + 20 = 23 > 22$. Hành động đúng tiếp theo là gì?
* A. Tăng con trỏ trái $L = L + 1$.
* B. **(Đáp án đúng)** Giảm con trỏ phải $R = R - 1$ (đưa $R$ về vị trí 3 có giá trị 15).
* C. Dừng thuật toán và kết luận không có nghiệm.
* D. Hoán đổi giá trị của $A[L]$ và $A[R]$.
> *Giải thích:* Do tổng hiện tại lớn hơn mục tiêu $S$, phần tử lớn nhất $A[R]=20$ cộng với phần tử nhỏ nhất $A[L]=3$ đã vượt quá 22, nên 20 không thể ghép với bất kỳ số nào khác để tạo ra 22. Ta phải loại bỏ 20 bằng cách giảm $R$.

---

#### Câu 3 (Bản chất — Explain):
Trong bài toán đếm số cặp có $A_i + A_j \le S$ trên mảng tăng dần, khi $A[L] + A[R] \le S$, tại sao ta có thể khẳng định ngay có đúng $R - L$ cặp hợp lệ kết thúc tại $R$?
* A. Vì $R - L$ là độ dài của mảng ban đầu.
* B. **(Đáp án đúng)** Vì mảng tăng dần nên với mọi $k$ thỏa mãn $L < k \le R$, ta luôn có $A_L + A_k \le A_L + A_R \le S$.
* C. Vì hàm `std::sort` tự động nhóm các cặp này lại với nhau.
* D. Vì số lượng cặp luôn bằng hiệu hai con trỏ trong mọi bài toán.
> *Giải thích:* Do $A[L]$ đã thỏa mãn khi cộng với $A[R]$, tất cả các phần tử từ $L+1$ đến $R$ khi ghép với $A[L]$ đều có tổng $\le S$. Có đúng $R - L$ cặp như vậy xuất phát từ $L$.

---

#### Câu 4 (Chuyển giao — Transfer):
Độ phức tạp thời gian tổng thể của bài toán Two Sum gồm 2 bước: Sắp xếp mảng $N$ phần tử bằng `std::sort` rồi duyệt bằng Two Pointers là bao nhiêu?
* A. $\mathcal{O}(N^2)$
* B. $\mathcal{O}(N)$
* C. **(Đáp án đúng)** $\mathcal{O}(N \log N)$ (trong đó sắp xếp mất $\mathcal{O}(N \log N)$ và duyệt Two Pointers mất $\mathcal{O}(N)$).
* D. $\mathcal{O}(\log N)$
> *Giải thích:* Bước sắp xếp tốn $\mathcal{O}(N \log N)$, bước duyệt 2 con trỏ tốn $\mathcal{O}(N)$. Tổng thời gian bị chi phối bởi bước sắp xếp là $\mathcal{O}(N \log N)$, nhanh hơn vượt bậc so với vét cạn $\mathcal{O}(N^2)$.

---

#### Câu 5 (Bẫy điều kiện dừng — Bug Traps):
Tại sao trong vòng lặp Two Pointers tìm cặp phần tử phân biệt ($i < j$), ta bắt buộc phải dùng điều kiện `while (l < r)` thay vì `while (l <= r)`?
* A. Vì nếu dùng `<=` thì chương trình sẽ bị lỗi tràn bộ nhớ (Out of Memory).
* B. **(Đáp án đúng)** Vì khi $L = R$, phần tử $A[L]$ sẽ tự cộng với chính nó ($2 \cdot A[L]$), vi phạm yêu cầu chọn 2 vị trí phân biệt của đề bài.
* C. Vì trình biên dịch C++ không hỗ trợ toán tử `<=` trong vòng lặp `while`.
* D. Vì khi $L = R$ con trỏ sẽ nhảy về vị trí 0.
> *Giải thích:* Cặp nghiệm đòi hỏi 2 chỉ số khác nhau $i < j$. Khi $L = R$, hai con trỏ trỏ vào cùng 1 phần tử, không thể tạo thành một cặp 2 phần tử phân biệt.

---

#### Câu 6 (Chiến lược tham lam — Greedy Pairing):
Trong bài toán **Ghép thuyền cứu hộ** (mỗi thuyền chở tối đa 2 người có tổng cân nặng $\le C$), tại sao khi $W[L] + W[R] > C$, ta lại để người nặng nhất $W[R]$ đi thuyền riêng một mình?
* A. Vì người nặng nhất luôn có quyền ưu tiên đi một mình.
* B. **(Đáp án đúng)** Vì người nặng nhất $W[R]$ ghép với người nhẹ nhất hiện tại $W[L]$ mà vẫn bị quá tải, thì $W[R]$ không thể ghép được với bất kỳ ai khác $\implies$ Bắt buộc phải đi riêng.
* C. Vì ta muốn dành người nhẹ nhất $W[L]$ cho một người khác nặng hơn.
* D. Vì thuật toán muốn giảm số lượng thuyền xuống mức tối thiểu.
> *Giải thích:* Nếu người nhẹ nhất trong tập hợp còn lại mà không thể đi chung với $W[R]$, thì bất kỳ ai khác (đều có cân nặng $\ge W[L]$) khi đi cùng $W[R]$ cũng sẽ làm quá tải thuyền.

---

#### Câu 7 (Khử chiều đa biến — Dimensionality Reduction):
Đối với bài toán **3-Sum** (tìm 3 số $A_i + A_j + A_k = S$ với $i < j < k$), kỹ thuật Two Pointers giúp tối ưu hóa thuật toán như thế nào?
* A. Giảm từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N \log N)$.
* B. **(Đáp án đúng)** Cố định chỉ số $i$ bằng 1 vòng for ($\mathcal{O}(N)$), sau đó dùng Two Pointers trên đoạn $[i+1 \dots N-1]$ ($\mathcal{O}(N)$) để tìm $A_j + A_k = S - A_i$, giảm tổng thời gian từ $\mathcal{O}(N^3)$ xuống $\mathcal{O}(N^2)$.
* C. Chạy 3 con trỏ cùng lúc từ 3 đầu mảng trong $\mathcal{O}(N)$.
* D. Tính tổng tiền tố của 3 mảng con trong $\mathcal{O}(1)$.
> *Giải thích:* Bằng cách cố định 1 biến, bài toán 3 biến quy về bài toán Two Sum 2 biến trên đoạn còn lại, giúp giảm đúng 1 bậc lũy thừa của độ phức tạp thời gian.

---

#### Câu 8 (Xử lý trùng lặp — Duplicates Handling):
Khi mảng có nhiều phần tử bằng nhau (ví dụ: $[2, 2, 2, 2]$ và $S = 4$), để đếm chính xác số lượng cặp có tổng bằng $S$ mà không bị chạy $\mathcal{O}(N^2)$, ta xử lý như thế nào?
* A. Xóa bỏ tất cả các phần tử trùng lặp trước khi chạy.
* B. **(Đáp án đúng)** Đếm số lượng phần tử bằng nhau liên tiếp ở 2 đầu $L$ và $R$ (ví dụ có $cnt_L$ số bằng $A[L]$ và $cnt_R$ số bằng $A[R]$), sau đó cộng $cnt_L \times cnt_R$ vào kết quả (hoặc $\frac{cnt_L \times (cnt_L - 1)}{2}$ nếu $A[L] == A[R]$).
* C. Chỉ duyệt một lần và bỏ qua các số giống nhau.
* D. Dùng vòng lặp lồng nhau duyệt lại đoạn trùng.
> *Giải thích:* Nhân trực tiếp số lượng tần suất ở 2 đầu cho phép nhảy qua toàn bộ khối phần tử trùng lặp trong $\mathcal{O}(1)$, giữ nguyên độ phức tạp tuyến tính $\mathcal{O}(N)$.

---

#### Câu 9 (Hai mảng độc lập — Multi-array Pointers):
Cho 2 mảng đã sắp xếp tăng dần $A$ kích thước $N$ và $B$ kích thước $M$. Để tìm giá trị nhỏ nhất của $|A_i - B_j|$, thuật toán Hai con trỏ điều khiển con trỏ $i$ (trên $A$) và $j$ (trên $B$) như thế nào?
* A. Luôn tăng $i$ trước, sau đó tăng $j$.
* B. **(Đáp án đúng)** So sánh $A[i]$ và $B[j]$: Nếu $A[i] < B[j]$ thì tăng `++i`; nếu $A[i] > B[j]$ thì tăng `++j`; nếu bằng nhau thì khoảng cách bằng 0 (dừng lại).
* C. Đặt $i = 0$ và $j = M - 1$ rồi thu hẹp vào giữa.
* D. Tăng cả hai con trỏ `++i` và `++j` đồng thời tại mỗi bước.
> *Giải thích:* Muốn thu hẹp khoảng cách giữa $A[i]$ và $B[j]$, ta phải tăng phần tử có giá trị nhỏ hơn để nó tiến gần hơn đến giá trị của phần tử lớn hơn.

---

#### Câu 10 (Phòng thủ kiểu dữ liệu — Data Overflow):
Trong bài toán Two Sum với các phần tử mảng $A_i \in [1, 10^9]$ và $S = 2 \cdot 10^9$, phát biểu nào sau đây về kiểu dữ liệu là chính xác?
* A. Dùng kiểu `int` cho biến `sum = a[l] + a[r]` là hoàn toàn an toàn vì $2 \cdot 10^9 < 2^{31} - 1$.
* B. **(Đáp án đúng)** Biến `current_sum` và biến đếm số lượng cặp bắt buộc phải khai báo `long long` để phòng ngừa tràn số 32-bit (số lượng cặp có thể lên tới $\frac{N(N-1)}{2} \approx 5 \cdot 10^9$).
* C. Chỉ cần dùng kiểu `double` là giải quyết được mọi trường hợp.
* D. Không cần quan tâm kiểu dữ liệu vì compiler tự động ép kiểu 64-bit.
> *Giải thích:* Giá trị tổng $A[L] + A[R]$ có thể vượt ngưỡng $2^{31}-1$ khi các số lớn hơn $10^9$, và số lượng cặp đếm được với $N = 2 \cdot 10^5$ có thể đạt tới $2 \cdot 10^{10}$, bắt buộc phải dùng `long long` cho biến đếm.

---

# DANH SÁCH BÀI TẬP THỰC HÀNH

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-HCT-01` | **Mô Phỏng Hai Con Trỏ Đối Đầu** | `P0` | $N \le 10^5, A_i \le 10^9$ | Cơ chế co hẹp $L \to \leftarrow R$ |
| 02 | `CPPB-HCT-02` | **Cặp Số Có Tổng Bằng S (Two Sum)** | `P1` | $N \le 10^5, A_i \le 10^9$ | Sắp xếp + Hai con trỏ |
| 03 | `CPPB-HCT-03` | **Đếm Cặp Có Tổng Không Quá S** | `P2` | $N \le 2 \cdot 10^5, A_i \le 10^9$ | Cộng dồn tổ hợp đoạn $(R - L)$ |
| 04 | `CPPB-HCT-04` | **Đếm Cặp Có Tổng Lớn Hơn Hoặc Bằng S** | `P2` | $N \le 2 \cdot 10^5, A_i \le 10^9$ | Biến thể chặn dưới tổ hợp |
| 05 | `CPPB-HCT-05` | **Ghép Thuyền Cứu Hộ Tối Ưu** | `P3` | $N \le 10^5, C \le 10^9$ | Tham lam ghép cực trị |
| 06 | `CPPB-HCT-06` | **Vận Chuyển Thùng Hàng Cực Đại** | `P4` | $N \le 10^5, W_i \le 10^{12}$ | Ghép cặp với dữ liệu cực lớn |
| 07 | `CPPB-HCT-07` | **Tìm Cặp Có Tổng Gần S Nhất** | `P1` | $N \le 10^5, A_i \le 10^9$ | Tối ưu sai số tuyệt đối |
| 08 | `CPPB-HCT-08` | **Tìm Cặp Có Hiệu Đúng Bằng K** | `P2` | $N \le 10^5, K \le 10^{18}$ | Hai con trỏ truy vết hiệu |
| 09 | `CPPB-HCT-09` | **Bộ Ba Số Có Tổng Bằng S (3-Sum)** | `P3` | $N \le 3000, A_i \le 10^9$ | Cố định 1 phần tử + Two Pointers |
| 10 | `CPPB-HCT-10` | **Đếm Số Tam Giác Có Thể Tạo Thành** | `P3` | $N \le 3000, A_i \le 10^9$ | Cố định cạnh lớn nhất + Two Pointers |
| 11 | `CPPB-HCT-11` | **Đếm Cặp Tổng S Trên Mảng Trùng Lặp** | `P4` | $N \le 2 \cdot 10^5$ | Xử lý tần suất giá trị trùng nhau |
| 12 | `CPPB-HCT-12` | **Ghép Cặp Trẻ Em Và Bánh Quy** | `P4` | $N, M \le 10^5$ | Hai con trỏ trên 2 mảng khác nhau |
| 13 | `CPPB-HCT-13` | **Bộ Bốn Số Có Tổng Bằng S (4-Sum)** | `P5` | $N \le 1000$ | Cố định 2 phần tử + Two Pointers |
| 14 | `CPPB-HCT-14` | **Cặp Số Tối Ưu Với Chênh Lệch Cực Hạn** | `P5` | $N, M \le 2 \cdot 10^5$ | Tìm $\min \vert A_i - B_j \vert$ tuyến tính |
