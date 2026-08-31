# Chuyên đề 15: Quy hoạch động chuỗi: LCS & Edit Distance

## 1. Không gian trạng thái hai tiền tố (2-prefix state)

Trong xử lý chuỗi ký tự thi đấu, các bài toán so khớp, tìm chuỗi tương đồng hay biến đổi xâu thường thao tác trên hai chuỗi $A$ (độ dài $N$) và $B$ (độ dài $M$).
* **Nguyên lý Thiết kế Trạng thái:** Ta định nghĩa trạng thái dựa trên **Cặp tiền tố** của hai chuỗi:

> **$dp[i][j]$ đại diện cho kết quả tối ưu khi xét tiền tố $A[1 \dots i]$ (gồm $i$ ký tự đầu của $A$) và tiền tố $B[1 \dots j]$ (gồm $j$ ký tự đầu của $B$).**

* **Trường hợp cơ sở (Base Cases):** Khi một trong hai tiền tố có độ dài bằng 0 ($i = 0$ hoặc $j = 0$), tương đương với chuỗi rỗng $\varepsilon$.

## 2. Dãy con chung dài nhất (longest common subsequence — LCS)

### 2.1. Bản chất toán học & hệ thức truy hồi
* **Định nghĩa:** Dãy con là dãy thu được bằng cách xóa đi một số ký tự mà **không làm thay đổi thứ tự** của các ký tự còn lại.
* **State Definition:** $dp[i][j]$ là độ dài của dãy con chung dài nhất giữa $A[1 \dots i]$ và $B[1 \dots j]$.
* **Base Cases:** `dp[0][j] = 0` và `dp[i][0] = 0` với mọi $i, j$.
* **State Transition:** So sánh ký tự đuôi $A[i]$ và $B[j]$:
1. Nếu $A[i] == B[j]$: Ký tự này chắc chắn thuộc LCS chung:
$$dp[i][j] = 1 + dp[i-1][j-1]$$
2. Nếu $A[i] \ne B[j]$: Bỏ qua $A[i]$ hoặc bỏ qua $B[j]$ để lấy phương án tốt hơn:
$$dp[i][j] = \max(dp[i-1][j], dp[i][j-1])$$
* **Độ phức tạp:** Thời gian $\mathcal{O}(N \cdot M)$, Bộ nhớ $\mathcal{O}(N \cdot M)$.

![Bảng phương án LCS và Đường truy vết](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-15-quy-hoach-dong-chuoi-lcs/assets/lcs_table_traceback_vi.svg)

### 2.2. Kỹ thuật khôi phục xâu LCS tối ưu (traceback)
Từ ô kết quả $(N, M)$ trên bảng phương án 2D:
1. Nếu $A[i] == B[j] \implies$ Thêm $A[i]$ vào xâu kết quả, lùi chéo về $(i-1, j-1)$.
2. Nếu $A[i] \ne B[j] \implies$ Đi về ô có giá trị lớn hơn: lên trên $(i-1, j)$ nếu $dp[i-1][j] \ge dp[i][j-1]$, ngược lại sang trái $(i, j-1)$.
3. Dừng lại khi $i = 0$ hoặc $j = 0$. Đảo ngược xâu kết quả thu được.

## 3. Khoảng cách biến đổi xâu (Edit Distance / Levenshtein Distance)

### 3.1. Bản chất 3 phép biến đổi
Cần tìm số phép biến đổi **ít nhất** để biến xâu $A$ thành xâu $B$. Các phép thao tác hợp lệ gồm:
1. **Chèn (Insert):** Thêm 1 ký tự vào xâu $A$.
2. **Xóa (Delete):** Xóa 1 ký tự khỏi xâu $A$.
3. **Thay thế (Replace):** Đổi 1 ký tự của $A$ thành ký tự khác.

### 3.2. Hệ thức chuyển trạng thái
* **State Definition:** $dp[i][j]$ là số thao tác ít nhất biến $A[1 \dots i]$ thành $B[1 \dots j]$.
* **Base Cases:**
* `dp[i][0] = i` (Biến xâu độ dài $i$ thành xâu rỗng cần $i$ phép xóa).
* `dp[0][j] = j` (Biến xâu rỗng thành xâu độ dài $j$ cần $j$ phép chèn).
* **State Transition:**
* Nếu $A[i] == B[j] \implies dp[i][j] = dp[i-1][j-1]$ (Không tốn chi phí).
* Nếu $A[i] \ne B[j]$:
$$dp[i][j] = 1 + \min(\underbrace{dp[i-1][j-1]}_{\text{Thay thế}}, \underbrace{dp[i-1][j]}_{\text{Xóa}}, \underbrace{dp[i][j-1]}_{\text{Chèn}})$$

![Khoảng cách biến đổi xâu Edit Distance](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-15-quy-hoach-dong-chuoi-lcs/assets/edit_distance_transitions_vi.svg)

## 4. Phân biệt rạch ròi: Xâu con đối xứng (substring) vs dãy con đối xứng (subsequence)

Đây là tử huyệt thuật ngữ cực kỳ quan trọng trong lập trình thi đấu:

![Phân biệt Xâu con liên tiếp vs Dãy con đối xứng](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-15-quy-hoach-dong-chuoi-lcs/assets/palindrome_substring_vs_subsequence_vi.svg)

### 4.1. Xâu con liên tiếp đối xứng dài nhất (longest palindromic substring)
* **Đặc tính:** Các ký tự phải **liên tiếp liền kề nhau**.
* **State Definition:** $dp[i][j]$ kiểu boolean, nhận giá trị `true` nếu đoạn con liên tiếp $S[i \dots j]$ là một xâu đối xứng.
* **Transition:** $dp[i][j] = (S[i] == S[j]) \land dp[i+1][j-1]$.
* **Duyệt:** Theo độ dài xâu con $len = 1 \to N$.

### 4.2. Dãy con không liên tiếp đối xứng dài nhất (longest palindromic subsequence)
* **Đặc tính:** Các ký tự **không cần liên tiếp**.
* **State Definition:** $dp[i][j]$ là độ dài lớn nhất của dãy con đối xứng trích xuất từ đoạn $S[i \dots j]$.
* **Transition:**
* Nếu $S[i] == S[j] \implies dp[i][j] = 2 + dp[i+1][j-1]$.
* Nếu $S[i] \ne S[j] \implies dp[i][j] = \max(dp[i+1][j], dp[i][j-1])$.
* *Cách giải tương đương:* Tính $LCS$ giữa xâu $S$ và xâu đảo ngược $S^R$!

## 5. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy lệch chỉ số 0-based của Xâu ký tự với 1-based của Bảng DP:**
* Trong C++, `string` có chỉ số từ `0` đến $N-1$. Khi truy cập ký tự thứ $i$ trong bảng DP 1-based, phải viết `A[i - 1]` thay vì `A[i]`.
2. **Bẫy thứ tự duyệt trong Quy hoạch động trên Đoạn con Palindrome:**
* Trạng thái $dp[i][j]$ phụ thuộc vào $dp[i+1][j-1]$ (đoạn ngắn hơn). Nếu duyệt $i$ từ $1 \to N$ xuôi thì ô $dp[i+1][\dots]$ chưa được tính $\implies$ Kết quả sai!
* **Quy tắc đúng:** Luôn duyệt theo độ dài $len = 1 \to N$, sau đó duyệt điểm đầu $i = 1 \to N - len + 1$ và $j = i + len - 1$.
3. **Bẫy khởi tạo Base Case của Edit Distance:**
* Quên khởi tạo cột $0$ (`dp[i][0] = i`) và hàng $0$ (`dp[0][j] = j`) sẽ dẫn đến toàn bộ bảng nhận giá trị rác.

## 6. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Dãy con chung dài nhất (LCS) kèm khôi phục xâu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    int n = a.size();
    int m = b.size();
    if (n == 0 || m == 0) {
        cout << 0 << "\n\n";
        return 0;
    }

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    cout << dp[n][m] << "\n";

    // Khôi phục xâu LCS
    string lcs_str = "";
    int i = n, j = m;
    while (i > 0 && j > 0) {

        if (a[i - 1] == b[j - 1]) {
            lcs_str.push_back(a[i - 1]);
            --i;
            --j;
        } else if (dp[i - 1][j] >= dp[i][j - 1]) {
            --i;
        } else {
            --j;
        }
    }
    reverse(lcs_str.begin(), lcs_str.end());
    cout << lcs_str << "\n";

    return 0;
}
```

### Mẫu 2: Khoảng cách biến đổi xâu (Edit Distance)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    int n = a.size();
    int m = b.size();

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 0; i <= n; ++i) dp[i][0] = i;
    for (int j = 0; j <= m; ++j) dp[0][j] = j;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + min({dp[i - 1][j - 1], // Replace
                                    dp[i - 1][j],     // Delete
                                    dp[i][j - 1]});   // Insert
            }
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}
```

## 7. Hệ thống câu hỏi kiểm tra khái niệm (Concept Quiz)

#### Câu 1 (Không gian trạng thái 2-Prefix):

Trong bài toán LCS trên hai chuỗi $A$ và $B$, trạng thái $dp[i][j]$ đại diện chính xác cho điều gì?

- **A.** Độ dài xâu $A$ cộng với độ dài xâu $B$.

- **B.** **[Đáp án đúng]** Độ dài dãy con chung dài nhất của tiền tố $A[1 \dots i]$ và tiền tố $B[1 \dots j]$.

- **C.** Số lượng ký tự giống nhau ở vị trí $i$ và $j$.

- **D.** Vị trí đầu tiên mà hai xâu khớp nhau.

> *Giải thích:* Bất biến trạng thái 2 tiền tố: Xét độc lập bài toán con trên tiền tố độ dài $i$ của $A$ và tiền tố độ dài $j$ của $B$.

#### Câu 2 (Trường hợp ký tự trùng khớp trong LCS):

Khi $A[i] == B[j]$, tại sao ta chuyển trạng thái $dp[i][j] = 1 + dp[i-1][j-1]$ mà không cần xét $\max(dp[i-1][j], dp[i][j-1])$?

- **A.** Vì phép gán này chạy nhanh hơn.

- **B.** **[Đáp án đúng]** Vì ghép cặp $A[i]$ với $B[j]$ luôn tối ưu tối đa và đảm bảo không làm mất bất kỳ nghiệm tối ưu nào.

- **C.** Vì $dp[i-1][j]$ luôn bằng 0.

- **D.** Vì hai chuỗi có độ dài bằng nhau.

> *Giải thích:* Bằng chứng minh Tham lam / Cấu trúc con tối ưu, khi 2 ký tự cuối trùng nhau, việc đưa cặp ký tự này vào LCS luôn đạt kết quả tốt nhất.

#### Câu 3 (Cơ sở của Edit Distance):

Tại sao trong bài toán Edit Distance, $dp[i][0] = i$ và $dp[0][j] = j$?

- **A.** Vì các ô này không dùng đến nên khởi tạo đại diện.

- **B.** **[Đáp án đúng]** Vì để biến chuỗi $i$ ký tự thành chuỗi rỗng cần đúng $i$ phép xóa, và từ chuỗi rỗng tạo chuỗi $j$ ký tự cần đúng $j$ phép chèn.

- **C.** Vì $i + j$ luôn dương.

- **D.** Để tránh mảng bị tràn số âm.

> *Giải thích:* Đây là các trường hợp cơ sở tự nhiên khi một trong hai chuỗi là chuỗi rỗng $\varepsilon$.

#### Câu 4 (Phân biệt Substring vs Subsequence):

Cho xâu $S = \text{"ABBA"}$. Khẳng định nào sau đây là đúng về bản chất Substring và Subsequence?

- **A.** Mọi Subsequence đều là Substring.

- **B.** **[Đáp án đúng]** Mọi Substring đều là Subsequence, nhưng Subsequence không bắt buộc phải liên tiếp.

- **C.** Substring và Subsequence là hai khái niệm hoàn toàn tương đương.

- **D.** Substring dài hơn Subsequence.

> *Giải thích:* Substring là chuỗi con liên tiếp (khối liền kề). Subsequence là dãy con được tạo bằng cách giữ nguyên thứ tự nhưng có thể bỏ qua một số ký tự trung gian.

#### Câu 5 (Độ phức tạp của LCS và Edit Distance):

Cho hai xâu có độ dài lần lượt là $N$ và $M$. Thuật toán DP chuẩn mực chạy trong thời gian và bộ nhớ là bao nhiêu?

- **A.** Thời gian $\mathcal{O}(N + M)$, Bộ nhớ $\mathcal{O}(1)$.

- **B.** **[Đáp án đúng]** Thời gian $\mathcal{O}(N \cdot M)$, Bộ nhớ $\mathcal{O}(N \cdot M)$ (hoặc $\mathcal{O}(\min(N, M))$ nếu nén mảng).

- **C.** Thời gian $\mathcal{O}(2^{N+M})$, Bộ nhớ $\mathcal{O}(N)$.

- **D.** Thời gian $\mathcal{O}(N^2 \cdot M^2)$, Bộ nhớ $\mathcal{O}(N \cdot M)$.

> *Giải thích:* Bảng quy hoạch động có kích thước $(N+1) \times (M+1)$, mỗi ô tính trong $\mathcal{O}(1) \implies \mathcal{O}(N \cdot M)$.

#### Câu 6 (Mối liên hệ giữa LCS và Xâu con chung ngắn nhất SCS):

Độ dài xâu ngắn nhất chứa cả hai xâu $A$ (độ dài $N$) và $B$ (độ dài $M$) dưới dạng dãy con (Shortest Common Supersequence) được tính bằng công thức nào?

- **A.** $N + M$

- **B.** **[Đáp án đúng]** $N + M - \text{LCS}(A, B)$

- **C.** $\text{LCS}(A, B)$

- **D.** $2 \cdot \text{LCS}(A, B)$

> *Giải thích:* Tổng độ dài 2 xâu là $N + M$. Các ký tự thuộc phần chung $\text{LCS}(A, B)$ chỉ cần xuất hiện đúng 1 lần trong xâu siêu chuỗi $\implies$ Trừ bớt $\text{LCS}(A, B)$.

#### Câu 7 (Tìm Dãy con đối xứng dài nhất bằng LCS):

Để tìm độ dài Dãy con không liên tiếp đối xứng dài nhất (Longest Palindromic Subsequence) của xâu $S$, ta có thể quy về bài toán nào?

- **A.** Tìm LIS trên xâu $S$.

- **B.** **[Đáp án đúng]** Tìm $\text{LCS}(S, S^R)$ với $S^R$ là xâu đảo ngược của $S$.

- **C.** Tìm Edit Distance giữa $S$ và chuỗi rỗng.

- **D.** Tìm kiếm nhị phân trên $S$.

> *Giải thích:* Dãy con đối xứng là dãy con xuất hiện giống nhau theo cả chiều xuôi và chiều ngược $\implies$ Chính là dãy con chung dài nhất giữa $S$ và $S^R$.

#### Câu 8 (Thứ tự duyệt trong DP Đoạn con Palindrome Substring):

Khi tính $dp[i][j] = (S[i] == S[j]) \land dp[i+1][j-1]$, thứ tự duyệt vòng lặp nào sau đây là đúng?

- **A.** Duyệt $i = 1 \to N$, $j = 1 \to N$.

- **B.** **[Đáp án đúng]** Duyệt độ dài $len = 1 \to N$, sau đó duyệt điểm đầu $i = 1 \to N - len + 1$ và đặt $j = i + len - 1$.

- **C.** Duyệt ngẫu nhiên.

- **D.** Duyệt $j = N \to 1$.

> *Giải thích:* Trạng thái đoạn $[i \dots j]$ độ dài $len$ phụ thuộc vào đoạn con bên trong $[i+1 \dots j-1]$ có độ dài $len - 2$. Do đó các đoạn ngắn hơn phải được tính xong trước.

#### Câu 9 (Bẫy truy cập ký tự 0-based trong C++):

Trong C++, nếu xâu `string s = "CODE"` và bảng DP khai báo 1-based từ $1 \to 4$, ký tự tương ứng với chỉ số $i = 3$ trong bảng DP được truy cập là gì?

- **A.** $s[3]$

- **B.** **[Đáp án đúng]** $s[2]$ (Tức $s[i - 1]$).

- **C.** $s[4]$

- **D.** $s[i + 1]$

> *Giải thích:* Chỉ số xâu trong C++ là 0-based ($0, 1, 2, 3$). Ký tự thứ $i$ (1-based) tương ứng với ô $s[i - 1]$.

#### Câu 10 (Số phép chèn tối thiểu để tạo xâu đối xứng):

Cho xâu $S$ độ dài $N$. Số ký tự ít nhất cần chèn thêm vào $S$ để biến nó thành một xâu đối xứng là:

- **A.** $N$

- **B.** **[Đáp án đúng]** $N - \text{LPS}(S)$ (với $\text{LPS}(S)$ là độ dài dãy con đối xứng dài nhất).

- **C.** $\text{LPS}(S) / 2$

- **D.** $N / 2$

> *Giải thích:* Giữ nguyên $\text{LPS}(S)$ ký tự đối xứng có sẵn, chỉ cần chèn thêm đối xứng cho $N - \text{LPS}(S)$ ký tự còn lại.

#### Câu 11 (Truy vết chuỗi thao tác Edit Distance):

Khi truy vết từ ô $(i, j)$ trong bảng Edit Distance, nếu $dp[i][j] == dp[i-1][j] + 1$, thao tác đã được thực hiện là gì?

- **A.** Chèn ký tự $B[j]$.

- **B.** **[Đáp án đúng]** Xóa ký tự $A[i]$ khỏi xâu $A$.

- **C.** Thay thế ký tự $A[i]$ bằng $B[j]$.

- **D.** Không làm gì cả.

> *Giải thích:* Ô $(i-1, j)$ tương ứng với việc tiền tố $A$ bớt đi 1 ký tự trong khi tiền tố $B$ giữ nguyên $\implies$ Thao tác xóa ký tự $A[i]$.

#### Câu 12 (So khớp chuỗi mẫu đại diện Wildcard DP):

Ký tự đại diện $*$ trong so khớp mẫu (khớp với chuỗi ký tự bất kỳ có độ dài $\ge 0$) có hệ thức chuyển trạng thái là:

- **A.** $dp[i][j] = dp[i-1][j-1]$

- **B.** **[Đáp án đúng]** $dp[i][j] = dp[i-1][j] \lor dp[i][j-1]$ (Khớp với 1/nhiều ký tự hoặc khớp với chuỗi rỗng).

- **C.** `dp[i][j] = dp[i][j]`

- **D.** `dp[i][j] = false`

> *Giải thích:* $dp[i-1][j]$ đại diện cho việc $$tiếp tục khớp thêm ký tự $A[i]$, còn $dp[i][j-1]$ đại diện cho việc$$ đại diện cho chuỗi rỗng không lấy ký tự nào.

#### Câu 13 (Nén bộ nhớ LCS còn 2 dòng):

Nếu chỉ cần tìm độ dài của LCS giữa 2 chuỗi độ dài $N$ và $M$ (không yêu cầu truy vết xâu), ta có thể nén bộ nhớ về mức nào?

- **A.** $\mathcal{O}(1)$

- **B.** **[Đáp án đúng]** $\mathcal{O}(\min(N, M))$ bằng cách chỉ lưu 2 dòng phương án $prev$ và $curr$.

- **C.** $\mathcal{O}(N \cdot M)$

- **D.** $\mathcal{O}(\log(N+M))$

> *Giải thích:* Dòng $i$ chỉ phụ thuộc dòng $i-1$, do đó có thể nén bộ nhớ về 2 dòng của chuỗi ngắn hơn, đạt $\mathcal{O}(\min(N, M))$.

#### Câu 14 (Bài toán Xâu đan xen Interleaving String):

Cho ba xâu $A$ (dài $N$), $B$ (dài $M$) và $C$ (dài $N+M$). Trạng thái $dp[i][j]$ là boolean kiểm tra xem tiền tố $C[1 \dots i+j]$ có thể tạo từ $A[1 \dots i]$ và $B[1 \dots j]$. Hệ thức chuyển trạng thái là:

- **A.** $dp[i][j] = dp[i-1][j-1]$

- **B.** **[Đáp án đúng]** $dp[i][j] = (dp[i-1][j] \land A[i]==C[i+j]) \lor (dp[i][j-1] \land B[j]==C[i+j])$

- **C.** $dp[i][j] = dp[i-1][j] + dp[i][j-1]$

- **D.** `dp[i][j] = true`

> *Giải thích:* Ký tự cuối cùng của tiền tố $C$ phải khớp với $A[i]$ (và phần trước tạo từ $A[1 \dots i-1], B[1 \dots j]$) hoặc khớp với $B[j]$.

#### Câu 15 (Đếm số lần xuất hiện xâu con Distinct Subsequences):

Cho xâu $S$ và xâu $T$. Gọi $dp[i][j]$ là số lần xâu $T[1 \dots j]$ xuất hiện dưới dạng dãy con trong $S[1 \dots i]$. Khi $S[i] == T[j]$, công thức chuyển trạng thái là:

- **A.** $dp[i][j] = dp[i-1][j-1]$

- **B.** **[Đáp án đúng]** $dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) \bmod MOD$

- **C.** $dp[i][j] = dp[i-1][j] \times dp[i-1][j-1]$

- **D.** $dp[i][j] = dp[i][j-1]$

> *Giải thích:* Có 2 lựa chọn: Không dùng $S[i]$ để khớp ($dp[i-1][j]$ cách) hoặc dùng $S[i]$ để khớp với $T[j]$ ($dp[i-1][j-1]$ cách).

## 8. Ma trận 15 bài tập thực hành theo mức độ (P0 → P5)

| Mã Bài Tập | Tên Bài Toán | Mức Độ | Trọng Tâm Kiến Thức & DP Invariant |
|---|---|:---:|---|
| $CPPB-DPS-01$ | Dãy con chung dài nhất Cơ Bản (LCS) | **P0** | $dp[i][j]$ trên 2 tiền tố, so khớp $A[i]==B[j]$. |
| $CPPB-DPS-02$ | Độ Dài LCS Của 3 Xâu Ngắn | **P1** | Quy hoạch động 3 chiều $dp[i][j][k]$ kích thước nhỏ. |
| $CPPB-DPS-03$ | Xâu Con Chung Ngắn Nhất (SCS) | **P1** | Áp dụng công thức $N + M - \text{LCS}(A, B)$. |
| $CPPB-DPS-04$ | Chèn Ít Ký Tự Nhất Tạo Xâu Đối Xứng | **P1** | Quy đổi về bài toán $N - \text{LPS}(S)$. |
| $CPPB-DPS-05$ | Khoảng cách biến đổi xâu (Edit Distance) | **P2** | 3 thao tác Chèn, Xóa, Thay thế kèm khởi tạo biên $\mathcal{O}(N \cdot M)$. |
| $CPPB-DPS-06$ | Edit Distance Chi Phí Thao Tác Bất Đối Xứng | **P2** | Chi phí chèn $c_I$, xóa $c_D$, thay thế $c_R$ khác nhau. |
| $CPPB-DPS-07$ | Xâu Con Liên Tiếp Đối Xứng Dài Nhất | **P2** | Longest Palindromic Substring boolean $dp[i][j]$ duyệt theo độ dài $len$. |
| $CPPB-DPS-08$ | Dãy Con Không Liên Tiếp Đối Xứng Dài Nhất | **P2** | Longest Palindromic Subsequence $dp[i][j]$ trên 2 đầu mút. |
| $CPPB-DPS-09$ | Đếm Số Lần Xuất Hiện Dãy Con (Distinct Subseq) | **P3** | Đếm số lần xâu $T$ xuất hiện dưới dạng dãy con của $S$ modulo $10^9+7$. |
| $CPPB-DPS-10$ | Xâu Đan Xen (Interleaving String) | **P3** | Kiểm tra xâu $C$ có được tạo bởi việc đan xen 2 xâu $A$ và $B$. |
| $CPPB-DPS-11$ | Xóa Ít Ký Tự Nhất Để Hai Xâu Bằng Nhau | **P3** | Cực tiểu hóa chi phí xóa ký tự mã ASCII. |
| $CPPB-DPS-12$ | Khôi Phục Chuỗi LCS Cụ Thể | **P4** | Lần ngược từ $(N, M)$ tái tạo chính xác xâu ký tự con chung. |
| $CPPB-DPS-13$ | Khôi Phục Lộ Trình Biến Đổi Edit Distance | **P4** | In ra từng bước thao tác Insert, Delete, Replace cụ thể. |
| $CPPB-DPS-14$ | So Khớp Ký Tự Đại Diện (Wildcard Matching) | **P4** | Xử lý ký tự `?` (1 ký tự) và $*$ (chuỗi bất kỳ $\ge 0$). |
| $CPPB-DPS-15$ | Quy Hoạch Động Chuỗi Olympic (Mastery) | **P5** | Bài toán tối ưu hóa xâu kết hợp điều kiện từ vựng chuẩn thi đấu. |
