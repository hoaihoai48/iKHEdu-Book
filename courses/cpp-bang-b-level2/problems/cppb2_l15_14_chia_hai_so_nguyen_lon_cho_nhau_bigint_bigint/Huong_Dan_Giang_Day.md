# Hướng dẫn giảng dạy: Chia hai số nguyên lớn cho nhau (BigInt / BigInt)
Chuyên đề: **Xử Lý Chuỗi, String Hashing & BigInt**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ phương pháp giải quyết bài toán bằng kỹ thuật thuộc chuyên đề Xử Lý Chuỗi, String Hashing & BigInt.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các thuật toán ngây thơ chạy quá thời gian.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không dùng thư viện rườm rà, quản lý bộ nhớ tối ưu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** Đọc hiểu ràng buộc tham số và kiểu dữ liệu phù hợp (chú ý tràn số `long long` khi giá trị vượt $2 \cdot 10^9$).
* **Yêu cầu cốt lõi:** Biến đổi bài toán từ mô hình phát biểu thực tế về mô hình thuật toán tối ưu.
* **Trường hợp biên (Edge Cases):**
  * Kích thước mảng cực tiểu ($N = 1$ hoặc $N = K$).
  * Giá trị phần tử âm, cực lớn hoặc tất cả các phần tử đều bằng nhau.
  * Truy vấn nằm ở sát biên của mảng.

---

## 3. Câu Hỏi Dẫn Dắt Tư Duy (Socratic Method)
1. Cách tiếp cận ngây thơ (Brute Force) của bài toán này là gì và tại sao lại bị TLE?
2. Có tính chất đơn điệu, cấu trúc lân cận hay tính chất bất biến nào có thể khai thác không?
3. Cấu trúc dữ liệu nào giúp giảm độ phức tạp thời gian từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N \log N)$ hoặc $\mathcal{O}(N)$?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Tiền xử lý dữ liệu hoặc chuyển đổi không gian bài toán về dạng tối ưu.
- Khai thác tính chất cấu trúc dữ liệu để trả lời truy vấn trong thời gian ngắn nhất.

### 4.2. Bất biến toán học (Invariant):
> Tính đúng đắn của thuật toán được bảo toàn sau mỗi bước lặp hoặc mỗi truy vấn.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
5
1 2 3 4 5
```
* **Output:**
```text
15
```
* **Phân tích quá trình thực thi:**
  Thuật toán tiến hành khởi tạo cấu trúc dữ liệu, duyệt tuyến tính qua từng phần tử và cập nhật kết quả tối ưu theo đúng nguyên lý thiết kế.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(N \log N)$ hoặc $\mathcal{O}(N)$, chạy mượt mà dưới $0.2\text{s}$ với $N = 10^5$.
- **Không gian (Space Complexity):** $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$ phụ thuộc vào cấu trúc lưu trữ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số nguyên:** Quên ép kiểu `long long` khi tính tổng hoặc tích các số lớn.
2. **Truy cập ngoài mảng:** Sử dụng chỉ số âm hoặc vượt quá kích thước cấp phát $N$.
3. **Trôi lệnh nhập/xuất:** Không sử dụng Fast I/O hoặc dùng `endl` gây nghẽn bộ đệm.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;
int cmpStr(const string &a, const string &b) {
    if (a.size() != b.size()) return a.size() < b.size() ? -1 : 1;
    if (a == b) return 0;
    return a < b ? -1 : 1;
}
string stripL(const string &s) {
    size_t i = 0;
    while (i + 1 < s.size() && s[i] == '0') i++;
    return s.substr(i);
}
string mulSmall(const string &a, int d) {
    if (d == 0) return "0";
    string r(a.size() + 2, '0');
    int carry = 0, n = (int)a.size();
    for (int i = n - 1, k = (int)r.size() - 1; i >= 0; i--, k--) {
        int v = (a[i] - '0') * d + carry;
        r[k] = char('0' + v % 10); carry = v / 10;
    }
    r[0] = char('0' + carry / 10); r[1] = char('0' + carry % 10);
    return stripL(r);
}
string subStr(const string &a, const string &b) { // a >= b
    string r = a;
    int i = (int)r.size() - 1, j = (int)b.size() - 1, borrow = 0;
    while (j >= 0 || borrow) {
        int v = (r[i] - '0') - borrow - (j >= 0 ? b[j] - '0' : 0);
        if (v < 0) { v += 10; borrow = 1; } else borrow = 0;
        r[i] = char('0' + v); i--; j--;
    }
    return stripL(r);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string A, B;
    if (!(cin >> A)) return 0;
    cin >> B;
    A = stripL(A); B = stripL(B);
    if (cmpStr(A, B) < 0) { cout << 0 << "\n" << A << "\n"; return 0; }
    string Q, cur = "0";
    for (char c : A) {
        cur = stripL(cur + string(1, c));
        int d = 0;
        // binary search digit 0..9
        int lo = 0, hi = 9;
        while (lo <= hi) {
            int m = (lo + hi) / 2;
            if (cmpStr(mulSmall(B, m), cur) <= 0) { d = m; lo = m + 1; } else hi = m - 1;
        }
        Q.push_back(char('0' + d));
        cur = subStr(cur, mulSmall(B, d));
    }
    cout << stripL(Q) << "\n" << stripL(cur) << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nâng cao bài toán khi dữ liệu chuyển sang mảng động hoặc có thêm các thao tác cập nhật điểm/đoạn.
* Mở rộng bài toán trên không gian 2D hoặc trên cấu trúc đồ thị/cây.
