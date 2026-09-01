# Hướng Dẫn Giảng Dạy: CAN NGUYEN NGUYEN THUY PRIMITIVE ROOT
Chuyên đề: **Số Học Cơ Bản & Chuyên Sâu (Number Theory)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán: **CAN NGUYEN NGUYEN THUY PRIMITIVE ROOT** thuộc chuyên đề Số Học Cơ Bản & Chuyên Sâu (Number Theory).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các thuật toán ngây thơ chạy quá thời gian $\mathcal{O}(N^2)$.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không dùng thư viện rườm rà, quản lý bộ nhớ tối ưu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Bản chất bài toán:** Trong lập trình thi đấu chuyên nghiệp, bài toán **Can Nguyen Nguyen Thuy Primitive Root** là một dạng bài điển hình thuộc chuyên đề **Số Học Cơ Bản & Chuyên Sâu (Number Theory)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.
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
7
```
* **Output:**
```text
3
```
* **Phân tích quá trình thực thi:**
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `3`.

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

long long power(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long p;
    if (!(cin >> p)) return 0;

    long long phi = p - 1;
    vector<long long> factors;
    long long temp = phi;
    for (long long i = 2; i * i <= temp; ++i) {
        if (temp % i == 0) {
            factors.push_back(i);
            while (temp % i == 0) temp /= i;
        }
    }
    if (temp > 1) factors.push_back(temp);

    for (long long g = 2; g < p; ++g) {
        bool ok = true;
        for (long long f : factors) {
            if (power(g, phi / f, p) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << g << "\n";
            return 0;
        }
    }
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Mở rộng bài toán khi dữ liệu chuyển sang môi trường động hoặc có các truy vấn cập nhật liên tục.
* Ứng dụng kỹ thuật này vào các bài toán kết hợp đồ thị hoặc quy hoạch động nâng cao.
