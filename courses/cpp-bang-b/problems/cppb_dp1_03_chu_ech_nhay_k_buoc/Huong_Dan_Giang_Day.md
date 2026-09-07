# Hướng Dẫn Giảng Dạy: Chú Ếch Nhảy K Bước

Chuyên đề: **Quy Hoạch Động 1 Chiều & Dãy Con Tăng (DP 1D / LIS)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho số lượng phiến đá $N$, tầm nhảy tối đa $K$ và danh sách độ cao của các phiến đá. Hãy lập trình tính toán tổng chi phí năng lượng ít nhất để chú ếch đi từ phiến đá $1$ tới phiến đá $N$.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i]$ là kết quả tối ưu cho bài toán con kết thúc tại bước/vị trí thứ $i$.
- **Công thức chuyển trạng thái:** Dựa trên các lựa chọn bước đi trước đó (như $dp[i] = dp[i-1] + dp[i-2]$ hoặc $\min/\max$ qua các trạng thái $j < i$).
- **Cơ sở quy hoạch động:** Khởi tạo các trường hợp biên nhỏ nhất $dp[0], dp[1]$ rõ ràng trước khi lặp.
- **Độ phức tạp:** Thời gian tối ưu $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$ (cho LIS cải tiến qua tìm kiếm nhị phân `lower_bound`), bộ nhớ $\mathcal{O}(N)$ hoặc nén về $\mathcal{O}(1)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `5 3 10 30 40 50 20` $\implies$ Đầu ra kỳ vọng: `30`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 3 10 30 40 50 20` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với $N = 5, K = 3$ và độ cao các phiến đá là $[10, 30, 40, 50, 20]$: - Từ đá 1 ($H_1 = 10$), chú ếch nhảy sang đá 2 ($H_2 = 30$) với kh... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `30` |

*Giải thích chi tiết:* Với $N = 5, K = 3$ và độ cao các phiến đá là $[10, 30, 40, 50, 20]$:
- Từ đá 1 ($H_1 = 10$), chú ếch nhảy sang đá 2 ($H_2 = 30$) với khoảng cách 1 bước hợp lệ ($\le 3$), chi phí là $|10 - 30| = 20$.
- Từ đá 2 ($H_2 = 30$), chú ếch nhảy thẳng tới đích là đá 5 ($H_5 = 20$) với khoảng cách $5 - 2 = 3$ bước (vẫn $\le K = 3$), chi phí là $|30 - 20| = 10$.
Tổng chi phí tối thiểu đạt được là $20 + 10 = 30$.

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

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    vector<long long> dp(n, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 1; j <= k && i + j < n; ++j) {
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]));
        }
    }

    cout << dp[n - 1] << "\n";
    return 0;
}
```
