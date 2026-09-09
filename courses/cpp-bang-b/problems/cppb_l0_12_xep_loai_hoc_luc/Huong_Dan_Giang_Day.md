# Hướng Dẫn Giảng Dạy: Xếp Loại Học Sinh & Kiểm Tra Điểm
Chuyên đề: **Chương 01 — Bài 02: Cấu Trúc Rẽ Nhánh & Cấu Trúc Vòng Lặp**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Thành thạo chuỗi câu lệnh rẽ nhánh nhiều tầng `if - else if - else`.
- Hiểu nguyên lý kiểm tra tính hợp lệ trước (Validation First) để loại trừ sớm dữ liệu sai.
- Nhận thức về thứ tự các điều kiện trong chuỗi rẽ nhánh loại trừ.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Kiểm tra tính hợp lệ: $S \in [0.0, 10.0]$. Nếu không thỏa mãn, in thông báo lỗi và kết thúc ngay.
- Khi điểm hợp lệ, do đã qua nhánh `s >= 8.0`, nên ở nhánh `else if (s >= 6.5)` ta ngầm hiểu rằng $S < 8.0$ mà không cần viết thêm `s < 8.0 && s >= 6.5`. Đây là kỹ thuật viết code gọn gàng và chuẩn mực.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Nếu ta đặt điều kiện `else if (s >= 5.0)` lên trước `else if (s >= 8.0)` thì điều gì sẽ xảy ra khi một bạn được 9.0 điểm
- Vì sao bước kiểm tra điểm hợp lệ nên được đưa lên đầu tiên

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc số thực $S$.
- Chuỗi rẽ nhánh từ thang điểm cao xuống thấp. In kết quả.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Điểm $S$ | Kiểm tra hợp lệ `s < 0 || s > 10` | Nhánh thỏa mãn | Kết quả in |
|:---:|:---:|:---:|:---:|
| `8.5` | Sai (Điểm hợp lệ) | `s >= 8.0` | `GIOI` |
| `11.5` | Đúng (Vượt ngưỡng 10) | Nhánh đầu tiên | `DIEM KHONG HOP LE` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Đảo lộn thứ tự các nhánh so sánh điểm khiến học sinh giỏi bị phân loại thành trung bình.
- Bỏ sót trường hợp biên đúng bằng ngưỡng $8.0$ hoặc $5.0$.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

double s;
if (!(cin >> s)) return 0;

if (s < 0.0 || s > 10.0) {
cout << "DIEM KHONG HOP LE\n";
} else if (s >= 8.0) {
cout << "GIOI\n";
} else if (s >= 6.5) {
cout << "KHA\n";
} else if (s >= 5.0) {
cout << "TRUNG BINH\n";
} else {
cout << "CHUA DAT\n";
}

return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính cước dịch vụ Internet hoặc biểu phí điện thoại theo các mức tiêu dùng.
