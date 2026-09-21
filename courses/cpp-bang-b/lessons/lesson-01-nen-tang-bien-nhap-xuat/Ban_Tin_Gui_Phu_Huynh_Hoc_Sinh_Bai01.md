# BẢN TIN TỔNG KẾT BÀI HỌC VÀ BÀI TẬP THỰC HÀNH C++ (GỬI PHỤ HUYNH & HỌC SINH)
**Khóa học:** C++ Lập trình thi đấu iKHEDU - Bảng B  
**Bài 01:** Biến, Kiểu dữ liệu, Toán tử & Nhập xuất an toàn

---

## 🌟 PHẦN 1: HÌNH ẢNH TỔNG KẾT BÀI HỌC VÀ BÀI TẬP (BẢN GỐC ĐÃ SỬA RÕ CHUẨN NÉT)

> Hình ảnh tổng kết chính thức gửi phụ huynh và học sinh (giữ nguyên 100% hình gốc, đã sửa rõ nét hoàn toàn mã nguồn bài 5):

![Tổng kết buổi học hôm nay - Bài 01 C++](/Users/vu/Developer/ikhEdu_lessons/assets/Noi_dung_bai_hoc_20_9_clarified.png)

---

## 📚 PHẦN 2: TÓM TẮT NỘI DUNG BÀI HỌC TRỌNG TÂM

### 1. Khung tư duy lập trình: Mô hình 3 bước (Input – Process – Output)
Mọi bài toán lập trình đều giải quyết theo chu trình khép kín:
1. **Input (Dữ liệu vào):** Nhận thông tin từ bàn phím/đề bài qua lệnh `cin`.
2. **Process (Xử lý):** Tính toán theo công thức, lưu trữ vào biến thích hợp.
3. **Output (Kết quả ra):** In kết quả ra màn hình chuẩn qua lệnh `cout`.

---

### 2. Cấu trúc chương trình C++ chuẩn thi đấu (Boilerplate)
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    // Fast I/O giúp chạy nhanh, tối ưu thời gian thi đấu
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Thân chương trình: Nhập -> Xử lý -> Xuất
    return 0;
}
```

---

### 3. Bảng các kiểu dữ liệu thường dùng
| Kiểu dữ liệu | Kích thước | Khoảng giá trị | Ứng dụng thực tế |
|---|:---:|---|---|
| `int` | 4 bytes | Khoảng $\pm 2 \times 10^9$ (dưới 2 tỷ) | Đếm số lượng, bài toán nhỏ |
| `long long` | 8 bytes | Khoảng $\pm 9 \times 10^{18}$ (9 tỷ tỷ) | **Tổng, tích hai số, tránh tràn số** |
| `double` | 8 bytes | Số thực (khoảng 15 chữ số) | Điểm trung bình, diện tích hình tròn |
| `char` | 1 byte | 1 ký tự (`'A'`, `'z'`, `'9'`) | Ký tự trong bảng mã ASCII |
| `string` | Động | Chuỗi nhiều ký tự | Họ tên, văn bản |

> **Quy tắc vàng:** Luôn dùng `long long` khi bài toán có phép nhân hoặc tính tổng lớn để phòng ngừa 100% hiện tượng tràn số nguyên!

---

## 🎯 PHẦN 3: NỘI DUNG 5 BÀI TẬP VÀ MÃ NGUỒN GIẢI CHUẨN C++

### Bài 1: Tính tổng hai số (`cppb_l0_01_tinh_tong_hai_so`)
- **Nhiệm vụ:** Cho 2 số nguyên $A, B$ (có thể lên tới $10^9$). Hãy in ra tổng $A + B$.
- **Bẫy lỗi:** $A + B$ có thể đạt $2 \times 10^9$ (nguy cơ tràn `int`), bắt buộc dùng `long long`.
- **Mã nguồn giải chuẩn:**
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    cout << a + b << '\n';
    return 0;
}
```

---

### Bài 2: Chu vi & Diện tích hình chữ nhật (`cppb_l0_02_dien_tich_hinh_chu_nhat`)
- **Nhiệm vụ:** Cho chiều dài $a$ và chiều rộng $b$. In chu vi và diện tích cách nhau một khoảng trắng.
- **Công thức:** Chu vi = $2 \times (a + b)$, Diện tích = $a \times b$.
- **Mã nguồn giải chuẩn:**
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    long long perimeter = 2 * (a + b);
    long long area = a * b;

    cout << perimeter << ' ' << area << '\n';
    return 0;
}
```

---

### Bài 3: Trung bình cộng ba số (`cppb_l0_03_trung_binh_ba_so`)
- **Nhiệm vụ:** Cho ba số thực $a, b, c$. Tính điểm trung bình cộng và in lấy đúng 2 chữ số thập phân.
- **Lưu ý:** Dùng kiểu `double` và chia cho `3.0` (không chia cho số nguyên `3`), kết hợp `fixed` và `setprecision(2)`.
- **Mã nguồn giải chuẩn:**
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    double avg = (a + b + c) / 3.0;

    cout << fixed << setprecision(2) << avg << '\n';
    return 0;
}
```

---

### Bài 4: Chữ số hàng chục và hàng đơn vị (`cppb_l0_04_chu_so_hang_don_vi`)
- **Nhiệm vụ:** Cho số nguyên $n \ge 10$. In ra chữ số hàng chục và chữ số hàng đơn vị cách nhau bởi dấu cách.
- **Quy tắc toán học:**
  - Hàng đơn vị: `n % 10`
  - Hàng chục: `(n / 10) % 10`
- **Mã nguồn giải chuẩn:**
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    int don_vi = n % 10;
    int hang_chuc = (n / 10) % 10;

    cout << hang_chuc << ' ' << don_vi << '\n';
    return 0;
}
```

---

### Bài 5: Tổng các chữ số của số có 3 chữ số (`cppb_l0_05_tong_chu_so`)
- **Nhiệm vụ:** Cho số nguyên có 3 chữ số $n$ ($100 \le n \le 999$). Hãy tính tổng 3 chữ số của $n$.
- **Quy tắc tách số:**
  - Chữ số hàng trăm: `n / 100`
  - Chữ số hàng chục: `(n / 10) % 10`
  - Chữ số hàng đơn vị: `n % 10`
- **Mã nguồn giải chuẩn:**
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int tram = n / 100;
    int chuc = (n / 10) % 10;
    int don_vi = n % 10;

    cout << tram + chuc + don_vi << '\n';
    return 0;
}
```

---
*Tài liệu học tập được chuẩn hóa theo tiêu chuẩn thi đấu iKHEDU - DKOJ.*
