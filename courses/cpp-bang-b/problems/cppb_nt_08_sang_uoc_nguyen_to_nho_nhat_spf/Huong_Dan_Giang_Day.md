# Hướng Dẫn Giảng Dạy: Sàng Ước Nguyên Tố Nhỏ Nhất (SPF)
Chuyên đề: **Lý Thuyết Số & Số Nguyên Tố (Number Theory)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán số học: Sàng Ước Nguyên Tố Nhỏ Nhất (SPF).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các vòng lặp lồng nhau $\mathcal{O}(N^2)$.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không tiền tố thừa, quản lý bộ nhớ tối ưu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).\n- Dòng 2: $Q$ số nguyên $N_1, N_2, \dots, N_Q$ ($2 \le N_i \le 10^6$).
* **Yêu cầu cốt lõi:** Cho $Q$ truy vấn, mỗi truy vấn chứa một số nguyên $N$. Hãy in ra ước số nguyên tố nhỏ nhất của $N$.
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
4\n15 49 13 100
```
* **Output:**
```text
3 7 13 2
```
* **Phân tích quá trình thực thi:**
  spf(15)=3, spf(49)=7, spf(13)=13, spf(100)=2.

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

const int MAXN = 1000000;
vector<int> spf(MAXN + 1);

void sieveSPF() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; 1LL * i * i <= MAXN; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieveSPF();

    int q;
    if (!(cin >> q)) return 0;

    for (int i = 0; i < q; ++i) {
        int n;
        cin >> n;
        cout << spf[n] << (i + 1 == q ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Áp dụng thuật toán khi số lượng truy vấn $Q$ lên tới $10^6$.
* **Mở rộng 2:** Tích hợp kỹ thuật vào các bài toán quy hoạch động hoặc chia để trị.
