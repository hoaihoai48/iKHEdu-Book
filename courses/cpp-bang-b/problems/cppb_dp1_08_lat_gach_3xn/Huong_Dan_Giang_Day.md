# Hướng Dẫn Giảng Dạy: Lát Gạch Bảng 3xN

Chuyên đề: **Quy Hoạch Động 1 Chiều & Dãy Con Tăng (DP 1D / LIS)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho số nguyên dương $N$ là chiều dài của sàn nhà. Hãy lập trình đếm số cách lát kín mặt sàn $3  × N$, lấy dư cho $10^9 + 7$. (Nếu $N$ lẻ, diện tích sàn là số lẻ nên không thể phủ kín bằng các viên gạch diện tích 2, khi đó in ra `0`).

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i]$ là kết quả tối ưu cho bài toán con kết thúc tại bước/vị trí thứ $i$.
- **Công thức chuyển trạng thái:** Dựa trên các lựa chọn bước đi trước đó (như $dp[i] = dp[i-1] + dp[i-2]$ hoặc $\min/\max$ qua các trạng thái $j < i$).
- **Cơ sở quy hoạch động:** Khởi tạo các trường hợp biên nhỏ nhất $dp[0], dp[1]$ rõ ràng trước khi lặp.
- **Độ phức tạp:** Thời gian tối ưu $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$ (cho LIS cải tiến qua tìm kiếm nhị phân `lower_bound`), bộ nhớ $\mathcal{O}(N)$ hoặc nén về $\mathcal{O}(1)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `2` $\implies$ Đầu ra kỳ vọng: `3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với sàn nhà kích thước $3  × 2$ ($N = 2$), tổng diện tích là $3  × 2 = 6$ ô đơn vị, cần dùng đúng 3 viên gạch domino. Có tất cả đúng 3 ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `3` |

*Giải thích chi tiết:* Với sàn nhà kích thước $3  × 2$ ($N = 2$), tổng diện tích là $3  × 2 = 6$ ô đơn vị, cần dùng đúng 3 viên gạch domino. Có tất cả đúng 3 cách ghép hợp lệ:

1. Một viên đặt dọc ở cột 1, hai viên đặt ngang ở hàng 2 và 3.
2. Hai viên đặt ngang ở hàng 1 và 2, một viên đặt dọc ở cột 2.
3. Ba viên đặt ngang song song với nhau.
Kết quả in ra là 3.

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

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    if (n % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> a(n + 1, 0), b(n + 1, 0);
    a[0] = 1;
    b[0] = 0;
    if (n >= 1) b[1] = 1;

    for (int i = 2; i <= n; ++i) {
        a[i] = (a[i - 2] + 2LL * b[i - 1]) % MOD;
        b[i] = (a[i - 1] + b[i - 2]) % MOD;
    }

    cout << a[n] << "\n";
    return 0;
}
```
