# Hướng Dẫn Giảng Dạy: Dãy Con Hình Sóng Núi (Longest Bitonic Subsequence)

Chuyên đề: **Quy Hoạch Động 1 Chiều & Dãy Con Tăng (DP 1D / LIS)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm độ dài lớn nhất của một dãy con có dạng sóng núi.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i]$ là kết quả tối ưu cho bài toán con kết thúc tại bước/vị trí thứ $i$.
- **Công thức chuyển trạng thái:** Dựa trên các lựa chọn bước đi trước đó (như $dp[i] = dp[i-1] + dp[i-2]$ hoặc $\min/\max$ qua các trạng thái $j < i$).
- **Cơ sở quy hoạch động:** Khởi tạo các trường hợp biên nhỏ nhất $dp[0], dp[1]$ rõ ràng trước khi lặp.
- **Độ phức tạp:** Thời gian tối ưu $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$ (cho LIS cải tiến qua tìm kiếm nhị phân `lower_bound`), bộ nhớ $\mathcal{O}(N)$ hoặc nén về $\mathcal{O}(1)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `8 1 11 2 10 4 5 2 1` $\implies$ Đầu ra kỳ vọng: `6`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `8 1 11 2 10 4 5 2 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với dãy số gồm 8 phần tử $[1, 11, 2, 10, 4, 5, 2, 1]$: Dãy con hình sóng núi dài nhất có thể chọn là $[1, 2, 10, 5, 2, 1]$ (với đỉnh là... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `6` |

*Giải thích chi tiết:* Với dãy số gồm 8 phần tử $[1, 11, 2, 10, 4, 5, 2, 1]$:
Dãy con hình sóng núi dài nhất có thể chọn là $[1, 2, 10, 5, 2, 1]$ (với đỉnh là 10; phần tăng gồm 1, 2, 10 và phần giảm gồm 10, 5, 2, 1). Tổng số phần tử của dãy sóng núi này là 6.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Quên chia lấy dư theo modulo $10^9 + 7$ tại mỗi phép cộng/nhân dẫn đến tràn số nguyên.
* Khởi tạo sai giá trị mảng $dp$: Các bài tìm giá trị nhỏ nhất cần khởi tạo giá trị vô cùng lớn (`INF = 1e18`), tránh dùng `0x3f` khi cộng dồn gây tràn số.
* Lỗi lệch chỉ số giữa 0-based và 1-based khi tham chiếu các phần tử liền kề.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;
if (n <= 0) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

// LIS từ trái sang phải
vector<int> inc(n, 1);
for (int i = 1; i < n; ++i) {
for (int j = 0; j < i; ++j) {
if (a[j] < a[i]) inc[i] = max(inc[i], inc[j] + 1);
}
}

// LDS từ phải sang trái
vector<int> dec(n, 1);
for (int i = n - 2; i >= 0; --i) {
for (int j = n - 1; j > i; --j) {
if (a[j] < a[i]) dec[i] = max(dec[i], dec[j] + 1);
}
}

int max_bitonic = 0;
for (int i = 0; i < n; ++i) {
max_bitonic = max(max_bitonic, inc[i] + dec[i] - 1);
}

cout << max_bitonic << "\n";
return 0;
}
```
