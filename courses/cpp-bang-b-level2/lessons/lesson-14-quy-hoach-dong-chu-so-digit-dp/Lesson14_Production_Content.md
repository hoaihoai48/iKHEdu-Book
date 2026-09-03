# Bài 14: Quy hoạch động chữ số (Digit DP)

## 1. Khái niệm & bản chất của Quy hoạch động chữ số

Quy hoạch động chữ số (Digit DP) là phương pháp chuyên dùng để giải quyết các bài toán: **Đếm số lượng số nguyên trong đoạn $[L, R]$ thỏa mãn một tính chất chữ số đặc biệt** (ví dụ: tổng chữ số bằng $K$, không chứa chữ số 4 và 7, các chữ số tăng dần, số nguyên tố, số chia hết cho $D$).

Với $L, R \le 10^{18}$, duyệt trâu từng số mất $10^{18}$ phép tính $\implies$ TLE.  
Digit DP giải quyết bài toán bằng cách:
1. Chuyển đổi bài toán đoạn: $\text{Count}([L, R]) = f(R) - f(L - 1)$ với $f(X)$ là số lượng số thỏa mãn trong $[0, X]$.
2. Biểu diễn số $X$ thành mảng các chữ số $D_0, D_1, \dots, D_{M-1}$ ($M \le 19$).
3. Xây dựng số từ trái sang phải qua hàm đệ quy có nhớ `memo[index][tight][leading_zero][state]`.

---

![Mô hình phân nhánh Digit DP](assets/l14_digit_dp_tree_visual.svg)

## 2. Các tham số trạng thái

1. **`index` (Vị trí chữ số hiện tại):** Duyệt từ chữ số đầu tiên (cao nhất) $0$ đến chữ số cuối cùng $M - 1$.
2. **`tight` (Cờ giới hạn cận trên):**
   - `tight = true`: Các chữ số phía trước đều đã chọn trùng khít với các chữ số của $X$. Chữ số hiện tại chỉ được chọn từ $0$ đến $D_{index}$.
   - `tight = false`: Đã có ít nhất một chữ số phía trước chọn nhỏ hơn $D$, số hiện tại được tự do chọn từ $0$ đến $9$.
3. **`leading_zero` (Cờ số 0 vô nghĩa ở đầu):** Xác định xem ta đã bắt đầu viết số thực tế chưa hay vẫn đang là các số 0 vô nghĩa (ảnh hưởng đến việc đếm chữ số 0).
4. **`state` (Trạng thái đặc thù của bài toán):** Ví dụ tổng các chữ số đã chọn, số dư khi chia cho $K$, mặt nạ bit của các chữ số đã xuất hiện.

---

## 3. Mẫu cài đặt chuẩn thi đấu: Đếm số có tổng chữ số bằng $S$ trong đoạn $[L, R]$

```cpp
#include <bits/stdc++.h>
using namespace std;

string num_str;
long long dp[20][2][200]; // dp[index][tight][sum]
int target_sum;

long long digit_dp(int idx, bool tight, int current_sum) {
    if (idx == num_str.size()) {
        return (current_sum == target_sum ? 1 : 0);
    }
    if (dp[idx][tight][current_sum] != -1) {
        return dp[idx][tight][current_sum];
    }

    int limit = (tight ? (num_str[idx] - '0') : 9);
    long long total = 0;

    for (int digit = 0; digit <= limit; ++digit) {
        bool next_tight = tight && (digit == limit);
        total += digit_dp(idx + 1, next_tight, current_sum + digit);
    }

    return dp[idx][tight][current_sum] = total;
}

long long count_valid(long long x) {
    if (x < 0) return 0;
    num_str = to_string(x);
    memset(dp, -1, sizeof(dp));
    return digit_dp(0, true, 0);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R >> target_sum)) return 0;

    cout << count_valid(R) - count_valid(L - 1) << "\n";
    return 0;
}
```

---

## 4. Ranh giới áp dụng

| Dạng Bài | Cận Biên $R$ | Kỹ Thuật Tối Ưu | Độ Phức Tạp |
|---|---|---|:---:|
| Đếm số theo tính chất chữ số | $R \le 10^{18}$ | Digit DP | $\mathcal{O}(\text{Length}(R) \times \text{States} \times 10) \approx 19 \times 200 \times 10 < 10^5$ |
| Đếm số theo tính chất đại số lớn | $R \le 10^9$ | Sàng / Toán học / Bù trừ PIE | $\mathcal{O}(\sqrt{R})$ hoặc $\mathcal{O}(1)$ |

---

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Cờ Tight — Logic):
Ý nghĩa của cờ `tight` trong Digit DP là gì?
- **A.** Đánh dấu số nguyên tố.
- **B.** **[Đáp án đúng]** Cho biết chữ số đang xét có bị giới hạn bởi chữ số tương ứng của cận trên $R$ hay không.
- **C.** Kiểm tra số âm.
- **D.** Đếm số lượng chữ số 0.

> *Giải thích:* Nếu `tight = true` thì chữ số chỉ được chạy từ $0 \dots D_{idx}$. Nếu `tight = false` thì được chạy tự do từ $0 \dots 9$.

#### Câu 2 (Quy tắc trừ đoạn — Invariant):
Để đếm số lượng số thỏa mãn tính chất $P$ trong đoạn $[A, B]$ ($A \le B$), công thức chuẩn là:
- **A.** `f(B) - f(A)`
- **B.** **[Đáp án đúng]** `f(B) - f(A - 1)`
- **C.** `f(B - A)`
- **D.** `f(B) + f(A)`

> *Giải thích:* $f(B)$ đếm các số trong $[0, B]$, $f(A-1)$ đếm các số trong $[0, A-1]$, hiệu của chúng là đoạn $[A, B]$.

---

## Ma trận bài tập thực hành (P0 → P5)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB2-L14-01` | **Đếm Số Không Chứa Chữ Số 4 Và 7** | `P0` | $L, R \le 10^{18}$ | Digit DP với cờ `tight` cơ bản |
| 02 | `CPPB2-L14-02` | **Tổng Các Chữ Số Bằng K Trong Đoạn [L, R]** | `P0` | $L, R \le 10^{18}, K \le 200$ | Digit DP lưu trạng thái `current_sum` |
| 03 | `CPPB2-L14-03` | **Đếm Số Lượng Chữ Số 0 Xuất Hiện** | `P1` | $L, R \le 10^{18}$ | Digit DP với cờ `leading_zero` |
| 04 | `CPPB2-L14-04` | **Số Có Các Chữ Số Tăng Ngặt** | `P1` | $L, R \le 10^{18}$ | Digit DP lưu chữ số liền trước `last_digit` |
| 05 | `CPPB2-L14-05` | **Số Chia Hết Cho Tổng Các Chữ Số Của Chính Nó** | `P2` | $L, R \le 10^{18}$ | Cố định tổng chữ số từ $1 \dots 162$ + Digit DP |
| 06 | `CPPB2-L14-06` | **Đếm Số Đối Xứng (Palindrome Numbers) Trong Đoạn** | `P2` | $L, R \le 10^{18}$ | Digit DP xây dựng nửa đầu và nửa sau |
| 07 | `CPPB2-L14-07` | **Số Không Chứa Hai Chữ Số Giống Nhau Liền Kề** | `P2` | $L, R \le 10^{18}$ | Duy trì điều kiện $D_{cur} \ne D_{prev}$ |
| 08 | `CPPB2-L14-08` | **Số Chứa Đầy Đủ Các Chữ Số Từ 0 Đến 9** | `P3` | $L, R \le 10^{18}$ | Digit DP kết hợp Bitmask lưu tập chữ số |
| 09 | `CPPB2-L14-09` | **Số Có Tích Các Chữ Số Bằng K** | `P3` | $L, R \le 10^{18}, K \le 10^9$ | Digit DP kiểm tra $K$ chỉ có ước nguyên tố 2, 3, 5, 7 |
| 10 | `CPPB2-L14-10` | **Tổng Giá Trị Các Số Thỏa Mãn Tính Chất Chữ Số** | `P3` | $L, R \le 10^{18}, M = 10^9+7$ | Digit DP trả về cặp `{số_lượng, tổng_giá_trị}` |
| 11 | `CPPB2-L14-11` | **Đếm Số Tự Mãn (Số Armstrong / Narcissistic) Trong Đoạn** | `P4` | $L, R \le 10^{18}$ | Digit DP tính tổng lũy thừa bậc $K$ chữ số |
| 12 | `CPPB2-L14-12` | **Đếm Số Đẹp Có Hiệu Hai Chữ Số Kề Nhau $\ge 2$ (Số Stepping)** | `P4` | $L, R \le 10^{18}$ | Digit DP kiểm tra $\vert D_i - D_{i-1} \vert \ge 2$ |
| 13 | `CPPB2-L14-13` | **Số Có Tổng Bình Phương Các Chữ Số Là Số Nguyên Tố** | `P4` | $L, R \le 10^{18}$ | Sàng nguyên tố kết hợp Digit DP |
| 14 | `CPPB2-L14-14` | **Tìm Số Thỏa Mãn Điều Kiện Chữ Số Thứ K Nhỏ Nhất** | `P5` | $K \le 10^{18}$ | Chặt nhị phân kết quả kết hợp hàm đếm Digit DP |
| 15 | `CPPB2-L14-15` | **Số Chia Hết Cho Tất Cả Các Chữ Số Khác Không Của Nó** | `P5` | $L, R \le 10^{18}$ | Digit DP trạng thái $lcm$ và số dư theo $2520$ |
| 16 | `CPPB2-L14-16` | **Tổng XOR Chữ Số Của Mọi Số Trong Đoạn $[L, R]$** | `P5` | $L, R \le 10^{18}$ | Digit DP đa chiều tính tổng tích lũy XOR |
