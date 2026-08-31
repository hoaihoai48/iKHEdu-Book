# Hướng Dẫn Giảng Dạy: Lũy Thừa Ma Trận Chia Để Trị 2x2
Chuyên đề: **Kỹ Thuật Chia Để Trị (Divide and Conquer)**

**Phân loại chuyên đề:** `Core Foundation`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Lũy Thừa Ma Trận Chia Để Trị 2x2.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân rã bài toán thành 3 pha chuẩn mực: `Divide` $\to$ `Solve` $\to$ `Combine`.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, tối ưu bộ nhớ đệm).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: 4 số nguyên $a, b, c, d$ ($0 \le a, b, c, d \le 10^9$).
- Dòng 2: Hai số nguyên $N, M$ ($0 \le N \le 10^{18}, 1 \le M \le 10^9 + 7$).
* **Yêu cầu cốt lõi:** Cho ma trận vuông $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ cấp $2 \times 2$ và số nguyên không âm $N$. Hãy tính ma trận $A^N \pmod M$ bằng thuật toán Lũy thừa nhị phân Chia Để Trị trong $\mathcal{O}(\log N)$.
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
1 1
1 0
4 1000
```
* **Output:**
```text
5 3
3 2
```
* **Phân tích thực thi:** Ma trận Fibonacci [[1,1],[1,0]]^4 = [[5,3],[3,2]].

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** $\Theta(\log N)$
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\Theta(\log N)$ (Độ sâu tối đa: $\log_2 N$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\mathcal{O}(1)$
* **Ghi chú phân tích:** Nhân ma trận 2x2 tốn O(1), độ sâu chia đôi số mũ log2(N).

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số 32-bit khi đếm nghịch thế hoặc tính tổng:** Luôn sử dụng kiểu dữ liệu `long long`.
2. **Bẫy bỏ sót trường hợp vắt ngang (Crossing):** Phải xét đầy đủ mọi khả năng giữa 2 nửa mảng.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Matrix {
    long long mat[2][2];
};

Matrix multiply(const Matrix &A, const Matrix &B, long long m) {
    Matrix C;
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            C.mat[i][j] = 0;
            for (int k = 0; k < 2; ++k) {
                C.mat[i][j] = (C.mat[i][j] + (A.mat[i][k] % m) * (B.mat[k][j] % m)) % m;
            }
        }
    }
    return C;
}

Matrix powerMatrix(Matrix A, long long n, long long m) {
    Matrix res = {{{1 % m, 0}, {0, 1 % m}}};
    while (n > 0) {
        if (n & 1) res = multiply(res, A, m);
        A = multiply(A, A, m);
        n >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Matrix A;
    if (!(cin >> A.mat[0][0] >> A.mat[0][1] >> A.mat[1][0] >> A.mat[1][1])) return 0;
    long long n, m;
    if (!(cin >> n >> m)) return 0;
    Matrix ans = powerMatrix(A, n, m);
    cout << ans.mat[0][0] << " " << ans.mat[0][1] << "\n";
    cout << ans.mat[1][0] << " " << ans.mat[1][1] << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Vận dụng tư duy phân rã không gian tìm kiếm sang các bài toán hình học và chuẩn bị bước đệm cho Quay lui & Nhánh cận (Lesson 12).
