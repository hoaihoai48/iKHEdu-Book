# Hướng Dẫn Giảng Dạy: Sinh Tất Cả Xâu Nhị Phân Độ Dài N
Chuyên đề: **Thuật Toán Quay Lui & Nhánh Cận (Backtracking & Branch and Bound)**

**Phân loại chuyên đề:** `Core Foundation`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Sinh Tất Cả Xâu Nhị Phân Độ Dài N.
* **Tư duy thuật toán:** Rèn luyện phản xạ xây dựng cây không gian trạng thái theo chuẩn mực `Choose` $\to$ `Explore` $\to$ `Unchoose` và phân biệt rõ ràng giữa Cắt tỉa ràng buộc (Feasibility Pruning) và Cắt tỉa tối ưu (Optimality Pruning).
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, hoàn tác an toàn).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 16$).
* **Yêu cầu cốt lõi:** Cho số nguyên dương $N$. Hãy sinh tất cả các xâu nhị phân độ dài $N$ theo thứ tự từ điển bằng thuật toán Quay Lui chuẩn mực (`Choose` $\to$ `Explore` $\to$ `Unchoose`).
* **Phân tích trường hợp biên:** Đảm bảo hàm dừng đúng khi chạm đáy cây trạng thái và hoàn tác đầy đủ cho các nhánh tiếp theo.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Tại mỗi bước của quá trình quay lui, ta có những lựa chọn nào và điều kiện hợp lệ là gì?
2. Sau khi gọi đệ quy đi sâu, trạng thái nào bắt buộc phải được hoàn tác (Unchoose)?
3. Ta có thể thiết lập hàm đánh giá (Bound) như thế nào để cắt tỉa sớm các nhánh không thể tối ưu?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **State Consistency Invariant:** Trạng thái hệ thống trước và sau mỗi lời gọi đệ quy nhánh con phải hoàn toàn bất biến (nhờ bước Unchoose).
* **Pruning Safety:** Cận dưới/Cận trên phải luôn bảo đảm tính đúng đắn toán học để không bao giờ cắt bỏ nghiệm tối ưu toàn cục.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
3
```
* **Output:**
```text
000
001
010
011
100
101
110
111
```
* **Phân tích thực thi:** Có đúng 2^3 = 8 xâu nhị phân độ dài 3.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** $\Theta(N \cdot 2^N)$
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\Theta(N)$ (Độ sâu tối đa: $N$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\mathcal{O}(1)$
* **Ghi chú phân tích:** Tổng số nghiệm lá là 2^N, in mỗi nghiệm độ dài N tốn Theta(N * 2^N).

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Quên bước hoàn tác (Unchoose):** Làm rò rỉ trạng thái giữa các nhánh gây thiếu nghiệm.
2. **Hàm Bound sai:** Cắt tỉa nhầm nghiệm tối ưu trong các bài toán Branch & Bound.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
string cur = "";

void backtrack(int step) {
    if (step > n) {
        cout << cur << "\n";
        return;
    }
    for (char c : {'0', '1'}) {
        cur.push_back(c);
        backtrack(step + 1);
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    backtrack(1);
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nhận diện hiện tượng trùng lặp trạng thái trên đồ thị có hướng không chu trình (DAG) để chuẩn bị bước chuyển mình mang tính quyết định sang **Module 05: Quy Hoạch Động (Dynamic Programming)**.
