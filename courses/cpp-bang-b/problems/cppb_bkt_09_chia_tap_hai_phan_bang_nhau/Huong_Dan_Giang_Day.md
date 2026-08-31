# Hướng Dẫn Giảng Dạy: Chia Tập Thành 2 Phần Có Tổng Bằng Nhau
Chuyên đề: **Thuật Toán Quay Lui & Nhánh Cận (Backtracking & Branch and Bound)**

**Phân loại chuyên đề:** `Core Foundation`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Chia Tập Thành 2 Phần Có Tổng Bằng Nhau.
* **Tư duy thuật toán:** Rèn luyện phản xạ xây dựng cây không gian trạng thái theo chuẩn mực `Choose` $\to$ `Explore` $\to$ `Unchoose` và phân biệt rõ ràng giữa Cắt tỉa ràng buộc (Feasibility Pruning) và Cắt tỉa tối ưu (Optimality Pruning).
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, hoàn tác an toàn).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: Số nguyên dương $N$ ($1 \le N \le 20$).
- Dòng 2: $N$ số nguyên dương $A_1, \dots, A_N$ ($1 \le A_i \le 100$).
* **Yêu cầu cốt lõi:** Cho mảng số nguyên dương $A$ gồm $N$ phần tử. Hãy kiểm tra xem có thể chia tập $A$ thành 2 tập con rời nhau sao cho tổng các phần tử của 2 tập con bằng nhau hay không. In `YES` nếu được, ngược lại in `NO`.
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
4
1 5 11 5
```
* **Output:**
```text
YES
```
* **Phân tích thực thi:** Chia thành 2 tập: {1, 5, 5} (tổng 11) và {11} (tổng 11).

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** $\mathcal{O}(2^N)$ (Pruned)
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\Theta(N)$ (Độ sâu tối đa: $N$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\Theta(N)$
* **Ghi chú phân tích:** Tổng mảng lẻ -> NO ngay lập tức; quay lui tìm tập con tổng Total/2.

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
long long target;
vector<long long> a;
bool possible = false;

void backtrack(int idx, long long cur_sum) {
    if (possible) return;
    if (cur_sum == target) {
        possible = true;
        return;
    }
    if (idx >= n || cur_sum > target) return;

    for (int i = idx; i < n; ++i) {
        if (cur_sum + a[i] <= target) {
            backtrack(i + 1, cur_sum + a[i]);
            if (possible) return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    a.resize(n);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total += a[i];
    }
    if (total % 2 != 0) {
        cout << "NO\n";
        return 0;
    }
    target = total / 2;
    sort(a.rbegin(), a.rend());
    backtrack(0, 0);
    cout << (possible ? "YES\n" : "NO\n");
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nhận diện hiện tượng trùng lặp trạng thái trên đồ thị có hướng không chu trình (DAG) để chuẩn bị bước chuyển mình mang tính quyết định sang **Module 05: Quy Hoạch Động (Dynamic Programming)**.
