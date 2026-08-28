# TÀI LIỆU GỐC — CHƯƠNG 12: THƯ VIỆN CẤU TRÚC DỮ LIỆU STL C++ (STL CONTAINERS)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững và sử dụng thành thạo các cấu trúc dữ liệu dựng sẵn trong thư viện chuẩn C++ STL (`set`, `multiset`, `map`, `unordered_map`); kỹ thuật Nén tọa độ (Coordinate Compression) giải quyết bài toán mảng tần suất với giá trị lớn $10^9$ |
| Kiến thức cần có | Con trỏ/Iterator cơ bản, mảng, sắp xếp, tìm kiếm nhị phân |
| Phạm vi | `set`, `multiset`, `map`, `unordered_map`, bảng băm, Nén tọa độ (Coordinate Compression) |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Sử dụng `set` và `multiset` để duy trì tập hợp tự động sắp xếp và loại bỏ trùng lặp trong $\mathcal{O}(\log N)$ — `LO-01`.
2. Sử dụng `map` và `unordered_map` làm mảng tần suất với khóa bất kỳ (chuỗi ký tự, số âm, số lớn $10^9$) — `LO-02`.
3. Phân biệt được độ phức tạp và nguy cơ bị hack TLE của `unordered_map` ($\mathcal{O}(1)$ average vs $\mathcal{O}(N)$ worst-case) so với `map` ($\mathcal{O}(\log N)$ guaranteed) — `LO-03`.
4. Cài đặt kỹ thuật Nén tọa độ rời rạc hóa mảng giá trị lớn thành chỉ số $0..K-1$ trong $\mathcal{O}(N \log N)$ — `LO-04`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để đếm tần suất hoặc kiểm tra sự tồn tại khi giá trị của phần tử lên tới $10^9$ hoặc là xâu ký tự?**

---

### Bài 12.1 — Tập hợp tự sắp xếp: `set` và `multiset`

#### 1. Khái niệm & Thuật toán
- `std::set`: Cây đỏ đen, không trùng lặp, tự sắp xếp tăng dần, thao tác trong $\mathcal{O}(\log N)$.
- `std::multiset`: Cho phép trùng lặp. Xóa 1 phần tử an toàn bằng `ms.erase(ms.find(x))`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 12.1: Quản Lý Danh Sách Phòng Họp Trực Tuyến Zoom**  
> **Bối cảnh:** Hệ thống Zoom Meeting duy trì danh sách các phòng họp đang hoạt động có ID là các số nguyên lớn. Thực hiện $Q$ thao tác:  
> - `1 x`: Mở phòng họp mới mang ID $x$.  
> - `2 x`: Đóng phòng họp $x$.  
> - `3 x`: Kiểm tra phòng $x$ có đang mở không (in `YES`/`NO`).  
> **Input:** `5` \ `1 5` \ `1 10` \ `3 5` \ `2 5` \ `3 5` $\implies$ **Output:** `YES` \ `NO`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    set<long long> s;
    while (q--) {
        int type;
        long long x;
        cin >> type >> x;
        if (type == 1) s.insert(x);
        else if (type == 2) s.erase(x);
        else cout << (s.count(x) ? "YES\n" : "NO\n");
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 12.1

##### Bài 12.1.1 — Liệt Kê Các Mã Khách Hàng Khác Nhau
- **Bối cảnh:** Nhập danh sách $N$ mã số khách hàng ($N \le 10^5, A_i \le 10^9$). Hãy in ra số lượng mã phân biệt và danh sách các mã đó theo thứ tự tăng dần.
- **Input:** `5` \ `10 20 10 30 20` $\implies$ **Output:** `3` \ `10 20 30`

##### Bài 12.1.2 — Xóa Một Bản Sao Trong Multiset
- **Bối cảnh:** Nhập danh sách $N$ phần tử vào `multiset`. Thực hiện xóa đúng 1 phần tử có giá trị $X$ (không xóa tất cả các bản sao) và in kích thước còn lại.
- **Input:** `4 2` \ `2 2 3 4` $\implies$ **Output:** `3`

---

### Bài 12.2 — Ánh xạ khóa $\to$ giá trị: `std::map`

#### 1. Khái niệm & Thuật toán
- `std::map<Key, Value>`: Ánh xạ từ khóa bất kỳ sang giá trị trong $\mathcal{O}(\log N)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 12.2: Thống Kê Tần Suất Từ Khóa Tìm Kiếm Tiki**  
> **Bối cảnh:** Sàn thương mại điện tử Tiki thống kê số lần tìm kiếm của $N$ từ khóa và in danh sách theo thứ tự từ điển tăng dần.  
> **Input:** `4` \ `apple banana apple orange` $\implies$ **Output:** `apple 2`, `banana 1`, `orange 1`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    map<string, int> freq;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        freq[s]++;
    }

    for (auto entry : freq) {
        cout << entry.first << " " << entry.second << "\n";
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 12.2

##### Bài 12.2.1 — Tra Cứu Điểm Tổng Kết Học Sinh
- **Bối cảnh:** Nhập danh sách tên và điểm thi của $N$ học sinh. Sau đó thực hiện $Q$ truy vấn tra cứu điểm của học sinh theo tên.
- **Input:** `2 1` \ `An 9` \ `Binh 8` \ `An` $\implies$ **Output:** `9`

##### Bài 12.2.2 — Đếm Tần Suất Ký Tự Bằng Map
- **Bối cảnh:** Đếm số lần xuất hiện của từng từ trong đoạn văn bản tiếng Anh.
- **Input:** `apple banana apple` $\implies$ **Output:** `apple: 2, banana: 1`

---

### Bài 12.3 — Cấu trúc Bảng băm: `unordered_map`

#### 1. Khái niệm & So sánh
- `unordered_map`: Bảng băm $\mathcal{O}(1)$ trung bình.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 12.3: Tra Cứu Nhanh Mã Vận Đơn Bưu Điện**  
> **Bối cảnh:** Bưu điện lưu trữ $N$ mã vận đơn bằng `unordered_map` để tra cứu trạng thái bưu kiện trong $\mathcal{O}(1)$ thời gian thực.  
> **Input:** `2 1` \ `VN123 GiaoHang` \ `VN456 DaNhan` \ `VN123` $\implies$ **Output:** `GiaoHang`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    unordered_map<string, string> status;
    for (int i = 0; i < n; i++) {
        string code, stat;
        cin >> code >> stat;
        status[code] = stat;
    }

    while (q--) {
        string queryCode;
        cin >> queryCode;
        if (status.count(queryCode)) cout << status[queryCode] << "\n";
        else cout << "KhongTimThay\n";
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 12.3

##### Bài 12.3.1 — Đếm Số Cặp Có Tổng Bằng S Với Giá Trị Lớn
- **Bối cảnh:** Đếm số cặp $(i, j)$ có $i < j$ và $A_i + A_j = S$ khi $|A_i| \le 10^9$ bằng `unordered_map`.
- **Input:** `4 5` \ `1 4 4 1` $\implies$ **Output:** `4`

##### Bài 12.3.2 — Kiểm Tra Tồn Tại Siêu Tốc
- **Bối cảnh:** Thực hiện $Q$ truy vấn kiểm tra sự tồn tại của chuỗi ký tự bằng `unordered_set`.
- **Input:** `2 1` \ `abc def` \ `abc` $\implies$ **Output:** `YES`

---

### Bài 12.4 — Kỹ thuật Nén tọa độ (Coordinate Compression)

#### 1. Khái niệm & 3 bước rời rạc hóa
1. Copy mảng sang `vals`.
2. Sắp xếp và xóa trùng: `sort`, `unique`, `erase`.
3. Tìm thứ hạng bằng `lower_bound`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 12.4: Rời Rạc Hóa Tọa Độ Trạm Thu Phát Sóng 5G**  
> **Bối cảnh:** $N$ trạm 5G đặt tại các mốc tọa độ cực lớn $|A_i| \le 10^9$. Hãy nén tọa độ về khoảng $[0, K - 1]$ mà vẫn bảo toàn thứ tự tương đối.  
> **Input:** `5` \ `1000000000 5 1000000000 20 5` $\implies$ **Output:** `2 0 2 1 0`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n), vals;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        vals.push_back(a[i]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    for (int i = 0; i < n; i++) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
        cout << rank << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 12.4

##### Bài 12.4.1 — Nén Tọa Độ Tuyến Đường 1-Based
- **Bối cảnh:** Nén mảng $N$ tọa độ về các số nguyên bắt đầu từ 1 đến $K$.
- **Input:** `3` \ `100 500 200` $\implies$ **Output:** `1 3 2`

##### Bài 12.4.2 — Nén Tọa Độ Đầu Mút Đoạn Tuyến
- **Bối cảnh:** Cho $N$ đoạn thẳng $[L_i, R_i]$ với $L_i, R_i \le 10^9$. Hãy nén toàn bộ $2N$ đầu mút về miền $[1, M]$.
- **Input:** `2` \ `10 100` \ `50 200` $\implies$ **Output:** `4 diem: 1 3 2 4`

---

### Bài 12.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 12.5.1 — Đếm Số Loại Hàng Hóa Bằng Set
- **Bối cảnh:** Đếm số loại mã hàng phân biệt trong $N$ lượt mua hàng bằng `std::set`.

##### Bài 12.5.2 — Thống Kê Điểm Thi Thí Sinh Bằng Map
- **Bối cảnh:** Đếm tần suất xuất hiện của từng họ tên thí sinh trong danh sách.

##### Bài 12.5.3 — Nén Tọa Độ Mảng Số Nguyên Lớn
- **Bối cảnh:** Nén mảng $N$ số $|A_i| \le 10^9$ thành mảng các số nguyên từ $0$ đến $K-1$.

##### Bài 12.5.4 — Tra Cứu Mã Căn Cước Công Dân Bằng Unordered Set
- **Bối cảnh:** Thực hiện $Q$ truy vấn kiểm tra sự tồn tại của số CCCD trong cơ sở dữ liệu.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 12.5.5 — Tìm Trung Vị Luồng Dữ Liệu Liên Tục (Running Median)
- **Bối cảnh:** Quản lý luồng điểm số đến liên tục bằng 2 `multiset` (hoặc 2 `priority_queue`) để lấy trung vị trong $\mathcal{O}(\log N)$.

##### Bài 12.5.6 — Đếm Cặp Giao Dịch Chênh Lệch K Với Tiền Tỷ
- **Bối cảnh:** Dùng `map` đếm số cặp $(i, j)$ có $A_i - A_j = K$ khi $A_i \le 10^9$.

##### Bài 12.5.7 — Hàng Đợi Khách Hàng Đa Mức Ưu Tiên Xóa An Toàn
- **Bối cảnh:** Thao tác xóa đúng 1 bản sao trong `multiset` thông qua iterator `ms.erase(ms.find(x))`.

##### Bài 12.5.8 — Nén Tọa Độ Các Tuyến Đường Cao Tốc
- **Bối cảnh:** Nén các mốc đầu mút $[L_i, R_i]$ ($L_i, R_i \le 10^9$) để áp dụng mảng hiệu Difference Array.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 12.5.9 — Tự Thiết Kế Hàm Băm Custom Hash Chống Hack TLE
- **Bối cảnh:** Cài đặt `custom_hash` bằng `splitmix64` cho `unordered_map` trên hệ thống thi đấu.

##### Bài 12.5.10 — Diện Tích Hợp Các Khu Đô Thị Hình Chữ Nhật
- **Bối cảnh:** Nén tọa độ kết hợp thuật toán quét đường Line Sweep tính diện tích hợp các hình chữ nhật.

##### Bài 12.5.11 — Truy Vấn Mặt Hàng Giá Đắt Thứ K Trong Cửa Sổ Trượt
- **Bối cảnh:** Quản lý cửa sổ trượt độ dài $M$ bằng `multiset` và con trỏ iterator.

##### Bài 12.5.12 — Hệ Thống Phân Cấp Danh Mục Sản Phẩm Đa Tầng
- **Bối cảnh:** Quản lý cấu trúc dữ liệu `map<string, vector<string>>` biểu diễn cây thư mục.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Gọi `ms.erase(val)` trên `multiset` xóa sạch tất cả bản sao | Dùng `ms.erase(ms.find(val))` nếu chỉ muốn xóa 1 bản sao |
| Truy cập `mp[key]` làm tự động tạo phần tử rác nếu khóa chưa tồn tại | Dùng `mp.count(key)` hoặc `mp.find(key)` để kiểm tra trước |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Sử dụng chính xác `set`, `map` và nén tọa độ 1D. |
| **Vận dụng (Tầng B)** | Quản lý `multiset` và đếm cặp số lớn bằng bảng băm. |
| **Thành thạo (Tầng C)** | Làm chủ nén tọa độ kết hợp Line Sweep và custom hash. |
