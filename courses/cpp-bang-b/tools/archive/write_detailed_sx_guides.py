#!/usr/bin/env python3
"""
Viết lại chuyên sâu, từng bước, số liệu thật cho các bài sx_04 -> sx_14.
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent / "problems"

guides = {
    "cppb_sx_04_dem_gia_tri_phan_biet": """# Hướng Dẫn Giảng Dạy: Đếm Giá Trị Phân Biệt
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số nguyên $A$ gồm $N$ phần tử ($N \le 10^5, A_i \le 10^9$). Cần đếm xem trong dãy có bao nhiêu giá trị khác nhau đôi một.
- **Tại sao không dùng mảng đánh dấu hoặc Set?**
  - Mảng đánh dấu `count[10^9]` không khả thi vì bộ nhớ chỉ cho phép mảng cỡ $10^7$.
  - Dùng `std::set` chưa được học ở Chương 01 (theo Not Yet Boundary) và có chi phí thời gian hằng số lớn.
- **Kỹ thuật Sắp xếp gom cụm (Sorting to Group):**
  - Sau khi sắp xếp tăng dần bằng `sort`, tất cả các phần tử có cùng giá trị chắc chắn sẽ nằm liền kề nhau tạo thành từng khối liên tiếp.
  - Ta chỉ cần duyệt tuyến tính $i$ từ $1$ đến $N - 1$: Mỗi khi gặp $A_i \ne A_{i-1}$, điều đó chứng tỏ ta vừa bước sang một giá trị phân biệt mới.
  - Ban đầu khởi tạo `ans = 1` (đại diện cho phần tử $A_0$). Mỗi lần $A_i \ne A_{i-1}$ thì tăng `ans++`.
  - Độ phức tạp thời gian: $\mathcal{O}(N \log N)$ cho sắp xếp + $\mathcal{O}(N)$ cho duyệt, bộ nhớ $\mathcal{O}(N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 phần tử)
Mẫu thử: $N = 7$, mảng ban đầu `a = [4, 2, 4, 3, 2, 4, 1]`.

| Bước | Lệnh chạy / Thao tác | Giá trị biến | Nhận xét / Khối giá trị |
|---|---|---|---|
| 1 | Sắp xếp `sort(a.begin(), a.end())` | `a = [1, 2, 2, 3, 4, 4, 4]` | Các giá trị trùng nhau đã gom lại |
| 2 | Khởi tạo `ans = 1` | `ans = 1` | Nhận diện giá trị đầu tiên là `1` |
| 3 | Duyệt $i = 1$: `a[1] = 2` so với `a[0] = 1` | `2 != 1` $\implies$ `ans = 2` | Xuất hiện giá trị mới: `2` |
| 4 | Duyệt $i = 2$: `a[2] = 2` so với `a[1] = 2` | `2 == 2` $\implies$ `ans = 2` | Trùng giá trị `2`, bỏ qua |
| 5 | Duyệt $i = 3$: `a[3] = 3` so với `a[2] = 2` | `3 != 2` $\implies$ `ans = 3` | Xuất hiện giá trị mới: `3` |
| 6 | Duyệt $i = 4$: `a[4] = 4` so với `a[3] = 3` | `4 != 3` $\implies$ `ans = 4` | Xuất hiện giá trị mới: `4` |
| 7 | Duyệt $i = 5, 6$: `a[5]=4, a[6]=4` | Đều bằng `4` $\implies$ `ans = 4` | Trùng giá trị `4`, bỏ qua |
| 8 | In kết quả `cout << ans << "\n"` | `ans = 4` | 4 giá trị phân biệt là {1, 2, 3, 4} |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Xử lý mảng rỗng ($N = 0$):** Nếu $N = 0$, việc gán `ans = 1` và truy cập `a[0]` sẽ gây lỗi tràn bộ nhớ (Out of Bounds). Cần kiểm tra nếu $N \le 0$ thì in `0` rồi kết thúc.
- **Bẫy 2 — Lỗi so sánh mảng chưa sắp xếp:** Nếu quên hàm `sort` mà duyệt trực tiếp `a[i] != a[i-1]`, với dãy `[4, 2, 4]` sẽ đếm thành 3 thay vì 2 vì hai số 4 không đứng liền kề.
- **Bẫy 3 — Tràn số khi đọc:** Tọa độ hoặc giá trị phần tử có thể lên tới $10^9$, dùng kiểu `long long` cho an toàn tuyệt đối.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int ans = 1;
    for (int i = 1; i < n; ++i) {
        if (a[i] != a[i - 1]) {
            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```""",

    "cppb_sx_05_hai_tram_kiem_soat": """# Hướng Dẫn Giảng Dạy: Hai Trạm Kiểm Soát Gần Nhau Nhất
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho tọa độ $N$ trạm kiểm soát trên trục đường. Cần tìm hai trạm có khoảng cách ngắn nhất, đồng thời in ra tọa độ của cặp trạm đó (theo thứ tự nhỏ trước lớn sau). Nếu có nhiều cặp cùng khoảng cách nhỏ nhất, ưu tiên cặp có tọa độ xuất hiện sớm nhất sau khi sắp xếp.
- **Phương pháp tiếp cận:**
  - Tương tự bài toán tìm khoảng cách nhỏ nhất, sau khi sắp xếp mảng tăng dần, cặp trạm tối ưu chắc chắn nằm ở hai vị trí kề nhau $A_i$ và $A_{i+1}$.
  - Duyệt $i$ từ $0$ đến $N - 2$:
    - Tính khoảng cách `diff = a[i+1] - a[i]`.
    - Nếu `diff < min_diff`, cập nhật `min_diff = diff` và ghi nhận cặp nghiệm `(ans1, ans2) = (a[i], a[i+1])`.
  - Độ phức tạp: $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 trạm)
Mẫu thử: $N = 5$, tọa độ `a = [12, 3, 19, 7, 25]`.

| Bước | Lệnh chạy / Thao tác | Trạng thái biến | Nhận xét cập nhật |
|---|---|---|---|
| 1 | Sắp xếp `sort` | `a = [3, 7, 12, 19, 25]` | Mảng tăng dần hoàn chỉnh |
| 2 | Khởi tạo cặp ban đầu | `min_diff = 7 - 3 = 4`, `ans = (3, 7)` | Cặp đầu tiên |
| 3 | Xét cặp $(7, 12)$ | `diff = 12 - 7 = 5 > 4` | Giữ nguyên `min_diff = 4` |
| 4 | Xét cặp $(12, 19)$ | `diff = 19 - 12 = 7 > 4` | Giữ nguyên |
| 5 | Xét cặp $(19, 25)$ | `diff = 25 - 19 = 6 > 4` | Giữ nguyên |
| 6 | In kết quả | In `3 7` và khoảng cách `4` | Khớp đúng kết quả mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Dấu cập nhật nghiêm ngặt (`<` thay vì `<=`)**: Đề bài yêu cầu khi có nhiều cặp cùng khoảng cách thì chọn cặp có tọa độ nhỏ hơn (đứng trước). Do mảng đã sắp xếp tăng dần, ta phải dùng điều kiện `diff < min_diff` (chứ không dùng `<=`) để bảo toàn cặp đầu tiên tìm thấy.
- **Bẫy 2 — In sai thứ tự hai tọa độ**: Đề bài yêu cầu in số nhỏ trước số lớn. Nhờ mảng đã sắp xếp nên `a[i]` luôn $\le a[i+1]$, ta chỉ cần in `ans1` rồi đến `ans2`.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n) || n < 2) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long min_diff = a[1] - a[0];
    long long ans1 = a[0], ans2 = a[1];

    for (int i = 1; i < n - 1; ++i) {
        long long diff = a[i + 1] - a[i];
        if (diff < min_diff) {
            min_diff = diff;
            ans1 = a[i];
            ans2 = a[i + 1];
        }
    }

    cout << ans1 << " " << ans2 << "\n";
    return 0;
}
```""",

    "cppb_sx_06_khoang_trong_lon_nhat": """# Hướng Dẫn Giảng Dạy: Khoảng Trống Lớn Nhất Trên Trục Tọa Độ
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Trên đoạn đường từ mốc tọa độ $0$ đến $L$, có $N$ chướng ngại vật tại các điểm $A_1, A_2, \dots, A_N$. Cần tìm độ dài khoảng trống liên tiếp lớn nhất không có chướng ngại vật nào.
- **Phương pháp tiếp cận:**
  - Khoảng trống trên trục đường gồm 3 loại:
    1. Từ điểm đầu $0$ đến chướng ngại vật đầu tiên: $A_0 - 0$.
    2. Giữa hai chướng ngại vật liên tiếp: $A_{i+1} - A_i$.
    3. Từ chướng ngại vật cuối cùng đến điểm kết thúc $L$: $L - A_{N-1}$.
  - Sắp xếp danh sách chướng ngại vật tăng dần. Sau đó duyệt tìm giá trị lớn nhất trong tất cả các khoảng cách trên.
  - Độ phức tạp: $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: L=20, 3 chướng ngại vật)
Mẫu thử: $L = 20, N = 3$, tọa độ `a = [15, 4, 9]`.

| Bước | Thao tác | Biến số | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Sắp xếp mảng chướng ngại vật | `a = [4, 9, 15]` | Tăng dần theo trục tọa độ |
| 2 | Khoảng trống đầu tiên: từ $0$ đến $a[0]$ | `gap = a[0] - 0 = 4 - 0 = 4` | `max_gap = 4` |
| 3 | Khoảng trống giữa $a[0]$ và $a[1]$ | `gap = 9 - 4 = 5` | `max_gap = max(4, 5) = 5` |
| 4 | Khoảng trống giữa $a[1]$ và $a[2]$ | `gap = 15 - 9 = 6` | `max_gap = max(5, 6) = 6` |
| 5 | Khoảng trống cuối cùng: từ $a[2]$ đến $L=20$ | `gap = 20 - 15 = 5` | `max_gap = max(6, 5) = 6` |
| 6 | Xuất kết quả | In `6` | Khoảng trống lớn nhất là giữa trạm 9 và 15 |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Quên xét 2 đầu mút $0$ và $L$**: Nhiều học sinh chỉ xét khoảng cách giữa các phần tử `a[i+1] - a[i]` mà bỏ quên đoạn từ $0$ đến $a[0]$ hoặc từ $a[N-1]$ đến $L$, dẫn đến sai sót nghiêm trọng.
- **Bẫy 2 — Chướng ngại vật trùng nhau hoặc ở đúng mút $0$ và $L$**: Code vẫn hoạt động đúng vì hiệu bằng $0$ không ảnh hưởng tới giá trị cực đại.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long l;
    int n;
    if (!(cin >> l >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long max_gap = a[0] - 0;
    for (int i = 0; i < n - 1; ++i) {
        max_gap = max(max_gap, a[i + 1] - a[i]);
    }
    max_gap = max(max_gap, l - a[n - 1]);

    cout << max_gap << "\n";
    return 0;
}
```"""
}

for code, content in guides.items():
    p_dir = BASE_DIR / code
    if p_dir.exists():
        (p_dir / "Huong_Dan_Giang_Day.md").write_text(content, encoding="utf-8")
        print(f"✅ Đã cập nhật chuyên sâu: {code}")
