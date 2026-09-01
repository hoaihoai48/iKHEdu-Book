# Chuyên đề 04: Kỹ thuật mảng: Hai con trỏ, Cửa sổ trượt, Mảng tiền tố & Mảng hiệu

## 1. Khái niệm & bản chất của tối ưu hóa tuyến tính trên mảng

Trong lập trình thi đấu, các kỹ thuật xử lý mảng như **Hai con trỏ (Two Pointers)**, **Cửa sổ trượt (Sliding Window)**, **Mảng tiền tố (Prefix Sum)**, **Mảng hiệu (Difference Array)** và **Nén tọa độ (Coordinate Compression)** là bộ công cụ nền tảng giúp chuyển đổi các thuật toán ngây thơ đa biến $\mathcal{O}(N^2)$ hoặc $\mathcal{O}(N \times Q)$ về độ phức tạp tối ưu tuyến tính $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$.

Ở Level 2, ta tập trung vào **Kỹ thuật kết hợp đa chiều & Mảng 2D**:
* **Hai con trỏ co giãn & Cửa sổ trượt linh hoạt:** Duy trì bất biến về tần suất, số lượng phần tử phân biệt hoặc tổng điều kiện khi kích thước cửa sổ thay đổi liên tục.
* **Mảng tiền tố 2D (2D Prefix Sum):** Trả lời truy vấn tính tổng hình chữ nhật con bất kỳ trên ma trận $N \times M$ trong $\mathcal{O}(1)$.
* **Mảng hiệu 2D (2D Difference Array):** Cập nhật cộng một giá trị lên toàn bộ vùng hình chữ nhật trong $\mathcal{O}(1)$ và khôi phục ma trận trong $\mathcal{O}(NM)$.
* **Nén tọa độ (Coordinate Compression):** Ánh xạ các giá trị rời rạc rất lớn ($A_i \le 10^9$) về dải chỉ số nhỏ liên tiếp $[1, N]$ mà vẫn bảo toàn hoàn toàn quan hệ thứ tự $A_i < A_j$.

---

![Sơ đồ 2D Prefix Sum](assets/l04_2d_prefix_sum_visual.svg)

## 2. Mảng tiền tố 2D

### 2.1. Công thức Mảng tiền tố 2D (2D Prefix Sum)

Định nghĩa: $pref[i][j]$ là tổng các phần tử trong hình chữ nhật từ góc trên-trái $(1, 1)$ đến $(i, j)$:
$$pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + A[i][j]$$

Truy vấn tổng hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$ trong $\mathcal{O}(1)$:
$$\text{Sum}(x_1, y_1, x_2, y_2) = pref[x_2][y_2] - pref[x_1-1][y_2] - pref[x_2][y_1-1] + pref[x_1-1][y_1-1]$$

### 2.2. Công thức Mảng hiệu 2D (2D Difference Array)

Để cộng thêm giá trị $V$ vào toàn bộ hình chữ nhật $[x_1, y_1] \to [x_2, y_2]$ trong $\mathcal{O}(1)$:
1. $diff[x_1][y_1] \mathrel{+}= V$
2. $diff[x_1][y_2 + 1] \mathrel{-}= V$
3. $diff[x_2 + 1][y_1] \mathrel{-}= V$
4. $diff[x_2 + 1][y_2 + 1] \mathrel{+}= V$

Sau khi thực hiện tất cả các cập nhật, chạy công thức Prefix Sum 2D trên mảng $diff$ để thu lại giá trị thực tế của ma trận.

---

## 3. Kỹ thuật nén tọa độ (Coordinate Compression)

### 3.1. Động lực & Cơ chế thực thi

Khi một bài toán có các giá trị tọa độ $X_i \in [-10^9, 10^9]$ nhưng số lượng điểm $N \le 10^5$, ta không thể dùng mảng đánh dấu kích thước $10^9$.  
Ta nén các giá trị này về tập $\{0, 1, \dots, K-1\}$ với $K \le N$:

```cpp
vector<int> vals = a;
sort(vals.begin(), vals.end());
vals.erase(unique(vals.begin(), vals.end()), vals.end());

// Tìm chỉ số đã nén (0-based) của a[i] trong O(log N)
for (int i = 0; i < n; ++i) {
    int compressed_val = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
}
```

---

## 4. Kỹ thuật hai con trỏ co giãn (Dynamic Sliding Window)

### 4.1. Bài toán: Tìm đoạn con ngắn nhất có tổng $\ge S$
Với mảng gồm các số nguyên dương $A_i > 0$:
* Khi mở rộng con trỏ phải $R$, tổng `current_sum` tăng ngặt.
* Khi `current_sum >= S`, ta thu hẹp con trỏ trái $L$ để tìm độ dài ngắn nhất thỏa mãn.

```cpp
int min_len = n + 1;
long long current_sum = 0;
int l = 0;

for (int r = 0; r < n; ++r) {
    current_sum += a[r];
    while (current_sum >= s) {
        min_len = min(min_len, r - l + 1);
        current_sum -= a[l];
        l++;
    }
}
```

---

## 5. Mẫu cài đặt chuẩn thi đấu: 2D Prefix Sum

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1, 0));
    vector<vector<long long>> pref(n + 1, vector<long long>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> a[i][j];
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + a[i][j];
        }
    }

    while (q--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        long long ans = pref[x2][y2] - pref[x1 - 1][y2] - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1];
        cout << ans << "\n";
    }
    return 0;
}
```

---

## 6. Ranh giới áp dụng

| Kỹ Thuật | Phạm Vi Sử Dụng | Độ Phức Tạp |
|---|---|:---:|
| **Two Pointers / Sliding Window** | Mảng 1D đơn điệu, tìm đoạn con thỏa mãn tính chất | $\mathcal{O}(N)$ |
| **2D Prefix Sum** | Truy vấn tổng ma trận con tĩnh | Tiền xử lý $\mathcal{O}(NM)$, truy vấn $\mathcal{O}(1)$ |
| **2D Difference Array** | Cập nhật cộng hình chữ nhật hàng loạt rồi mới truy vấn | Cập nhật $\mathcal{O}(1)$, khôi phục $\mathcal{O}(NM)$ |
| **Coordinate Compression** | Tọa độ lớn $10^9$ cần đưa về dải nhỏ để làm mảng đếm/cây | $\mathcal{O}(N \log N)$ |

---

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Công thức 2D Prefix Sum — Math):
Công thức truy vấn tổng vùng hình chữ nhật $[x_1, y_1] \to [x_2, y_2]$ trên mảng tiền tố 2D `pref` là:
- **A.** `pref[x2][y2] - pref[x1][y1]`
- **B.** **[Đáp án đúng]** `pref[x2][y2] - pref[x1-1][y2] - pref[x2][y1-1] + pref[x1-1][y1-1]`
- **C.** `pref[x2][y2] - pref[x1-1][y2-1]`
- **D.** `pref[x2][y2] + pref[x1][y1]`

> *Giải thích:* Phải trừ hai phần giao với các cạnh biên và cộng bù lại phần góc chung bị trừ 2 lần.

#### Câu 2 (2D Difference Array — Operations):
Để cộng giá trị $V$ vào hình chữ nhật $[x_1, y_1] \to [x_2, y_2]$, ta cần thay đổi bao nhiêu ô trên mảng hiệu 2D?
- **A.** $(x_2 - x_1 + 1) \times (y_2 - y_1 + 1)$ ô.
- **B.** **[Đáp án đúng]** Đúng 4 ô: $(x_1, y_1), (x_1, y_2+1), (x_2+1, y_1), (x_2+1, y_2+1)$.
- **C.** 2 ô.
- **D.** $N \times M$ ô.

> *Giải thích:* 4 điểm nút đại diện cho các biên bật/tắt của hình chữ nhật.

#### Câu 3 (Coordinate Compression — Space):
Nén tọa độ giúp ích gì khi các phần tử $A_i \in [-10^9, 10^9]$ với $N = 10^5$?
- **A.** Làm giảm giá trị của các số về $0$.
- **B.** **[Đáp án đúng]** Đưa các giá trị về tập chỉ số $[0, N-1]$ mà vẫn giữ nguyên thứ tự lớn bé, cho phép dùng làm chỉ số mảng hoặc cấu trúc cây.
- **C.** Tự động sắp xếp mảng giảm dần.
- **D.** Loại bỏ số âm.

> *Giải thích:* Ánh xạ về dải $[0, N-1]$ giúp tạo mảng đếm tần suất hoặc Segment Tree mà không bị tràn bộ nhớ.

---

## Ma trận bài tập thực hành (P0 → P5)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB2-L04-01` | **Truy Vấn Tổng Ma Trận Con 2D** | `P0` | $N, M \le 1000, Q \le 10^5$ | Cài đặt 2D Prefix Sum |
| 02 | `CPPB2-L04-02` | **Cập Nhật Hình Chữ Nhật Ma Trận 2D** | `P0` | $N, M \le 1000, Q \le 10^5$ | Cài đặt 2D Difference Array |
| 03 | `CPPB2-L04-03` | **Đoạn Con Ngắn Nhất Có Tổng $\ge S$** | `P1` | $N \le 10^5, A_i > 0, S \le 10^{14}$ | Cửa sổ trượt co giãn |
| 04 | `CPPB2-L04-04` | **Nén Tọa Độ & Đếm Tần Suất Trên Dải Lớn** | `P1` | $N \le 10^5, \vert X_i \vert \le 10^9$ | `sort` + `unique` + `lower_bound` |
| 05 | `CPPB2-L04-05` | **Đoạn Con Dài Nhất Có Không Quá K Số Khác Nhau** | `P2` | $N \le 2 \times 10^5, K \le N$ | Two pointers kết hợp mảng tần suất |
| 06 | `CPPB2-L04-06` | **Ma Trận Con Có Tổng Lớn Nhất (Maximum Submatrix Sum)** | `P2` | $N, M \le 400, \vert A_{i, j} \vert \le 10^9$ | Cố định 2 hàng + Thuật toán Kadane 1D |
| 07 | `CPPB2-L04-07` | **Diện Tích Phủ Bởi Các Hình Chữ Nhật Rời Rạc** | `P2` | $N \le 1000$, tọa độ $\le 10^9$ | Nén tọa độ 2D kết hợp mảng hiệu 2D |
| 08 | `CPPB2-L04-08` | **Đếm Cặp Đoạn Thẳng Chồng Lấn Nhau** | `P3` | $N \le 10^5, [L_i, R_i] \le 10^9$ | Nén tọa độ + Mảng hiệu 1D |
| 09 | `CPPB2-L04-09` | **Cửa Sổ Trượt Đếm Số Lượng Xâu Anagram** | `P3` | $\vert S \vert \le 10^6, \vert P \vert \le 10^5$ | Sliding window duy trì vector tần suất 26 chữ cái |
| 10 | `CPPB2-L04-10` | **Đếm Hình Vuông Con Có Tổng Đúng Bằng K** | `P3` | $N, M \le 1000, K \le 10^9$ | 2D Prefix Sum + Hai con trỏ trên đường chéo |
| 11 | `CPPB2-L04-11` | **Khử Chiều 3-Sum & 4-Sum Hai Con Trỏ** | `P4` | $N \le 5000, \vert A_i \vert \le 10^9$ | Khử chiều không gian từ $\mathcal{O}(N^3) \to \mathcal{O}(N^2)$ |
| 12 | `CPPB2-L04-12` | **Đếm Số Đoạn Con Có Hiệu Max - Min $\le K$** | `P4` | $N \le 2 \times 10^5, K \le 10^9$ | Two Pointers kết hợp 2 Deque đơn điệu |
| 13 | `CPPB2-L04-13` | **Đoạn Con Ngắn Nhất Chứa Đầy Đủ Bảng Chữ Cái** | `P4` | $\vert S \vert \le 10^6$ | Cửa sổ trượt co giãn duy trì biến đếm `unique_count` |
| 14 | `CPPB2-L04-14` | **Mảng Hiệu Trên Cây (Tree Difference Array)** | `P5` | $N, Q \le 10^5$ | Cập nhật cộng trọng số trên đường đi $(u, v)$ qua LCA |
| 15 | `CPPB2-L04-15` | **Đếm Tam Giác Có Độ Dài Cạnh Hợp Lệ** | `P5` | $N \le 5000, A_i \le 10^9$ | Two Pointers đếm tổ hợp bất đẳng thức tam giác |
| 16 | `CPPB2-L04-16` | **Quét Đường Thẳng Nén Tọa Độ (Sweep-line Area 2D)** | `P5` | $N \le 10^5$, hình chữ nhật lớn | Sweep-line kết hợp Segment Tree tính diện tích hợp |
