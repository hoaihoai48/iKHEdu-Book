# Hướng Dẫn Giảng Dạy: Lát Gạch Bảng 2xN

Chuyên đề: **Quy Hoạch Động 1 Chiều & Dãy Con Tăng (DP 1D / LIS)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho số nguyên dương $N$ là chiều dài của mặt sàn. Hãy lập trình tính số cách lát gạch khác nhau để phủ kín mặt sàn $2  × N$, lấy dư cho $10^9 + 7$.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i]$ là kết quả tối ưu cho bài toán con kết thúc tại bước/vị trí thứ $i$.
- **Công thức chuyển trạng thái:** Dựa trên các lựa chọn bước đi trước đó (như $dp[i] = dp[i-1] + dp[i-2]$ hoặc $\min/\max$ qua các trạng thái $j < i$).
- **Cơ sở quy hoạch động:** Khởi tạo các trường hợp biên nhỏ nhất $dp[0], dp[1]$ rõ ràng trước khi lặp.
- **Độ phức tạp:** Thời gian tối ưu $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$ (cho LIS cải tiến qua tìm kiếm nhị phân `lower_bound`), bộ nhớ $\mathcal{O}(N)$ hoặc nén về $\mathcal{O}(1)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `4` $\implies$ Đầu ra kỳ vọng: `5`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với sàn nhà kích thước $2  × 4$ ($N = 4$), có tất cả 5 cách lát kín hợp lệ: 1. Đặt 4 viên gạch dựng đứng liên tiếp. 2. Đặt 2 viên nằm n... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `5` |

*Giải thích chi tiết:* Với sàn nhà kích thước $2  × 4$ ($N = 4$), có tất cả 5 cách lát kín hợp lệ:
1. Đặt 4 viên gạch dựng đứng liên tiếp.
2. Đặt 2 viên nằm ngang ở đầu, theo sau là 2 viên dựng đứng.
3. Đặt 1 viên dựng đứng, 2 viên nằm ngang ở giữa, 1 viên dựng đứng ở cuối.
4. Đặt 2 viên dựng đứng ở đầu, theo sau là 2 viên nằm ngang.
5. Đặt 2 cặp viên nằm ngang chồng lên nhau.
Kết quả in ra là 5.

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

    if (n == 1) { cout << 1 << "\n"; return 0; }
    if (n == 2) { cout << 2 << "\n"; return 0; }

    int p2 = 1, p1 = 2, cur = 0;
    for (int i = 3; i <= n; ++i) {
        cur = (p1 + p2) % MOD;
        p2 = p1;
        p1 = cur;
    }

    cout << cur << "\n";
    return 0;
}
```
