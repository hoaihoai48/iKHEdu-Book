# Hướng dẫn giảng dạy: Đếm số có tổng chữ số bằng k
Chuyên đề: **Quy Hoạch Động Chữ Số (Digit DP)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ phương pháp giải quyết bài toán bằng kỹ thuật thuộc chuyên đề Quy Hoạch Động Chữ Số (Digit DP).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các thuật toán ngây thơ chạy quá thời gian.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không dùng thư viện rườm rà, quản lý bộ nhớ tối ưu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** Đọc hiểu ràng buộc tham số và kiểu dữ liệu phù hợp (chú ý tràn số `long long` khi giá trị vượt $2 \cdot 10^9$).
* **Yêu cầu cốt lõi:** Biến đổi bài toán từ mô hình phát biểu thực tế về mô hình thuật toán tối ưu.
* **Trường hợp biên (Edge Cases):**
  * Kích thước mảng cực tiểu ($N = 1$ hoặc $N = K$).
  * Giá trị phần tử âm, cực lớn hoặc tất cả các phần tử đều bằng nhau.
  * Truy vấn nằm ở sát biên của mảng.

---

## 3. Câu Hỏi Dẫn Dắt Tư Duy (Socratic Method)
1. Cách tiếp cận ngây thơ (Brute Force) của bài toán này là gì và tại sao lại bị TLE?
2. Có tính chất đơn điệu, cấu trúc lân cận hay tính chất bất biến nào có thể khai thác không?
3. Cấu trúc dữ liệu nào giúp giảm độ phức tạp thời gian từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N \log N)$ hoặc $\mathcal{O}(N)$?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Tiền xử lý dữ liệu hoặc chuyển đổi không gian bài toán về dạng tối ưu.
- Khai thác tính chất cấu trúc dữ liệu để trả lời truy vấn trong thời gian ngắn nhất.

### 4.2. Bất biến toán học (Invariant):
> Tính đúng đắn của thuật toán được bảo toàn sau mỗi bước lặp hoặc mỗi truy vấn.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
1 100 5
```
* **Output:**
```text
6
```
* **Phân tích quá trình thực thi:**
  Thuật toán tiến hành khởi tạo cấu trúc dữ liệu, duyệt tuyến tính qua từng phần tử và cập nhật kết quả tối ưu theo đúng nguyên lý thiết kế.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(N \log N)$ hoặc $\mathcal{O}(N)$, chạy mượt mà dưới $0.2\text{s}$ với $N = 10^5$.
- **Không gian (Space Complexity):** $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$ phụ thuộc vào cấu trúc lưu trữ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số nguyên:** Quên ép kiểu `long long` khi tính tổng hoặc tích các số lớn.
2. **Truy cập ngoài mảng:** Sử dụng chỉ số âm hoặc vượt quá kích thước cấp phát $N$.
3. **Trôi lệnh nhập/xuất:** Không sử dụng Fast I/O hoặc dùng `endl` gây nghẽn bộ đệm.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

long long Kglob;
vector<int> dig;
long long memo[20][185];
bool vis[20][185];

long long dfs(int pos, int sum, bool tight) {
    if (sum > Kglob) return 0;
    if (pos == (int)dig.size()) return (sum == Kglob) ? 1 : 0;
    if (!tight && vis[pos][sum]) return memo[pos][sum];
    int lim = tight ? dig[pos] : 9;
    long long res = 0;
    for (int d = 0; d <= lim; ++d) {
        res += dfs(pos + 1, sum + d, tight && (d == lim));
    }
    if (!tight) {
        vis[pos][sum] = true;
        memo[pos][sum] = res;
    }
    return res;
}

long long countLE(long long x) {
    if (x <= 0) return 0;
    dig.clear();
    string s = to_string(x);
    for (char c : s) dig.push_back(c - '0');
    memset(vis, 0, sizeof(vis));
    return dfs(0, 0, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    long long K;
    if (!(cin >> L >> R >> K)) return 0;
    Kglob = K;

    cout << countLE(R) - countLE(L - 1) << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nâng cao bài toán khi dữ liệu chuyển sang mảng động hoặc có thêm các thao tác cập nhật điểm/đoạn.
* Mở rộng bài toán trên không gian 2D hoặc trên cấu trúc đồ thị/cây.
