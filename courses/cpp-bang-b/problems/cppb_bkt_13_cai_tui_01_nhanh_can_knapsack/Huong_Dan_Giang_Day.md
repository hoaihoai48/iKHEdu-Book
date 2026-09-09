# Hướng Dẫn Giảng Dạy: Bài Toán Cái Túi 0/1 Nhánh Cận (B&B Knapsack)
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho $N$ đồ vật với trọng lượng $W_i$ và giá trị $V_i$ tương ứng, cùng sức chứa tối đa $M$ của ba lô. Hãy áp dụng thuật toán Nhánh Cận (Branch and Bound) sử dụng hàm cận trên Fractional Knapsack (sắp xếp theo tỷ lệ đơn giá $\frac{V_i}{W_i}$ giảm dần) để tìm giá trị tài sản lớn nhất có thể mang về.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
- Xây dựng không gian trạng thái dạng cây tìm kiếm.
- Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 10 3 40 4 50 5 60 6 70` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Chọn đồ vật thứ 2 (trọng lượng 4, giá trị 50) và đồ vật thứ 4 (trọng lượng 6, giá trị 70). Tổng trọng lượng là $4 + 6 = ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `120` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Chọn đồ vật thứ 2 (trọng lượng 4, giá trị 50) và đồ vật thứ 4 (trọng lượng 6, giá trị 70). Tổng trọng lượng là $4 + 6 = 10 \le 10$ và tổng giá trị đạt được là $50 + 70 = 120$, là giá trị lớn nhất có thể đạt được.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Tràn số nguyên:** Khi tính toán tổng, tích hoặc lũy thừa lớn hơn $2 \cdot 10^9$, bắt buộc phải sử dụng kiểu dữ liệu `long long` (64-bit) để tránh tràn số âm.
- **Bẫy 2 — Chỉ số mảng & Giới hạn biên:** Chú ý giữa đánh chỉ số 0-based (`0 .. N-1`) và 1-based (`1 .. N`). Kiểm tra kỹ trường hợp $N = 1$ hoặc giá trị biên tối đa của đề bài.
- **Bẫy 3 — Tối ưu thời gian I/O:** Luôn sử dụng `ios::sync_with_stdio(false); cin.tie(nullptr);` ở đầu hàm `main()` để đọc ghi nhanh, tránh bị TLE khi số lượng testcase lớn.

---

## 4. Lời giải tham khảo
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
