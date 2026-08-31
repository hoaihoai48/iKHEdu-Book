# Hướng Dẫn Giảng Dạy: Cặp Điểm Gần Nhất (Closest Pair of Points)
Chuyên đề: **Kỹ Thuật Chia Để Trị (Divide and Conquer)**

**Phân loại chuyên đề:** `Challenge`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Cặp Điểm Gần Nhất (Closest Pair of Points).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân rã bài toán thành 3 pha chuẩn mực: `Divide` $\to$ `Solve` $\to$ `Combine`.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, tối ưu bộ nhớ đệm).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: Số nguyên dương $N$ ($2 \le N \le 5 \cdot 10^4$).
- $N$ dòng tiếp theo: Mỗi dòng chứa 2 số nguyên $X_i, Y_i$ ($|X_i|, |Y_i| \le 10^9$).
* **Yêu cầu cốt lõi:** Cho $N$ điểm trên mặt phẳng tọa độ $2D$. Hãy tìm khoảng cách Euclidean nhỏ nhất giữa 2 điểm bất kỳ trong tập hợp bằng thuật toán Chia Để Trị $\mathcal{O}(N \log N)$ (chia đôi theo hoành độ và quét dải Strip $\le 7$ điểm).
* **Phân tích trường hợp biên:** Xử lý chính xác Base Case khi kích thước mảng thu nhỏ về $\le 1$ phần tử.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Làm thế nào để chia bài toán hiện tại thành các bài toán con độc lập có kích thước $N/2$?
2. Bước gộp (Combine) kết quả từ 2 nửa đòi hỏi những thao tác gì và độ phức tạp là bao nhiêu?
3. Tại sao kỹ thuật Chia Để Trị lại giúp giảm độ phức tạp so với duyệt vét cạn tuần tự?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Divide & Combine Invariant:** Đảm bảo tính đúng đắn được bảo toàn qua từng tầng gộp mảng.
* **Bộ nhớ đệm tái sử dụng:** Tránh cấp phát động liên tục trong hàm đệ quy để chống tràn bộ nhớ và TLE.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
4
0 0
1 1
2 4
3 1
```
* **Output:**
```text
2
```
* **Phân tích thực thi:** Khoảng cách giữa (0,0) và (1,1) là sqrt(2) -> bình phương bằng 2.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** $\Theta(N \log N)$
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\Theta(\log N)$ (Độ sâu tối đa: $\log_2 N$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\Theta(N)$
* **Ghi chú phân tích:** Chia đôi theo hoành độ X và quét dải Strip <= 7 điểm kề cạnh.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số 32-bit khi đếm nghịch thế hoặc tính tổng:** Luôn sử dụng kiểu dữ liệu `long long`.
2. **Bẫy bỏ sót trường hợp vắt ngang (Crossing):** Phải xét đầy đủ mọi khả năng giữa 2 nửa mảng.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    long long x, y;
};

long long distSq(const Point &p1, const Point &p2) {
    return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
}

long long closestPairRec(vector<Point> &pts, int l, int r) {
    if (r - l <= 3) {
        long long min_d = 4e18;
        for (int i = l; i <= r; ++i) {
            for (int j = i + 1; j <= r; ++j) {
                min_d = min(min_d, distSq(pts[i], pts[j]));
            }
        }
        sort(pts.begin() + l, pts.begin() + r + 1, [](const Point &a, const Point &b) {
            return a.y < b.y;
        });
        return min_d;
    }

    int mid = l + (r - l) / 2;
    long long mid_x = pts[mid].x;
    long long dl = closestPairRec(pts, l, mid);
    long long dr = closestPairRec(pts, mid + 1, r);
    long long d = min(dl, dr);

    vector<Point> temp(r - l + 1);
    merge(pts.begin() + l, pts.begin() + mid + 1, pts.begin() + mid + 1, pts.begin() + r + 1, temp.begin(), [](const Point &a, const Point &b) {
        return a.y < b.y;
    });
    for (int i = 0; i < (int)temp.size(); ++i) pts[l + i] = temp[i];

    vector<Point> strip;
    for (int i = l; i <= r; ++i) {
        if ((pts[i].x - mid_x) * (pts[i].x - mid_x) < d) {
            strip.push_back(pts[i]);
        }
    }

    for (int i = 0; i < (int)strip.size(); ++i) {
        for (int j = i + 1; j < (int)strip.size() && (strip[j].y - strip[i].y) * (strip[j].y - strip[i].y) < d; ++j) {
            d = min(d, distSq(strip[i], strip[j]));
        }
    }
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;
    sort(pts.begin(), pts.end(), [](const Point &a, const Point &b) {
        return a.x < b.x;
    });
    cout << closestPairRec(pts, 0, n - 1) << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Vận dụng tư duy phân rã không gian tìm kiếm sang các bài toán hình học và chuẩn bị bước đệm cho Quay lui & Nhánh cận (Lesson 12).
