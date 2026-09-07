# Hướng Dẫn Giảng Dạy: Cài Đặt Hàng Đợi Cơ Bản

Chuyên đề: **Cấu Trúc Dữ Liệu Hàng Đợi (Queue, Deque) & Monotonic Deque**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách $Q$ thao tác thuộc 3 loại: `1 x` (thêm $x$ vào cuối hàng), `2` (loại bỏ phần tử đầu hàng nếu hàng không rỗng), `3` (in ra phần tử đầu hàng, nếu rỗng in ra `-1`). Hãy lập trình mô phỏng lại hàng đợi và in ra kết quả cho các thao tác loại 3.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý Hàng đợi chuẩn (Queue):** Vào trước Ra trước (FIFO), là cấu trúc nền tảng phục vụ duyệt đồ thị theo chiều rộng (BFS).
- **Hàng đợi hai đầu (Deque) & Monotonic Deque:**
  * Hỗ trợ thêm/xoá ở cả hai đầu trong $\mathcal{O}(1)$.
  * Khi trượt cửa sổ kích thước $K$, lưu chỉ số phần tử trong deque sao cho giá trị tương ứng luôn đơn điệu.
  * Loại bỏ phần tử trượt ra khỏi cửa sổ ở đầu trước (`pop_front()`) và loại bỏ phần tử kém tối ưu ở đầu sau (`pop_back()`).
- **Độ phức tạp:** Thời gian $\mathcal{O}(N)$, không gian phụ trợ $\mathcal{O}(K)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `5 1 10 1 20 3 2 3` $\implies$ Đầu ra kỳ vọng: `10 20`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 1 10 1 20 3 2 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với chuỗi thao tác: thêm 10, thêm 20, truy vấn đầu hàng -> in ra 10; phục vụ đầu hàng (loại 10), truy vấn đầu hàng -> in ra 20. | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `10 20` |

*Giải thích chi tiết:* Với chuỗi thao tác: thêm 10, thêm 20, truy vấn đầu hàng -> in ra 10; phục vụ đầu hàng (loại 10), truy vấn đầu hàng -> in ra 20.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Lưu giá trị thay vì lưu chỉ số vị trí (index) trong Deque: Phải lưu index để kiểm tra điều kiện phần tử đã trượt ra khỏi cửa sổ $i - K$ hay chưa (`dq.front() <= i - K`).
* Quên kiểm tra `!dq.empty()` trước khi truy xuất `dq.front()` hoặc `dq.back()` gây crash chương trình.
* Không khởi tạo kết quả cho $K-1$ vị trí đầu tiên trước khi bắt đầu ghi nhận đáp án từ vị trí thứ $K$.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    queue<long long> qu;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) { // Push x
            long long x;
            cin >> x;
            qu.push(x);
        } else if (type == 2) { // Pop
            if (!qu.empty()) qu.pop();
        } else if (type == 3) { // Front
            if (qu.empty()) cout << "EMPTY\n";
            else cout << qu.front() << "\n";
        }
    }
    return 0;
}
```
