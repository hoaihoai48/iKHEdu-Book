# Hướng Dẫn Giảng Dạy: Trò Chơi Sudoku 9x9
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho bảng Sudoku $9 \times 9$ với các ô trống mang giá trị `0`. Hãy sử dụng thuật toán Quay lui để điền các chữ số từ $1$ đến $9$ vào các ô trống sao cho: mỗi hàng, mỗi cột và mỗi khối vuông con $3 \times 3$ đều chứa đủ 9 chữ số từ $1$ đến $9$ không lặp lại. Đảm bảo dữ liệu đầu vào luôn có nghiệm duy nhất.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
  - Xây dựng không gian trạng thái dạng cây tìm kiếm.
  - Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 0 6 5 0 8 4 0 0 5 2 0 0)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 0 6 5 0 8 4 0 0 5 2 0 0 0 0 0 0 0` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Tất cả các số 0 được thay thế bằng các chữ số từ 1 đến 9 thỏa mãn trọn vẹn quy tắc: hàng ngang, cột dọc và các phân vùng... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3 1 6 5 7 8 4 9 2 5 2 9 1 3 4 7 6 8` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Tất cả các số 0 được thay thế bằng các chữ số từ 1 đến 9 thỏa mãn trọn vẹn quy tắc: hàng ngang, cột dọc và các phân vùng $3 \times 3$ đều không có số nào bị lặp lại.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Tràn số nguyên:** Khi tính toán tổng, tích hoặc lũy thừa lớn hơn $2 \cdot 10^9$, bắt buộc phải sử dụng kiểu dữ liệu `long long` (64-bit) để tránh tràn số âm.
- **Bẫy 2 — Chỉ số mảng & Giới hạn biên:** Chú ý giữa đánh chỉ số 0-based (`0 .. N-1`) và 1-based (`1 .. N`). Kiểm tra kỹ trường hợp $N = 1$ hoặc giá trị biên tối đa của đề bài.
- **Bẫy 3 — Tối ưu thời gian I/O:** Luôn sử dụng `ios::sync_with_stdio(false); cin.tie(nullptr);` ở đầu hàm `main()` để đọc ghi nhanh, tránh bị TLE khi số lượng testcase lớn.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int board[9][9];
bool row_used[9][10], col_used[9][10], box_used[9][10];

bool solveSudoku(int r, int c) {
    if (r == 9) return true;
    if (c == 9) return solveSudoku(r + 1, 0);
    if (board[r][c] != 0) return solveSudoku(r, c + 1);

    int b = (r / 3) * 3 + (c / 3);
    for (int num = 1; num <= 9; ++num) {
        if (!row_used[r][num] && !col_used[c][num] && !box_used[b][num]) {
            board[r][c] = num;
            row_used[r][num] = col_used[c][num] = box_used[b][num] = true;
            if (solveSudoku(r, c + 1)) return true;
            row_used[r][num] = col_used[c][num] = box_used[b][num] = false;
            board[r][c] = 0;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (!(cin >> board[i][j])) return 0;
            int num = board[i][j];
            if (num != 0) {
                row_used[i][num] = col_used[j][num] = box_used[(i / 3) * 3 + (j / 3)][num] = true;
            }
        }
    }
    solveSudoku(0, 0);
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            cout << board[i][j] << (j == 8 ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}
```
