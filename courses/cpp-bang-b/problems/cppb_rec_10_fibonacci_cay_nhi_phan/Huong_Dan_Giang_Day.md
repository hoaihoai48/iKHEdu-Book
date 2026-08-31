# Hướng Dẫn Giảng Dạy: Dãy Fibonacci Đệ Quy & Khảo Sát Cây Gọi Hàm
Chuyên đề: **Thuật Toán Đệ Quy & Cây Gọi Hàm (Recursion & Call Stack)**

**Phân loại chuyên đề:** `Core Foundation`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Dãy Fibonacci Đệ Quy & Khảo Sát Cây Gọi Hàm.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích Base Case, Winding/Unwinding Phase và quản lý bộ nhớ Call Stack.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, đệ quy an toàn).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 30$).
* **Yêu cầu cốt lõi:** Cho số nguyên $N$. Hãy tính số Fibonacci $F_N$ ($F_0 = 0, F_1 = 1, F_N = F_{N-1} + F_{N-2}$) bằng hàm đệ quy thuần túy và đếm tổng số lần hàm `fib()` được gọi.
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
3 9
```
* **Phân tích thực thi:** F(4) = 3. Tổng số lần gọi hàm fib là 9 lần.

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

long long call_count = 0;

long long fibRec(int n) {
    call_count++;
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibRec(n - 1) + fibRec(n - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    long long val = fibRec(n);
    cout << val << " " << call_count << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Vận dụng tư duy đệ quy sang các bài toán phân nhánh phức tạp hơn và chuẩn bị bước đệm cho Divide & Conquer ở Chuyên đề 11.
