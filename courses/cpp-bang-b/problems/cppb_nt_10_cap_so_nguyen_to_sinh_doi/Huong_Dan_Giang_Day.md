# Hướng Dẫn Giảng Dạy: Cặp Số Nguyên Tố Sinh Đôi (Twin Primes)
Chuyên đề: **Lý Thuyết Số & Số Nguyên Tố (Number Theory)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán số học: Cặp Số Nguyên Tố Sinh Đôi (Twin Primes).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các vòng lặp lồng nhau $\mathcal{O}(N^2)$.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không tiền tố thừa, quản lý bộ nhớ tối ưu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^7$).
* **Yêu cầu cốt lõi:** Một cặp số $(p, p+2)$ được gọi là số nguyên tố sinh đôi nếu cả $p$ và $p+2$ đều là số nguyên tố. Cho số nguyên $N$, hãy đếm số lượng cặp nguyên tố sinh đôi mà $p+2 \le N$.
* **Trường hợp biên (Edge Cases):**
  * Kích thước mảng cực tiểu ($N = 1$ hoặc $N = 2$).
  * Giá trị cực lớn (cần dùng `long long` hoặc `unsigned long long`).
  * Các số đặc biệt như 0, 1 không phải là số nguyên tố.

---

## 3. Câu Hỏi Dẫn Dắt Tư Duy (Socratic Method)
1. Dạng dữ liệu bài toán có tính chất nhân tính (multiplicative) hay cộng dồn không?
2. Có thể thu hẹp không gian tìm kiếm từ $\mathcal{O}(N)$ xuống $\mathcal{O}(\sqrt{N})$ hoặc $\mathcal{O}(\log N)$ không?
3. Cần tiền xử lý bằng Sàng nguyên tố hay tính trực tiếp cho mỗi truy vấn?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Nhận diện mô hình toán và cài đặt thuật toán tối ưu.
- Khai thác tính chất số học để giảm độ phức tạp.

### 4.2. Bất biến toán học (Invariant):
> Tính chất số học được bảo toàn xuyên suốt các bước biến đổi đại số.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
20
```
* **Output:**
```text
4
```
* **Phân tích quá trình thực thi:**
  Các cặp nguyên tố sinh đôi <= 20: (3, 5), (5, 7), (11, 13), (17, 19) -> 4 cặp.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** Thuật toán tối ưu đảm bảo chạy mượt mà dưới $1.0\text{s}$.
- **Không gian (Space Complexity):** $\mathcal{O}(1)$ hoặc $\mathcal{O}(N)$ bộ nhớ phụ trợ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. Tràn số khi nhân hai số lớn (cần chia trước nhân sau hoặc dùng `long long`).
2. Quên xét trường hợp $N = 1$.
3. Khai báo mảng sàng quá nhỏ dẫn đến truy cập ngoài bộ nhớ.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n < 5) {
        cout << 0 << "\n";
        return 0;
    }

    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; 1LL * i * i <= n; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) is_prime[j] = false;
        }
    }

    int count_twin = 0;
    for (int p = 3; p + 2 <= n; p += 2) {
        if (is_prime[p] && is_prime[p + 2]) count_twin++;
    }

    cout << count_twin << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Áp dụng thuật toán khi số lượng truy vấn $Q$ lên tới $10^6$.
* **Mở rộng 2:** Tích hợp kỹ thuật vào các bài toán quy hoạch động hoặc chia để trị.
