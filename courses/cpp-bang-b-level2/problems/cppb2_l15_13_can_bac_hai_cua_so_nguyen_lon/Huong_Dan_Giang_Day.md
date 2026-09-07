# Hướng dẫn giảng dạy: Căn bậc hai của số nguyên lớn
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
const int BASE = 1000000000;
using Big = vector<int>; // little-endian
int cmp(const Big &a, const Big &b) {
    if (a.size() != b.size()) return a.size() < b.size() ? -1 : 1;
    for (int i = (int)a.size() - 1; i >= 0; i--) if (a[i] != b[i]) return a[i] < b[i] ? -1 : 1;
    return 0;
}
Big fromStr(const string &s) {
    Big a;
    for (int i = (int)s.size(); i > 0; i -= 9) {
        int l = max(0, i - 9);
        a.push_back(stoi(s.substr(l, i - l)));
    }
    while (a.size() > 1 && a.back() == 0) a.pop_back();
    return a;
}
string toStr(const Big &a) {
    string s = to_string(a.back());
    char buf[16];
    for (int i = (int)a.size() - 2; i >= 0; i--) {
        // 9 digits with leading zeros
        int v = a[i];
        string t(9, '0');
        for (int z = 8; z >= 0; z--) { t[z] = char('0' + v % 10); v /= 10; }
        s += t;
    }
    (void)buf;
    return s;
}
Big addB(const Big &a, const Big &b) {
    Big c; c.reserve(max(a.size(), b.size()) + 1);
    long long carry = 0;
    for (size_t i = 0; i < max(a.size(), b.size()) || carry; i++) {
        long long v = carry;
        if (i < a.size()) v += a[i];
        if (i < b.size()) v += b[i];
        c.push_back(int(v % BASE)); carry = v / BASE;
    }
    return c;
}
Big div2B(const Big &a) {
    Big c(a.size());
    long long carry = 0;
    for (int i = (int)a.size() - 1; i >= 0; i--) {
        long long v = carry * BASE + a[i];
        c[i] = int(v / 2); carry = v % 2;
    }
    while (c.size() > 1 && c.back() == 0) c.pop_back();
    return c;
}
Big mulB(const Big &a, const Big &b) {
    if ((a.size() == 1 && a[0] == 0) || (b.size() == 1 && b[0] == 0)) return Big{0};
    vector<long long> t(a.size() + b.size(), 0);
    for (size_t i = 0; i < a.size(); i++)
        for (size_t j = 0; j < b.size(); j++) t[i + j] += (long long)a[i] * b[j];
    Big c(t.size());
    long long carry = 0;
    for (size_t i = 0; i < t.size(); i++) {
        long long v = t[i] + carry;
        c[i] = int(v % BASE); carry = v / BASE;
    }
    while (carry) { c.push_back(int(carry % BASE)); carry /= BASE; }
    while (c.size() > 1 && c.back() == 0) c.pop_back();
    return c;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    Big A = fromStr(s);
    int half = ((int)s.size() + 1) / 2;
    Big lo{0}, hi = fromStr(string("1") + string(half, '0'));
    while (cmp(lo, hi) < 0) {
        Big mid = div2B(addB(lo, hi));
        if (cmp(mid, lo) == 0) { // lo and hi adjacent: test hi directly
            if (cmp(mulB(hi, hi), A) <= 0) lo = hi;
            break;
        }
        if (cmp(mulB(mid, mid), A) <= 0) lo = mid;
        else {
            Big m = mid; // m = mid - 1 (mid >= 1 here)
            int i = 0;
            while (i < (int)m.size() && m[i] == 0) { m[i] = BASE - 1; i++; }
            if (i < (int)m.size()) m[i]--;
            while (m.size() > 1 && m.back() == 0) m.pop_back();
            hi = m;
        }
    }
    cout << toStr(lo) << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nâng cao bài toán khi dữ liệu chuyển sang mảng động hoặc có thêm các thao tác cập nhật điểm/đoạn.
* Mở rộng bài toán trên không gian 2D hoặc trên cấu trúc đồ thị/cây.
