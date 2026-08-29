# THUẬT TOÁN SẮP XẾP
## Tối Ưu Hóa Dữ Liệu Với sort & Custom Comparator Trong C++

---

## 1. Khái Niệm & Bản Chất Của Sắp Xếp Trong Tối Ưu Thuật Toán

**Sắp xếp (Sorting)** là quá trình tái sắp đặt các phần tử trong một tập dữ liệu theo một trật tự xác định (thường là tăng dần hoặc giảm dần theo một hoặc nhiều tiêu chí).

Trong lập trình thi đấu và khoa học máy tính, sắp xếp không đơn thuần là định dạng lại dữ liệu hiển thị, mà là một **phép biến đổi cấu trúc dữ liệu** nhằm:
* **Tạo tính đơn điệu (Monotonicity):** Đưa dãy số về trạng thái có trật tự để áp dụng các kỹ thuật tối ưu như *Hai con trỏ (Two Pointers)*, *Tìm kiếm nhị phân (Binary Search)* hoặc *Tham lam (Greedy)*.
* **Khai thác tính chất lân cận (Adjacency Property):** Gom các phần tử có giá trị bằng nhau hoặc gần nhau nhất về các vị trí liền kề, giúp giảm không gian tìm kiếm từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N)$.

---

## 2. Tính Chất Lân Cận & Chứng Minh Toán Học

### 2.1. Định lý về cặp phần tử có khoảng cách nhỏ nhất
> **Định lý:** Trong một tập hợp các số thực $A = \{A_1, A_2, \dots, A_N\}$, sau khi sắp xếp tăng dần $A_1 \le A_2 \le \dots \le A_N$, giá trị nhỏ nhất của $|A_i - A_j|$ ($i \neq j$) luôn đạt được tại ít nhất một cặp phần tử kề nhau $(A_k, A_{k+1})$.

### 2.2. Chứng minh toán học
Xét hai chỉ số bất kỳ $i < j$. Nếu $j > i + 1$ (hai phần tử không kề nhau), tồn tại phần tử trung gian $A_{i+1}$ thỏa mãn:
$$A_i \le A_{i+1} \le A_j$$

Hiệu khoảng cách giữa $A_i$ và $A_j$:
$$A_j - A_i = (A_j - A_{i+1}) + (A_{i+1} - A_i)$$

Vì $A_j - A_{i+1} \ge 0$, ta luôn có:
$$A_j - A_i \ge A_{i+1} - A_i$$

**Hệ quả:** Mọi cặp phần tử không kề nhau đều có khoảng cách lớn hơn hoặc bằng khoảng cách của cặp kề nhau $(A_i, A_{i+1})$. Do đó, để tìm khoảng cách nhỏ nhất, ta chỉ cần duyệt qua $N - 1$ cặp kề nhau sau khi sắp xếp.

#### 💡 Ví Dụ Minh Họa 1: Tìm khoảng cách nhỏ nhất giữa hai phần tử
Cho mảng gồm 6 phần tử chưa sắp xếp: $A = [15, 3, 9, 22, 4, 11]$

1. **Bước 1: Sắp xếp tăng dần $\mathcal{O}(N \log N)$:**
   $$A = [3, 4, 9, 11, 15, 22]$$
2. **Bước 2: Quét $N - 1 = 5$ cặp kề nhau $\mathcal{O}(N)$:**

| Cặp Kề Nhau $(A_i, A_{i+1})$ | Tính Hiệu Số $A_{i+1} - A_i$ | Hiệu Nhỏ Nhất Tạm Thời ($\min$) |
|:---:|:---:|:---:|
| $(3, 4)$ | $4 - 3 = \mathbf{1}$ | $\mathbf{1}$ |
| $(4, 9)$ | $9 - 4 = 5$ | $1$ |
| $(9, 11)$ | $11 - 9 = 2$ | $1$ |
| $(11, 15)$ | $15 - 11 = 4$ | $1$ |
| $(15, 22)$ | $22 - 15 = 7$ | $1$ |

$$\implies \text{Kết quả: Khoảng cách nhỏ nhất là } \mathbf{1} \text{ (giữa cặp 3 và 4), tìm ra trong đúng 5 phép trừ!}$$

---

## 3. Các Ứng Dụng Thuật Toán Kinh Điển Của Sắp Xếp

| Dạng Bài Toán | Cách Xử Lý Chưa Sắp Xếp | Sau Khi Sắp Xếp $\mathcal{O}(N \log N)$ | Độ Phức Tạp Tối Ưu |
|---|---|---|:---:|
| **Tìm cặp có hiệu nhỏ nhất** | Duyệt mọi cặp $(i, j)$ | So sánh $N-1$ cặp kề $(A_i, A_{i+1})$ | $\mathcal{O}(N \log N)$ |
| **Đếm số giá trị phân biệt** | Quét trùng lặp từng phần tử | Đếm khi $A_i \neq A_{i-1}$ | $\mathcal{O}(N \log N)$ |
| **Tìm phần tử có tần suất cực đại** | Bảng đếm / Quét lặp $\mathcal{O}(N^2)$ | Đếm độ dài khối bằng nhau liên tiếp | $\mathcal{O}(N \log N)$ |
| **Gom cụm chênh lệch $\le K$** | Tìm kiếm nhánh cận | Duyệt tuyến tính gom đoạn kề nhau | $\mathcal{O}(N \log N)$ |

---

## 4. Hàm `sort` & Nguyên Lý Strict Weak Ordering

### 4.1. Cú pháp chuẩn trong C++
C++ cung cấp hai hàm sắp xếp có sẵn:
* `sort(first, last)`: Sử dụng thuật toán **IntroSort** (kết hợp giữa QuickSort, HeapSort và InsertionSort), đạt độ phức tạp thời gian $\mathcal{O}(N \log N)$ trong mọi trường hợp (trung bình và xấu nhất). Không bảo toàn thứ tự ban đầu của các phần tử bằng nhau.
* `stable_sort(first, last)`: Sử dụng thuật toán **MergeSort**, độ phức tạp $\mathcal{O}(N \log N)$, đảm bảo bảo toàn nguyên vẹn thứ tự xuất hiện ban đầu của các phần tử có giá trị bằng nhau.

### 4.2. Nguyên lý Strict Weak Ordering (Toán tử so sánh nghiêm ngặt)
Một hàm so sánh `cmp(a, b)` truyền vào `sort` **bắt buộc** phải thỏa mãn 3 tiên đề toán học:
1. **Tính bất phản xạ (Irreflexivity):** `cmp(a, a)` luôn trả về `false`.
2. **Tính bất đối xứng (Asymmetry):** Nếu `cmp(a, b)` là `true` thì `cmp(b, a)` bắt buộc phải là `false`.
3. **Tính bắc cầu (Transitivity):** Nếu `cmp(a, b)` là `true` và `cmp(b, c)` là `true` thì `cmp(a, c)` phải là `true`.

> [!CAUTION]
> **TỬ HUYỆT LẬP TRÌNH: BẪY DẤU `<= ` TRONG COMPARATOR**
> 
> Nếu viết `return a <= b;`, khi `a == b` thì cả `cmp(a, b)` và `cmp(b, a)` đều trả về `true` $\implies$ Vi phạm tiên đề Bất phản xạ và Bất đối xứng $\implies$ `sort` sẽ tiếp tục truy cập vùng nhớ ngoài biên của mảng $\implies$ **RUNTIME ERROR / CRASH CHƯƠNG TRÌNH**.
> 
> **QUY TẮC BẮT BUỘC:** Luôn dùng toán tử so sánh nghiêm ngặt (`<` hoặc `>`). Khi hai phần tử bằng nhau (`a == b`), hàm so sánh bắt buộc phải trả về `false`!

---

## 5. Các Kỹ Thuật Custom Comparator Nâng Cao

### 5.1. Sắp xếp đa tiêu chí với Vector lồng nhau (Multi-criteria Sorting)
Khi mỗi phần tử gồm nhiều thuộc tính số (ví dụ: điểm bắt đầu $L = a[0]$ và điểm kết thúc $R = a[1]$ của một đoạn thẳng), ta sử dụng **vector lồng nhau `vector<vector<int>>`** để tận dụng mảng sẵn có:

```cpp
// Ví dụ: Sắp xếp các đoạn thẳng theo điểm kết thúc a[1] tăng dần,
// nếu trùng điểm kết thúc thì theo điểm bắt đầu a[0] giảm dần
bool cmpInterval(const vector<int> &a, const vector<int> &b) {
    if (a[1] != b[1]) {
        return a[1] < b[1]; // Ưu tiên kết thúc sớm hơn đứng trước
    }
    return a[0] > b[0]; // Cùng điểm kết thúc: Bắt đầu muộn hơn đứng trước
}
```

#### 💡 Ví Dụ Minh Họa 2: Sắp xếp danh sách 4 đoạn thẳng
Cho 4 đoạn thẳng: $\{ [1, 5], [2, 3], [3, 6], [1, 3] \}$

* **Trước khi sắp xếp:** $[1, 5], [2, 3], [3, 6], [1, 3]$
* **Tiêu chí 1 (Điểm kết thúc tăng dần):** Các đoạn kết thúc tại $3$ đứng trước, sau đó đến $5$, rồi đến $6$.
* **Tiêu chí 2 (Cùng điểm kết thúc $\implies$ bắt đầu giảm dần):** Giữa $[2, 3]$ và $[1, 3]$, đoạn $[2, 3]$ có điểm bắt đầu $2 > 1$ nên được xếp trước.

> **Kết quả sau sắp xếp:** $[[2, 3], [1, 3], [1, 5], [3, 6]]$

---

### 5.2. Sắp xếp lưu chỉ số ban đầu (Index Tracking)
Khi bài toán yêu cầu in ra vị trí gốc của các phần tử sau khi sắp xếp, sử dụng **vector 2 chiều `vector<vector<long long>>`** lưu cặp `{giá_trị, chỉ_số_gốc}`:

```cpp
// Khởi tạo vector 2 chiều n hàng, 2 cột: a[i][0] là giá trị, a[i][1] là chỉ số gốc
vector<vector<long long>> a(n, vector<long long>(2));
for (int i = 0; i < n; ++i) {
    cin >> a[i][0];   // Giá trị phần tử
    a[i][1] = i + 1;  // Chỉ số ban đầu (1-based)
}

// sort mặc định so sánh cột 0 (giá trị), nếu bằng nhau so sánh tiếp cột 1 (chỉ số gốc)
sort(a.begin(), a.end());
```

### 5.3. Comparator hàm mục tiêu (Objective Comparison)
Bài toán ghép $N$ chuỗi số để tạo thành số lớn nhất:

```cpp
bool cmpConcat(const string &a, const string &b) {
    // Sắp xếp sao cho chuỗi ghép a + b lớn hơn chuỗi ghép b + a
    return a + b > b + a;
}
```

---

## 6. Mẫu Cài Đặt Chuẩn Thi Đấu (Competitive Template)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    // Tối ưu hóa tốc độ I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    // Bước 1: Sắp xếp mảng O(N log N)
    sort(a.begin(), a.end());

    // Bước 2: Khai thác trật tự tuyến tính O(N)
    long long min_diff = a[1] - a[0];
    for (int i = 1; i < n - 1; ++i) {
        min_diff = min(min_diff, a[i + 1] - a[i]);
    }

    cout << min_diff << "\n";
    return 0;
}
```

---

## 7. Ranh Giới Áp Dụng: Khi Nào Được & Không Được Sắp Xếp?

* **ĐƯỢC PHÉP SẮP XẾP:** Khi bài toán khảo sát tính chất trên **toàn bộ tập hợp** mà không phụ thuộc vào vị trí ban đầu của phần tử (như tìm $\min/\max$, đếm giá trị phân biệt, tìm cặp thỏa mãn điều kiện đại số).
* **KHÔNG ĐƯỢC PHÉP SẮP XẾP:** Khi bài toán có ràng buộc gắn liền với **dòng thời gian hoặc vị trí liền kề nguyên thủy** (như tìm đoạn con liên tiếp, chuỗi con tăng dài nhất bảo toàn thứ tự ban đầu).

---

# CÂU HỎI TRẮC NGHIỆM ĐO LƯỜNG TƯ DUY (CONCEPT QUIZ)

#### Câu 1 (Nhận diện — Recognize):
Một bài toán ghi nhận biến động giá vàng trong $N$ ngày liên tiếp: $[28, 31, 30, 27, 29]$. Đề bài yêu cầu tìm **hai ngày liên tiếp nhau có mức chênh lệch giá nhỏ nhất**. Bạn có được phép dùng hàm `sort()` để sắp xếp lại mảng này trước khi xử lý không?
* A. Được phép, vì sắp xếp luôn giúp tìm hiệu số nhỏ nhất nhanh hơn.
* B. **(Đáp án đúng)** Không được phép, vì yêu cầu "hai ngày liên tiếp" gắn chặt với trục thời gian gốc; sắp xếp lại sẽ làm đảo lộn thứ tự thời gian và dẫn đến kết quả sai hoàn toàn.
* C. Được phép, nhưng phải sắp xếp theo thứ tự giảm dần.
* D. Được phép, nếu ta lưu lại giá trị trung bình của mảng.
> *Giải thích:* Yêu cầu đề bài là "hai thời điểm liên tiếp nhau", nghĩa là các vị trí kề nhau theo trật tự thời gian gốc. Sắp xếp lại sẽ làm đảo lộn thứ tự thời gian và dẫn đến kết quả sai hoàn toàn.

---

#### Câu 2 (Dự đoán — Predict):
Cho dãy tọa độ chưa sắp xếp $A = [21, 5, 13, 8, 30, 14]$. Sau khi sắp xếp tăng dần thành $[5, 8, 13, 14, 21, 30]$, để tìm khoảng cách nhỏ nhất giữa 2 điểm bất kỳ, ta chỉ cần kiểm tra những cặp số nào?
* A. $(5, 30), (8, 21), (13, 14)$
* B. **(Đáp án đúng)** $(5, 8), (8, 13), (13, 14), (14, 21), (21, 30)$
* C. Bắt buộc phải kiểm tra tất cả 15 cặp có thể tạo ra từ 6 số.
* D. Chỉ cần kiểm tra cặp đầu tiên $(5, 8)$ và cặp cuối cùng $(21, 30)$.
> *Giải thích:* Nhờ tính chất lân cận của dãy số tăng dần, khoảng cách nhỏ nhất toàn cục luôn nằm ở một trong $N - 1 = 5$ cặp kề nhau.

---

#### Câu 3 (Bản chất — Explain):
Trong hàm so sánh Custom Comparator `bool cmp(int a, int b)`, nếu lập trình viên viết `return a <= b;` thì điều gì sẽ xảy ra khi mảng có các phần tử bằng nhau và $N$ lớn?
* A. Chương trình vẫn chạy đúng và sắp xếp ổn định.
* B. Mảng sẽ được sắp xếp theo thứ tự giảm dần.
* C. **(Đáp án đúng)** Chương trình có thể bị dừng đột ngột (Runtime Error) do vi phạm nguyên lý Strict Weak Ordering khi $a = b$.
* D. Hàm `sort` tự động chuyển sang `stable_sort` để xử lý.
> *Giải thích:* Khi $a = b$, `cmp(a, b)` và `cmp(b, a)` đều trả về `true`, vi phạm tính bất đối xứng nghiêm ngặt khiến thuật toán `sort` truy cập vùng nhớ ngoài biên dẫn đến Crash.

---

#### Câu 4 (Chuyển giao — Transfer):
Khi $N = 100.000$, vì sao phương pháp **Sắp xếp rồi duyệt kề nhau** $\mathcal{O}(N \log N + N)$ lại vượt trội hơn hẳn phương pháp **Duyệt mọi cặp** $\mathcal{O}(N^2)$?
* A. Vì hàm `sort()` làm giảm bớt số lượng phần tử cần lưu trữ trong bộ nhớ.
* B. **(Đáp án đúng)** Vì việc sắp xếp tạo ra cấu trúc trật tự, giúp loại bỏ hàng tỷ cặp không có khả năng tối ưu mà chỉ cần xét $N-1$ cặp kề nhau.
* C. Vì `sort()` được biên dịch sang mã máy đa luồng của CPU.
* D. Vì số phép tính của 2 cách là như nhau nhưng `sort()` tốn ít bộ nhớ RAM hơn.
> *Giải thích:* Bản chất của việc sắp xếp là biến đổi bài toán để giảm thiểu không gian tìm kiếm, giúp ta không phải kiểm tra những trường hợp chắc chắn không tối ưu.

---

#### Câu 5 (Cú pháp & Ứng dụng — Syntax):
Cách nào sau đây là chuẩn mực và an toàn nhất trong C++ để sắp xếp một `vector<int> a` theo thứ tự **giảm dần**?
* A. `sort(a.begin(), a.end(), less<int>());`
* B. **(Đáp án đúng)** `sort(a.begin(), a.end(), greater<int>());` hoặc `sort(a.rbegin(), a.rend());`
* C. `sort(a.end(), a.begin());`
* D. `sort(a.begin(), a.end()); reverse(a.begin() + 1, a.end());`
> *Giải thích:* `greater<int>()` là functor so sánh lớn hơn chuẩn của C++, hoặc dùng cặp iterator đảo ngược `rbegin()` và `rend()` để sắp xếp mảng giảm dần.

---

#### Câu 6 (Phân biệt cấu trúc — Compare):
Sự khác biệt cốt lõi giữa `sort` và `stable_sort` trong thư viện chuẩn C++ là gì?
* A. `sort` có độ phức tạp $\mathcal{O}(N^2)$, còn `stable_sort` là $\mathcal{O}(N \log N)$.
* B. **(Đáp án đúng)** `stable_sort` đảm bảo giữ nguyên thứ tự xuất hiện ban đầu của các phần tử có giá trị tương đương nhau, còn `sort` thì không đảm bảo điều này.
* C. `sort` chỉ sắp xếp được số nguyên, còn `stable_sort` sắp xếp được chuỗi.
* D. `stable_sort` không tốn thêm bất kỳ bộ nhớ phụ trợ nào ($\mathcal{O}(1)$).
> *Giải thích:* Tính ổn định (Stability) nghĩa là nếu $A_i = A_j$ và $i < j$, sau khi sort thì $A_i$ vẫn đứng trước $A_j$. `stable_sort` đảm bảo tính chất này (dùng MergeSort).

---

#### Câu 7 (Thuật toán lân cận — Technique):
Sau khi sắp xếp một mảng $N$ phần tử tăng dần, thuật toán đếm số lượng giá trị phân biệt (Distinct values) hoạt động trong thời gian bao lâu?
* A. $\mathcal{O}(N^2)$ vì phải so sánh từng cặp.
* B. $\mathcal{O}(N \log N)$ vì phải dùng thêm cây nhị phân tìm kiếm.
* C. **(Đáp án đúng)** $\mathcal{O}(N)$ vì các giá trị bằng nhau đã gom thành các khối liên tiếp, chỉ cần duyệt 1 vòng và đếm khi $A[i] \neq A[i-1]$.
* D. $\mathcal{O}(1)$ bằng công thức toán học.
> *Giải thích:* Sau khi sort, toàn bộ các phần tử trùng lặp đều nằm liền kề. Duyệt qua mảng và tăng biến đếm mỗi khi gặp một giá trị khác với phần tử đứng trước nó chỉ tốn $\mathcal{O}(N)$.

---

#### Câu 8 (Comparator hàm mục tiêu — Logic):
Trong bài toán ghép $N$ chuỗi số $S_1, S_2, \dots, S_N$ để tạo ra số nguyên lớn nhất, tại sao hàm so sánh `bool cmp(string a, string b)` lại được định nghĩa là `return a + b > b + a;`?
* A. Vì chuỗi có độ dài dài hơn luôn tạo ra số lớn hơn.
* B. **(Đáp án đúng)** Vì thứ tự ghép trực tiếp $a + b$ so với $b + a$ phản ánh chính xác đóng góp vị trí chữ số của $a$ và $b$ vào số ghép tổng thể, đồng thời thỏa mãn tính chất bắc cầu.
* C. Vì đây là quy ước bắt buộc của chuẩn ANSI C++.
* D. Vì phép cộng chuỗi tự động ép kiểu về số nguyên 64-bit.
> *Giải thích:* Nếu ghép $a$ trước $b$ tạo ra chuỗi lớn hơn ghép $b$ trước $a$ ($a + b > b + a$), thì việc đặt $a$ đứng trước $b$ trong mảng sẽ tối ưu hóa toàn cục chuỗi kết quả.

---

#### Câu 9 (Sắp xếp đa tiêu chí — Multi-criteria):
Khi sắp xếp danh sách các đoạn thẳng $[L_i, R_i]$ theo tiêu chí: *Điểm bắt đầu $L$ tăng dần; nếu trùng $L$ thì điểm kết thúc $R$ giảm dần*, comparator nào sau đây viết đúng chuẩn Strict Weak Ordering?
* A. `return (a[0] <= b[0]) && (a[1] >= b[1]);`
* B. `if (a[0] < b[0]) return true; else return a[1] > b[1];`
* C. **(Đáp án đúng)** `if (a[0] != b[0]) return a[0] < b[0]; return a[1] > b[1];`
* D. `return a[0] < b[0] || a[1] > b[1];`
> *Giải thích:* Phải kiểm tra sự khác biệt của tiêu chí chính trước (`a[0] != b[0]`). Chỉ khi tiêu chí chính bằng nhau mới so sánh tiêu chí phụ. Cả hai nhánh đều phải dùng toán tử nghiêm ngặt `<` hoặc `>`.

---

#### Câu 10 (Xử lý kiểu dữ liệu & Tràn số — Robustness):
Cho bài toán tìm khoảng cách nhỏ nhất giữa 2 điểm trong $N$ điểm trên trục tọa độ, với tọa độ $X_i \in [-10^{18}, 10^{18}]$. Sai lầm nguy hiểm nhất khi duyệt cặp kề nhau $(X_i, X_{i+1})$ là gì?
* A. Sử dụng `sort` thay vì tự viết QuickSort.
* B. **(Đáp án đúng)** Lưu biến kết quả bằng kiểu `int` hoặc `long` (32-bit), gây tràn số âm khi tính hiệu $X_{i+1} - X_i$.
* C. Đọc dữ liệu bằng `cin` có Fast I/O.
* D. Duyệt vòng lặp từ $i = 0$ đến $N - 2$.
> *Giải thích:* Với $X_i$ lên tới $10^{18}$, khoảng cách giữa 2 điểm có thể đạt tới $2 \cdot 10^{18}$, vượt xa giới hạn $2 \cdot 10^9$ của kiểu `int`. Bắt buộc phải dùng kiểu `long long` (64-bit) cho toàn bộ mảng và biến tính khoảng cách.

---

# DANH SÁCH BÀI TẬP THỰC HÀNH

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-SX-01` | **Xếp Hàng Điểm Danh** | `P0` | $N \le 1000, A_i \le 10^6$ | Cú pháp `sort` cơ bản |
| 02 | `CPPB-SX-02` | **Khoảng Cách Nhỏ Nhất** | `P1` | $N \le 10^5, A_i \le 10^9$ | Sắp xếp duyệt cặp kề |
| 03 | `CPPB-SX-03` | **Sắp Xếp Theo Trị Tuyệt Đối** | `P1` | $N \le 10^5, \vert A_i \vert \le 10^9$ | Custom comparator cơ bản |
| 04 | `CPPB-SX-04` | **Đếm Giá Trị Phân Biệt** | `P2` | $N \le 2 \cdot 10^5, \vert A_i \vert \le 10^9$ | Gom nhóm sau sắp xếp |
| 05 | `CPPB-SX-05` | **Hai Trạm Kiểm Soát Gần Nhau Nhất** | `P2` | $N \le 10^5, X_i \le 10^{12}$ | Xử lý dữ liệu lớn `long long` |
| 06 | `CPPB-SX-06` | **Khoảng Trống Lớn Nhất Trên Trục Tọa Độ** | `P3` | $N \le 10^5, \vert A_i \vert \le 10^{18}$ | Khai thác trật tự tuyến tính |
| 07 | `CPPB-SX-07` | **Sắp Xếp Theo Tổng Chữ Số** | `P1` | $N \le 10^5, A_i \le 10^9$ | Hàm biến đổi phụ trong comparator |
| 08 | `CPPB-SX-08` | **Gom Cụm Chênh Lệch Không Quá K** | `P2` | $N \le 2 \cdot 10^5, A_i \le 10^9$ | Tham lam tuyến tính trên mảng sắp xếp |
| 09 | `CPPB-SX-09` | **Tìm Phần Tử Xuất Hiện Nhiều Nhất** | `P2` | $N \le 2 \cdot 10^5, \vert A_i \vert \le 10^9$ | Đếm tần suất khối liên tiếp |
| 10 | `CPPB-SX-10` | **Sắp Xếp Lưu Vị Trí Ban Đầu** | `P3` | $N \le 10^5, \vert A_i \vert \le 10^9$ | Theo dõi chỉ số gốc (Index Tracking) |
| 11 | `CPPB-SX-11` | **Ghép Chuỗi Tạo Số Lớn Nhất** | `P3` | $N \le 10^4$ | So sánh chuỗi bắc cầu ($a+b > b+a$) |
| 12 | `CPPB-SX-12` | **Bảng Điểm Học Sinh Đa Trường** | `P4` | $N \le 10^5$ | Sắp xếp đa khóa ưu tiên |
| 13 | `CPPB-SX-13` | **Bảng Xếp Hạng Giải Đấu Thể Thao** | `P4` | $N \le 10^5$ | Sắp xếp tổ hợp 4 tiêu chí |
| 14 | `CPPB-SX-14` | **Sắp Xếp Đoạn Thẳng Không Giao Lỗi** | `P5` | $N \le 2 \cdot 10^5$ | Strict Weak Ordering & `stable_sort` |
