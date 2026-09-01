# Hướng Dẫn Giảng Dạy: SỐ TRIBONACCI THỨ N BẰNG NHÂN MA TRẬN 3X3
Chuyên đề: **Đại Số Đồng Dư & Lũy Thừa Nhanh (Modular Arithmetic)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán: **SỐ TRIBONACCI THỨ N BẰNG NHÂN MA TRẬN 3X3** thuộc chuyên đề Đại Số Đồng Dư & Lũy Thừa Nhanh (Modular Arithmetic).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các thuật toán ngây thơ chạy quá thời gian $\mathcal{O}(N^2)$.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không dùng thư viện rườm rà, quản lý bộ nhớ tối ưu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Bản chất bài toán:** Dãy số Tribonacci được định nghĩa bởi hệ thức truy hồi bậc ba: $T_0 = 0, T_1 = 1, T_2 = 1$ và $T_n = T_{n-1} + T_{n-2} + T_{n-3}$ với mọi $n \ge 3$. Với $N$ cực lớn lên tới $10^{18}$, ta biểu diễn trạng thái truy hồi dưới dạng nhân vector với ma trận chuyển tiếp kích thước $3 \times 3$: $\begin{pmatrix} T_{n} \\ T_{n-1} \\ T_{n-2} \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} T_{n-1} \\ T_{n-2} \\ T_{n-3} \end{pmatrix}$. Áp dụng thuật toán Lũy thừa ma trận nhị phân để tính $T_N \pmod{10^9+7}$ trong $\mathcal{O}(3^3 \log N)$.
* **Trường hợp biên (Edge Cases):**
  * Giá trị biên cực tiểu ($N = 1$, giá trị tại $0$ hoặc $1$).
  * Giá trị cực đại đạt ngưỡng $10^18$ cần xử lý tràn số nguyên 64-bit (`long long` hoặc modulo chống tràn).
  * Xử lý trường hợp không tìm thấy kết quả hoặc bài toán vô nghiệm.

---

## 3. Câu Hỏi Dẫn Dắt Tư Duy (Socratic Method)
1. Cách tiếp cận duyệt tuần tự (Brute Force) của bài toán này sẽ gặp giới hạn thời gian như thế nào khi dữ liệu lớn?
2. Có tính chất toán học, công thức truy hồi tuyến tính hay cấu trúc dữ liệu nào giúp giảm độ phức tạp thời gian xuống $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N)$?
3. Các bẫy lỗi tràn số hoặc tràn mảng có thể xảy ra ở những bước tính toán nào?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Biến đổi bài toán về dạng cấu trúc chuẩn thi đấu.
- Khai thác tính chất cấu trúc dữ liệu hoặc đại số để giải quyết từng truy vấn trong thời gian tối ưu.

### 4.2. Bất biến toán học (Invariant):
> Tính đúng đắn của cấu trúc dữ liệu và giá trị nghiệm toán học được bảo toàn qua các bước lặp và cập nhật.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
4
0
1
3
4
```
* **Output:**
```text
0
1
2
4
```
* **Phân tích quá trình thực thi:**
* $T_0 = 0, T_1 = 1, T_2 = 1, T_3 = 0+1+1=2, T_4 = 1+1+2=4$.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** Thuật toán tối ưu đảm bảo thời gian chạy $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log N)$, chạy mượt mà dưới $0.2\text{s}$ trên hệ thống online judge.
- **Không gian (Space Complexity):** $\mathcal{O}(1)$ hoặc $\mathcal{O}(N)$ bộ nhớ phụ trợ, tối ưu dung lượng RAM dưới $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số nguyên 64-bit:** Quên ép kiểu `long long` khi nhân hai số lớn trước khi lấy modulo.
2. **Trôi bộ đệm I/O:** Không bật Fast I/O hoặc dùng `endl` trong vòng lặp lớn gây nghẽn TLE.
3. **Lỗi chỉ số mảng:** Truy cập phần tử ngoài biên cấp phát $N$.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B) {
    Matrix C(3, vector<long long>(3, 0));
    for (int i = 0; i < 3; ++i)
        for (int k = 0; k < 3; ++k)
            for (int j = 0; j < 3; ++j)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
}

Matrix matPow(Matrix A, long long k) {
    Matrix res(3, vector<long long>(3, 0));
    for (int i = 0; i < 3; ++i) res[i][i] = 1;
    while (k > 0) {
        if (k & 1) res = multiply(res, A);
        A = multiply(A, A);
        k >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    if (n == 0) { cout << 0 << "\n"; return 0; }
    if (n == 1 || n == 2) { cout << 1 << "\n"; return 0; }

    Matrix T = {
        {1, 1, 1},
        {1, 0, 0},
        {0, 1, 0}
    };
    Matrix Tn = matPow(T, n - 2);
    long long ans = (Tn[0][0] * 1 + Tn[0][1] * 1 + Tn[0][2] * 0) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Mở rộng bài toán khi dữ liệu chuyển sang môi trường động hoặc có các truy vấn cập nhật liên tục.
* Ứng dụng kỹ thuật này vào các bài toán kết hợp đồ thị hoặc quy hoạch động nâng cao.
