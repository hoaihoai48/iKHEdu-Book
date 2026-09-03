# Bài 10: Thư viện STL C++ nâng cao (Advanced C++ STL)

## 1. Khái niệm & bản chất của các cấu trúc dữ liệu STL nâng cao

Thư viện mẫu chuẩn C++ (Standard Template Library - STL) cung cấp các cấu trúc dữ liệu trừu tượng hiệu năng cao được xây dựng trên nền tảng **Cây đỏ-đen (Red-Black Tree)** và **Bảng băm (Hash Table)**:
* **`set` / `multiset` / `map`:** Cấu trúc cây tự cân bằng (Balanced BST), duy trì các phần tử luôn được sắp xếp có thứ tự, hỗ trợ thêm, xóa, tìm kiếm, tìm kiếm nhị phân (`lower_bound`, `upper_bound`) trong thời gian logarit $\mathcal{O}(\log N)$.
* **`unordered_set` / `unordered_map`:** Cấu trúc bảng băm (Hash Table), đạt độ phức tạp trung bình $\mathcal{O}(1)$ cho các thao tác tìm kiếm và thêm xóa (nhưng có thể suy biến về $\mathcal{O}(N)$ khi bị đụng độ băm).
* **`priority_queue` (Hàng đợi ưu tiên):** Cấu trúc đống nhị phân (Binary Heap), luôn duy trì phần tử lớn nhất (Max-Heap) hoặc nhỏ nhất (Min-Heap) ở đỉnh trong $\mathcal{O}(1)$, thêm và xóa trong $\mathcal{O}(\log N)$.
* **Tùy biến hàm so sánh (Custom Struct Comparator / Functor):** Tùy chỉnh trật tự sắp xếp phức tạp cho các cấu trúc dữ liệu STL.

---

## 2. Bảng so sánh cấu trúc & hiệu năng của các Container STL

| Container STL | Cấu Trúc Ngầm Định | Trật Tự Dữ Liệu | Thao Tác Thêm / Xóa / Tìm | Tìm Kiếm Nhị Phân (`lower_bound`) |
|---|---|---|:---:|:---:|
| `vector<T>` | Mảng động liên tiếp | Theo thứ tự chèn | $\mathcal{O}(1)$ cuối, $\mathcal{O}(N)$ giữa | Cần sort trước $\mathcal{O}(\log N)$ |
| `set<T>` | Cây đỏ-đen (Red-Black Tree) | Tăng dần, duy nhất | $\mathcal{O}(\log N)$ | `s.lower_bound(x)` trong $\mathcal{O}(\log N)$ |
| `multiset<T>` | Cây đỏ-đen | Tăng dần, cho phép trùng | $\mathcal{O}(\log N)$ | `ms.lower_bound(x)` trong $\mathcal{O}(\log N)$ |
| `unordered_set<T>` | Bảng băm (Hash Table) | Không có thứ tự | Trung bình $\mathcal{O}(1)$, xấu nhất $\mathcal{O}(N)$ | Không hỗ trợ |
| `priority_queue<T>` | Đống nhị phân (Max-Heap) | Phần tử cực trị ở đỉnh | `push/pop` $\mathcal{O}(\log N)$, `top` $\mathcal{O}(1)$ | Không hỗ trợ |

---

## 3. Tử huyệt lập trình: Bẫy xóa phần tử trong `multiset` & Bẫy `unordered_map`

> **Cảnh báo bẫy lỗi 1: BẪY XÓA TẤT CẢ PHẦN TỬ TRÙNG NHAU TRONG MULTISET**

> Trong `multiset<int> ms`, nếu viết `ms.erase(val)`, C++ sẽ **xóa sạch toàn bộ mọi phần tử có giá trị bằng `val`**!  
> **Cách xóa đúng duy nhất 1 phần tử:** Truyền vào iterator trỏ tới phần tử đó:
> ```cpp
> auto it = ms.find(val);
> if (it != ms.end()) {
>     ms.erase(it); // Chỉ xóa đúng 1 phần tử tại vị trí it
> }
> ```

> **Cảnh báo bẫy lỗi 2: BẪY TẤN CÔNG BẢNG BĂM (ANTI-HASH TEST / HASH COLLISION)**

> `unordered_map` mặc định trong `libstdc++` dùng hàm băm chia dư đơn giản, dễ bị các bộ test sinh đối kháng (Anti-hash tests) làm đụng độ băm khiến thời gian chạy tụt từ $\mathcal{O}(1)$ xuống $\mathcal{O}(N) \implies \text{TLE}$.  
> **Giải pháp:** Sử dụng Custom Hash kết hợp thời gian hệ thống (Chrono):
> ```cpp
> struct custom_hash {
>     static uint64_t splitmix64(uint64_t x) {
>         x += 0x9e3779b97f4a7c15;
>         x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
>         x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
>         return x ^ (x >> 31);
>     }
>     size_t operator()(uint64_t x) const {
>         static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
>         return splitmix64(x + FIXED_RANDOM);
>     }
> };
> unordered_map<long long, int, custom_hash> safe_map;
> ```

---

![Hai Heap duy trì Trung vị động](assets/l10_two_heaps_median_visual.svg)

## 4. Mẫu cài đặt chuẩn thi đấu: Duy trì trung vị

Bài toán: Cho một luồng số liên tục, sau mỗi số được thêm vào, hãy in ra trung vị của toàn bộ các số đã nhập.
* **Chiến lược 2 Heap:**
  - Max-Heap `left_heap` chứa nửa nhỏ hơn của dãy số.
  - Min-Heap `right_heap` chứa nửa lớn hơn của dãy số.
  - Duy trì kích thước: `left_heap.size()` luôn bằng `right_heap.size()` hoặc hơn đúng $1$ phần tử.
  - Trung vị luôn là `left_heap.top()`.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    priority_queue<int> left_heap; // Max-heap
    priority_queue<int, vector<int>, greater<int>> right_heap; // Min-heap

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;

        if (left_heap.empty() || x <= left_heap.top()) left_heap.push(x);
        else right_heap.push(x);

        // Cân bằng kích thước
        if (left_heap.size() > right_heap.size() + 1) {
            right_heap.push(left_heap.top());
            left_heap.pop();
        } else if (right_heap.size() > left_heap.size()) {
            left_heap.push(right_heap.top());
            right_heap.pop();
        }

        cout << left_heap.top() << " ";
    }
    cout << "\n";
    return 0;
}
```

---

## 5. Ranh giới áp dụng

| Mục Đích | Chọn Container Phù Hợp |
|---|---|
| Cần tập hợp phần tử duy nhất, liên tục tìm $\ge X$ | `set<T>` |
| Cần tập hợp có phần tử trùng lặp, liên tục lấy $\min/\max$ và xóa | `multiset<T>` |
| Chỉ cần đếm tần suất cực nhanh không cần thứ tự | `unordered_map<T, int, custom_hash>` |
| Liên tục tìm phần tử lớn nhất/nhỏ nhất, không cần tìm kiếm tùy ý | `priority_queue<T>` |

---

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Bẫy multiset erase — Syntax):
Lệnh nào sau đây xóa đúng MỘT phần tử có giá trị bằng $5$ trong `multiset<int> ms`?
- **A.** `ms.erase(5);`
- **B.** **[Đáp án đúng]** `ms.erase(ms.find(5));` (khi đã kiểm tra `ms.find(5) != ms.end()`).
- **C.** `ms.pop(5);`
- **D.** `ms.remove(5);`

> *Giải thích:* `ms.erase(5)` xóa tất cả các số 5. Muốn xóa 1 số phải xóa qua iterator `ms.find(5)`.

#### Câu 2 (Phương thức member lower_bound — Performance):
Khi tìm kiếm phần tử đầu tiên $\ge X$ trong `set<int> s`, cú pháp nào đạt độ phức tạp tối ưu $\mathcal{O}(\log N)$?
- **A.** `lower_bound(s.begin(), s.end(), x);`
- **B.** **[Đáp án đúng]** `s.lower_bound(x);`
- **C.** `binary_search(s.begin(), s.end(), x);`
- **D.** `find(s.begin(), s.end(), x);`

> *Giải thích:* `std::lower_bound` thông thường duyệt theo bước nhảy iterator tuần tự $\mathcal{O}(N)$ trên cây. Phương thức thành viên `s.lower_bound(x)` đi trực tiếp trên cây trong $\mathcal{O}(\log N)$.

---

## Ma trận bài tập thực hành (P0 → P5)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB2-L10-01` | **Quản Lý Tập Hợp Số Động (Set & Multiset)** | `P0` | $Q \le 10^5$, thêm/xóa/tìm kiếm | Thao tác `set/multiset` chuẩn |
| 02 | `CPPB2-L10-02` | **Đếm Tần Suất Giá Trị Bằng Safe Hash Map** | `P0` | $N \le 10^5, A_i \le 10^{18}$ | `unordered_map` với `custom_hash` |
| 03 | `CPPB2-L10-03` | **Nối Dây Tiết Kiệm Bằng Priority Queue** | `P1` | $N \le 10^5, L_i \le 10^6$ | Min-Heap `priority_queue` |
| 04 | `CPPB2-L10-04` | **Duy Trì Trung Vị Động (Running Median)** | `P1` | $N \le 2 \times 10^5$ | 2 Heap cân bằng kích thước |
| 05 | `CPPB2-L10-05` | **Tìm Phần Tử Kế Tiếp Nhỏ Nhất Lớn Hơn X** | `P2` | $Q \le 2 \times 10^5, X \le 10^9$ | `s.upper_bound(x)` trên `set` |
| 06 | `CPPB2-L10-06` | **Lập Lịch Phòng Họp Đa Năng (Meeting Rooms)** | `P2` | $N \le 10^5$, $[S_i, E_i] \le 10^9$ | Min-Heap theo dõi thời điểm kết thúc |
| 07 | `CPPB2-L10-07` | **Duy Trì K Phần Tử Lớn Nhất Trong Luồng Dữ Liệu** | `P2` | $N \le 10^6, K \le 1000$ | Min-Heap kích thước cố định $K$ |
| 08 | `CPPB2-L10-08` | **Tối Ưu Hóa Chi Phí Mua Cổ Phiếu Theo Thời Gian** | `P3` | $N \le 10^5, P_i \le 10^9$ | `multiset` duy trì trật tự giá trị |
| 09 | `CPPB2-L10-09` | **Hệ Thống Đặt Chỗ Rạp Chiếu Phim Tối Ưu** | `P3` | $N \le 10^5, M \le 10^9$ | `set<pair<int, int>>` quản lý đoạn trống |
| 10 | `CPPB2-L10-10` | **Đếm Số Phần Tử Phân Biệt Trong Mọi Cửa Sổ K** | `P3` | $N \le 2 \times 10^5, K \le N$ | `unordered_map` kết hợp Sliding Window |
| 11 | `CPPB2-L10-11` | **Hợp Nhất Các Đoạn Số Rời Rạc (Merge Intervals)** | `P4` | $N \le 10^5, [L_i, R_i] \le 10^9$ | `map` hoặc `set` quản lý các khoảng rời |
| 12 | `CPPB2-L10-12` | **Tìm Cặp Điểm Có Khoảng Cách Manhattan Nhỏ Nhất** | `P4` | $N \le 10^5$, tọa độ 2D | Sweep-line kết hợp `set` tìm kiếm lân cận |
| 13 | `CPPB2-L10-13` | **Hệ Thống Xếp Hạng Trực Tuyến Đa Tiêu Chí** | `P4` | $Q \le 10^5$, cập nhật điểm động | `set<CustomStruct>` với Strict Weak Ordering |
| 14 | `CPPB2-L10-14` | **Tối Ưu Phân Bổ Băng Thông Máy Chủ (Server Load Balancer)** | `P5` | $N, M \le 10^5$ | 2 `set` quản lý máy chủ bận và máy chủ rảnh |
| 15 | `CPPB2-L10-15` | **Duy Trì Tổng Của K Phần Tử Lớn Nhất Động** | `P5` | $Q \le 10^5$, thêm/xóa phần tử | 2 `multiset` cân bằng kích thước $K$ và tổng |
| 16 | `CPPB2-L10-16` | **Kỹ Thuật Small-to-Large Merging Trên STL Map** | `P5` | Cây $N \le 10^5$ đỉnh | Gộp `map` từ cây con lên gốc trong $\mathcal{O}(N \log^2 N)$ |
