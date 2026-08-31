# Hướng Dẫn Giảng Dạy: Bài Toán Cái Túi 0/1 Nhánh Cận (B&B Knapsack)
Chuyên đề: **Thuật Toán Quay Lui & Nhánh Cận (Backtracking & Branch and Bound)**

**Phân loại chuyên đề:** `Advanced`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Bài Toán Cái Túi 0/1 Nhánh Cận (B&B Knapsack).
* **Tư duy thuật toán:** Rèn luyện phản xạ xây dựng cây không gian trạng thái theo chuẩn mực `Choose` $\to$ `Explore` $\to$ `Unchoose` và phân biệt rõ ràng giữa Cắt tỉa ràng buộc (Feasibility Pruning) và Cắt tỉa tối ưu (Optimality Pruning).
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, hoàn tác an toàn).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: Hai số nguyên $N, M$ ($1 \le N \le 25, 1 \le M \le 10^9$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $W_i, V_i$ ($1 \le W_i, V_i \le 10^7$).
* **Yêu cầu cốt lõi:** Cho $N$ đồ vật, mỗi đồ vật $i$ có trọng lượng $W_i$ và giá trị $V_i$. Một cái túi có sức chứa tối đa $M$. Hãy tìm tổng giá trị lớn nhất của các đồ vật chọn vào túi bằng thuật toán Nhánh Cận (Branch and Bound) sử dụng hàm cận trên Fractional Knapsack.
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
4 10
3 40
4 50
5 60
6 70
```
* **Output:**
```text
120
```
* **Phân tích thực thi:** Chọn vật 2 (W=4, V=50) và vật 6 (W=6, V=70) -> Tổng W=10, Tổng V=120.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** Exponential worst-case (Phụ thuộc chất lượng Bound)
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\Theta(N)$ (Độ sâu tối đa: $N$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\Theta(N)$
* **Ghi chú phân tích:** Upper Bound bằng Fractional Knapsack; UB <= best_val -> Prune.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Quên bước hoàn tác (Unchoose):** Làm rò rỉ trạng thái giữa các nhánh gây thiếu nghiệm.
2. **Hàm Bound sai:** Cắt tỉa nhầm nghiệm tối ưu trong các bài toán Branch & Bound.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Item {
    long long w, v;
    double ratio;
};

int n;
long long max_w;
vector<Item> items;
long long best_val = 0;

double getUpperBound(int idx, long long cur_w, long long cur_v) {
    long long remain_w = max_w - cur_w;
    double bound = cur_v;
    for (int i = idx; i < n; ++i) {
        if (items[i].w <= remain_w) {
            remain_w -= items[i].w;
            bound += items[i].v;
        } else {
            bound += items[i].ratio * remain_w;
            break;
        }
    }
    return bound;
}

void branchAndBound(int idx, long long cur_w, long long cur_v) {
    if (cur_v > best_val) best_val = cur_v;
    if (idx >= n) return;

    if (getUpperBound(idx, cur_w, cur_v) <= best_val) return;

    // Nhánh 1: Chọn vật idx
    if (cur_w + items[idx].w <= max_w) {
        branchAndBound(idx + 1, cur_w + items[idx].w, cur_v + items[idx].v);
    }
    // Nhánh 2: Không chọn vật idx
    branchAndBound(idx + 1, cur_w, cur_v);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> max_w)) return 0;
    items.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> items[i].w >> items[i].v;
        items[i].ratio = (double)items[i].v / items[i].w;
    }
    sort(items.begin(), items.end(), [](const Item &a, const Item &b) {
        return a.ratio > b.ratio;
    });
    branchAndBound(0, 0, 0);
    cout << best_val << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nhận diện hiện tượng trùng lặp trạng thái trên đồ thị có hướng không chu trình (DAG) để chuẩn bị bước chuyển mình mang tính quyết định sang **Module 05: Quy Hoạch Động (Dynamic Programming)**.
