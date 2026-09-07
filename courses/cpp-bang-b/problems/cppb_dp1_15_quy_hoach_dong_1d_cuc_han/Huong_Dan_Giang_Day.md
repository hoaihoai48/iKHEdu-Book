# Hướng Dẫn Giảng Dạy: Tối Ưu Hóa Chuỗi Dự Án Năng Lượng

Chuyên đề: **Quy Hoạch Động 1 Chiều & Dãy Con Tăng (DP 1D / LIS)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách $N$ dự án với công suất $P_i$ và doanh thu $V_i$. Hãy lập trình chọn ra một chuỗi các dự án có công suất tăng nghiêm ngặt sao cho tổng doanh thu thu về là lớn nhất.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i]$ là kết quả tối ưu cho bài toán con kết thúc tại bước/vị trí thứ $i$.
- **Công thức chuyển trạng thái:** Dựa trên các lựa chọn bước đi trước đó (như $dp[i] = dp[i-1] + dp[i-2]$ hoặc $\min/\max$ qua các trạng thái $j < i$).
- **Cơ sở quy hoạch động:** Khởi tạo các trường hợp biên nhỏ nhất $dp[0], dp[1]$ rõ ràng trước khi lặp.
- **Độ phức tạp:** Thời gian tối ưu $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$ (cho LIS cải tiến qua tìm kiếm nhị phân `lower_bound`), bộ nhớ $\mathcal{O}(N)$ hoặc nén về $\mathcal{O}(1)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `3 10 100 5 50 20 200` $\implies$ Đầu ra kỳ vọng: `350`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 10 100 5 50 20 200` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với 3 dự án năng lượng có thông số $[(10, 100), (5, 50), (20, 200)]$: Chuỗi dự án có công suất tăng dần nghiêm ngặt là chọn dự án 2 (cô... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `350` |

*Giải thích chi tiết:* Với 3 dự án năng lượng có thông số $[(10, 100), (5, 50), (20, 200)]$:
Chuỗi dự án có công suất tăng dần nghiêm ngặt là chọn dự án 2 (công suất 5), sau đó dự án 1 (công suất 10), và cuối cùng là dự án 3 (công suất 20). Chuỗi công suất là $5 < 10 < 20$, mang lại tổng doanh thu tối đa là $50 + 100 + 200 = 350$.

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

struct Item {
    long long v, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<Item> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].v >> a[i].c;
    }

    // Sắp xếp theo v tăng dần
    sort(a.begin(), a.end(), [](const Item& x, const Item& y) {
        if (x.v != y.v) return x.v < y.v;
        return x.c > y.c;
    });

    vector<long long> dp(n);
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        dp[i] = a[i].c;
        for (int j = 0; j < i; ++j) {
            if (a[j].v < a[i].v) {
                dp[i] = max(dp[i], dp[j] + a[i].c);
            }
        }
        ans = max(ans, dp[i]);
    }

    cout << ans << "\n";
    return 0;
}
```
