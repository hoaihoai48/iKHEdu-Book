# Hướng Dẫn Giảng Dạy: Tính Tổng Dãy Số & Giai Thừa Bằng Đệ Quy
Chuyên đề: **Thuật Toán Đệ Quy & Cây Gọi Hàm (Recursion & Call Stack)**

**Phân loại chuyên đề:** `Core Foundation`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Tính Tổng Dãy Số & Giai Thừa Bằng Đệ Quy.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích Base Case, Winding/Unwinding Phase và quản lý bộ nhớ Call Stack.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, đệ quy an toàn).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 20$).
* **Yêu cầu cốt lõi:** Cho số nguyên dương $N$. Hãy tính tổng $S = 1 + 2 + \dots + N$ và tích giai thừa $P = N! = 1 \times 2 \times \dots \times N$ bằng các hàm đệ quy có giá trị trả về.
* **Phân tích trường hợp biên:** Đảm bảo hàm dừng đúng tại Base Case nhỏ nhất.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Trường hợp đơn giản nhất của bài toán là gì mà ta có thể trả lời ngay không cần gọi tiếp?
2. Khi quy mô bài toán giảm từ $N$ về bài toán con, mối liên hệ giữa $f(N)$ và kết quả con là gì?
3. Tại sao cần lưu ý thứ tự câu lệnh trước và sau lời gọi đệ quy?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Base Case Invariant:** Mọi nhánh đệ quy bắt buộc phải hội tụ về Base Case sau số bước hữu hạn.
* **Call Stack Safety:** Không khai báo mảng cục bộ kích thước lớn trong thân hàm để tránh Stack Overflow.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
4
```
* **Output:**
```text
10 24
```
* **Phân tích thực thi:** S = 1 + 2 + 3 + 4 = 10, P = 1 * 2 * 3 * 4 = 24.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** Đạt tiệm cận tối ưu.
* **Không gian (Space Complexity):** Bộ nhớ stack tỷ lệ thuận với độ sâu đệ quy lớn nhất.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Quên Base Case hoặc chặn cận sai:** Dẫn đến đệ quy vô tận và sập ngăn xếp.
2. **Khai báo biến mảng trong hàm:** Làm phình to Stack Frame.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

long long getSum(int n) {
    if (n <= 1) return n;
    return n + getSum(n - 1);
}

long long getFact(int n) {
    if (n <= 1) return 1;
    return 1LL * n * getFact(n - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << getSum(n) << " " << getFact(n) << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Vận dụng tư duy đệ quy sang các bài toán phân nhánh phức tạp hơn và chuẩn bị bước đệm cho Divide & Conquer ở Chuyên đề 11.
