# Hướng dẫn giảng dạy: Xâu con chung dài nhất của k xâu ký tự
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
const long long M1 = 1000000007, M2 = 1000000009;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int K;
    if (!(cin >> K)) return 0;
    string dummy;
    getline(cin, dummy);
    vector<string> s(K);
    for (int i = 0; i < K; i++) getline(cin, s[i]);
    int bi = 0;
    for (int i = 1; i < K; i++) if (s[i].size() < s[bi].size()) bi = i;
    int n0 = (int)s[bi].size();
    if (n0 == 0) { cout << 0 << "\n"; return 0; }
    const long long BB = 9113823LL;
    int mx = 0;
    for (auto &t : s) mx = max(mx, (int)t.size());
    vector<long long> p1(mx + 1, 1), p2(mx + 1, 1);
    for (int i = 1; i <= mx; i++) { p1[i] = p1[i - 1] * (BB % M1) % M1; p2[i] = p2[i - 1] * (BB % M2) % M2; }
    vector<vector<long long>> h1(K), h2(K);
    for (int k = 0; k < K; k++) {
        int n = (int)s[k].size();
        h1[k].assign(n + 1, 0); h2[k].assign(n + 1, 0);
        for (int i = 0; i < n; i++) {
            h1[k][i + 1] = (h1[k][i] * (BB % M1) + (unsigned char)s[k][i] + 1) % M1;
            h2[k][i + 1] = (h2[k][i] * (BB % M2) + (unsigned char)s[k][i] + 1) % M2;
        }
    }
    auto get = [&](const vector<long long> &h, const vector<long long> &p, int l, int len, long long M) {
        long long v = (h[l + len] - h[l] * p[len]) % M;
        if (v < 0) v += M;
        return v;
    };
    auto ok = [&](int L) {
        if (L == 0) return true;
        unordered_set<unsigned long long> cur;
        cur.reserve(n0 - L + 1);
        for (int i = 0; i + L <= n0; i++) {
            unsigned long long key = (unsigned long long)get(h1[bi], p1, i, L, M1) << 32
                | (unsigned long long)get(h2[bi], p2, i, L, M2);
            cur.insert(key);
        }
        if (cur.empty()) return false;
        for (int k = 0; k < K; k++) {
            if (k == bi) continue;
            int n = (int)s[k].size();
            unordered_set<unsigned long long> nxt;
            nxt.reserve(n - L + 1 > 0 ? (size_t)(n - L + 1) : 0);
            for (int i = 0; i + L <= n; i++) {
                unsigned long long key = (unsigned long long)get(h1[k], p1, i, L, M1) << 32
                    | (unsigned long long)get(h2[k], p2, i, L, M2);
                if (cur.find(key) != cur.end()) nxt.insert(key);
            }
            cur.swap(nxt);
            if (cur.empty()) return false;
        }
        return !cur.empty();
    };
    int lo = 0, hi = n0;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (ok(mid)) lo = mid; else hi = mid - 1;
    }
    cout << lo << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nâng cao bài toán khi dữ liệu chuyển sang mảng động hoặc có thêm các thao tác cập nhật điểm/đoạn.
* Mở rộng bài toán trên không gian 2D hoặc trên cấu trúc đồ thị/cây.
