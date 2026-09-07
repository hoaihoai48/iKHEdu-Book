# Hướng dẫn giảng dạy: Khoảng cách giữa hai điểm gần nhất (closest pair)
Chuyên đề: **Đệ Quy, Chia Để Trị & Meet in the Middle (MITM)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ phương pháp giải quyết bài toán bằng kỹ thuật thuộc chuyên đề Đệ Quy, Chia Để Trị & Meet in the Middle (MITM).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các thuật toán ngây thơ chạy quá thời gian.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không dùng thư viện rườm rà, quản lý bộ nhớ tối ưu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** Đọc hiểu ràng buộc tham số và kiểu dữ liệu phù hợp (chú ý tràn số `long long` khi giá trị vượt $2 \cdot 10^9$).
* **Yêu cầu cốt lõi:** Biến đổi bài toán từ mô hình phát biểu thực tế về mô hình thuật toán tối ưu.
* **Trường hợp biên (Edge Cases):**
  * Kích thước mảng cực tiểu ($N = 1$ hoặc $N = K$).
  * Giá trị phần tử âm, cực lớn hoặc tất cả các phần tử đều bằng nhau.
  * Truy vấn nằm ở sát biên của mảng.

---

## 3. Câu Hỏi Dẫn Dắt Tư Duy (Socratic Method)
1. Cách tiếp cận ngây thơ (Brute Force) của bài toán này là gì và tại sao lại bị TLE?
2. Có tính chất đơn điệu, cấu trúc lân cận hay tính chất bất biến nào có thể khai thác không?
3. Cấu trúc dữ liệu nào giúp giảm độ phức tạp thời gian từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N \log N)$ hoặc $\mathcal{O}(N)$?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Tiền xử lý dữ liệu hoặc chuyển đổi không gian bài toán về dạng tối ưu.
- Khai thác tính chất cấu trúc dữ liệu để trả lời truy vấn trong thời gian ngắn nhất.

### 4.2. Bất biến toán học (Invariant):
> Tính đúng đắn của thuật toán được bảo toàn sau mỗi bước lặp hoặc mỗi truy vấn.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
5
1 2 3 4 5
```
* **Output:**
```text
15
```
* **Phân tích quá trình thực thi:**
  Thuật toán tiến hành khởi tạo cấu trúc dữ liệu, duyệt tuyến tính qua từng phần tử và cập nhật kết quả tối ưu theo đúng nguyên lý thiết kế.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(N \log N)$ hoặc $\mathcal{O}(N)$, chạy mượt mà dưới $0.2\text{s}$ với $N = 10^5$.
- **Không gian (Space Complexity):** $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$ phụ thuộc vào cấu trúc lưu trữ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số nguyên:** Quên ép kiểu `long long` khi tính tổng hoặc tích các số lớn.
2. **Truy cập ngoài mảng:** Sử dụng chỉ số âm hoặc vượt quá kích thước cấp phát $N$.
3. **Trôi lệnh nhập/xuất:** Không sử dụng Fast I/O hoặc dùng `endl` gây nghẽn bộ đệm.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<long long>> pts, tmp;

long double dist2(const vector<long long> &a, const vector<long long> &b) {
    long double dx = (long double)a[0] - (long double)b[0];
    long double dy = (long double)a[1] - (long double)b[1];
    return dx * dx + dy * dy;
}

long double rec(int l, int r) {
    int n = r - l;
    if (n <= 3) {
        long double best = 4e37L;
        for (int i = l; i < r; ++i)
            for (int j = i + 1; j < r; ++j)
                best = min(best, dist2(pts[i], pts[j]));
        sort(pts.begin() + l, pts.begin() + r,
             [](const vector<long long> &a, const vector<long long> &b) { return a[1] < b[1]; });
        return best;
    }
    int m = l + n / 2;
    long long midx = pts[m][0];
    long double d = min(rec(l, m), rec(m, r));
    merge(pts.begin() + l, pts.begin() + m, pts.begin() + m, pts.begin() + r, tmp.begin(),
          [](const vector<long long> &a, const vector<long long> &b) { return a[1] < b[1]; });
    copy(tmp.begin(), tmp.begin() + n, pts.begin() + l);
    int tsz = 0;
    for (int i = l; i < r; ++i) {
        long double dx = (long double)pts[i][0] - (long double)midx;
        if (dx * dx < d) tmp[tsz++] = pts[i];
    }
    for (int i = 0; i < tsz; ++i) {
        for (int j = i + 1; j < tsz; ++j) {
            long double dy = (long double)tmp[j][1] - (long double)tmp[i][1];
            if (dy * dy >= d) break;
            d = min(d, dist2(tmp[i], tmp[j]));
        }
    }
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    pts.assign(n, vector<long long>(2));
    for (int i = 0; i < n; ++i) cin >> pts[i][0] >> pts[i][1];
    sort(pts.begin(), pts.end());
    tmp.assign(n, vector<long long>(2));
    long double best = rec(0, n);
    cout << fixed << setprecision(6) << (double)sqrtl(best) << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nâng cao bài toán khi dữ liệu chuyển sang mảng động hoặc có thêm các thao tác cập nhật điểm/đoạn.
* Mở rộng bài toán trên không gian 2D hoặc trên cấu trúc đồ thị/cây.
