# Hướng Dẫn Giảng Dạy: Sinh Chuỗi Số Nhị Phân Bằng Queue

Chuyên đề: **Cấu Trúc Dữ Liệu Hàng Đợi (Queue, Deque) & Monotonic Deque**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho số nguyên dương $N$. Hãy lập trình sinh và in ra chuỗi biểu diễn nhị phân của tất cả các số từ $1$ đến $N$, các chuỗi cách nhau bởi khoảng trắng.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý Hàng đợi chuẩn (Queue):** Vào trước Ra trước (FIFO), là cấu trúc nền tảng phục vụ duyệt đồ thị theo chiều rộng (BFS).
- **Hàng đợi hai đầu (Deque) & Monotonic Deque:**
  * Hỗ trợ thêm/xoá ở cả hai đầu trong $\mathcal{O}(1)$.
  * Khi trượt cửa sổ kích thước $K$, lưu chỉ số phần tử trong deque sao cho giá trị tương ứng luôn đơn điệu.
  * Loại bỏ phần tử trượt ra khỏi cửa sổ ở đầu trước (`pop_front()`) và loại bỏ phần tử kém tối ưu ở đầu sau (`pop_back()`).
- **Độ phức tạp:** Thời gian $\mathcal{O}(N)$, không gian phụ trợ $\mathcal{O}(K)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `4` $\implies$ Đầu ra kỳ vọng: `1 10 11 100`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với $N = 5$, danh sách biểu diễn nhị phân của các số từ 1 đến 5 là: 1 (số 1), 10 (số 2), 11 (số 3), 100 (số 4), 101 (số 5). | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `1 10 11 100` |

*Giải thích chi tiết:* Với $N = 5$, danh sách biểu diễn nhị phân của các số từ 1 đến 5 là: 1 (số 1), 10 (số 2), 11 (số 3), 100 (số 4), 101 (số 5).

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

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    queue<string> q;
    q.push("1");

    for (int i = 1; i <= n; ++i) {
        string s = q.front();
        q.pop();

        cout << s << (i == n ? "" : " ");

        q.push(s + "0");
        q.push(s + "1");
    }
    cout << "\n";
    return 0;
}
```
