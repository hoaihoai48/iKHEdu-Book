# Hướng Dẫn Giảng Dạy: Đếm Cặp Tổng S Trên Mảng Trùng Lặp
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ phương pháp giải quyết bài toán bằng kỹ thuật thuộc chuyên đề Kỹ Thuật Hai Con Trỏ (Two Pointers).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các vòng lặp lồng nhau $\mathcal{O}(N^2)$.
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
1. Mảng đã có thứ tự tăng dần chưa? Nếu chưa, cần tiền xử lý gì?
2. Khi tổng $A[L] + A[R]$ lớn hơn $S$, ta nên dịch con trỏ nào để giảm tổng?
3. Có bao nhiêu cặp thỏa mãn nếu $A[L] + A[R] \le S$?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Sắp xếp mảng để tạo tính đơn điệu.
- Đặt 2 con trỏ $L$ ở đầu và $R$ ở cuối mảng (đối đầu), hoặc cùng chạy từ đầu mảng.
- Tại mỗi bước, dựa vào mối quan hệ giữa tổng/hiệu hiện tại và mục tiêu để quyết định tăng $L$ hay giảm $R$ một cách đơn điệu.

### 4.2. Bất biến toán học (Invariant):
> Nếu $A[L] + A[R] > S$, vì mảng tăng dần nên $\forall k \ge L, A[k] + A[R] > S \implies$ phần tử $A[R]$ không thể ghép với bất kỳ số nào từ $L \dots R-1$, việc giảm $R$ là an toàn tuyệt đối và không bỏ sót nghiệm.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
6 6
3 3 3 3 3 3
```
* **Output:**
```text
15
```
* **Phân tích quá trình thực thi:**
  Thuật toán tiến hành khởi tạo cấu trúc dữ liệu, duyệt tuyến tính qua từng phần tử và cập nhật kết quả tối ưu theo đúng nguyên lý thiết kế.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(N \log N)$ (nếu cần sắp xếp) + $\mathcal{O}(N)$ duyệt 2 con trỏ $\implies \mathcal{O}(N \log N)$ tổng thể.
- **Không gian (Space Complexity):** $\mathcal{O}(1)$ bộ nhớ phụ trợ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. Quên sắp xếp mảng trước khi chạy Hai con trỏ đối đầu khiến điều kiện di chuyển $L/R$ bị sai logic.
2. Lỗi tràn số $A[L] + A[R] \ge 2 \cdot 10^9$ khi tính tổng hai số lớn.
3. Vòng lặp dừng không đúng (ví dụ $L \le R$ thay vì $L < R$ khi chọn 2 phần tử phân biệt).

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
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
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long ans = 0;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum == s) {
            if (a[l] == a[r]) {
                long long cnt = r - l + 1;
                ans += cnt * (cnt - 1) / 2;
                break;
            } else {
                long long c1 = 1, c2 = 1;
                while (l + 1 < r && a[l + 1] == a[l]) { ++c1; ++l; }
                while (r - 1 > l && a[r - 1] == a[r]) { ++c2; --r; }
                ans += c1 * c2;
                ++l;
                --r;
            }
        } else if (sum < s) {
            ++l;
        } else {
            --r;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Thử thách học sinh giải bài toán khi dữ liệu cập nhật động liên tục (Online Queries).
* **Mở rộng 2:** Áp dụng thuật toán trên không gian nhiều chiều (Ma trận 2D hoặc đồ thị).
* **Tự giải thích:** Yêu cầu học sinh giải thích tại sao không thể dùng thuật toán ngây thơ và chứng minh độ phức tạp tối ưu trước lớp.
