# CHUYÊN ĐỀ 12: THUẬT TOÁN QUAY LUI & NHÁNH CẬN (STATE-SPACE SEARCH: BACKTRACKING & BRANCH AND BOUND)
*(State Space Tree, State Identity, Choose-Explore-Unchoose Pattern, Feasibility vs Optimality Pruning, State Restoration Invariant)*

---

## 1. Cầu Nối Kiến Trúc: Recursion $\to$ Divide & Conquer $\to$ State-Space Search $\to$ Dynamic Programming

Để có cái nhìn toàn cảnh về các phương pháp giải thuật lớn trong Lập trình thi đấu:

```text
                               RECURSION (Cơ Chế Điều Khiển Call Stack)
                                                  │
                 ┌────────────────────────────────┴────────────────────────────────┐
                 ▼                                                                 ▼
   DIVIDE & CONQUER (Chia Để Trị)                                    STATE-SPACE SEARCH (Duyệt Không Gian Trạng Thái)
"Phân chia bài toán lớn thành các bài                                              │
 toán con, thường độc lập hoặc giải riêng biệt"                   ┌────────────────┴────────────────┐
                                                                 ▼                                 ▼
                                                        BACKTRACKING (Quay Lui)         BRANCH & BOUND (Nhánh Cận)
                                                   "Xây dựng nghiệm từng bước +         "Tìm kiếm tối ưu kết hợp hàm Cận
                                                    Feasibility Pruning khi vi phạm"     để cắt tỉa nhánh không thể tốt hơn"
                                                                 │                                 │
                                                                 └────────────────┬────────────────┘
                                                                                  │
               Khi nhiều đường đi trong quá trình tìm kiếm gặp lại cùng một State Identity và có thể tái sử dụng kết quả
                                                                                  ▼
                                                        DYNAMIC PROGRAMMING & MEMOIZATION (Quy Hoạch Động)
                                                        "Ghi nhớ kết quả trạng thái để không phải tính lại"
```

* **Divide & Conquer:** $\text{Bài toán lớn} \longrightarrow \text{Các bài toán con riêng biệt}$.
* **Backtracking / State-Space Search:** $\text{Trạng thái hiện tại} \longrightarrow \text{Các nhánh quyết định thử nghiệm (Choices)}$.
* **Dynamic Programming:** $\text{Nhiều đường đi khác nhau} \longrightarrow \text{Cùng một State Identity (Overlapping States)} \implies \text{Memoization / Bảng DP}$.

---

## 2. Bản Chất Trạng Thái (State Definition & State Identity)

### 🧠 Khái niệm State (Trạng thái) & State Identity:
> **Định nghĩa:** **State (Trạng thái)** là tập thông tin tối thiểu cần thiết để xác định chính xác các lựa chọn tiếp theo và kết quả có thể đạt được từ trạng thái hiện tại.
>
> * **Không phải mọi biến xuất hiện trong hàm đệ quy đều là thành phần của State Identity; chỉ những thông tin có thể làm thay đổi các lựa chọn hoặc kết quả của phần còn lại mới cần thiết.**
> * **Trong cài đặt DFS / Quay lui:** State bao gồm cả dữ liệu cấu hình đang xây dựng và các đại lượng tích lũy (`current_value`, `current_cost`).
> * **Khi chuyển sang Quy Hoạch Động (DP):** Ta chắt lọc những biến thực sự tạo nên **"State Identity"** (ví dụ: `dp[index][remaining_weight]` hoặc `dp[city][mask]`), còn giá trị mục tiêu trở thành giá trị lưu trong bảng DP thay vì là tham số đệ quy.

| Bài Toán | State Trong Cài Đặt DFS | State Identity Khi Chuyển Sang DP (Nếu có Memoization/DP) |
|---|---|---|
| **Sinh Hoán Vị** | `(step, visited[], cur[])` | *Thường không dùng DP kiểu thông thường (trừ Bitmask DP về sau)* |
| **N-Queens** | `(row, col_used[], diag1[], diag2[])` | *Không tự động trở thành DP chỉ vì có State (thiếu cấu trúc con tối ưu)* |
| **Subset Sum** | `(index, current_sum, cur_set[])` | `dp[index][current_sum]` |
| **Cái Túi 0/1 (Knapsack)** | `(index, current_weight, current_value)` | `dp[index][remaining_weight]` |
| **Người Du Lịch (TSP)** | `(current_city, visited_mask, current_cost)` | `dp[current_city][visited_mask]` |
| **Sudoku 9x9** | `(board[9][9], empty_cells_list)` | *Không phải ví dụ DP điển hình (CSP Backtracking)* |

> **Quy luật cốt lõi:** Không phải cứ có State là có thể chuyển sang DP. Để chuyển sang DP, bài toán bắt buộc phải có **State Identity gọn gàng** + **Hiện tượng trùng lặp trạng thái (Overlapping Subproblems)** + **Cấu trúc con tối ưu (Optimal Substructure)**.

---

## 3. Khung Phương Pháp Luận: Design-Time Framework vs Runtime Pattern

### 📐 1. Khung Thiết Kế Thuật Toán (Design-Time Framework):
```text
1. Define State (Xác định các biến trạng thái tối thiểu)
       ↓
2. Generate Candidates (Xác định danh sách các lựa chọn khả dĩ)
       ↓
3. Define Feasibility (Thiết lập điều kiện ràng buộc hợp lệ)
       ↓
4. Define Bound (Thiết lập hàm cận LB / UB nếu là bài toán tối ưu)
       ↓
5. Define Transition & Restoration (Quy tắc chuyển trạng thái và hoàn tác)
```

### ⚡ 2. Khung Thực Thi Mã Nguồn (Runtime Pattern):
```cpp
void search(State state) {
    if (isGoal(state)) {
        processSolution(state);
        return;
    }
    for (const auto &candidate : getCandidates(state)) {
        if (!isFeasible(state, candidate)) continue; // Feasibility Pruning

        if (boundSaysImpossible(state, candidate)) continue; // Optimality Pruning (B&B)

        choose(state, candidate);  // 1. Chuyển sang State_new
        search(state);             // 2. Đi sâu vào nhánh con (Explore)
        unchoose(state, candidate);// 3. Hoàn tác về State_before (Restoration)
    }
}
```

---

## 4. Khung Tư Duy Mental Model: Hai Sơ Đồ Cốt Lõi Của Lesson 12

### 🌲 Sơ đồ 1: Cây Quyết Định Quay Lui Thuần Túy (Backtracking)
```text
                    TRẠNG THÁI (STATE)
                            │
            ┌───────────────┴───────────────┐
            │                               │
         HỢP LỆ                          SAI / VI PHẠM
            │                               │
       Đi sâu (Explore)               [CẮT TỈA - PRUNE]
            │
      ┌─────┴─────┐
      │           │
   ĐẠT LÁ      CHƯA XONG
      │           │
  Ghi nhận      Đi tiếp
  nghiệm          │
      │           │
   Return ◄───────┘
      │
  [UNCHOOSE] ──► Khôi phục trạng thái cha để thử nhánh kế tiếp
```

### 🎯 Sơ đồ 2: Cây Nhánh Cận Tối Ưu (Branch & Bound)
```text
                 TRẠNG THÁI (STATE)
                         │
        ┌────────────────┴────────────────┐
        │                                 │
  VI PHẠM RÀNG BUỘC?                    HỢP LỆ
        │                                 │
 [CẮT TỈA - PRUNE]                        ▼
                           ĐÁNH GIÁ HÀM BOUND (LB / UB)
                                          │
                         ┌────────────────┴────────────────┐
                         │                                 │
             BOUND KHÔNG THỂ CẢI THIỆN BEST?       CÓ THỂ CẢI THIỆN BEST?
                         │                                 │
                 [CẮT TỈA - PRUNE]                  Đi sâu (Explore)
```

---

## 5. Bất Biến Trung Tâm: State Restoration Invariant

> **Quy luật cốt lõi:** `Choose-Explore-Unchoose` là một pattern cài đặt phổ biến. Bản chất kỹ thuật sâu sắc là **Bất biến Khôi phục Trạng Thái (State Restoration Invariant)**:
>
> $$\text{State}_{\text{before}} \xrightarrow{\text{Choose}} \text{State}_{\text{new}} \xrightarrow{\text{Explore}} \text{Subtree} \xrightarrow{\text{Unchoose}} \text{State}_{\text{before}}$$
>
> Sau khi khám phá xong một nhánh con và hàm con return, trạng thái phải được trả về **nguyên vẹn 100%** như trước khi bước vào nhánh đó, đảm bảo nhánh kế tiếp bắt đầu từ cùng một trạng thái cha.

---

## 6. Phân Biệt Cắt Tỉa Ràng Buộc (Feasibility) vs Cắt Tỉa Tối Ưu (Branch & Bound)

```text
BACKTRACKING
"Xây dựng nghiệm từng bước + quay lui khi cần (có thể không cần pruning như sinh nhị phân)"

FEASIBILITY PRUNING
"Cắt những trạng thái chắc chắn không thể dẫn tới nghiệm hợp lệ"

BRANCH AND BOUND
"Framework tìm kiếm tối ưu trên không gian trạng thái, kết hợp hàm Cận (Bound) để cắt tỉa nhánh không thể tốt hơn best hiện tại"
```

> **Lưu ý mở rộng:** Trong chuyên đề này, ta triển khai Branch & Bound trên nền DFS / Backtracking để nắm vững nguyên lý. Về tổng quát, Branch & Bound là một framework tìm kiếm tối ưu có thể triển khai bằng Best-First Search với hàng đợi ưu tiên `priority_queue` hoặc BFS.

### Định Nghĩa Chuẩn Xác: $OPT(\text{state})$ vs $best$ Hiện Tại:
* **$OPT(\text{state})$:** Giá trị tốt nhất thực sự có thể đạt được khi hoàn thành nghiệm từ trạng thái hiện tại.
* **$best$ (hoặc $best\_so\_far$ / $incumbent$):** Nghiệm tốt nhất đã tìm thấy trên toàn bộ các nhánh đã khám phá tính đến thời điểm hiện tại (chưa chắc là nghiệm tối ưu toàn cục cho đến khi duyệt xong).

### Nguyên Tắc Thiết Lập Hàm Bound Chuẩn Xác:

1. **Với bài toán Cực Tiểu Hóa (Minimization - ví dụ TSP, Đổi tiền ít xu nhất, Job Assignment):**
   * Ta duy trì hàm Cận Dưới $LB(\text{state}) \le OPT(\text{state})$.
   * **Điều kiện cắt tỉa:** Nếu $LB(\text{state}) \ge \text{best}$, thì $OPT(\text{state}) \ge LB(\text{state}) \ge \text{best} \implies$ **Cắt tỉa ngay!**
   * *Ví dụ:* $best = 100$. Nếu tại một nhánh ta tính được $LB = 105 \implies$ Cắt tỉa ngay vì $OPT \ge 105 > 100$. Nếu $LB = 95 \implies$ **Không được cắt tỉa** vì $OPT$ có thể là $95, 98$ tốt hơn $100$.

2. **Với bài toán Cực Đại Hóa (Maximization - ví dụ Cái túi Knapsack $0/1$):**
   * Ta duy trì hàm Cận Trên $UB(\text{state}) \ge OPT(\text{state})$.
   * **Điều kiện cắt tỉa:** Nếu $UB(\text{state}) \le \text{best}$, thì $OPT(\text{state}) \le UB(\text{state}) \le \text{best} \implies$ **Cắt tỉa ngay!**

> **Mối liên hệ giữa Heuristic Ordering & Branch and Bound:** Heuristic ordering giúp tìm ra nghiệm tốt sớm hơn $\implies best$ được cải thiện nhanh hơn $\implies$ Hàm Bound cắt tỉa được nhiều nhánh hơn $\implies$ Thuật toán B&B chạy nhanh hơn vượt trội!

---

## 7. Phân Loại 4 Cấp Độ Kỹ Thuật Trong Tìm Kiếm Toàn Vẹn

| Kỹ Thuật | Ảnh Hưởng Đến Tính Đúng Đắn | Vai Trò Thuật Toán |
|---|:---:|---|
| **Feasibility Pruning Hợp Lệ** | ✅ Không mất nghiệm hợp lệ | Loại bỏ trạng thái chắc chắn vi phạm ràng buộc bài toán. |
| **Valid Lower / Upper Bound** | ✅ Không mất nghiệm tối ưu | Loại bỏ trạng thái đã chứng minh toán học không thể vượt qua `best`. |
| **Heuristic Ordering** | ✅ Không làm mất nghiệm | Sắp xếp thứ tự thử nhánh (như Warnsdorff) để tìm thấy nghiệm tốt sớm hơn; tính đầy đủ vẫn bảo toàn nếu duyệt hết. |
| **Heuristic Pruning không chứng minh** | ❌ Có thể mất nghiệm | Cắt nhánh theo cảm tính, có nguy cơ bỏ sót nghiệm tối ưu toàn cục. |

---

## 8. Cầu Nối Sâu Sang DP: Từ Cây Tìm Kiếm (Search Tree) Đến Đồ Thị Trạng Thái (State DAG)

```text
                  CÂY TÌM KIẾM (SEARCH TREE)
                          Trạng Thái A
                         /            \
                   Trạng Thái B     Trạng Thái C
                   /          \     /          \
                  D            E   E            F
                               ▲   ▲
                      CÙNG LẶP LẠI TRẠNG THÁI E!
```

* **Duyệt cây thuần túy (Tree Search):** Phải tính toán lại trạng thái `E` nhiều lần ở các nhánh con khác nhau.
* **Quan điểm Đồ thị (State DAG View):** `E` chỉ là một đỉnh duy nhất trong không gian trạng thái.
* **Quy Hoạch Động (Dynamic Programming / Memoization):** Trong những bài toán mà State Identity có số lượng trạng thái đa thức theo kích thước input, Memoization/DP có thể giảm một cây tìm kiếm hàm mũ xuống $\text{Số trạng thái} \times \text{Chi phí chuyển trạng thái}$; ví dụ Knapsack đạt $\mathcal{O}(N \cdot W)$ khi $W$ là tham số giới hạn. Với các bài như TSP, Bitmask DP đạt $\mathcal{O}(N^2 \cdot 2^N)$ nhanh hơn rất nhiều so với vét cạn $N!$.

---

## 9. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

1. **Quên hoàn tác trạng thái (Missing Unchoose Step):**
   * Sau khi gọi đệ quy `backtrack(i + 1)`, quên viết `visited[val] = false;` hoặc `cur_sum -= val;` $\implies$ Trạng thái của nhánh trước bị rò rỉ sang nhánh sau, làm mất toàn bộ các nghiệm tiếp theo.
2. **Bẫy cắt tỉa `break` trong Subset Sum có số âm:**
   * Lệnh `if (current_sum + A[i] > S) break;` chỉ an toàn khi **mọi phần tử $A_i > 0$** và mảng đã sort tăng dần. Tuyệt đối không áp dụng nguyên trạng cho mảng có phần tử âm!
3. **Đánh dấu sai mảng các họ đường chéo trong bài $N$-Queens:**
   * Với chỉ số 1-based:
     * Họ đường chéo xuôi `\`: $row - col \in [-(N-1), N-1] \implies row - col + N \in [1, 2N-1]$.
     * Họ đường chéo ngược `/`: $row + col \in [2, 2N]$.
   * Khai báo `diag1` và `diag2` tối thiểu kích thước $2N + 1$.
4. **Giả thiết về mệnh giá xu trong Coin Change:**
   * Mọi mệnh giá xu $C_i \ge 1$ để đảm bảo độ sâu tối đa bị chặn trên bởi $\lfloor S / C_{\min} \rfloor$.

---

## 10. Mẫu Cài Đặt Chuẩn Thi Đấu (Competitive Templates)

```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

// 1. Sinh Hoán Vị 1..N chuẩn State Restoration Invariant
int n = 3;
vector<int> cur;
vector<bool> visited;

void genPermutations(int step) {
    if (step > n) {
        for (int i = 0; i < n; ++i) cout << cur[i] << (i + 1 == n ? "" : " ");
        cout << "\n";
        return;
    }
    for (int val = 1; val <= n; ++val) {
        if (!visited[val]) {
            visited[val] = true;       // 1. CHOOSE
            cur.push_back(val);
            genPermutations(step + 1); // 2. EXPLORE
            cur.pop_back();            // 3. UNCHOOSE (Khôi phục)
            visited[val] = false;
        }
    }
}

// 2. Bài Toán N-Queens (Đếm số cách đặt N quân hậu)
int n_queens = 4;
ll queen_ways = 0;
vector<bool> col_used, diag1_used, diag2_used;

void solveNQueens(int row) {
    if (row > n_queens) {
        queen_ways++;
        return;
    }
    for (int col = 1; col <= n_queens; ++col) {
        if (!col_used[col] && !diag1_used[row - col + n_queens] && !diag2_used[row + col]) {
            col_used[col] = diag1_used[row - col + n_queens] = diag2_used[row + col] = true; // CHOOSE
            solveNQueens(row + 1); // EXPLORE
            col_used[col] = diag1_used[row - col + n_queens] = diag2_used[row + col] = false; // UNCHOOSE
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    visited.assign(n + 1, false);
    genPermutations(1);

    col_used.assign(n_queens + 1, false);
    diag1_used.assign(2 * n_queens + 1, false);
    diag2_used.assign(2 * n_queens + 1, false);
    solveNQueens(1);
    cout << "So cach dat " << n_queens << " quan hau: " << queen_ways << "\n";
    return 0;
}
```

---

## 11. Hệ Thống Câu Hỏi Kiểm Tra Khái Niệm (Concept Quiz)

#### Câu 1 (Bản chất 3 bước Quay lui):
Thứ tự thực hiện chuẩn mực trong thân vòng lặp của một hàm quay lui (Backtracking) là:
* A. `Explore` $\to$ `Choose` $\to$ `Unchoose`.
* B. **(Đáp án đúng)** `Choose` (Thử và đánh dấu trạng thái) $\to$ `Explore` (Gọi đệ quy đi sâu) $\to$ `Unchoose` (Hoàn tác trạng thái sau khi đệ quy return).
* C. `Unchoose` $\to$ `Choose` $\to$ `Explore`.
* D. `Choose` $\to$ `Unchoose` $\to$ `Explore`.
> *Giải thích:* Quy trình chuẩn là chọn thử một ứng viên hợp lệ, đệ quy khám phá cây con, sau đó bắt buộc phải hoàn tác khi hàm đệ quy return để thử ứng viên tiếp theo.

---

#### Câu 2 (Phân biệt Feasibility vs Optimality Pruning):
Sự khác biệt cốt lõi giữa Cắt tỉa tính khả thi (Feasibility Pruning) và Cắt tỉa tính tối ưu (Optimality Pruning - Branch & Bound) là gì?
* A. Feasibility Pruning chỉ dùng cho bài toán tìm đường đi.
* B. **(Đáp án đúng)** Feasibility Pruning cắt nhánh vì vi phạm ràng buộc không thể tạo nghiệm hợp lệ; Optimality Pruning cắt nhánh vì hàm cận chứng minh nhánh này không thể tạo ra nghiệm tốt hơn `best` hiện có.
* C. Optimality Pruning chạy chậm hơn.
* D. Hai khái niệm hoàn toàn giống hệt nhau.
> *Giải thích:* Feasibility loại bỏ nghiệm sai; Optimality loại bỏ nghiệm đúng nhưng kém tối ưu so với `best` hiện tại.

---

#### Câu 3 (Hậu quả của việc quên Unchoose):
Điều gì sẽ xảy ra nếu lập trình viên quên câu lệnh hoàn tác `visited[i] = false` sau lời gọi đệ quy trong bài toán sinh hoán vị?
* A. Chương trình vẫn chạy đúng nhưng tốn nhiều bộ nhớ hơn.
* B. **(Đáp án đúng)** Trạng thái bị rò rỉ, các nhánh duyệt tiếp theo coi phần tử `i` đã được dùng và bỏ qua, dẫn đến thiếu sót nghiêm trọng các nghiệm hợp lệ.
* C. Chương trình bị tràn số `int`.
* D. Mảng tự động sắp xếp lại.
> *Giải thích:* Quên hoàn tác vi phạm State Restoration Invariant, làm đóng băng trạng thái của các nhánh sau.

---

#### Câu 4 (Đánh dấu các họ đường chéo N-Queens):
Trong bài toán xếp $N$ quân hậu trên bàn cờ $N \times N$ (1-based indexing), để tránh chỉ số mảng bị âm khi đánh dấu một họ đường chéo (hướng `\`) đi qua ô $(row, col)$, công thức chỉ số chuẩn xác là:
* A. `row - col`
* B. **(Đáp án đúng)** `row - col + N` (với $N$ là kích thước bàn cờ, chỉ số thuộc $[1, 2N-1]$).
* C. `row * col`
* D. `(row + col) % N`
> *Giải thích:* Vì $row - col$ có thể nhận giá trị âm từ $-(N-1)$ đến $N-1$, cộng thêm $N$ đảm bảo chỉ số luôn nằm trong khoảng an toàn $[1, 2N-1]$.

---

#### Câu 5 (Bản chất quy tắc Warnsdorff trong Mã đi tuần):
Trong bài toán Mã đi tuần (Knight's Tour), quy tắc Heuristic Warnsdorff (ưu tiên nhảy vào ô có ít nước đi tiếp theo nhất) có vai trò chuẩn xác là gì?
* A. Đảm bảo chắc chắn tìm thấy nghiệm trong $\mathcal{O}(1)$ bước mà không cần quay lui.
* B. **(Đáp án đúng)** Trong framework bài học này, Warnsdorff được xem là Heuristic Ordering: nó thay đổi thứ tự ưu tiên thử nước đi để tìm nghiệm sớm hơn, không tự động loại bỏ các nhánh còn lại.
* C. Dùng để cắt bỏ hoàn toàn các nhánh khác.
* D. Là một thuật toán Quy hoạch động.
> *Giải thích:* Heuristic chỉ đóng vai trò sắp xếp thứ tự thử nước đi (ordering), không thay thế cho toàn bộ cây tìm kiếm.

---

#### Câu 6 (Tình huống thực tế đánh giá hàm Bound trong bài toán Cực tiểu):
Trong bài toán tìm hành trình TSP ngắn nhất, giả sử nghiệm tốt nhất tìm được tính tới thời điểm hiện tại là `best = 100`. Tại một trạng thái nhánh $X$, hàm Cận Dưới tính ra $LB(X) = 105$. Quyết định chuẩn xác của thuật toán là gì?
* A. **(Đáp án đúng)** Cắt tỉa (Prune) ngay lập tức nhánh $X$, vì chi phí thực tế $OPT(X) \ge LB(X) = 105 > 100 = best$, nhánh này chắc chắn không thể cải thiện nghiệm.
* B. Đi sâu tiếp vào nhánh $X$ vì có thể chi phí thực tế sẽ giảm xuống dưới 100.
* C. Đặt lại giá trị `best = 105`.
* D. Dừng toàn bộ chương trình.
> *Giải thích:* Vì $LB(X) \le OPT(X)$, nếu $LB(X) \ge best$ thì chi phí thực tế chắc chắn không thể tốt hơn $best$.

---

#### Câu 7 (Độ phức tạp không gian: Exponential Tree $\ne$ Exponential Stack):
Thuật toán quay lui sinh tất cả $N!$ hoán vị của tập hợp $\{1, \dots, N\}$ tiêu tốn bộ nhớ ngăn xếp (Call Stack Space) tối đa là bao nhiêu?
* A. `Theta(N!)`
* B. `Theta(N^2)`
* C. **(Đáp án đúng)** `Theta(N)` (Search Space đo tổng số trạng thái lá $N!$, nhưng Call Stack chỉ đo độ sâu của một đường đi đang khám phá là $N$).
* D. `Theta(1)`
> *Giải thích:* Cây tìm kiếm khổng lồ không đồng nghĩa với Call Stack khổng lồ; độ sâu ngăn xếp chỉ tỷ lệ thuận với chiều dài nghiệm đang xây dựng.

---

#### Câu 8 (Cắt tỉa kết hợp sắp xếp trong Subset Sum):
Khi tìm các tập con của mảng các số nguyên dương ($A_i > 0$) có tổng bằng $S$, nếu mảng đã được sắp xếp tăng dần, điều kiện cắt tỉa tính khả thi hiệu quả nhất tại vòng lặp duyệt phần tử $A_i$ là gì?
* A. Dừng lại khi mảng còn hơn 10 phần tử.
* B. **(Đáp án đúng)** Dùng lệnh `break` dừng duyệt toàn bộ các phần tử còn lại ngay khi `current_sum + A[i] > S` (dựa trên tính đơn điệu Monotonicity: các phần tử sau $A_{i+1} \ge A_i$ chắc chắn cũng vượt $S$).
* C. Dừng lại khi gặp số chẵn.
* D. Dừng lại khi `current_sum == 0`.
> *Giải thích:* Sắp xếp mảng trước kết hợp giả thiết $A_i > 0$ giúp chuyển điều kiện từ `continue` ở từng nhánh thành `break` triệt tiêu toàn bộ cây con phía sau.

---

#### Câu 9 (Độ phức tạp tổng thể khi in toàn bộ xâu nhị phân):
Chương trình sinh và in toàn bộ các xâu nhị phân độ dài $N$ ra màn hình có tổng thời gian thực thi (Time Complexity) là:
* A. `Theta(2^N)`
* B. **(Đáp án đúng)** `Theta(N * 2^N)` (có đúng $2^N$ xâu nghiệm, và mỗi xâu tốn $\mathcal{O}(N)$ thời gian để xuất ra màn hình).
* C. `Theta(N!)`
* D. `Theta(N)`
> *Giải thích:* Cần phân biệt rõ giữa số lượng nghiệm lá ($\Theta(2^N)$) và tổng thời gian thực thi khi phải xuất toàn bộ nội dung từng nghiệm ($\Theta(N \cdot 2^N)$).

---

#### Câu 10 (Cầu nối từ Backtracking sang Dynamic Programming):
Khi một bài toán quay lui có hiện tượng nhiều nhánh trạng thái khác nhau gặp lại cùng một trạng thái con (Overlapping States trong đồ thị State DAG), dấu hiệu này gợi ý điều gì?
* A. Thuật toán quay lui đã bị lỗi bộ nhớ.
* B. **(Đáp án đúng)** Trùng lặp trạng thái là dấu hiệu quan trọng để xem xét Memoization / Dynamic Programming, lưu kết quả mỗi trạng thái $1$ lần duy nhất thay vì tính lại trên cây.
* C. Bỏ qua hoàn toàn bài toán.
* D. Tăng kích thước mảng lên gấp đôi.
> *Giải thích:* Chuyển từ duyệt cây tìm kiếm (Tree Search) sang đồ thị trạng thái (State DAG) có lưu vết chính là bản chất của Quy Hoạch Động.

---

#### Câu 11 (Bản chất State Identity trong bài toán Subset Sum):
Trong bài toán Subset Sum, giả sử hai lời gọi đệ quy khác nhau đều đang đứng tại chỉ số `index = 5`, nhưng một nhánh có `current_sum = 12` và nhánh kia có `current_sum = 18`. Hai lời gọi này có được xem là cùng một State Identity trong DP không?
* A. Có, vì chúng có cùng chỉ số `index = 5`.
* B. **(Đáp án đúng)** Không, vì `current_sum` quyết định trực tiếp đến các lựa chọn và khả năng đạt tổng mục tiêu còn lại, nên `(index, current_sum)` mới là State Identity hoàn chỉnh.
* C. Có, vì chỉ số mảng quan trọng hơn tổng.
* D. Tùy thuộc vào việc mảng có số âm hay không.
> *Giải thích:* State Identity phải bao hàm đủ thông tin để xác định không gian nghiệm phía sau; khác `current_sum` dẫn đến các bài toán con phía sau hoàn toàn khác nhau.

---

#### Câu 12 (Nguyên tắc an toàn của hàm Bound trong Branch & Bound):
Nếu một lập trình viên thiết kế một hàm Cận Dưới $LB(\text{state})$ cho bài toán tìm chi phí nhỏ nhất, nhưng trong một số trường hợp hiếm gặp $LB(\text{state}) > OPT(\text{state})$ (ước lượng quá cao so với thực tế), hậu quả là gì?
* A. Thuật toán chạy nhanh hơn và luôn cho kết quả đúng.
* B. **(Đáp án đúng)** Thuật toán có thể vô tình cắt tỉa nhánh chứa nghiệm tối ưu thực sự và đưa ra kết quả sai (Invalid Bound).
* C. Bộ nhớ bị tràn.
* D. Không có ảnh hưởng gì vì hiếm khi xảy ra.
> *Giải thích:* Bất biến sống còn của Branch & Bound là $LB \le OPT$; chỉ cần vi phạm một lần, nghiệm tối ưu có thể bị xóa sổ khỏi không gian tìm kiếm.

---

## 12. Ma Trận 16 Bài Tập Thực Hành 4 Tầng Phân Cấp (Level 1 $\to$ Level 4)

### 📌 Lộ Trình Phân Tầng Học Tập Chuẩn Mực:
* **LEVEL 1: Pattern Sinh Cấu Hình Cơ Bản (`CPPB-BKT-01` $\to$ `04`):** Xâu nhị phân, Tập con, Hoán vị, Tổ hợp chập $K$.
* **LEVEL 2: Constraint Backtracking / Feasibility Pruning (`CPPB-BKT-05` $\to$ `09`):** Dãy ngoặc đúng, $N$-Queens, Mê cung, Subset Sum, Chia tập bằng nhau.
* **LEVEL 3: Optimization Search & Branch and Bound (`CPPB-BKT-10`, `13`, `14`, `16`):** Đổi tiền xu ít nhất (B&B), Cái túi $0/1$ B&B, TSP B&B, Phân công công việc B&B.
* **LEVEL 4: Advanced CSP & Heuristic Search (`CPPB-BKT-11`, `12`, `15`):** Mã đi tuần Warnsdorff, Sudoku $9 \times 9$, Tô màu đồ thị ($K$-Coloring).

| STT | Mã Bài | Tên Bài Toán | Difficulty | Concept Group | Output / Time Complexity | Search Space / Number of Solutions | Call Stack | Max Depth |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| 01 | `CPPB-BKT-01` | **Sinh Xâu Nhị Phân Độ Dài $N$** | `P0` | **Level 1** | $\Theta(N \cdot 2^N)$ (Output-sensitive)| $2^N$ nghiệm lá | $\Theta(N)$ | $N$ |
| 02 | `CPPB-BKT-02` | **Sinh Tập Con Của Tập $N$ Phần Tử** | `P0` | **Level 1** | $\Theta(N \cdot 2^N)$ (Output-sensitive)| $2^N$ tập con | $\Theta(N)$ | $N$ |
| 03 | `CPPB-BKT-03` | **Sinh Hoán Vị $1 \dots N$** | `P1` | **Level 1** | $\Theta(N \cdot N!)$ (Output-sensitive)| $N!$ hoán vị lá | $\Theta(N)$ | $N$ |
| 04 | `CPPB-BKT-04` | **Sinh Tổ Hợp Chập $K$ Của $N$** | `P1` | **Level 1** | $\Theta(K \cdot C_N^K)$ (Output-sensitive)| $C_N^K$ tổ hợp | $\Theta(K)$ | $K$ |
| 05 | `CPPB-BKT-05` | **Sinh Dãy Ngoặc Hợp Lệ Độ Dài $2N$** | `P1` | **Level 2** | $\Theta(N \cdot \text{Catalan}(N))$| $\text{Catalan}(N)$ nghiệm | $\Theta(N)$ | $2N$ |
| 06 | `CPPB-BKT-06` | **Bài Toán $N$-Queens (Đếm Số Cách)** | `P2` | **Level 2** | $\mathcal{O}(N!)$ (Worst-case bound) | $\le N!$ gán thô (pruned mạnh) | $\Theta(N)$ | $N$ |
| 07 | `CPPB-BKT-07` | **Mê Cung (Rat in a Maze)** | `P2` | **Level 2** | $\mathcal{O}(4^{N^2})$ (Loose bound) | Cây đường đi $\le 4^{N^2}$ | $\Theta(N^2)$ | $N^2$ |
| 08 | `CPPB-BKT-08` | **Tập Con Có Tổng Bằng $S$ (Subset Sum)** | `P2` | **Level 2** | $\mathcal{O}(2^N)$ (Pruned) | $\le 2^N$ tập con ($A_i > 0$) | $\Theta(N)$ | $N$ |
| 09 | `CPPB-BKT-09` | **Chia Tập Thành 2 Phần Bằng Nhau** | `P3` | **Level 2** | $\mathcal{O}(2^N)$ (Pruned) | $\le 2^N$ phân hoạch | $\Theta(N)$ | $N$ |
| 10 | `CPPB-BKT-10` | **Đổi Tiền Xu Ít Nhất (B&B Coin Change)** | `P3` | **Level 3** | Exponential worst-case | Phụ thuộc chất lượng Bound | $\mathcal{O}(S / C_{\min})$ | $\le \lfloor S / C_{\min} \rfloor$ |
| 11 | `CPPB-BKT-11` | **Mã Đi Tuần (Knight's Tour)** | `P3` | **Level 4** | $\mathcal{O}(8^{N^2})$ (Loose bound) | Search tree with heuristic order | $\Theta(N^2)$ | $N^2$ |
| 12 | `CPPB-BKT-12` | **Trò Chơi Sudoku $9 \times 9$** | `P3` | **Level 4** | $\mathcal{O}(9^E)$ ($E \le 81$ ô trống) | Không gian gán thô $\le 9^E$ | $\mathcal{O}(E)$ | $E \le 81$ |
| 13 | `CPPB-BKT-13` | **Bài Toán Cái Túi $0/1$ Nhánh Cận (B&B)**| `P4` | **Level 3** | Exponential worst-case | Fractional Bound Pruned | $\Theta(N)$ | $N$ |
| 14 | `CPPB-BKT-14` | **Người Du Lịch (TSP) Nhánh Cận** | `P4` | **Level 3** | $\mathcal{O}(N!)$ worst-case | Min-edge Bound Pruned | $\Theta(N)$ | $N$ |
| 15 | `CPPB-BKT-15` | **Tô Màu Đồ Thị (Graph $K$-Coloring)** | `P4` | **Level 4** | $\mathcal{O}(K^V)$ (Pruned) | $\le K^V$ trạng thái màu | $\Theta(V)$ | $V$ |
| 16 | `CPPB-BKT-16` | **Phân Công Công Việc Tối Ưu (Job Assign)**| `P5` | **Level 3** | $\mathcal{O}(N!)$ worst-case | Min-row Bound Pruned | $\Theta(N)$ | $N$ |
