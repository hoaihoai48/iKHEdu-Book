# Hướng Dẫn Giảng Dạy: Truy Vết Dãy Con Tăng Dài Nhất

Chuyên đề: **Quy Hoạch Động 1 Chiều & Dãy Con Tăng (DP 1D / LIS)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm và in ra toàn bộ các phần tử thuộc về một dãy con tăng nghiêm ngặt dài nhất. Nếu có nhiều dãy con cùng đạt độ dài lớn nhất, bạn chỉ cần in ra một dãy con bất kỳ thỏa mãn.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i]$ là kết quả tối ưu cho bài toán con kết thúc tại bước/vị trí thứ $i$.
- **Công thức chuyển trạng thái:** Dựa trên các lựa chọn bước đi trước đó (như $dp[i] = dp[i-1] + dp[i-2]$ hoặc $\min/\max$ qua các trạng thái $j < i$).
- **Cơ sở quy hoạch động:** Khởi tạo các trường hợp biên nhỏ nhất $dp[0], dp[1]$ rõ ràng trước khi lặp.
- **Độ phức tạp:** Thời gian tối ưu $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$ (cho LIS cải tiến qua tìm kiếm nhị phân `lower_bound`), bộ nhớ $\mathcal{O}(N)$ hoặc nén về $\mathcal{O}(1)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `5 2 1 4 3 5` $\implies$ Đầu ra kỳ vọng: `3 2 4 5`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 2 1 4 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với dãy số gốc là $[2, 1, 4, 3, 5]$: Dãy con tăng dài nhất có độ dài bằng 3. Một dãy con hợp lệ thỏa mãn điều kiện tăng nghiêm ngặt là ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `3 2 4 5` |

*Giải thích chi tiết:* Với dãy số gốc là $[2, 1, 4, 3, 5]$:
Dãy con tăng dài nhất có độ dài bằng 3. Một dãy con hợp lệ thỏa mãn điều kiện tăng nghiêm ngặt là $[2, 4, 5]$ (hoặc $[1, 4, 5]$, $[1, 3, 5]$). Kết quả dòng 1 in ra 3, dòng 2 in ra các số 2 4 5.

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
for (int i = 0; i < n; ++i) cin >> a[i];

vector<int> dp(n, 1);
vector<int> parent(n, -1);
int max_len = 1;
int best_end = 0;

for (int i = 1; i < n; ++i) {
for (int j = 0; j < i; ++j) {
if (a[j] < a[i] && dp[j] + 1 > dp[i]) {
dp[i] = dp[j] + 1;
parent[i] = j;
}
}
if (dp[i] > max_len) {
max_len = dp[i];
best_end = i;
}
}

vector<long long> lis;
int curr = best_end;
while (curr != -1) {
lis.push_back(a[curr]);
curr = parent[curr];
}
reverse(lis.begin(), lis.end());

cout << max_len << "\n";
for (int i = 0; i < (int)lis.size(); ++i) {
cout << lis[i] << (i + 1 == (int)lis.size() "" : " ");
}
cout << "\n";
return 0;
}
```
