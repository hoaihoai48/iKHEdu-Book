# Hướng Dẫn Giảng Dạy: Tổng Đoạn Con Không Liền Kề Lớn Nhất

Chuyên đề: **Quy Hoạch Động 1 Chiều & Dãy Con Tăng (DP 1D / LIS)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách giá trị thương mại của $N$ căn nhà. Hãy lập trình chọn ra một tập hợp các căn nhà không kề nhau sao cho tổng giá trị thu được là lớn nhất có thể.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i]$ là kết quả tối ưu cho bài toán con kết thúc tại bước/vị trí thứ $i$.
- **Công thức chuyển trạng thái:** Dựa trên các lựa chọn bước đi trước đó (như $dp[i] = dp[i-1] + dp[i-2]$ hoặc $\min/\max$ qua các trạng thái $j < i$).
- **Cơ sở quy hoạch động:** Khởi tạo các trường hợp biên nhỏ nhất $dp[0], dp[1]$ rõ ràng trước khi lặp.
- **Độ phức tạp:** Thời gian tối ưu $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$ (cho LIS cải tiến qua tìm kiếm nhị phân `lower_bound`), bộ nhớ $\mathcal{O}(N)$ hoặc nén về $\mathcal{O}(1)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `4 1 2 3 1` $\implies$ Đầu ra kỳ vọng: `4`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 1 2 3 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với dãy giá trị của 4 căn nhà là $[1, 2, 3, 1]$: - Nếu chọn nhà 2 và nhà 4: Tổng giá trị là $2 + 1 = 3$. - Phương án tối ưu: Chọn nhà 1... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `4` |

*Giải thích chi tiết:* Với dãy giá trị của 4 căn nhà là $[1, 2, 3, 1]$:

- Nếu chọn nhà 2 và nhà 4: Tổng giá trị là $2 + 1 = 3$.
- Phương án tối ưu: Chọn nhà 1 (giá trị 1) và nhà 3 (giá trị 3). Hai nhà này không kề nhau và mang lại tổng giá trị lớn nhất là $1 + 3 = 4$.

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

if (n == 1) { cout << a[0] << "\n"; return 0; }

long long prev2 = a[0];
long long prev1 = max(a[0], a[1]);
long long cur = prev1;

for (int i = 2; i < n; ++i) {
cur = max(prev1, prev2 + a[i]);
prev2 = prev1;
prev1 = cur;
}

cout << cur << "\n";
return 0;
}
```
