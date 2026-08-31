# Hướng Dẫn Giảng Dạy: Số Gần Nguyên Tố (Almost Prime)
Chuyên đề: **Lý Thuyết Số & Số Nguyên Tố (Number Theory)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán số học: Số Gần Nguyên Tố (Almost Prime).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các vòng lặp lồng nhau $\mathcal{O}(N^2)$.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không tiền tố thừa, quản lý bộ nhớ tối ưu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^7$).
* **Yêu cầu cốt lõi:** Một số nguyên dương được gọi là 'gần nguyên tố' nếu nó có đúng 2 ước nguyên tố phân biệt. Cho số $N$, hãy đếm số lượng số gần nguyên tố $\le N$.
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
10
```
* **Output:**
```text
2
```
* **Phân tích quá trình thực thi:**
  Các số gần nguyên tố <= 10 là {6 (2*3), 10 (2*5)} -> 2 số.

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

    vector<int> prime_count(n + 1, 0);
    for (int i = 2; i <= n; ++i) {
        if (prime_count[i] == 0) { // i là số nguyên tố
            for (int j = i; j <= n; j += i) {
                prime_count[j]++;
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        if (prime_count[i] == 2) ans++;
    }

    cout << ans << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Áp dụng thuật toán khi số lượng truy vấn $Q$ lên tới $10^6$.
* **Mở rộng 2:** Tích hợp kỹ thuật vào các bài toán quy hoạch động hoặc chia để trị.
