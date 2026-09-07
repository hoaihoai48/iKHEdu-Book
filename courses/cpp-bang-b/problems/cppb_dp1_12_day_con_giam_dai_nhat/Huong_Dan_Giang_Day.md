# Hướng Dẫn Giảng Dạy: Dãy Con Giảm Dài Nhất (LDS)

Chuyên đề: **Quy Hoạch Động 1 Chiều & Dãy Con Tăng (DP 1D / LIS)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm độ dài của dãy con giảm nghiêm ngặt dài nhất.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i]$ là kết quả tối ưu cho bài toán con kết thúc tại bước/vị trí thứ $i$.
- **Công thức chuyển trạng thái:** Dựa trên các lựa chọn bước đi trước đó (như $dp[i] = dp[i-1] + dp[i-2]$ hoặc $\min/\max$ qua các trạng thái $j < i$).
- **Cơ sở quy hoạch động:** Khởi tạo các trường hợp biên nhỏ nhất $dp[0], dp[1]$ rõ ràng trước khi lặp.
- **Độ phức tạp:** Thời gian tối ưu $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$ (cho LIS cải tiến qua tìm kiếm nhị phân `lower_bound`), bộ nhớ $\mathcal{O}(N)$ hoặc nén về $\mathcal{O}(1)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `5 10 9 2 5 3 7 101 18` $\implies$ Đầu ra kỳ vọng: `4`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 10 9 2 5 3 7 101 18` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với dãy 8 số nguyên $[10, 9, 2, 5, 3, 7, 101, 18]$: Một dãy con giảm nghiêm ngặt dài nhất có thể trích xuất là $[10, 9, 5, 3]$ (hoặc $[... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `4` |

*Giải thích chi tiết:* Với dãy 8 số nguyên $[10, 9, 2, 5, 3, 7, 101, 18]$:
Một dãy con giảm nghiêm ngặt dài nhất có thể trích xuất là $[10, 9, 5, 3]$ (hoặc $[10, 9, 7, 3]$). Độ dài lớn nhất đạt được là 4.

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
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] = -a[i]; // Đảo dấu để tìm LIS tương đương LDS
    }

    vector<long long> tails;
    for (int i = 0; i < n; ++i) {
        auto it = lower_bound(tails.begin(), tails.end(), a[i]);
        if (it == tails.end()) {
            tails.push_back(a[i]);
        } else {
            *it = a[i];
        }
    }

    cout << tails.size() << "\n";
    return 0;
}
```
