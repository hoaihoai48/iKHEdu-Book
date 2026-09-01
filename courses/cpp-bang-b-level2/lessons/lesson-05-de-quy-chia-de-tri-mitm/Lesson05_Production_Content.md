# Chuyên đề 05: Đệ quy, chia để trị & kỹ thuật Meet in the Middle

## 1. Khái niệm & bản chất của phân rã không gian tìm kiếm

Đệ quy (Recursion) và Chia để trị (Divide and Conquer) là nền tảng tư duy cốt lõi trong khoa học máy tính: chia bài toán lớn thành các bài toán con đồng dạng có kích thước nhỏ hơn, giải quyết độc lập và kết hợp nghiệm.

Ở Level 2, ta khai thác bước nhảy vọt về tư duy tối ưu hóa:
* **Cây đệ quy & Định lý thợ (Master Theorem):** Phân tích chính xác chi phí thời gian của các hàm đệ quy phân nhánh $T(N) = a T(N/b) + \mathcal{O}(N^d)$.
* **Kỹ thuật Đếm nghịch thế (Inversion Count):** Vận dụng Merge Sort để đếm số cặp nghịch thế $i < j$ mà $A_i > A_j$ trong $\mathcal{O}(N \log N)$ (thay vì duyệt ngây thơ $\mathcal{O}(N^2)$).
* **Kỹ thuật Gặp nhau ở giữa (Meet in the Middle - MITM):** Khi không gian tìm kiếm là $2^N$ với $N = 40$ ($2^{40} \approx 10^{12} \implies \text{TLE}$), ta chia đôi tập hợp thành hai nửa $N/2 = 20$. Duyệt hai nửa độc lập ($2 \times 2^{20} \approx 2 \times 10^6$) rồi dùng Two Pointers / Binary Search để ghép nghiệm $\implies$ **Giảm độ phức tạp từ $\mathcal{O}(2^N)$ xuống $\mathcal{O}(2^{N/2} \log(2^{N/2}))$.**

---

## 2. Kỹ thuật đếm số cặp nghịch thế bằng Merge Sort

### 2.1. Bản chất toán học

Trong quá trình trộn (merge) hai nửa đã sắp xếp $[L \dots mid]$ và $[mid+1 \dots R]$:
Nếu phần tử bên nửa phải $A[j]$ nhỏ hơn phần tử bên nửa trái $A[i]$ ($A[j] < A[i]$), thì do nửa trái đã tăng dần, $A[j]$ sẽ nhỏ hơn **tất cả các phần tử từ $i$ đến $mid$**.  
Số lượng cặp nghịch thế tạo bởi $A[j]$ chính là:
$$\Delta = mid - i + 1$$

```cpp
long long merge_and_count(vector<int> &a, int l, int mid, int r) {
    vector<int> left(a.begin() + l, a.begin() + mid + 1);
    vector<int> right(a.begin() + mid + 1, a.begin() + r + 1);
    int i = 0, j = 0, k = l;
    long long inv_count = 0;

    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            a[k++] = left[i++];
        } else {
            a[k++] = right[j++];
            inv_count += (left.size() - i); // Khai thác tính chất tăng dần
        }
    }
    while (i < left.size()) a[k++] = left[i++];
    while (j < right.size()) a[k++] = right[j++];
    return inv_count;
}
```

---

![Kỹ thuật Meet in the Middle](assets/l05_mitm_split_visual.svg)

## 3. Kỹ thuật Meet in the Middle

### 3.1. Bài toán Knapsack với $N \le 40$ và $W \le 10^{18}$

* Không thể dùng Quy hoạch động vì $W = 10^{18}$ quá lớn.
* Không thể duyệt nhánh cận toàn phần vì $2^{40} \approx 10^{12}$ quá lớn.

### 3.2. Thuật toán 3 bước MITM
1. **Nửa 1 ($N_1 = 20$):** Sinh tất cả $2^{20}$ tổng tập con, lưu vào `vector<long long> sum1`. Sắp xếp và lọc bỏ các trạng thái không tối ưu.
2. **Nửa 2 ($N_2 = 20$):** Sinh tất cả $2^{20}$ tổng tập con, lưu vào `vector<long long> sum2`.
3. **Ghép nghiệm:** Với mỗi giá trị $S \in sum2$, tìm giá trị lớn nhất trong $sum1$ mà $\le W - S$ bằng `upper_bound` trong $\mathcal{O}(\log(2^{N_1}))$.

---

## 4. Mẫu cài đặt chuẩn thi đấu: Meet in the Middle

```cpp
#include <bits/stdc++.h>
using namespace std;

void generate_sums(int idx, int end_idx, long long current_sum, const vector<long long> &a, vector<long long> &res) {
    if (idx == end_idx) {
        res.push_back(current_sum);
        return;
    }
    generate_sums(idx + 1, end_idx, current_sum, a, res);            // Không chọn
    generate_sums(idx + 1, end_idx, current_sum + a[idx], a, res);    // Có chọn
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long w;
    if (!(cin >> n >> w)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int mid = n / 2;
    vector<long long> sum1, sum2;
    generate_sums(0, mid, 0, a, sum1);
    generate_sums(mid, n, 0, a, sum2);

    sort(sum2.begin(), sum2.end());

    long long max_weight = 0;
    for (long long s1 : sum1) {
        if (s1 <= w) {
            auto it = upper_bound(sum2.begin(), sum2.end(), w - s1);
            if (it != sum2.begin()) {
                --it;
                max_weight = max(max_weight, s1 + *it);
            }
        }
    }

    cout << max_weight << "\n";
    return 0;
}
```

---

## 5. Ranh giới áp dụng

| Phạm Vi $N$ | Thuật Toán Tối Ưu | Độ Phức Tạp |
|---|---|:---:|
| $N \le 20$ | Duyệt đệ quy / Bitmask toàn phần | $\mathcal{O}(2^N)$ |
| $N \le 40$ | Meet in the Middle (MITM) | $\mathcal{O}(2^{N/2} \log(2^{N/2}))$ |
| $N \le 10^5, W \le 10^5$ | Quy hoạch động Cái túi (DP Knapsack) | $\mathcal{O}(NW)$ |
| $N \le 10^5, W \le 10^{18}$ | Tham lam (nếu các phần tử chia hết) | $\mathcal{O}(N \log N)$ |

---

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Độ phức tạp MITM — Complexity):
Tại sao kỹ thuật Meet in the Middle lại hiệu quả khi $N = 40$?
- **A.** Vì nó giảm số phép tính từ $2^{40} \approx 10^{12}$ xuống $2 \times 2^{20} \approx 2 \cdot 10^6$.
- **B.** **[Đáp án đúng]** Chia đôi bài toán thành 2 nửa kích thước 20, duyệt độc lập mất $\mathcal{O}(2^{20})$ rồi ghép nghiệm bằng Binary Search, chạy tốt trong $0.2\text{s}$.
- **C.** Vì nó tự động chuyển sang giải bằng DP.
- **D.** Vì nó chỉ xét các số nguyên tố.

> *Giải thích:* $2^{20} \approx 1.05 \times 10^6$ phép tính, hoàn toàn nằm trong giới hạn $10^8$ phép tính/giây của máy chấm.

#### Câu 2 (Đếm nghịch thế — Inversion):
Tại sao Merge Sort lại đếm được số cặp nghịch thế trong $\mathcal{O}(N \log N)$?
- **A.** Vì khi trộn hai nửa tăng dần, nếu $A[j] < A[i]$ thì $A[j]$ nhỏ hơn toàn bộ các phần tử còn lại của nửa trái.
- **B.** **[Đáp án đúng]** Tận dụng tính chất có thứ tự của hai nửa con để đếm gộp $mid - i + 1$ cặp trong $\mathcal{O}(1)$ tại mỗi bước so sánh.
- **C.** Vì QuickSort không làm được điều này.
- **D.** Để tránh tràn số.

> *Giải thích:* Tính chất tăng dần của mảng con giúp đếm số lượng phần tử lớn hơn mà không cần duyệt tuyến tính từng cặp.

---

## Ma trận bài tập thực hành (P0 → P5)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB2-L05-01` | **Đếm Cặp Nghịch Thế (Inversion Count)** | `P0` | $N \le 10^5, A_i \le 10^9$ | Cài đặt Merge Sort đếm nghịch thế |
| 02 | `CPPB2-L05-02` | **Tháp Hà Nội Mở Rộng Nhiều Cột** | `P0` | $N \le 20, K = 3, 4$ cọc | Đệ quy chuyển đĩa tối ưu Frame-Stewart |
| 03 | `CPPB2-L05-03` | **Cái Túi Kích Thước Nhỏ (Knapsack $N \le 40$)** | `P1` | $N \le 40, W \le 10^{18}$ | Cài đặt Meet in the Middle cơ bản |
| 04 | `CPPB2-L05-04` | **Tập Con Có Tổng Gần S Nhất** | `P1` | $N \le 36, S \le 10^{15}$ | MITM kết hợp `lower_bound` |
| 05 | `CPPB2-L05-05` | **Giải Phương Trình $4$ Ẩn Tuyến Tính (4-Sum MITM)** | `P2` | $N \le 4000, A_i \le 10^9$ | Tách thành 2 cặp $(A+B)$ và $-(C+D)$ |
| 06 | `CPPB2-L05-06` | **Đếm Số Tập Con Có XOR Bằng K** | `P2` | $N \le 36, K \le 10^9$ | MITM với phép toán Bitwise XOR |
| 07 | `CPPB2-L05-07` | **QuickSelect Tìm Phần Tử Nhỏ Thứ K** | `P2` | $N \le 10^6, K \le N$ | Chia để trị tìm $K$-th trong thời gian trung bình $\mathcal{O}(N)$ |
| 08 | `CPPB2-L05-08` | **Khoảng Cách Giữa Hai Điểm Gần Nhất (Closest Pair 2D)** | `P3` | $N \le 10^5$, tọa độ 2D | Chia để trị trên mặt phẳng 2D $\mathcal{O}(N \log N)$ |
| 09 | `CPPB2-L05-09` | **Bẻ Khóa Mật Mã Đổi Dấu (Subset Sum with Signs)** | `P3` | $N \le 38, \sum \pm a_i = 0$ | MITM với 3 trạng thái mỗi phần tử (0, +1, -1) |
| 10 | `CPPB2-L05-10` | **Đếm Cặp $A_i > 2 A_j$ (Significant Inversions)** | `P3` | $N \le 10^5, A_i \le 10^9$ | Biến thể Merge Sort đếm cặp điều kiện nâng cao |
| 11 | `CPPB2-L05-11` | **Tổng Cấp Số Nhân Bằng Chia Để Trị** | `P4` | $A, N \le 10^{18}, M = 10^9+7$ | Phân rã $S_N = S_{N/2} \times (1 + A^{N/2})$ |
| 12 | `CPPB2-L05-12` | **Tối Ưu Hóa Tuyến Đường Đi Qua Đỉnh (Shortest Path MITM)** | `P4` | Đồ thị $N \le 40$, chi phí không âm | BFS 2 đầu gặp nhau ở giữa |
| 13 | `CPPB2-L05-13` | **Trò Chơi Xếp Gạch Đa Diện (15-Puzzle MITM)** | `P4` | Trạng thái $2^{44}$ | MITM kết hợp Hash Table nén bộ nhớ |
| 14 | `CPPB2-L05-14` | **Phân Chia Tập Hợp Thành Hai Nửa Có Tổng Bằng Nhau** | `P5` | $N \le 36, A_i \le 10^9$ | MITM kết hợp tối ưu hóa bộ nhớ RAM |
| 15 | `CPPB2-L05-15` | **Đếm Số Đoạn Con Có Tổng Nằm Trong $[L, R]$** | `P5` | $N \le 10^5, \vert A_i \vert \le 10^9$ | Chia để trị trên mảng tiền tố $\mathcal{O}(N \log N)$ |
| 16 | `CPPB2-L05-16` | **Chia Để Trị Trên Cây (Centroid Decomposition Cơ Bản)** | `P5` | Cây $N \le 10^5$ đỉnh | Tìm trọng tâm cây đệ quy chia để trị |
