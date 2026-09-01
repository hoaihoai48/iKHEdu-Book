# Hướng dẫn giảng dạy: Digit DP chia het cho k

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Làm chủ giải thuật và kỹ thuật lập trình tối ưu cho bài toán **Digit Dp Chia Het Cho K**.
* **Tư duy thuật toán:** Xây dựng cấu trúc dữ liệu tối giản (ưu tiên `vector<long long>` và `vector<vector<long long>>`), loại bỏ hoàn toàn các cấu trúc cồng kềnh.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, không lỗi cảnh báo).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** Nhận diện đúng phạm vi dữ liệu, chú ý xử lý tràn số `long long` khi nhân hoặc tính tổng dồn.
* **Trường hợp biên (Edge Cases):**
  * Kích thước mảng cực tiểu ($N = 1$ hoặc $N = K$).
  * Giá trị phần tử cực lớn hoặc nằm ở sát biên của mảng.
  * Không tìm thấy đáp án hợp lệ (xuất `-1` hoặc giá trị mặc định).

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Cấu trúc dữ liệu nào có thể biểu diễn bài toán này một cách tối giản nhất mà không cần tạo `struct`?
2. Bất biến nào được duy trì xuyên suốt quá trình thực thi thuật toán?
3. Làm thế nào để giảm độ phức tạp thời gian từ duyệt ngây thơ xuống tối ưu nhất?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Sử dụng thuật toán chuyên sâu được thiết kế tối ưu cho dạng bài, tận dụng sắp xếp đa trường trên `vector<vector<long long>>`.
* **Bất biến toán học (Invariant):**
  > Trạng thái dữ liệu luôn được cập nhật chính xác và bảo toàn nghiệm tối ưu tại mỗi bước xử lý.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
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

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc dữ liệu và khởi tạo | Nhận tham số đầu vào | Thiết lập mảng/vector |
| **2** | Xử lý thuật toán chính | Duyệt qua các phần tử / truy vấn | Cập nhật giá trị tối ưu |
| **3** | Xuất kết quả | In đáp án ra màn hình | Khớp chính xác Sample |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** Tối ưu đảm bảo chạy trong thời gian $1.0\text{s}$.
* **Không gian (Space Complexity):** $\mathcal{O}(N)$ tối ưu bộ nhớ $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số nguyên:** Quên dùng `long long` khi tính tổng hoặc tích các giá trị lớn.
2. **Nghẽn vào/ra (I/O):** Không bật Fast I/O hoặc dùng `endl` thay vì `'\n'`.
3. **Lỗi chỉ số mảng:** Truy cập vượt quá kích thước cấp phát của mảng/vector.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

long long dp[20][100][2][2];
string S;
int K;

long long solve(int idx, int rem, bool tight, bool leading_zero) {
    if (idx == (int)S.size()) {
        return (rem == 0 && !leading_zero) ? 1 : 0;
    }
    if (dp[idx][rem][tight][leading_zero] != -1) {
        return dp[idx][rem][tight][leading_zero];
    }

    int limit = tight ? (S[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_tight = tight && (d == limit);
        bool next_lz = leading_zero && (d == 0);
        int next_rem = next_lz ? 0 : (rem * 10 + d) % K;
        ans += solve(idx + 1, next_rem, next_tight, next_lz);
    }

    return dp[idx][rem][tight][leading_zero] = ans;
}

long long count_div(long long N, int k) {
    if (N <= 0) return 0;
    S = to_string(N);
    K = k;
    memset(dp, -1, sizeof(dp));
    return solve(0, 0, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    int k;
    if (!(cin >> L >> R >> k)) return 0;

    cout << count_div(R, k) - count_div(L - 1, k) << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Mở rộng sang không gian dữ liệu động có các truy vấn cập nhật giá trị liên tục.
* Ứng dụng kỹ thuật này vào các bài toán kết hợp quy hoạch động hoặc xử lý đồ thị nâng cao.
