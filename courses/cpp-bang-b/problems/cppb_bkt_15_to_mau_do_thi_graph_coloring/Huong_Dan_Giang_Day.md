# Hướng Dẫn Giảng Dạy: Tô Màu Đồ Thị (Graph K-Coloring)
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho đồ thị vô hướng $G = (V, E)$ gồm $V$ đỉnh và $E$ cạnh, cùng số lượng màu khả dụng $K$. Hãy áp dụng thuật toán Quay lui để kiểm tra xem có thể gán cho mỗi đỉnh của đồ thị một trong $K$ màu sao cho không có bất kỳ hai đỉnh kề nhau nào có cùng màu hay không. Nếu có thể tô màu hợp lệ in ra `YES`, ngược lại in ra `NO`.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
- Xây dựng không gian trạng thái dạng cây tìm kiếm.
- Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 5 3 1 2 2 3 3 4 4 1 1 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với 4 đỉnh và 5 cạnh xung đột, đồ thị hoàn toàn có thể được tô hợp lệ bằng 3 màu: đỉnh 1 màu 1, đỉnh 2 màu 2, đỉnh 3 màu... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `YES` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với 4 đỉnh và 5 cạnh xung đột, đồ thị hoàn toàn có thể được tô hợp lệ bằng 3 màu: đỉnh 1 màu 1, đỉnh 2 màu 2, đỉnh 3 màu 3, đỉnh 4 màu 2. Khi đó mọi cặp đỉnh kề nhau đều mang màu sắc khác nhau. Do đó đáp án là `YES`.

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

int V, E, K;
vector<int> adj[15];
int color[15];
bool possible = false;

bool isSafe(int u, int c) {
for (int v : adj[u]) {
if (color[v] == c) return false;
}
return true;
}

void backtrack(int u) {
if (possible) return;
if (u > V) {
possible = true;
return;
}
for (int c = 1; c <= K; ++c) {
if (isSafe(u, c)) {
color[u] = c;
backtrack(u + 1);
color[u] = 0;
if (possible) return;
}
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
if (!(cin >> V >> E >> K)) return 0;
for (int i = 0; i < E; ++i) {
int u, v;
cin >> u >> v;
adj[u].push_back(v);
adj[v].push_back(u);
}
memset(color, 0, sizeof(color));
backtrack(1);
cout << (possible "YES\n" : "NO\n");
return 0;
}
```
