# Hướng Dẫn Giảng Dạy: Tháp Hà Nội Có Ràng Buộc Nước Đi
Chuyên đề: **Thuật Toán Đệ Quy & Cây Gọi Hàm (Recursion & Call Stack)**

**Phân loại chuyên đề:** `Advanced Challenge`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Tháp Hà Nội Có Ràng Buộc Nước Đi.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích Base Case, Winding/Unwinding Phase và quản lý bộ nhớ Call Stack.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, đệ quy an toàn).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10$).
* **Yêu cầu cốt lõi:** Cho $N$ đĩa trên cọc $A$. Quy tắc: **Cấm tuyệt đối mọi nước đi trực tiếp giữa cọc A và cọc C** (mọi đĩa muốn đi từ $A \to C$ hoặc $C \to A$ bắt buộc phải đi qua cọc trung gian $B$). Hãy in ra số bước di chuyển tối thiểu $K = 3^N - 1$ và danh sách các bước di chuyển hợp lệ.
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
2
```
* **Output:**
```text
8
A -> B
B -> C
A -> B
C -> B
B -> A
B -> C
A -> B
B -> C
```
* **Phân tích thực thi:** Với N = 2 đĩa và cấm A <-> C trực tiếp, cần đúng 3^2 - 1 = 8 bước.

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

void moveAtoB(int n, char a, char b, char c);
void moveBtoC(int n, char b, char c, char a);

void solveConstrainedHanoi(int n, char from, char to, char aux) {
    if (n == 0) return;
    // Chuyển n-1 đĩa from -> to
    solveConstrainedHanoi(n - 1, from, to, aux);
    // Chuyển đĩa n: from -> aux
    cout << from << " -> " << aux << "\n";
    // Chuyển n-1 đĩa to -> from
    solveConstrainedHanoi(n - 1, to, from, aux);
    // Chuyển đĩa n: aux -> to
    cout << aux << " -> " << to << "\n";
    // Chuyển n-1 đĩa from -> to
    solveConstrainedHanoi(n - 1, from, to, aux);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    long long total_steps = 1;
    for (int i = 0; i < n; ++i) total_steps *= 3;
    total_steps -= 1;
    cout << total_steps << "\n";
    solveConstrainedHanoi(n, 'A', 'C', 'B');
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Vận dụng tư duy đệ quy sang các bài toán phân nhánh phức tạp hơn và chuẩn bị bước đệm cho Divide & Conquer ở Chuyên đề 11.
