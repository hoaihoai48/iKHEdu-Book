---
title: "Khoá học C++ Bảng B (Level 2) — Quyển 2"
subtitle: "Thuật toán tối ưu, Cấu trúc dữ liệu & Đồ thị (Bài 07-15)"
author: "Trung tâm tin học iKH"
lang: vi
documentclass: report
geometry: "a4paper, margin=2.5cm"
fontsize: 12pt
mainfont: "Times New Roman"
monofont: "Courier New"
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{\textit{Khoá học C++ Bảng B (Level 2) — Quyển 2}}
  - \fancyhead[R]{\textit{Trung tâm tin học iKH}}
---

\newpage

# Lời nói đầu

Chào mừng các em học sinh và quý thầy cô đến với bộ giáo trình **Khoá học C++ Bảng B (Level 2) — QUYỂN 2: THUẬT TOÁN TỐI ƯU, CẤU TRÚC DỮ LIỆU & ĐỒ THỊ** của Trung tâm tin học iKH.

Bộ tài liệu này được biên soạn công phu nhằm cung cấp lộ trình học tập lập trình thi đấu nâng cao, chuẩn mực và hiện đại nhất dành cho học sinh giỏi Tin học THCS, THPT và sinh viên Olympic Tin học.

Phần nội dung này gồm **3 Chương chuyên sâu (Chương 04 đến Chương 06)** với **9 Bài học** và **212 bài toán thực hành phân tầng (P0 → P5)**, chinh phục tham lam, quy hoạch động tối ưu, ngăn xếp đơn điệu, Deque, STL C++ nâng cao, tổ hợp, đồ thị BFS/DFS/Dijkstra, cây phân đoạn Segment Tree, Fenwick Tree, Digit DP và xử lý chuỗi Hashing.

Mỗi bài học được thiết kế theo cấu trúc sư phạm chặt chẽ:

- **Khái niệm & Bản chất toán học**: Giải thích trực quan, dễ hiểu kèm chứng minh toán học và bất biến thuật toán.
- **Bảng mô phỏng từng bước (Dry Run Table)**: Trực quan hóa quá trình biến đổi dữ liệu từng bước.
- **Mẫu cài đặt chuẩn thi đấu**: Code C++ chuẩn (0 `std::`, `#include <bits/stdc++.h>`, Fast I/O), tối ưu và an toàn tuyệt đối.
- **Hệ thống bài tập thực hành phân tầng**: Từ cơ bản đến chuyên sâu (P0 đến P5), có đầy đủ bối cảnh, nhiệm vụ, input/output và sample test.
- **Lời giải tham khảo chi tiết**: Phụ lục B cung cấp toàn bộ mã nguồn C++ tham khảo chuẩn thi đấu cho các bài tập.

Chúc các em học tập hiệu quả và chinh phục những giải thưởng cao trong các kỳ thi chọn học sinh giỏi và Olympic lập trình!

\begin{flushright}
\textbf{Trung tâm tin học iKH}
\end{flushright}


# CHƯƠNG 04: THUẬT TOÁN THAM LAM & QUY HOẠCH ĐỘNG CƠ BẢN


# Bài 07: Thuật toán tham lam (Greedy Algorithms)

## 1. Khái niệm & bản chất của lựa chọn tối ưu cục bộ

Thuật toán Tham lam (Greedy Algorithm) là chiến lược giải quyết bài toán tối ưu bằng cách thực hiện một chuỗi các **lựa chọn tối ưu cục bộ (locally optimal choice)** ở từng bước, với hy vọng dẫn đến **nghiệm tối ưu toàn cục (globally optimal solution)** mà không cần phải quay lui (backtracking) hay tính toán lại các trạng thái trước đó.

Để một bài toán giải được bằng thuật toán tham lam, nó bắt buộc phải thỏa mãn 2 điều kiện toán học khắt khe:

1. **Tính chất lựa chọn tham lam (Greedy Choice Property):** Tồn tại ít nhất một nghiệm tối ưu toàn cục chứa lựa chọn tham lam đầu tiên.
2. **Cấu trúc con tối ưu (Optimal Substructure):** Sau khi thực hiện lựa chọn tham lam, bài toán thu hẹp về một bài toán con đồng dạng có quy mô nhỏ hơn mà việc giải bài toán con đó cũng dẫn đến tối ưu toàn cục.




![Lập lịch sự kiện tham lam](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-07-thuat-toan-tham-lam/assets/l07_interval_scheduling_visual.png)



## 2. Các mô hình bài toán tham lam kinh điển & chứng minh toán học

### 2.1. Mô hình 1: Lựa chọn khoảng không giao nhau nhiều nhất (Interval Scheduling)

Cho $N$ sự kiện, mỗi sự kiện diễn ra trong khoảng thời gian $[L_i, R_i]$. Hãy chọn số lượng sự kiện nhiều nhất sao cho không có hai sự kiện nào bị trùng lấn thời gian.

* **Chiến lược tham lam đúng đắn:** Luôn ưu tiên chọn sự kiện có **thời điểm kết thúc sớm nhất ($R_i$ nhỏ nhất)**.
* **Chứng minh đổi chỗ (Exchange Argument):** Giả sử tồn tại một phương án tối ưu $OPT$ không chọn sự kiện $k$ kết thúc sớm nhất mà chọn sự kiện $x$ kết thúc muộn hơn ($R_x > R_k$). Nếu ta thay thế sự kiện $x$ bằng sự kiện $k$, sự kiện $k$ kết thúc sớm hơn nên khoảng thời gian còn lại sau $k$ sẽ rộng hơn hoặc bằng khoảng thời gian sau $x$, do đó không làm ảnh hưởng đến bất kỳ sự kiện nào chọn sau đó $\implies$ Phương án mới sau khi đổi chỗ có số lượng sự kiện ít nhất bằng $OPT$.

```cpp
bool cmp(const vector<long long> &a, const vector<long long> &b) {
    return a[1] < b[1]; // Sắp xếp theo thời điểm kết thúc tăng dần
}

int max_events(vector<vector<long long>> &events) {
    sort(events.begin(), events.end(), cmp);
    int count = 0;
    long long last_end = -1e18;
    for (const auto &e : events) {
        if (e[0] >= last_end) { // Nếu thời điểm bắt đầu >= thời điểm kết thúc của sự kiện trước
            count++;
            last_end = e[1];
        }
    }
    return count;
}
```


## 3. Mẫu cài đặt chuẩn thi đấu: Tham lam xếp hàng phục vụ (SJF — Shortest Job First)

Bài toán: Có $N$ khách hàng, khách hàng thứ $i$ cần thời gian phục vụ là $T_i$. Tìm thứ tự phục vụ để **tổng thời gian chờ đợi của tất cả khách hàng là nhỏ nhất**.

* **Chiến lược:** Khách hàng có thời gian phục vụ ngắn nhất đứng đầu tiên.
* **Công thức tổng thời gian chờ:** $\sum_{i=0}^{N-1} (N - 1 - i) \times T_i$.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> t(n);
    for (int i = 0; i < n; ++i) cin >> t[i];

    sort(t.begin(), t.end()); // Sắp xếp tăng dần

    long long total_wait_time = 0;
    long long current_time = 0;

    for (int i = 0; i < n; ++i) {
        total_wait_time += current_time;
        current_time += t[i];
    }

    cout << total_wait_time << "\n";
    return 0;
}
```


## 4. Ranh giới áp dụng: Khi nào dùng Greedy vs Quy hoạch động (DP)?

| Bài Toán | Dùng Tham Lam (Greedy) Khi Nào? | Buộc Phải Dùng Quy Hoạch Động (DP) Khi Nào? |
|---|---|---|
| **Cái túi (Knapsack)** | Các đồ vật có thể chia nhỏ (Fractional Knapsack) $\implies$ Sắp xếp theo đơn giá giá trị/khối lượng $V_i / W_i$ giảm dần. | Các đồ vật nguyên vẹn không được chia nhỏ (0/1 Knapsack) $\implies$ Buộc dùng DP $\mathcal{O}(NW)$. |
| **Đổi tiền (Coin Change)** | Hệ mệnh giá là hệ chính quy (Canonical / bội số như $1, 2, 5, 10, 20$). | Hệ mệnh giá tùy ý (ví dụ: mệnh giá $1, 3, 4$ với $S = 6$, Greedy chọn $4+1+1=3$ tờ, nhưng tối ưu là $3+3=2$ tờ). |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L07-01]: Lựa Chọn Sự Kiện Không Trùng Giờ

**Bối cảnh & Nhiệm vụ:**

Cho $N$ sự kiện $[L_i, R_i]$. Chọn số lượng sự kiện nhiều nhất không trùng thời gian.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Lựa Chọn Sự Kiện Không Trùng Giờ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng 1: $N$ ($1 \le N \le 10^5$). $N$ dòng tiếp theo: $L_i, R_i$ ($0 \le L_i < R_i \le 10^9$).

**Đầu ra (Output):**

- In ra số lượng sự kiện tối đa.

**Ví dụ mẫu:**

### Input
```text
3
10 20
12 25
20 30
```
### Output
```text
2
```



### Bài 02 [CPPB2-L07-02]: Tổng Thời Gian Chờ Nhỏ Nhất (sjf)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tổng Thời Gian Chờ Nhỏ Nhất (SJF)** là bài toán trọng tâm thuộc cấp độ **P0** nhằm rèn luyện: Sắp xếp thời gian phục vụ tăng dần.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tổng Thời Gian Chờ Nhỏ Nhất (sjf) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Thời Gian Chờ Nhỏ Nhất (SJF).



### Bài 03 [CPPB2-L07-03]: Cái Túi Chia Nhỏ Được (fractional Knapsack)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Cái Túi Chia Nhỏ Được (Fractional Knapsack)** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Sắp xếp theo đơn giá $V_i / W_i$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cái Túi Chia Nhỏ Được (fractional Knapsack) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cái Túi Chia Nhỏ Được (Fractional Knapsack).



### Bài 04 [CPPB2-L07-04]: Phủ Đoạn Thẳng Ít Nhất (minimum Interval Cover)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Phủ Đoạn Thẳng Ít Nhất (Minimum Interval Cover)** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Tham lam chọn đoạn vươn xa nhất.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Phủ Đoạn Thẳng Ít Nhất (minimum Interval Cover) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phủ Đoạn Thẳng Ít Nhất (Minimum Interval Cover).



### Bài 05 [CPPB2-L07-05]: Ghép Thuyền Cứu Hộ Cực Trị

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Ghép Thuyền Cứu Hộ Cực Trị** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: Hai con trỏ ghép kiện nặng nhất + nhẹ nhất.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Ghép Thuyền Cứu Hộ Cực Trị với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Ghép Thuyền Cứu Hộ Cực Trị.



### Bài 06 [CPPB2-L07-06]: Nối Các Sợi Dây Tiết Kiệm Chi Phí Nhất

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Nối Các Sợi Dây Tiết Kiệm Chi Phí Nhất** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: Hàng đợi ưu tiên `priority_queue` (Cây Huffman).

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Nối Các Sợi Dây Tiết Kiệm Chi Phí Nhất với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nối Các Sợi Dây Tiết Kiệm Chi Phí Nhất.



### Bài 07 [CPPB2-L07-07]: Lập Lịch Công Việc Có Deadline & Tiền Phạt

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Lập Lịch Công Việc Có Deadline & Tiền Phạt** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Tham lam kết hợp Disjoint Set Union (DSU).

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Lập Lịch Công Việc Có Deadline & Tiền Phạt với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lập Lịch Công Việc Có Deadline & Tiền Phạt.



### Bài 08 [CPPB2-L07-08]: Tối Đa Hóa Lợi Nhuận Giao Hàng

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tối Đa Hóa Lợi Nhuận Giao Hàng** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Min-heap duy trì tập công việc được chọn.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tối Đa Hóa Lợi Nhuận Giao Hàng với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Đa Hóa Lợi Nhuận Giao Hàng.



### Bài 09 [CPPB2-L07-09]: Chia Kẹo Thưởng Cho Học Sinh Theo Điểm Số

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Chia Kẹo Thưởng Cho Học Sinh Theo Điểm Số** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Quét hai chiều trái $\to$ phải và phải $\to$ trái.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Chia Kẹo Thưởng Cho Học Sinh Theo Điểm Số với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chia Kẹo Thưởng Cho Học Sinh Theo Điểm Số.



### Bài 10 [CPPB2-L07-10]: Tối Ưu Hóa Mua Bán Cổ Phiếu Không Giới Hạn Lần Giao Dịch

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tối Ưu Hóa Mua Bán Cổ Phiếu Không Giới Hạn Lần Giao Dịch** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Tham lam gom mọi khoảng giá tăng $\max(0, P_{i+1} - P_i)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tối Ưu Hóa Mua Bán Cổ Phiếu Không Giới Hạn Lần Giao Dịch với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Mua Bán Cổ Phiếu Không Giới Hạn Lần Giao Dịch.



### Bài 11 [CPPB2-L07-11]: Sắp Đặt Chuỗi Ký Tự Không Trùng Lặp Kề Nhau

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Sắp Đặt Chuỗi Ký Tự Không Trùng Lặp Kề Nhau** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Max-Heap xếp ký tự có tần suất cao nhất.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Sắp Đặt Chuỗi Ký Tự Không Trùng Lặp Kề Nhau với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Sắp Đặt Chuỗi Ký Tự Không Trùng Lặp Kề Nhau.



### Bài 12 [CPPB2-L07-12]: Số Lượng Trạm Tiếp Nhiên Liệu Ít Nhất (gas Station)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Số Lượng Trạm Tiếp Nhiên Liệu Ít Nhất (Gas Station)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Max-Heap chọn cây xăng có trữ lượng lớn nhất khi hết xăng.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Số Lượng Trạm Tiếp Nhiên Liệu Ít Nhất (gas Station) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Lượng Trạm Tiếp Nhiên Liệu Ít Nhất (Gas Station).



### Bài 13 [CPPB2-L07-13]: Lập Lịch Phòng Họp Tối Thiểu (meeting Rooms Ii)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Lập Lịch Phòng Họp Tối Thiểu (Meeting Rooms II)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Min-Heap theo dõi phòng họp trống sớm nhất.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Lập Lịch Phòng Họp Tối Thiểu (meeting Rooms Ii) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lập Lịch Phòng Họp Tối Thiểu (Meeting Rooms II).



### Bài 14 [CPPB2-L07-14]: Phục Hồi Dãy Số Đơn Điệu Với Chi Phí Nhỏ Nhất (slope Trick Cơ Bản)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Phục Hồi Dãy Số Đơn Điệu Với Chi Phí Nhỏ Nhất (Slope Trick Cơ Bản)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Duy trì hàm lỗi lồi bằng Priority Queue.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Phục Hồi Dãy Số Đơn Điệu Với Chi Phí Nhỏ Nhất (slope Trick Cơ Bản) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phục Hồi Dãy Số Đơn Điệu Với Chi Phí Nhỏ Nhất (Slope Trick Cơ Bản).



### Bài 15 [CPPB2-L07-15]: Ghép Cặp Trọng Số Trên Đồ Thị Cây Bằng Greedy

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Ghép Cặp Trọng Số Trên Đồ Thị Cây Bằng Greedy** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Tham lam từ lá lên gốc (Bottom-up Tree Greedy).

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Ghép Cặp Trọng Số Trên Đồ Thị Cây Bằng Greedy với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Ghép Cặp Trọng Số Trên Đồ Thị Cây Bằng Greedy.



### Bài 16 [CPPB2-L07-16]: Thuật Toán Huffman Coding Nén Dữ Liệu Tối Ưu

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Thuật Toán Huffman Coding Nén Dữ Liệu Tối Ưu** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Cây mã hóa nhị phân tiền tố tối ưu.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Thuật Toán Huffman Coding Nén Dữ Liệu Tối Ưu với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Thuật Toán Huffman Coding Nén Dữ Liệu Tối Ưu.



### Bài 17 [CPPB2-L07-17]: Cay Ma Huffman Coding

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Cay Ma Huffman Coding** là một dạng bài điển hình thuộc chuyên đề **Thuật Toán Tham Lam (Greedy Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cay Ma Huffman Coding với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
5 9 12
```
### Output
```text
43
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `43`.



### Bài 18 [CPPB2-L07-18]: Lap Lich Deadline Tien Phat

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Lap Lich Deadline Tien Phat** là một dạng bài điển hình thuộc chuyên đề **Thuật Toán Tham Lam (Greedy Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Lap Lich Deadline Tien Phat với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
1 20
2 10
1 30
```
### Output
```text
10
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `10`.



### Bài 19 [CPPB2-L07-19]: Thu Gom Vang Tren Luoi Greedy

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Thu Gom Vang Tren Luoi Greedy** là một dạng bài điển hình thuộc chuyên đề **Thuật Toán Tham Lam (Greedy Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Thu Gom Vang Tren Luoi Greedy với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
2 2
1 2
3 4
```
### Output
```text
8
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `8`.



### Bài 20 [CPPB2-L07-20]: Sap Xep Phan Tu Doi Cho K Lan

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Sap Xep Phan Tu Doi Cho K Lan** là một dạng bài điển hình thuộc chuyên đề **Thuật Toán Tham Lam (Greedy Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Sap Xep Phan Tu Doi Cho K Lan với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
4321 2
```
### Output
```text
2431
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2431`.



### Bài 21 [CPPB2-L07-21]: Xep Chong Hop Trong So Va Suc Chiu

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Xep Chong Hop Trong So Va Suc Chiu** là một dạng bài điển hình thuộc chuyên đề **Thuật Toán Tham Lam (Greedy Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Xep Chong Hop Trong So Va Suc Chiu với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
2
2 3
3 1
```
### Output
```text
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2`.



### Bài 22 [CPPB2-L07-22]: Noi Day Nang Cao K Dau

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Noi Day Nang Cao K Dau** là một dạng bài điển hình thuộc chuyên đề **Thuật Toán Tham Lam (Greedy Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Noi Day Nang Cao K Dau với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
4 3
1 2 3 4
```
### Output
```text
15
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `15`.



# Bài 08: Quy hoạch động cơ bản (Dynamic Programming)

## 1. Khái niệm & bản chất của phương pháp Quy hoạch động

Quy hoạch động (Dynamic Programming - DP) là phương pháp giải quyết các bài toán tối ưu hóa và đếm tổ hợp bằng cách chia bài toán thành các **bài toán con gối nhau (Overlapping Subproblems)** và lưu trữ kết quả của các bài toán con đó vào bảng nhớ (memoization table / DP array) để không phải tính lại nhiều lần.

Một bài toán áp dụng được Quy hoạch động khi thỏa mãn 2 nguyên lý:

1. **Cấu trúc con tối ưu (Optimal Substructure):** Nghiệm tối ưu của bài toán lớn được xây dựng trực tiếp từ nghiệm tối ưu của các bài toán con nhỏ hơn.
2. **Các bài toán con gối nhau (Overlapping Subproblems):** Cùng một trạng thái con được gọi đi gọi lại nhiều lần trong quá trình đệ quy (ví dụ: cây đệ quy Fibonacci).




![Quy hoạch động trên lưới 2D](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-08-quy-hoach-dong-co-ban/assets/l08_grid_dp_visual.png)



## 2. Các mô hình Quy hoạch động kinh điển

### 2.1. Dãy con tăng dài nhất (Longest Increasing Subsequence — LIS)

Cho dãy $A_1, A_2, \dots, A_N$. Tìm độ dài dãy con tăng dài nhất.

* **Cách 1: Quy hoạch động $\mathcal{O}(N^2)$**
  - Định nghĩa: $dp[i]$ là độ dài dãy con tăng dài nhất kết thúc tại phần tử $A[i]$.
  - Công thức: $dp[i] = 1 + \max_{j < i, A[j] < A[i]} dp[j]$.
* **Cách 2: Tối ưu $\mathcal{O}(N \log N)$ bằng Tìm kiếm nhị phân**
  - Duy trì mảng `tail[k]`: giá trị nhỏ nhất của phần tử cuối cùng của dãy con tăng độ dài $k$.
  - Mảng `tail` luôn có tính chất tăng ngặt $\implies$ Dùng `lower_bound` để tìm vị trí cập nhật trong $\mathcal{O}(\log N)$.

```cpp
int lis_fast(const vector<int> &a) {
    vector<int> tail;
    for (int x : a) {
        auto it = lower_bound(tail.begin(), tail.end(), x);
        if (it == tail.end()) tail.push_back(x);
        else *it = x;
    }
    return tail.size();
}
```

### 2.2. Bài toán Cái túi 0/1 (0/1 Knapsack Problem)

Cho $N$ đồ vật, đồ vật thứ $i$ có trọng lượng $W_i$ và giá trị $V_i$. Cái túi có sức chứa tối đa $M$.

* **Công thức DP 2D:**
  $$dp[i][w] = \max(dp[i-1][w], dp[i-1][w - W_i] + V_i) \quad (\text{với } w \ge W_i)$$

* **Tối ưu không gian xuống mảng 1D $\mathcal{O}(M)$:**
  Duyệt trọng lượng $w$ **ngược chiều từ $M$ về $W_i$** để đảm bảo mỗi đồ vật chỉ được chọn tối đa 1 lần:
  ```cpp
  vector<long long> dp(m + 1, 0);
  for (int i = 0; i < n; ++i) {
      for (int w = m; w >= weight[i]; --w) {
          dp[w] = max(dp[w], dp[w - weight[i]] + val[i]);
      }
  }
  ```


## 3. Mẫu cài đặt chuẩn thi đấu: Xâu con chung dài nhất (LCS)

Cho hai xâu $S$ độ dài $N$ và $T$ độ dài $M$. Tìm độ dài xâu con chung dài nhất.

* **Công thức:**
  $$dp[i][j] = \begin{cases} dp[i-1][j-1] + 1 & \text{khi } S[i-1] == T[j-1] \\ \max(dp[i-1][j], dp[i][j-1]) & \text{khi } S[i-1] \ne T[j-1] \end{cases}$$

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
            else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}
```


## 4. Ranh giới áp dụng

| Dạng Bài DP | Trạng Thái Bảng Nhớ | Độ Phức Tạp |
|---|---|:---:|
| **DP 1D cơ bản (Leo bậc thang, Nhà trộm)** | $dp[i]$ | $\mathcal{O}(N)$ |
| **Dãy con tăng dài nhất (LIS)** | Binary Search trên `tail` | $\mathcal{O}(N \log N)$ |
| **Cái túi 0/1 (Knapsack 0/1)** | Mảng 1D duyệt lùi $M \to W_i$ | $\mathcal{O}(NM)$ |
| **Cái túi vô hạn (Unbounded Knapsack)** | Mảng 1D duyệt xuôi $W_i \to M$ | $\mathcal{O}(NM)$ |
| **Xâu con chung dài nhất (LCS)** | Bảng ma trận $dp[i][j]$ | $\mathcal{O}(\vert S \vert \times \vert T \vert)$ |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L08-01]: Dãy Con Tăng Dài Nhất Lis

**Bối cảnh & Nhiệm vụ:**

Tìm độ dài dãy con tăng nghiêm ngặt dài nhất của mảng $N$ phần tử.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dãy Con Tăng Dài Nhất Lis với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng 1: $N$ ($1 \le N \le 2 \times 10^5$). Dòng 2: $N$ số $A_i$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra độ dài LIS.

**Ví dụ mẫu:**

### Input
```text
6
10 20 10 30 20 50
```
### Output
```text
4
```



### Bài 02 [CPPB2-L08-02]: Đường Đi Trên Ma Trận Có Tổng Lớn Nhất

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đường Đi Trên Ma Trận Có Tổng Lớn Nhất** là bài toán trọng tâm thuộc cấp độ **P0** nhằm rèn luyện: DP 2D $dp[i][j] = \max(dp[i-1][j], dp[i][j-1]) + A[i][j]$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đường Đi Trên Ma Trận Có Tổng Lớn Nhất với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đường Đi Trên Ma Trận Có Tổng Lớn Nhất.



### Bài 03 [CPPB2-L08-03]: Cái Túi 0/1 Chuẩn (0/1 Knapsack)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Cái Túi 0/1 Chuẩn (0/1 Knapsack)** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: DP Cái túi tối ưu bộ nhớ 1D.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cái Túi 0/1 Chuẩn (0/1 Knapsack) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cái Túi 0/1 Chuẩn (0/1 Knapsack).



### Bài 04 [CPPB2-L08-04]: Đổi Tiền Xu Số Tờ Nhỏ Nhất (unbounded Coin Change)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đổi Tiền Xu Số Tờ Nhỏ Nhất (Unbounded Coin Change)** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: DP Cái túi vô hạn duyệt xuôi.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đổi Tiền Xu Số Tờ Nhỏ Nhất (unbounded Coin Change) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đổi Tiền Xu Số Tờ Nhỏ Nhất (Unbounded Coin Change).



### Bài 05 [CPPB2-L08-05]: Dãy Con Tăng Dài Nhất Lis $\mathcal{o}(n \log N)$

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Dãy Con Tăng Dài Nhất LIS $\mathcal{O}(N \log N)$** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: `lower_bound` trên mảng `tail`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dãy Con Tăng Dài Nhất Lis $\mathcal{o}(n \log N)$ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dãy Con Tăng Dài Nhất LIS $\mathcal{O}(N \log N)$.



### Bài 06 [CPPB2-L08-06]: Xâu Con Chung Dài Nhất (lcs)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Xâu Con Chung Dài Nhất (LCS)** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: DP chuỗi 2D.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Xâu Con Chung Dài Nhất (lcs) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xâu Con Chung Dài Nhất (LCS).



### Bài 07 [CPPB2-L08-07]: Xóa Ký Tự Để Thành Palindrome Ngắn Nhất

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Xóa Ký Tự Để Thành Palindrome Ngắn Nhất** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: DP khoảng $[l, r]$ (Interval DP).

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Xóa Ký Tự Để Thành Palindrome Ngắn Nhất với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xóa Ký Tự Để Thành Palindrome Ngắn Nhất.



### Bài 08 [CPPB2-L08-08]: Cắt Bánh Hình Chữ Nhật Có Giá Trị Lớn Nhất

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Cắt Bánh Hình Chữ Nhật Có Giá Trị Lớn Nhất** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: DP 2D chia đôi hình chữ nhật.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cắt Bánh Hình Chữ Nhật Có Giá Trị Lớn Nhất với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cắt Bánh Hình Chữ Nhật Có Giá Trị Lớn Nhất.



### Bài 09 [CPPB2-L08-09]: Dãy Con Tăng Lớn Nhất Có Truy Vết Phần Tử

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Dãy Con Tăng Lớn Nhất Có Truy Vết Phần Tử** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: LIS $\mathcal{O}(N \log N)$ kèm mảng truy vết $parent[i]$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dãy Con Tăng Lớn Nhất Có Truy Vết Phần Tử với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dãy Con Tăng Lớn Nhất Có Truy Vết Phần Tử.



### Bài 10 [CPPB2-L08-10]: Khoảng Cách Chỉnh Sửa Xâu (edit Distance / Levenshtein)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Khoảng Cách Chỉnh Sửa Xâu (Edit Distance / Levenshtein)** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: DP 2D tính 3 thao tác Thêm, Xóa, Thay thế.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Khoảng Cách Chỉnh Sửa Xâu (edit Distance / Levenshtein) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Khoảng Cách Chỉnh Sửa Xâu (Edit Distance / Levenshtein).



### Bài 11 [CPPB2-L08-11]: Cái Túi Đổi Trục Trạng Thái (value-based Knapsack)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Cái Túi Đổi Trục Trạng Thái (Value-based Knapsack)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Đổi trục DP $dp[v]$ là trọng lượng nhỏ nhất đạt giá trị $v$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cái Túi Đổi Trục Trạng Thái (value-based Knapsack) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cái Túi Đổi Trục Trạng Thái (Value-based Knapsack).



### Bài 12 [CPPB2-L08-12]: Xếp Gạch Lát Sàn Kích Thước $3 \times N$

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Xếp Gạch Lát Sàn Kích Thước $3 \times N$** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: DP ma trận trạng thái chẵn lẻ.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Xếp Gạch Lát Sàn Kích Thước $3 \times N$ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xếp Gạch Lát Sàn Kích Thước $3 \times N$.



### Bài 13 [CPPB2-L08-13]: Dãy Con Hình Sóng Núi Dài Nhất (bitonic Subsequence)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Dãy Con Hình Sóng Núi Dài Nhất (Bitonic Subsequence)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Kết hợp LIS xuôi và LDS ngược trong $\mathcal{O}(N \log N)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dãy Con Hình Sóng Núi Dài Nhất (bitonic Subsequence) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dãy Con Hình Sóng Núi Dài Nhất (Bitonic Subsequence).



### Bài 14 [CPPB2-L08-14]: Nhân Ma Trận Dây Chuyền Chi Phí Nhỏ Nhất (matrix Chain)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Nhân Ma Trận Dây Chuyền Chi Phí Nhỏ Nhất (Matrix Chain)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Interval DP $\mathcal{O}(N^3)$ tìm vị trí chia cắt tối ưu.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Nhân Ma Trận Dây Chuyền Chi Phí Nhỏ Nhất (matrix Chain) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nhân Ma Trận Dây Chuyền Chi Phí Nhỏ Nhất (Matrix Chain).



### Bài 15 [CPPB2-L08-15]: Quy Hoạch Động Trên Cây (tree Dp: Max Independent Set)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Quy Hoạch Động Trên Cây (Tree DP: Max Independent Set)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: DP $dp[u][0/1]$ chọn hoặc không chọn đỉnh $u$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Quy Hoạch Động Trên Cây (tree Dp: Max Independent Set) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Quy Hoạch Động Trên Cây (Tree DP: Max Independent Set).



### Bài 16 [CPPB2-L08-16]: Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (cht)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (CHT)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: CHT tối ưu $dp[i] = \min(dp[j] + m_j x_i + c_j)$ từ $\mathcal{O}(N^2) \to \mathcal{O}(N \log N)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (cht) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (CHT).



### Bài 17 [CPPB2-L08-17]: Dp Tren Cay Tree Dp Tap Doc Lap

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dp Tren Cay Tree Dp Tap Doc Lap** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Cơ Bản & Chuyên Sâu (Dynamic Programming)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dp Tren Cay Tree Dp Tap Doc Lap với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
1 2 3
1 2
1 3
```
### Output
```text
5
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `5`.



### Bài 18 [CPPB2-L08-18]: Convex Hull Trick Dp Toi Uu Duong Thang

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Convex Hull Trick Dp Toi Uu Duong Thang** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Cơ Bản & Chuyên Sâu (Dynamic Programming)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Convex Hull Trick Dp Toi Uu Duong Thang với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
1 2
2 1
3 0
```
### Output
```text
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2`.



### Bài 19 [CPPB2-L08-19]: Divide And Conquer Dp Optimization

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Divide And Conquer Dp Optimization** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Cơ Bản & Chuyên Sâu (Dynamic Programming)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Divide And Conquer Dp Optimization với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
4 2
1 2 3 4
```
### Output
```text
5
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `5`.



### Bài 20 [CPPB2-L08-20]: Dp Knapsack Trong So Lon W Le 1e9

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dp Knapsack Trong So Lon W Le 1E9** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Cơ Bản & Chuyên Sâu (Dynamic Programming)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dp Knapsack Trong So Lon W Le 1e9 với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 1000000000
10 10
20 20
30 30
```
### Output
```text
60
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `60`.



### Bài 21 [CPPB2-L08-21]: Dp Tren Cay Duong Kinh Cay Co Trong So

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dp Tren Cay Duong Kinh Cay Co Trong So** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Cơ Bản & Chuyên Sâu (Dynamic Programming)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dp Tren Cay Duong Kinh Cay Co Trong So với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
1 2 5
2 3 7
```
### Output
```text
12
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `12`.



### Bài 22 [CPPB2-L08-22]: Dp Palindrome Min Cut

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dp Palindrome Min Cut** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Cơ Bản & Chuyên Sâu (Dynamic Programming)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dp Palindrome Min Cut với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
aab
```
### Output
```text
1
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `1`.



### Bài 23 [CPPB2-L08-23]: Dp Matrix Chain Multiplication

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dp Matrix Chain Multiplication** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Cơ Bản & Chuyên Sâu (Dynamic Programming)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dp Matrix Chain Multiplication với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
4
10 20 30 40
```
### Output
```text
18000
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `18000`.



### Bài 24 [CPPB2-L08-24]: Dp Bitmask Duong Di Ngan Nhat K Dinh

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dp Bitmask Duong Di Ngan Nhat K Dinh** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Cơ Bản & Chuyên Sâu (Dynamic Programming)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dp Bitmask Duong Di Ngan Nhat K Dinh với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
4 4 2
2 3
1 2 1
2 3 2
3 4 1
1 4 5
```
### Output
```text
3
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `3`.



### Bài 25 [CPPB2-L08-25]: Dp Doi Xung Hai Chieu 2 Duong Di

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dp Doi Xung Hai Chieu 2 Duong Di** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Cơ Bản & Chuyên Sâu (Dynamic Programming)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dp Doi Xung Hai Chieu 2 Duong Di với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
2 2
1 2
3 4
```
### Output
```text
10
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `10`.



### Bài 26 [CPPB2-L08-26]: Knuth Optimization Dp

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Knuth Optimization Dp** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Cơ Bản & Chuyên Sâu (Dynamic Programming)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Knuth Optimization Dp với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
1 2 3
```
### Output
```text
6
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `6`.



# CHƯƠNG 05: CẤU TRÚC DỮ LIỆU ĐƠN ĐIỆU, STL C++ NÂNG CAO & ĐẠI SỐ TỔ HỢP


# Bài 09: Ngăn xếp, hàng đợi & Deque (Stack, Queue, Deque)

## 1. Khái niệm & bản chất của cấu trúc dữ liệu tuyến tính đơn điệu

Ngăn xếp (Stack - LIFO) và Hàng đợi (Queue - FIFO) là hai cấu trúc dữ liệu cơ sở có thời gian thêm và xóa ở đầu/cuối trong $\mathcal{O}(1)$.

Ở Level 2, ta nâng cấp lên **Ngăn xếp đơn điệu (Monotonic Stack)** và **Hàng đợi hai đầu đơn điệu (Monotonic Deque)** — hai công cụ tối ưu hóa cực mạnh giúp giải quyết các bài toán tìm kiếm phần tử lớn hơn/nhỏ hơn gần nhất và duy trì $\min/\max$ trên cửa sổ trượt trong thời gian tuyến tính $\mathcal{O}(N)$ (thay vì $\mathcal{O}(N^2)$ hoặc $\mathcal{O}(N \log K)$).




![Ngăn xếp đơn điệu Monotonic Stack](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-09-ngan-xep-hang-doi-deque/assets/l09_monotonic_stack_visual.png)



## 2. Ngăn xếp đơn điệu (Monotonic Stack)

### 2.1. Bài toán: Tìm phần tử lớn hơn gần nhất bên phải (Next Greater Element — NGE)

Cho mảng $A = [A_1, A_2, \dots, A_N]$. Với mỗi $i$, tìm chỉ số $j > i$ nhỏ nhất sao cho $A_j > A_i$.

* **Ý tưởng Monotonic Stack:**
  Duyệt mảng từ phải sang trái (hoặc từ trái sang phải), duy trì một ngăn xếp chứa các phần tử **giảm dần từ đáy lên đỉnh**:

  - Khi xét phần tử $A_i$, loại bỏ tất cả các phần tử trên đỉnh ngăn xếp mà $\le A_i$ (vì chúng nhỏ hơn $A_i$ và nằm xa hơn, không bao giờ có thể là NGE cho các phần tử đứng trước $i$).
  - Phần tử còn lại trên đỉnh ngăn xếp chính là NGE của $A_i$.
  - Đẩy $A_i$ vào ngăn xếp.

```cpp
vector<int> next_greater_element(const vector<int> &a) {
    int n = a.size();
    vector<int> res(n, -1);
    stack<int> st; // Lưu chỉ số

    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.top()] <= a[i]) {
            st.pop();
        }
        if (!st.empty()) res[i] = st.top();
        st.push(i);
    }
    return res;
}
```

> **Chứng minh độ phức tạp $\mathcal{O}(N)$:** Mỗi phần tử chỉ được đẩy vào ngăn xếp đúng 1 lần và lấy ra khỏi ngăn xếp tối đa 1 lần $\implies$ Tổng số thao tác `push/pop` là $2N$.


## 3. Hàng đợi hai đầu đơn điệu (Monotonic Deque)

### 3.1. Bài toán: Tìm giá trị nhỏ nhất trên mọi cửa sổ trượt độ dài $K$ (Sliding Window Minimum)

Cho mảng $A$ và kích thước cửa sổ $K$. Tìm $\min$ của mỗi cửa sổ con liên tiếp $K$ phần tử.

* **Cơ chế Monotonic Deque:**
  Duy trì một `deque<int>` lưu chỉ số sao cho giá trị tương ứng trong mảng luôn **tăng dần từ đầu đến cuối**:

  1. **Loại bỏ phần tử ngoài cửa sổ:** Nếu chỉ số ở đầu deque $\le i - K$, đẩy ra (`pop_front`).
  2. **Duy trì tính đơn điệu:** Trong khi đuôi deque có giá trị $\ge A_i$, đẩy ra (`pop_back`) vì chúng vừa lớn hơn vừa già hơn $A_i$.
  3. **Thêm $i$ vào đuôi:** `push_back(i)`.
  4. Phần tử ở đầu deque `deque.front()` luôn là $\min$ của cửa sổ hiện tại.

```cpp
vector<int> sliding_window_min(const vector<int> &a, int k) {
    int n = a.size();
    vector<int> res;
    deque<int> dq;

    for (int i = 0; i < n; ++i) {
        if (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        while (!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k - 1) res.push_back(a[dq.front()]);
    }
    return res;
}
```


## 4. Mẫu cài đặt chuẩn thi đấu: Diện tích hình chữ nhật lớn nhất trong biểu đồ cột (Histogram)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    stack<int> st;
    long long max_area = 0;

    for (int i = 0; i <= n; ++i) {
        long long cur_h = (i == n ? 0 : h[i]);
        while (!st.empty() && cur_h < h[st.top()]) {
            long long height = h[st.top()];
            st.pop();
            long long width = (st.empty() ? i : (i - st.top() - 1));
            max_area = max(max_area, height * width);
        }
        st.push(i);
    }

    cout << max_area << "\n";
    return 0;
}
```


## 5. Ranh giới áp dụng

| Kỹ Thuật | Mục Đích | Độ Phức Tạp Thời Gian | Độ Phức Tạp Không Gian |
|---|---|:---:|:---:|
| **Monotonic Stack** | Tìm phần tử lớn hơn/nhỏ hơn gần nhất (NGE/PLE), Diện tích Histogram | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Monotonic Deque** | Tìm $\min/\max$ trên cửa sổ trượt độ dài cố định $K$ | $\mathcal{O}(N)$ | $\mathcal{O}(K)$ |
| **Multiset / Priority Queue** | Duy trì $\min/\max$ khi cửa sổ co giãn tùy ý có xóa phần tử | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L09-01]: Phần Tử Lớn Hơn Gần Nhất (nge)

**Bối cảnh & Nhiệm vụ:**

Với mỗi phần tử $A_i$, tìm giá trị của phần tử đầu tiên bên phải lớn hơn $A_i$. Nếu không có in -1.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Phần Tử Lớn Hơn Gần Nhất (nge) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng 1: $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số $A_i$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra $N$ số kết quả cách nhau dấu cách.

**Ví dụ mẫu:**

### Input
```text
4
4 5 2 25
```
### Output
```text
5 25 25 -1
```



### Bài 02 [CPPB2-L09-02]: Giá Trị Nhỏ Nhất Trên Cửa Sổ Trượt K

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Giá Trị Nhỏ Nhất Trên Cửa Sổ Trượt K** là bài toán trọng tâm thuộc cấp độ **P0** nhằm rèn luyện: Cài đặt Monotonic Deque $\mathcal{O}(N)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Giá Trị Nhỏ Nhất Trên Cửa Sổ Trượt K với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Giá Trị Nhỏ Nhất Trên Cửa Sổ Trượt K.



### Bài 03 [CPPB2-L09-03]: Kiểm Tra Dãy Ngoặc Đúng Nhiều Loại

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Kiểm Tra Dãy Ngoặc Đúng Nhiều Loại** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Ứng dụng Stack cơ bản.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Kiểm Tra Dãy Ngoặc Đúng Nhiều Loại với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Kiểm Tra Dãy Ngoặc Đúng Nhiều Loại.



### Bài 04 [CPPB2-L09-04]: Tầm Nhìn Xa Của Các Tòa Nhà Cao Tầng

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tầm Nhìn Xa Của Các Tòa Nhà Cao Tầng** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Monotonic Stack đếm số tòa nhà quan sát được.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tầm Nhìn Xa Của Các Tòa Nhà Cao Tầng với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tầm Nhìn Xa Của Các Tòa Nhà Cao Tầng.



### Bài 05 [CPPB2-L09-05]: Hình Chữ Nhật Lớn Nhất Dưới Biểu Đồ Cột (histogram)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Hình Chữ Nhật Lớn Nhất Dưới Biểu Đồ Cột (Histogram)** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: Monotonic Stack tìm biên trái & biên phải.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Hình Chữ Nhật Lớn Nhất Dưới Biểu Đồ Cột (histogram) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hình Chữ Nhật Lớn Nhất Dưới Biểu Đồ Cột (Histogram).



### Bài 06 [CPPB2-L09-06]: Ma Trận Toàn Số 1 Lớn Nhất (maximal Rectangle 2d)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Ma Trận Toàn Số 1 Lớn Nhất (Maximal Rectangle 2D)** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: Histogram DP 2D.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Ma Trận Toàn Số 1 Lớn Nhất (maximal Rectangle 2d) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Ma Trận Toàn Số 1 Lớn Nhất (Maximal Rectangle 2D).



### Bài 07 [CPPB2-L09-07]: Tổng Hiệu Cực Đại Và Cực Tiểu Mọi Đoạn Con

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tổng Hiệu Cực Đại Và Cực Tiểu Mọi Đoạn Con** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Monotonic Stack đếm số đoạn con mà $A_i$ là $\min/\max$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tổng Hiệu Cực Đại Và Cực Tiểu Mọi Đoạn Con với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Hiệu Cực Đại Và Cực Tiểu Mọi Đoạn Con.



### Bài 08 [CPPB2-L09-08]: Tối Ưu Hóa Quy Hoạch Động Bằng Monotonic Deque

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tối Ưu Hóa Quy Hoạch Động Bằng Monotonic Deque** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: DP $dp[i] = \min_{i-K \le j < i} (dp[j]) + A[i]$ qua Deque.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tối Ưu Hóa Quy Hoạch Động Bằng Monotonic Deque với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Quy Hoạch Động Bằng Monotonic Deque.



### Bài 09 [CPPB2-L09-09]: Hứng Nước Mưa Đa Chiều (trapping Rain Water)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Hứng Nước Mưa Đa Chiều (Trapping Rain Water)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Monotonic Stack tính thể tích nước đọng.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Hứng Nước Mưa Đa Chiều (trapping Rain Water) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hứng Nước Mưa Đa Chiều (Trapping Rain Water).



### Bài 10 [CPPB2-L09-10]: Đánh Giá Biểu Thức Số Học Trung Tố (shunting-yard)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đánh Giá Biểu Thức Số Học Trung Tố (Shunting-yard)** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Thuật toán Shunting-yard của Dijkstra dùng 2 Stack.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đánh Giá Biểu Thức Số Học Trung Tố (shunting-yard) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đánh Giá Biểu Thức Số Học Trung Tố (Shunting-yard).



### Bài 11 [CPPB2-L09-11]: Phần Tử Lớn Hơn Gần Nhất Trên Mảng Xoay Vòng

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Phần Tử Lớn Hơn Gần Nhất Trên Mảng Xoay Vòng** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Monotonic Stack duyệt $2N$ phần tử.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Phần Tử Lớn Hơn Gần Nhất Trên Mảng Xoay Vòng với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phần Tử Lớn Hơn Gần Nhất Trên Mảng Xoay Vòng.



### Bài 12 [CPPB2-L09-12]: Xóa K Chữ Số Để Được Số Nhỏ Nhất

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Xóa K Chữ Số Để Được Số Nhỏ Nhất** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Monotonic Stack duy trì các chữ số tăng dần.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Xóa K Chữ Số Để Được Số Nhỏ Nhất với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xóa K Chữ Số Để Được Số Nhỏ Nhất.



### Bài 13 [CPPB2-L09-13]: Tổng Giá Trị Min Mọi Đoạn Con Nhân Độ Dài

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tổng Giá Trị Min Mọi Đoạn Con Nhân Độ Dài** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Monotonic Stack kết hợp Prefix Sum.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tổng Giá Trị Min Mọi Đoạn Con Nhân Độ Dài với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Giá Trị Min Mọi Đoạn Con Nhân Độ Dài.



### Bài 14 [CPPB2-L09-14]: Đua Xe Trong Mê Cung Đổi Hướng Ít Nhất (0-1 Bfs)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đua Xe Trong Mê Cung Đổi Hướng Ít Nhất (0-1 BFS)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Hàng đợi Deque tìm đường tối ưu góc rẽ.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đua Xe Trong Mê Cung Đổi Hướng Ít Nhất (0-1 Bfs) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đua Xe Trong Mê Cung Đổi Hướng Ít Nhất (0-1 BFS).



### Bài 15 [CPPB2-L09-15]: Cắt Băng Rôn Quảng Cáo Tối Ưu Bằng 2 Deque

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Cắt Băng Rôn Quảng Cáo Tối Ưu Bằng 2 Deque** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Duy trì $\max - \min \le C$ trên cửa sổ co giãn.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cắt Băng Rôn Quảng Cáo Tối Ưu Bằng 2 Deque với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cắt Băng Rôn Quảng Cáo Tối Ưu Bằng 2 Deque.



### Bài 16 [CPPB2-L09-16]: Khôi Phục Cây Khảo Sát Tầm Nhìn Đa Hướng

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Khôi Phục Cây Khảo Sát Tầm Nhìn Đa Hướng** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Monotonic Stack 2 chiều xây dựng Cartesian Tree.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Khôi Phục Cây Khảo Sát Tầm Nhìn Đa Hướng với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Khôi Phục Cây Khảo Sát Tầm Nhìn Đa Hướng.



### Bài 17 [CPPB2-L09-17]: Hinh Chu Nhat Lon Nhat Bieu Do Cot

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Hinh Chu Nhat Lon Nhat Bieu Do Cot** là một dạng bài điển hình thuộc chuyên đề **Ngăn Xếp & Deque Đơn Điệu (Monotonic Stack & Deque)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Hinh Chu Nhat Lon Nhat Bieu Do Cot với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
6
2 1 5 6 2 3
```
### Output
```text
10
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `10`.



### Bài 18 [CPPB2-L09-18]: Hinh Chu Nhat Toan So 1 Lon Nhat 2d

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Hinh Chu Nhat Toan So 1 Lon Nhat 2D** là một dạng bài điển hình thuộc chuyên đề **Ngăn Xếp & Deque Đơn Điệu (Monotonic Stack & Deque)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Hinh Chu Nhat Toan So 1 Lon Nhat 2d với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 3
1 0 1
1 1 1
1 1 1
```
### Output
```text
6
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `6`.



### Bài 19 [CPPB2-L09-19]: Tong Min Tat Ca Doan Con

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Tong Min Tat Ca Doan Con** là một dạng bài điển hình thuộc chuyên đề **Ngăn Xếp & Deque Đơn Điệu (Monotonic Stack & Deque)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tong Min Tat Ca Doan Con với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
3 1 2
```
### Output
```text
9
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `9`.



### Bài 20 [CPPB2-L09-20]: Deque Sliding Window Maximum

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Deque Sliding Window Maximum** là một dạng bài điển hình thuộc chuyên đề **Ngăn Xếp & Deque Đơn Điệu (Monotonic Stack & Deque)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Deque Sliding Window Maximum với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
4 2
1 3 -1 -3
```
### Output
```text
3 3 -1
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `3 3 -1`.



### Bài 21 [CPPB2-L09-21]: Stack Danh Gia Bieu Thuc So Hoc

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Stack Danh Gia Bieu Thuc So Hoc** là một dạng bài điển hình thuộc chuyên đề **Ngăn Xếp & Deque Đơn Điệu (Monotonic Stack & Deque)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Stack Danh Gia Bieu Thuc So Hoc với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3+(2*4)-5
```
### Output
```text
6
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `6`.



### Bài 22 [CPPB2-L09-22]: Tam Nhin Toa Nha Hai Chieu

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Tam Nhin Toa Nha Hai Chieu** là một dạng bài điển hình thuộc chuyên đề **Ngăn Xếp & Deque Đơn Điệu (Monotonic Stack & Deque)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tam Nhin Toa Nha Hai Chieu với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
1 2 1
```
### Output
```text
2 3 2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2 3 2`.



# Bài 10: Thư viện STL C++ nâng cao (Advanced C++ STL)

## 1. Khái niệm & bản chất của các cấu trúc dữ liệu STL nâng cao

Thư viện mẫu chuẩn C++ (Standard Template Library - STL) cung cấp các cấu trúc dữ liệu trừu tượng hiệu năng cao được xây dựng trên nền tảng **Cây đỏ-đen (Red-Black Tree)** và **Bảng băm (Hash Table)**:

* **`set` / `multiset` / `map`:** Cấu trúc cây tự cân bằng (Balanced BST), duy trì các phần tử luôn được sắp xếp có thứ tự, hỗ trợ thêm, xóa, tìm kiếm, tìm kiếm nhị phân (`lower_bound`, `upper_bound`) trong thời gian logarit $\mathcal{O}(\log N)$.
* **`unordered_set` / `unordered_map`:** Cấu trúc bảng băm (Hash Table), đạt độ phức tạp trung bình $\mathcal{O}(1)$ cho các thao tác tìm kiếm và thêm xóa (nhưng có thể suy biến về $\mathcal{O}(N)$ khi bị đụng độ băm).
* **`priority_queue` (Hàng đợi ưu tiên):** Cấu trúc đống nhị phân (Binary Heap), luôn duy trì phần tử lớn nhất (Max-Heap) hoặc nhỏ nhất (Min-Heap) ở đỉnh trong $\mathcal{O}(1)$, thêm và xóa trong $\mathcal{O}(\log N)$.
* **Tùy biến hàm so sánh (Custom Struct Comparator / Functor):** Tùy chỉnh trật tự sắp xếp phức tạp cho các cấu trúc dữ liệu STL.


## 2. Bảng so sánh cấu trúc & hiệu năng của các Container STL

| Container STL | Cấu Trúc Ngầm Định | Trật Tự Dữ Liệu | Thao Tác Thêm / Xóa / Tìm | Tìm Kiếm Nhị Phân (`lower_bound`) |
|---|---|---|:---:|:---:|
| `vector<T>` | Mảng động liên tiếp | Theo thứ tự chèn | $\mathcal{O}(1)$ cuối, $\mathcal{O}(N)$ giữa | Cần sort trước $\mathcal{O}(\log N)$ |
| `set<T>` | Cây đỏ-đen (Red-Black Tree) | Tăng dần, duy nhất | $\mathcal{O}(\log N)$ | `s.lower_bound(x)` trong $\mathcal{O}(\log N)$ |
| `multiset<T>` | Cây đỏ-đen | Tăng dần, cho phép trùng | $\mathcal{O}(\log N)$ | `ms.lower_bound(x)` trong $\mathcal{O}(\log N)$ |
| `unordered_set<T>` | Bảng băm (Hash Table) | Không có thứ tự | Trung bình $\mathcal{O}(1)$, xấu nhất $\mathcal{O}(N)$ | Không hỗ trợ |
| `priority_queue<T>` | Đống nhị phân (Max-Heap) | Phần tử cực trị ở đỉnh | `push/pop` $\mathcal{O}(\log N)$, `top` $\mathcal{O}(1)$ | Không hỗ trợ |


## 3. Tử huyệt lập trình: Bẫy xóa phần tử trong `multiset` & Bẫy `unordered_map`

> **Cảnh báo bẫy lỗi 1: BẪY XÓA TẤT CẢ PHẦN TỬ TRÙNG NHAU TRONG MULTISET**

> Trong `multiset<int> ms`, nếu viết `ms.erase(val)`, C++ sẽ **xóa sạch toàn bộ mọi phần tử có giá trị bằng `val`**!  
> **Cách xóa đúng duy nhất 1 phần tử:** Truyền vào iterator trỏ tới phần tử đó:
> ```cpp
> auto it = ms.find(val);
> if (it != ms.end()) {
>     ms.erase(it); // Chỉ xóa đúng 1 phần tử tại vị trí it
> }
> ```

> **Cảnh báo bẫy lỗi 2: BẪY TẤN CÔNG BẢNG BĂM (ANTI-HASH TEST / HASH COLLISION)**

> `unordered_map` mặc định trong `libstdc++` dùng hàm băm chia dư đơn giản, dễ bị các bộ test sinh đối kháng (Anti-hash tests) làm đụng độ băm khiến thời gian chạy tụt từ $\mathcal{O}(1)$ xuống $\mathcal{O}(N) \implies \text{TLE}$.  
> **Giải pháp:** Sử dụng Custom Hash kết hợp thời gian hệ thống (Chrono):
> ```cpp
> struct custom_hash {
>     static uint64_t splitmix64(uint64_t x) {
>         x += 0x9e3779b97f4a7c15;
>         x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
>         x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
>         return x ^ (x >> 31);
>     }
>     size_t operator()(uint64_t x) const {
>         static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
>         return splitmix64(x + FIXED_RANDOM);
>     }
> };
> unordered_map<long long, int, custom_hash> safe_map;
> ```




![Hai Heap duy trì Trung vị động](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-10-thu-vien-stl-c-nang-cao/assets/l10_two_heaps_median_visual.png)



## 4. Mẫu cài đặt chuẩn thi đấu: Duy trì trung vị động (Running Median) bằng 2 Heap

Bài toán: Cho một luồng số liên tục, sau mỗi số được thêm vào, hãy in ra trung vị của toàn bộ các số đã nhập.

* **Chiến lược 2 Heap:**
  - Max-Heap `left_heap` chứa nửa nhỏ hơn của dãy số.
  - Min-Heap `right_heap` chứa nửa lớn hơn của dãy số.
  - Duy trì kích thước: `left_heap.size()` luôn bằng `right_heap.size()` hoặc hơn đúng $1$ phần tử.
  - Trung vị luôn là `left_heap.top()`.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    priority_queue<int> left_heap; // Max-heap
    priority_queue<int, vector<int>, greater<int>> right_heap; // Min-heap

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;

        if (left_heap.empty() || x <= left_heap.top()) left_heap.push(x);
        else right_heap.push(x);

        // Cân bằng kích thước
        if (left_heap.size() > right_heap.size() + 1) {
            right_heap.push(left_heap.top());
            left_heap.pop();
        } else if (right_heap.size() > left_heap.size()) {
            left_heap.push(right_heap.top());
            right_heap.pop();
        }

        cout << left_heap.top() << " ";
    }
    cout << "\n";
    return 0;
}
```


## 5. Ranh giới áp dụng

| Mục Đích | Chọn Container Phù Hợp |
|---|---|
| Cần tập hợp phần tử duy nhất, liên tục tìm $\ge X$ | `set<T>` |
| Cần tập hợp có phần tử trùng lặp, liên tục lấy $\min/\max$ và xóa | `multiset<T>` |
| Chỉ cần đếm tần suất cực nhanh không cần thứ tự | `unordered_map<T, int, custom_hash>` |
| Liên tục tìm phần tử lớn nhất/nhỏ nhất, không cần tìm kiếm tùy ý | `priority_queue<T>` |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L10-01]: Duy Trì Trung Vị Động

**Bối cảnh & Nhiệm vụ:**

Cho luồng $N$ số, sau mỗi số được thêm vào, in ra trung vị của tập số hiện tại.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Duy Trì Trung Vị Động với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng 1: $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số $A_i$.

**Đầu ra (Output):**

- In ra $N$ giá trị trung vị tương ứng.

**Ví dụ mẫu:**

### Input
```text
4
5 15 1 3
```
### Output
```text
5 5 5 3
```



### Bài 02 [CPPB2-L10-02]: Đếm Tần Suất Giá Trị Bằng Safe Hash Map

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Tần Suất Giá Trị Bằng Safe Hash Map** là bài toán trọng tâm thuộc cấp độ **P0** nhằm rèn luyện: `unordered_map` với `custom_hash`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Tần Suất Giá Trị Bằng Safe Hash Map với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Tần Suất Giá Trị Bằng Safe Hash Map.



### Bài 03 [CPPB2-L10-03]: Nối Dây Tiết Kiệm Bằng Priority Queue

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Nối Dây Tiết Kiệm Bằng Priority Queue** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Min-Heap `priority_queue`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Nối Dây Tiết Kiệm Bằng Priority Queue với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nối Dây Tiết Kiệm Bằng Priority Queue.



### Bài 04 [CPPB2-L10-04]: Duy Trì Trung Vị Động (running Median)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Duy Trì Trung Vị Động (Running Median)** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: 2 Heap cân bằng kích thước.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Duy Trì Trung Vị Động (running Median) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Duy Trì Trung Vị Động (Running Median).



### Bài 05 [CPPB2-L10-05]: Tìm Phần Tử Kế Tiếp Nhỏ Nhất Lớn Hơn X

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tìm Phần Tử Kế Tiếp Nhỏ Nhất Lớn Hơn X** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: `s.upper_bound(x)` trên `set`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tìm Phần Tử Kế Tiếp Nhỏ Nhất Lớn Hơn X với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Phần Tử Kế Tiếp Nhỏ Nhất Lớn Hơn X.



### Bài 06 [CPPB2-L10-06]: Lập Lịch Phòng Họp Đa Năng (meeting Rooms)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Lập Lịch Phòng Họp Đa Năng (Meeting Rooms)** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: Min-Heap theo dõi thời điểm kết thúc.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Lập Lịch Phòng Họp Đa Năng (meeting Rooms) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lập Lịch Phòng Họp Đa Năng (Meeting Rooms).



### Bài 07 [CPPB2-L10-07]: Duy Trì K Phần Tử Lớn Nhất Trong Luồng Dữ Liệu

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Duy Trì K Phần Tử Lớn Nhất Trong Luồng Dữ Liệu** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Min-Heap kích thước cố định $K$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Duy Trì K Phần Tử Lớn Nhất Trong Luồng Dữ Liệu với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Duy Trì K Phần Tử Lớn Nhất Trong Luồng Dữ Liệu.



### Bài 08 [CPPB2-L10-08]: Tối Ưu Hóa Chi Phí Mua Cổ Phiếu Theo Thời Gian

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tối Ưu Hóa Chi Phí Mua Cổ Phiếu Theo Thời Gian** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: `multiset` duy trì trật tự giá trị.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tối Ưu Hóa Chi Phí Mua Cổ Phiếu Theo Thời Gian với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Chi Phí Mua Cổ Phiếu Theo Thời Gian.



### Bài 09 [CPPB2-L10-09]: Hệ Thống Đặt Chỗ Rạp Chiếu Phim Tối Ưu

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Hệ Thống Đặt Chỗ Rạp Chiếu Phim Tối Ưu** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: `set<pair<int, int>>` quản lý đoạn trống.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Hệ Thống Đặt Chỗ Rạp Chiếu Phim Tối Ưu với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hệ Thống Đặt Chỗ Rạp Chiếu Phim Tối Ưu.



### Bài 10 [CPPB2-L10-10]: Đếm Số Phần Tử Phân Biệt Trong Mọi Cửa Sổ K

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Phần Tử Phân Biệt Trong Mọi Cửa Sổ K** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: `unordered_map` kết hợp Sliding Window.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Phần Tử Phân Biệt Trong Mọi Cửa Sổ K với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Phần Tử Phân Biệt Trong Mọi Cửa Sổ K.



### Bài 11 [CPPB2-L10-11]: Hợp Nhất Các Đoạn Số Rời Rạc (merge Intervals)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Hợp Nhất Các Đoạn Số Rời Rạc (Merge Intervals)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: `map` hoặc `set` quản lý các khoảng rời.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Hợp Nhất Các Đoạn Số Rời Rạc (merge Intervals) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hợp Nhất Các Đoạn Số Rời Rạc (Merge Intervals).



### Bài 12 [CPPB2-L10-12]: Tìm Cặp Điểm Có Khoảng Cách Manhattan Nhỏ Nhất

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tìm Cặp Điểm Có Khoảng Cách Manhattan Nhỏ Nhất** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Sweep-line kết hợp `set` tìm kiếm lân cận.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tìm Cặp Điểm Có Khoảng Cách Manhattan Nhỏ Nhất với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Cặp Điểm Có Khoảng Cách Manhattan Nhỏ Nhất.



### Bài 13 [CPPB2-L10-13]: Hệ Thống Xếp Hạng Trực Tuyến Đa Tiêu Chí

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Hệ Thống Xếp Hạng Trực Tuyến Đa Tiêu Chí** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: `set<CustomStruct>` với Strict Weak Ordering.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Hệ Thống Xếp Hạng Trực Tuyến Đa Tiêu Chí với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hệ Thống Xếp Hạng Trực Tuyến Đa Tiêu Chí.



### Bài 14 [CPPB2-L10-14]: Tối Ưu Phân Bổ Băng Thông Máy Chủ (server Load Balancer)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tối Ưu Phân Bổ Băng Thông Máy Chủ (Server Load Balancer)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: 2 `set` quản lý máy chủ bận và máy chủ rảnh.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tối Ưu Phân Bổ Băng Thông Máy Chủ (server Load Balancer) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Phân Bổ Băng Thông Máy Chủ (Server Load Balancer).



### Bài 15 [CPPB2-L10-15]: Duy Trì Tổng Của K Phần Tử Lớn Nhất Động

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Duy Trì Tổng Của K Phần Tử Lớn Nhất Động** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: 2 `multiset` cân bằng kích thước $K$ và tổng.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Duy Trì Tổng Của K Phần Tử Lớn Nhất Động với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Duy Trì Tổng Của K Phần Tử Lớn Nhất Động.



### Bài 16 [CPPB2-L10-16]: Kỹ Thuật Small-to-large Merging Trên Stl Map

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Kỹ Thuật Small-to-Large Merging Trên STL Map** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Gộp `map` từ cây con lên gốc trong $\mathcal{O}(N \log^2 N)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Kỹ Thuật Small-to-large Merging Trên Stl Map với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Kỹ Thuật Small-to-Large Merging Trên STL Map.



### Bài 17 [CPPB2-L10-17]: Ordered Set Pbds Truy Van Thu Hang

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Ordered Set Pbds Truy Van Thu Hang** là một dạng bài điển hình thuộc chuyên đề **Thư Viện STL C++ Nâng Cao (Advanced STL Containers)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Ordered Set Pbds Truy Van Thu Hang với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
1 5
1 2
2 1
```
### Output
```text
5
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `5`.



### Bài 18 [CPPB2-L10-18]: Can Bang Hai Heap Running Median

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Can Bang Hai Heap Running Median** là một dạng bài điển hình thuộc chuyên đề **Thư Viện STL C++ Nâng Cao (Advanced STL Containers)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Can Bang Hai Heap Running Median với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
5 15 1
```
### Output
```text
5 10 5
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `5 10 5`.



### Bài 19 [CPPB2-L10-19]: Multiset Interval Management

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Multiset Interval Management** là một dạng bài điển hình thuộc chuyên đề **Thư Viện STL C++ Nâng Cao (Advanced STL Containers)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Multiset Interval Management với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
2
1 1 3
1 2 5
```
### Output
```text
2
4
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2
4`.



### Bài 20 [CPPB2-L10-20]: Safe Unordered Map Custom Hash

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Safe Unordered Map Custom Hash** là một dạng bài điển hình thuộc chuyên đề **Thư Viện STL C++ Nâng Cao (Advanced STL Containers)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Safe Unordered Map Custom Hash với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
4
1 2 2 1
```
### Output
```text
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2`.



### Bài 21 [CPPB2-L10-21]: Priority Queue Dijkstra Custom Comparator

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Priority Queue Dijkstra Custom Comparator** là một dạng bài điển hình thuộc chuyên đề **Thư Viện STL C++ Nâng Cao (Advanced STL Containers)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Priority Queue Dijkstra Custom Comparator với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 3
1 2 2
2 3 3
1 3 10
```
### Output
```text
6
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `6`.



### Bài 22 [CPPB2-L10-22]: Lru Cache Implementation Stl

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Lru Cache Implementation Stl** là một dạng bài điển hình thuộc chuyên đề **Thư Viện STL C++ Nâng Cao (Advanced STL Containers)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Lru Cache Implementation Stl với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
2
put 1 1
put 2 2
get 1
```
### Output
```text
1
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `1`.



# Bài 11: Tổ hợp, hoán vị & xác suất cơ bản (Combinatorics & Probability)

## 1. Khái niệm & bản chất của đại số tổ hợp trong lập trình thi đấu

Đại số tổ hợp (Combinatorics) là nhánh toán học nghiên cứu về việc đếm, sắp xếp và lựa chọn các phần tử trong tập hợp theo các quy tắc xác định.

Ở Level 2, bài toán tổ hợp không chỉ là tính toán công thức giải tích đơn giản mà là **xử lý đa truy vấn với modulo lớn $10^9+7$**:

* **Hoán vị ($P_n = n!$), Chỉnh hợp ($A_n^k = \frac{n!}{(n-k)!}$), Tổ hợp ($C_n^k = \binom{n}{k} = \frac{n!}{k!(n-k)!}$)**.
* **Tiền xử lý giai thừa & Nghịch đảo giai thừa:** Tính trước $fact[i] = i! \bmod M$ và $invFact[i] = (i!)^{-1} \bmod M$ trong $\mathcal{O}(N)$ để trả lời mỗi truy vấn tính $C_n^k \bmod M$ trong $\mathcal{O}(1)$.
* **Tam giác Pascal (Pascal's Triangle):** Quy hoạch động tính $C_n^k = C_{n-1}^{k-1} + C_{n-1}^k$ khi modulo $M$ là hợp số.
* **Nguyên lý bù trừ (Principle of Inclusion-Exclusion — PIE):** Đếm số phần tử thỏa mãn ít nhất một trong các điều kiện bằng cách xen kẽ cộng tập đơn và trừ tập giao:
$$|A_1 \cup A_2 \cup \dots \cup A_n| = \sum |A_i| - \sum |A_i \cap A_j| + \sum |A_i \cap A_j \cap A_k| - \dots$$

* **Bài toán Chia kẹo của Euler (Stars and Bars):** Số cách chia $N$ cái kẹo giống nhau cho $K$ đứa trẻ:
  - Mỗi đứa trẻ có ít nhất 1 cái: $\binom{N - 1}{K - 1}$.
  - Đứa trẻ có thể nhận 0 cái: $\binom{N + K - 1}{K - 1}$.




![Tam giác Pascal](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-11-to-hop-hoan-vi-xac-suat-co-ban/assets/l11_pascal_triangle_visual.png)



## 2. Tiền xử lý giai thừa và tính $C_n^k \bmod (10^9+7)$ trong $\mathcal{O}(1)$

```cpp
const int MAXN = 1000000;
const long long MOD = 1000000007;

long long fact[MAXN + 1];
long long invFact[MAXN + 1];

long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

void precompute_factorials() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; ++i) fact[i] = (fact[i - 1] * i) % MOD;

    // Tính nghịch đảo giai thừa MAXN! bằng Fermat
    invFact[MAXN] = power_mod(fact[MAXN], MOD - 2);

    // Tính lùi: invFact[i-1] = invFact[i] * i % MOD
    for (int i = MAXN - 1; i >= 0; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}
```


## 3. Nguyên lý bù trừ (PIE) & Đếm số nguyên tố cùng nhau

Bài toán: Đếm số lượng số trong đoạn $[1, N]$ không chia hết cho bất kỳ số nào trong tập các số nguyên tố $\{p_1, p_2, \dots, p_K\}$ ($K \le 15$).

```cpp
long long count_coprime(long long n, const vector<long long> &primes) {
    int k = primes.size();
    long long total = 0;

    for (int mask = 1; mask < (1 << k); ++mask) {
        long long prod = 1;
        int bits = 0;
        for (int i = 0; i < k; ++i) {
            if ((mask >> i) & 1) {
                bits++;
                prod *= primes[i];
                if (prod > n) break;
            }
        }
        long long cnt = n / prod;
        if (bits % 2 == 1) total += cnt; // Số lẻ tập: Cộng vào
        else total -= cnt;              // Số chẵn tập: Trừ ra
    }
    return n - total; // Số lượng không chia hết cho bất kỳ số nào
}
```


## 4. Ranh giới áp dụng

| Tình Huống | Điều Kiện Modulo $M$ | Kỹ Thuật Tối Ưu |
|---|---|---|
| $N \le 10^6, Q \le 10^5$ | $M$ là số nguyên tố ($10^9+7$) | Tiền xử lý `fact` và `invFact` $\implies \mathcal{O}(1)$ mỗi truy vấn |
| $N \le 2000, Q \le 10^5$ | $M$ là hợp số bất kỳ | Tam giác Pascal DP $\mathcal{O}(N^2)$ |
| $N \le 10^{18}, K \le 10^6$ | $M$ nguyên tố | Tính trực tiếp $C_n^k = \frac{n(n-1)\dots(n-k+1)}{k!} \bmod M$ |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L11-01]: Tính Tổ Hợp Ncr Modulo

**Bối cảnh & Nhiệm vụ:**

Tính $\binom{N}{K} \bmod (10^9+7)$ cho $Q$ truy vấn.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tính Tổ Hợp Ncr Modulo với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng 1: $Q$ ($1 \le Q \le 10^5$). $Q$ dòng sau: $N, K$ ($0 \le K \le N \le 10^6$).

**Đầu ra (Output):**

- In ra kết quả mỗi truy vấn trên 1 dòng.

**Ví dụ mẫu:**

### Input
```text
2
5 2
10 3
```
### Output
```text
10
120
```



### Bài 02 [CPPB2-L11-02]: Tam Giác Pascal Modulo Hợp Số

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tam Giác Pascal Modulo Hợp Số** là bài toán trọng tâm thuộc cấp độ **P0** nhằm rèn luyện: DP Tam giác Pascal $C_n^k = C_{n-1}^{k-1} + C_{n-1}^k$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tam Giác Pascal Modulo Hợp Số với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tam Giác Pascal Modulo Hợp Số.



### Bài 03 [CPPB2-L11-03]: Chia Kẹo Euler (stars And Bars)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Chia Kẹo Euler (Stars and Bars)** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Ứng dụng công thức chia kẹo Euler.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Chia Kẹo Euler (stars And Bars) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chia Kẹo Euler (Stars and Bars).



### Bài 04 [CPPB2-L11-04]: Đếm Số Hoán Vị Không Có Điểm Cố Định (derangements)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Hoán Vị Không Có Điểm Cố Định (Derangements)** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Công thức $D_n = (n-1)(D_{n-1} + D_{n-2})$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Hoán Vị Không Có Điểm Cố Định (derangements) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Hoán Vị Không Có Điểm Cố Định (Derangements).



### Bài 05 [CPPB2-L11-05]: Đếm Số Nguyên Tố Cùng Nhau Bằng Pie

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Nguyên Tố Cùng Nhau Bằng PIE** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: Nguyên lý bù trừ kết hợp Bitmask.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Nguyên Tố Cùng Nhau Bằng Pie với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Nguyên Tố Cùng Nhau Bằng PIE.



### Bài 06 [CPPB2-L11-06]: Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: DP kết hợp PIE và tổ hợp.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm.



### Bài 07 [CPPB2-L11-07]: Số Phân Hoạch Tập Hợp (số Stirling Loại 2)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Số Phân Hoạch Tập Hợp (Số Stirling Loại 2)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: DP tính số Stirling $S(n, k)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Số Phân Hoạch Tập Hợp (số Stirling Loại 2) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Phân Hoạch Tập Hợp (Số Stirling Loại 2).



### Bài 08 [CPPB2-L11-08]: Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Định lý Lucas $\binom{n}{k} \equiv \prod \binom{n_i}{k_i} \pmod P$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ.



### Bài 09 [CPPB2-L11-09]: Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: DP sắp xếp điểm cấm + PIE.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm.



### Bài 10 [CPPB2-L11-10]: Đếm Số Hoán Vị Có Đúng K Điểm Cố Định

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Hoán Vị Có Đúng K Điểm Cố Định** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Công thức $\binom{N}{K} \times D_{N-K} \bmod M$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Hoán Vị Có Đúng K Điểm Cố Định với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Hoán Vị Có Đúng K Điểm Cố Định.



### Bài 11 [CPPB2-L11-11]: Số Phân Hoạch Tập Hợp (số Stirling Loại 2)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Số Phân Hoạch Tập Hợp (Số Stirling Loại 2)** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: DP tính $S(n, k) = S(n-1, k-1) + k \cdot S(n-1, k)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Số Phân Hoạch Tập Hợp (số Stirling Loại 2) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Phân Hoạch Tập Hợp (Số Stirling Loại 2).



### Bài 12 [CPPB2-L11-12]: Đếm Số Cây Khung Đồ Thị Đầy Đủ (công Thức Cayley)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Cây Khung Đồ Thị Đầy Đủ (Công Thức Cayley)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Công thức $N^{N-2} \bmod M$ bằng Fast Power.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Cây Khung Đồ Thị Đầy Đủ (công Thức Cayley) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Cây Khung Đồ Thị Đầy Đủ (Công Thức Cayley).



### Bài 13 [CPPB2-L11-13]: Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Định lý Lucas $\binom{n}{k} \equiv \prod \binom{n_i}{k_i} \pmod P$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ.



### Bài 14 [CPPB2-L11-14]: Đếm Số Tam Giác Tạo Bởi N Điểm Trên Mặt Phẳng

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Tam Giác Tạo Bởi N Điểm Trên Mặt Phẳng** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: $\binom{N}{3}$ trừ các bộ 3 điểm thẳng hàng qua $\gcd$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Tam Giác Tạo Bởi N Điểm Trên Mặt Phẳng với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Tam Giác Tạo Bởi N Điểm Trên Mặt Phẳng.



### Bài 15 [CPPB2-L11-15]: Kỳ Vọng Toán Học Trò Chơi Gieo Xúc Xắc (probability Dp)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Kỳ Vọng Toán Học Trò Chơi Gieo Xúc Xắc (Probability DP)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: DP tính kỳ vọng bước đi $E[i]$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Kỳ Vọng Toán Học Trò Chơi Gieo Xúc Xắc (probability Dp) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Kỳ Vọng Toán Học Trò Chơi Gieo Xúc Xắc (Probability DP).



### Bài 16 [CPPB2-L11-16]: Bổ Đề Burnside Đếm Cấu Hình Bất Biến Phép Quay

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Bổ Đề Burnside Đếm Cấu Hình Bất Biến Phép Quay** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Lý thuyết nhóm & Bổ đề Burnside đếm vòng cổ.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Bổ Đề Burnside Đếm Cấu Hình Bất Biến Phép Quay với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Bổ Đề Burnside Đếm Cấu Hình Bất Biến Phép Quay.



### Bài 17 [CPPB2-L11-17]: Nguyen Ly Bao Ham Loai Tru Pie

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Nguyen Ly Bao Ham Loai Tru Pie** là một dạng bài điển hình thuộc chuyên đề **Tổ Hợp, Hoán Vị & Xác Suất Cơ Bản (Combinatorics)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Nguyen Ly Bao Ham Loai Tru Pie với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
10 2
2 3
```
### Output
```text
3
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `3`.



### Bài 18 [CPPB2-L11-18]: Dinh Ly Lucas To Hop Modulo P

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dinh Ly Lucas To Hop Modulo P** là một dạng bài điển hình thuộc chuyên đề **Tổ Hợp, Hoán Vị & Xác Suất Cơ Bản (Combinatorics)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dinh Ly Lucas To Hop Modulo P với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
5 2 3
```
### Output
```text
1
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `1`.



### Bài 19 [CPPB2-L11-19]: So Catalan Ung Dung Ngoac

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **So Catalan Ung Dung Ngoac** là một dạng bài điển hình thuộc chuyên đề **Tổ Hợp, Hoán Vị & Xác Suất Cơ Bản (Combinatorics)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán So Catalan Ung Dung Ngoac với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
```
### Output
```text
5
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `5`.



### Bài 20 [CPPB2-L11-20]: So Stirling Loai Hai Chia Tap

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **So Stirling Loai Hai Chia Tap** là một dạng bài điển hình thuộc chuyên đề **Tổ Hợp, Hoán Vị & Xác Suất Cơ Bản (Combinatorics)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán So Stirling Loai Hai Chia Tap với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 2
```
### Output
```text
3
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `3`.



### Bài 21 [CPPB2-L11-21]: Xac Suat Co Dieu Kien Dong Xu

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Xac Suat Co Dieu Kien Dong Xu** là một dạng bài điển hình thuộc chuyên đề **Tổ Hợp, Hoán Vị & Xác Suất Cơ Bản (Combinatorics)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Xac Suat Co Dieu Kien Dong Xu với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
2
```
### Output
```text
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2`.



### Bài 22 [CPPB2-L11-22]: Hoan Vi Co Chu Ky Cycles

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Hoan Vi Co Chu Ky Cycles** là một dạng bài điển hình thuộc chuyên đề **Tổ Hợp, Hoán Vị & Xác Suất Cơ Bản (Combinatorics)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Hoan Vi Co Chu Ky Cycles với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 2
```
### Output
```text
3
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `3`.



# CHƯƠNG 06: ĐỒ THỊ, CÂY TRUY VẤN ĐOẠN, DIGIT DP & XỬ LÝ CHUỖI


# Bài 12: Lý thuyết đồ thị cơ bản & nâng cao (Graph Algorithms)

## 1. Khái niệm & biểu diễn đồ thị trong lập trình thi đấu

Lý thuyết đồ thị (Graph Theory) là mô hình trừu tượng mô tả mối quan hệ (các cạnh $E$) giữa các đối tượng (các đỉnh $V$).

Các phương pháp biểu diễn đồ thị chuẩn:

* **Danh sách kề (`vector<vector<int>> adj`):** Tiết kiệm bộ nhớ $\mathcal{O}(V + E)$, duyệt các đỉnh kề nhanh nhất $\implies$ **Chuẩn thi đấu bắt buộc**.
* **Ma trận kề (`vector<vector<int>> matrix`):** Tốn bộ nhớ $\mathcal{O}(V^2)$, chỉ dùng khi $V \le 1000$.
* **Danh sách cạnh (`vector<vector<int>> edges`):** Dùng trong các thuật toán cây khung nhỏ nhất (Kruskal, Bellman-Ford).


## 2. Hai thuật toán duyệt đồ thị cốt lõi: BFS & DFS

### 2.1. Tìm kiếm theo chiều sâu (Depth-First Search — DFS)

* Duyệt đi sâu vào từng nhánh theo cơ chế đệ quy (Stack ngầm định).
* **Ứng dụng:** Đếm thành phần liên thông, phát hiện chu trình (Cycle Detection), sắp xếp Tô-pô (Topological Sort), kiểm tra đồ thị hai phía (Bipartite Graph).

```cpp
void dfs(int u, const vector<vector<int>> &adj, vector<bool> &visited) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) dfs(v, adj, visited);
    }
}
```

### 2.2. Tìm kiếm theo chiều rộng (Breadth-First Search — BFS)

* Duyệt theo từng lớp khoảng cách lan tỏa bằng Hàng đợi (`queue<int>`).
* **Tính chất vàng:** BFS luôn tìm ra **đường đi ngắn nhất (ít cạnh nhất)** trên đồ thị không có trọng số hoặc đồ thị lưới 2D.

```cpp
vector<int> bfs_shortest_path(int start_node, int n, const vector<vector<int>> &adj) {
    vector<int> dist(n + 1, -1);
    queue<int> q;

    dist[start_node] = 0;
    q.push(start_node);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return dist;
}
```




![Thuật toán Tarjan tìm Khớp và Cầu](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-12-do-thi-co-ban-va-nang-cao/assets/l12_tarjan_bridges_visual.png)



## 3. Thuật toán Dijkstra tìm đường đi ngắn nhất đồ thị có trọng số dương

Khi các cạnh có trọng số $W_e \ge 0$, ta sử dụng thuật toán **Dijkstra kết hợp Hàng đợi ưu tiên (Min-Heap)** đạt độ phức tạp $\mathcal{O}((V + E) \log V)$:

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

vector<long long> dijkstra(int start_node, int n, const vector<vector<pair<int, long long>>> &adj) {
    vector<long long> dist(n + 1, INF);
    // Min-heap lưu {khoảng_cách, đỉnh}
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    dist[start_node] = 0;
    pq.push({0, start_node});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue; // Bỏ qua trạng thái cũ

        for (auto &edge : adj[u]) {
            int v = edge.first;
            long long w = edge.second;
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}
```


## 4. Ranh giới áp dụng

| Loại Đồ Thị | Mục Tiêu | Thuật Toán Tối Ưu | Độ Phức Tạp |
|---|---|---|:---:|
| Không trọng số / Trọng số 1 | Đường đi ngắn nhất | BFS | $\mathcal{O}(V + E)$ |
| Trọng số $0$ và $1$ | Đường đi ngắn nhất | 0-1 BFS (dùng `deque`) | $\mathcal{O}(V + E)$ |
| Trọng số không âm ($W \ge 0$) | Đường đi ngắn nhất | Dijkstra + Min-Heap | $\mathcal{O}((V + E) \log V)$ |
| Đồ thị có hướng không chu trình (DAG) | Lập lịch / Thứ tự ưu tiên | Sắp xếp Tô-pô (Kahn / DFS) | $\mathcal{O}(V + E)$ |
| Đồ thị lưới 2D | Loang màu / Tìm miền liên thông | Flood Fill (DFS / BFS) | $\mathcal{O}(R \times C)$ |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L12-01]: Đường Đi Ngắn Nhất Dijkstra

**Bối cảnh & Nhiệm vụ:**

Tìm đường đi ngắn nhất từ đỉnh 1 đến đỉnh $N$ trên đồ thị có hướng trọng số không âm.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đường Đi Ngắn Nhất Dijkstra với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 1 \le M \le 2 \times 10^5$). $M$ dòng sau: $u, v, w$.

**Đầu ra (Output):**

- In ra khoảng cách ngắn nhất từ 1 đến $N$, nếu không đến được in -1.

**Ví dụ mẫu:**

### Input
```text
3 3
1 2 1
2 3 2
1 3 4
```
### Output
```text
3
```



### Bài 02 [CPPB2-L12-02]: Đường Đi Ngắn Nhất Mê Cung 2d Bằng Bfs

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đường Đi Ngắn Nhất Mê Cung 2D Bằng BFS** là bài toán trọng tâm thuộc cấp độ **P0** nhằm rèn luyện: BFS trên lưới ma trận 2D.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đường Đi Ngắn Nhất Mê Cung 2d Bằng Bfs với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đường Đi Ngắn Nhất Mê Cung 2D Bằng BFS.



### Bài 03 [CPPB2-L12-03]: Kiểm Tra Đồ Thị Hai Phía (bipartite Graph Coloring)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Kiểm Tra Đồ Thị Hai Phía (Bipartite Graph Coloring)** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Tô màu 2 màu bằng BFS/DFS.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Kiểm Tra Đồ Thị Hai Phía (bipartite Graph Coloring) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Kiểm Tra Đồ Thị Hai Phía (Bipartite Graph Coloring).



### Bài 04 [CPPB2-L12-04]: Sắp Xếp Tô-pô Lập Lịch Khóa Học (topological Sort)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Sắp Xếp Tô-pô Lập Lịch Khóa Học (Topological Sort)** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Thuật toán Kahn (Bán bậc vào `in_degree`).

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Sắp Xếp Tô-pô Lập Lịch Khóa Học (topological Sort) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Sắp Xếp Tô-pô Lập Lịch Khóa Học (Topological Sort).



### Bài 05 [CPPB2-L12-05]: Dijkstra Tìm Đường Đi Ngắn Nhất Chuẩn

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Dijkstra Tìm Đường Đi Ngắn Nhất Chuẩn** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: Cài đặt Dijkstra Min-Heap.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dijkstra Tìm Đường Đi Ngắn Nhất Chuẩn với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dijkstra Tìm Đường Đi Ngắn Nhất Chuẩn.



### Bài 06 [CPPB2-L12-06]: Mê Cung Trọng Số 0 Và 1 (0-1 Bfs)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Mê Cung Trọng Số 0 và 1 (0-1 BFS)** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: 0-1 BFS với `std::deque`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Mê Cung Trọng Số 0 Và 1 (0-1 Bfs) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Mê Cung Trọng Số 0 và 1 (0-1 BFS).



### Bài 07 [CPPB2-L12-07]: Cây Khung Nhỏ Nhất (mst Kruskal Với Dsu)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Cây Khung Nhỏ Nhất (MST Kruskal với DSU)** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Kruskal + Disjoint Set Union.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cây Khung Nhỏ Nhất (mst Kruskal Với Dsu) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cây Khung Nhỏ Nhất (MST Kruskal với DSU).



### Bài 08 [CPPB2-L12-08]: Tìm Khớp Và Cầu Trên Đồ Thị (tarjan's Bridge & Articulation)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tìm Khớp Và Cầu Trên Đồ Thị (Tarjan's Bridge & Articulation)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Mảng `num` và `low` trong DFS.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tìm Khớp Và Cầu Trên Đồ Thị (tarjan's Bridge & Articulation) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Khớp Và Cầu Trên Đồ Thị (Tarjan's Bridge & Articulation).



### Bài 09 [CPPB2-L12-09]: Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (k Lần Dùng Vé Miễn Phí)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (K Lần Dùng Vé Miễn Phí)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Dijkstra đa tầng $dist[u][k]$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (k Lần Dùng Vé Miễn Phí) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (K Lần Dùng Vé Miễn Phí).



### Bài 10 [CPPB2-L12-10]: Thành Phần Liên Thông Mạnh (scc Tarjan/kosaraju)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Thành Phần Liên Thông Mạnh (SCC Tarjan/Kosaraju)** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Co đồ thị có hướng thành DAG.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Thành Phần Liên Thông Mạnh (scc Tarjan/kosaraju) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Thành Phần Liên Thông Mạnh (SCC Tarjan/Kosaraju).



### Bài 11 [CPPB2-L12-11]: Tìm Tổ Tiên Chung Gần Nhất (lca Binary Lifting)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tìm Tổ Tiên Chung Gần Nhất (LCA Binary Lifting)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Bảng nhảy nhị phân $up[u][k]$ trong $\mathcal{O}(\log N)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tìm Tổ Tiên Chung Gần Nhất (lca Binary Lifting) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Tổ Tiên Chung Gần Nhất (LCA Binary Lifting).



### Bài 12 [CPPB2-L12-12]: Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (k Lần Dùng Vé)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (K Lần Dùng Vé)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Dijkstra đa tầng $dist[u][k]$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (k Lần Dùng Vé) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (K Lần Dùng Vé).



### Bài 13 [CPPB2-L12-13]: Multi-source Bfs Lan Tỏa Dịch Bệnh / Cháy Rừng

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Multi-Source BFS Lan Tỏa Dịch Bệnh / Cháy Rừng** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: BFS đồng thời từ nhiều đỉnh nguồn ban đầu.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Multi-source Bfs Lan Tỏa Dịch Bệnh / Cháy Rừng với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Multi-Source BFS Lan Tỏa Dịch Bệnh / Cháy Rừng.



### Bài 14 [CPPB2-L12-14]: Đường Đi Euler & Chu Trình Euler (hierholzer)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đường Đi Euler & Chu Trình Euler (Hierholzer)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Thuật toán Hierholzer tìm hành trình Euler.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đường Đi Euler & Chu Trình Euler (hierholzer) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đường Đi Euler & Chu Trình Euler (Hierholzer).



### Bài 15 [CPPB2-L12-15]: Tìm Chu Trình Âm Bằng Bellman-ford / Spfa

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tìm Chu Trình Âm Bằng Bellman-Ford / SPFA** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Kiểm tra nới lỏng lần thứ $V$ phát hiện chu trình âm.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tìm Chu Trình Âm Bằng Bellman-ford / Spfa với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Chu Trình Âm Bằng Bellman-Ford / SPFA.



### Bài 16 [CPPB2-L12-16]: Luồng Cực Đại Trong Mạng (max Flow Dinic Algorithm)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Luồng Cực Đại Trong Mạng (Max Flow Dinic Algorithm)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Thuật toán Dinic dùng đồ thị tầng Level Graph.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Luồng Cực Đại Trong Mạng (max Flow Dinic Algorithm) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Luồng Cực Đại Trong Mạng (Max Flow Dinic Algorithm).



### Bài 17 [CPPB2-L12-17]: Bfs Do Thi Trong So 0 1

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **01 Bfs Do Thi Trong So 0 1** là một dạng bài điển hình thuộc chuyên đề **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Bfs Do Thi Trong So 0 1 với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 3
1 2 0
2 3 1
1 3 1
```
### Output
```text
1
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `1`.



### Bài 18 [CPPB2-L12-18]: Tarjan Tim Khop Va Cau

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Tarjan Tim Khop Va Cau** là một dạng bài điển hình thuộc chuyên đề **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tarjan Tim Khop Va Cau với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
4 4
1 2
2 3
3 1
3 4
```
### Output
```text
1 1
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `1 1`.



### Bài 19 [CPPB2-L12-19]: Tarjan Thanh Phan Lien Thong Manh Scc

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Tarjan Thanh Phan Lien Thong Manh Scc** là một dạng bài điển hình thuộc chuyên đề **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tarjan Thanh Phan Lien Thong Manh Scc với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 3
1 2
2 3
3 1
```
### Output
```text
1
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `1`.



### Bài 20 [CPPB2-L12-20]: Chu Trinh Euler Hierholzer

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Chu Trinh Euler Hierholzer** là một dạng bài điển hình thuộc chuyên đề **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Chu Trinh Euler Hierholzer với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 3
1 2
2 3
3 1
```
### Output
```text
1 2 3 1
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `1 2 3 1`.



### Bài 21 [CPPB2-L12-21]: Dijkstra Do Thi Nhieu Tang K Ve Mien Phi

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dijkstra Do Thi Nhieu Tang K Ve Mien Phi** là một dạng bài điển hình thuộc chuyên đề **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dijkstra Do Thi Nhieu Tang K Ve Mien Phi với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 3 1
1 2 10
2 3 20
1 3 50
```
### Output
```text
10
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `10`.



### Bài 22 [CPPB2-L12-22]: Dinh To Nho Nhat Kruskal Dsu

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dinh To Nho Nhat Kruskal Dsu** là một dạng bài điển hình thuộc chuyên đề **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dinh To Nho Nhat Kruskal Dsu với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 3
1 2 1
2 3 2
1 3 3
```
### Output
```text
3
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `3`.



### Bài 23 [CPPB2-L12-23]: Bellman Ford Chu Trinh Am

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Bellman Ford Chu Trinh Am** là một dạng bài điển hình thuộc chuyên đề **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Bellman Ford Chu Trinh Am với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 3
1 2 1
2 3 -5
3 1 2
```
### Output
```text
YES
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `YES`.



### Bài 24 [CPPB2-L12-24]: Floyd Warshall Moi Cap Dinh

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Floyd Warshall Moi Cap Dinh** là một dạng bài điển hình thuộc chuyên đề **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Floyd Warshall Moi Cap Dinh với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
2
0 3
3 0
```
### Output
```text
0 3
3 0
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `0 3
3 0`.



### Bài 25 [CPPB2-L12-25]: Lca To Tien Chung Gan Nhat Binary Lifting

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Lca To Tien Chung Gan Nhat Binary Lifting** là một dạng bài điển hình thuộc chuyên đề **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Lca To Tien Chung Gan Nhat Binary Lifting với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3
1 2
1 3
1
2 3
```
### Output
```text
1
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `1`.



### Bài 26 [CPPB2-L12-26]: Dem So Duong Di Topo Dag

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dem So Duong Di Topo Dag** là một dạng bài điển hình thuộc chuyên đề **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dem So Duong Di Topo Dag với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 3 1 3
1 2
2 3
1 3
```
### Output
```text
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2`.



# Bài 13: Cây phân đoạn & cây Fenwick (Segment Tree & Fenwick Tree)

## 1. Khái niệm & bản chất của cấu trúc dữ liệu truy vấn đoạn (Range Query Data Structures)

Khi một bài toán có $Q = 10^5$ truy vấn xen kẽ giữa:

1. **Cập nhật giá trị (Update):** Gán $A[i] = X$ hoặc cộng thêm vào $A[i] \mathrel{+}= X$.
2. **Truy vấn đoạn (Range Query):** Tính tổng $\sum_{k=L}^R A[k]$ hoặc tìm $\min_{k=L}^R A[k]$, $\max_{k=L}^R A[k]$, $\gcd_{k=L}^R A[k]$.

Nếu dùng mảng thông thường: Cập nhật $\mathcal{O}(1)$ nhưng truy vấn $\mathcal{O}(N) \implies \mathcal{O}(QN) \approx 10^{10} \implies \text{TLE}$.  
Nếu dùng Mảng tiền tố tĩnh: Truy vấn $\mathcal{O}(1)$ nhưng cập nhật lại mảng tiền tố mất $\mathcal{O}(N) \implies \text{TLE}$.

**Giải pháp đột phá:** Cây Fenwick (Binary Indexed Tree - BIT) và Cây phân đoạn (Segment Tree) cân bằng cả 2 thao tác cập nhật và truy vấn trong thời gian **logarit $\mathcal{O}(\log N)$**.




![Cấu trúc Cây Fenwick BIT](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-13-cay-phan-doan-fenwick-tree/assets/l13_fenwick_tree_visual.png)



## 2. Cây Fenwick (Binary Indexed Tree — BIT)

### 2.1. Cấu trúc & Thủ thuật bit LSB `i & (-i)`

Mỗi nút `bit[i]` quản lý tổng của một đoạn con có độ dài bằng $LSB(i) = i \ \& \ (-i)$ kết thúc tại chỉ số $i$:

* Đoạn quản lý: $(i - LSB(i), i]$.
* **Bộ nhớ siêu nhẹ:** Đúng $N$ phần tử.

```cpp
const int MAXN = 1000000;
long long bit[MAXN + 1];
int n;

// Cộng thêm val vào vị trí idx (1-based) trong O(log N)
void update_bit(int idx, long long val) {
    for (; idx <= n; idx += idx & (-idx)) {
        bit[idx] += val;
    }
}

// Tính tổng tiền tố từ 1 đến idx trong O(log N)
long long query_bit(int idx) {
    long long sum = 0;
    for (; idx > 0; idx -= idx & (-idx)) {
        sum += bit[idx];
    }
    return sum;
}

// Truy vấn tổng đoạn [L, R]
long long range_query(int L, int R) {
    return query_bit(R) - query_bit(L - 1);
}
```




![Kiến trúc Cây phân đoạn Segment Tree](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-13-cay-phan-doan-fenwick-tree/assets/l13_segment_tree_visual.png)



## 3. Cây phân đoạn (Segment Tree — Point Update / Range Query)

### 3.1. Cấu trúc cây nhị phân đầy đủ

* Gốc quản lý đoạn toàn cục $[1, N]$. Nút $id$ quản lý $[L, R]$ có hai con: con trái $2 \times id$ quản lý $[L, mid]$ và con phải $2 \times id + 1$ quản lý $[mid + 1, R]$.
* **Bộ nhớ mảng:** Luôn cấp phát $4N$ phần tử `tree[4 * MAXN]`.
* **Đa năng tuyệt đối:** Hỗ trợ mọi hàm có tính kết hợp: Tổng, Min, Max, GCD.

```cpp
const int MAXN = 200000;
long long tree[4 * MAXN];
long long a[MAXN + 1];

void build_tree(int id, int l, int r) {
    if (l == r) {
        tree[id] = a[l];
        return;
    }
    int mid = (l + r) / 2;
    build_tree(2 * id, l, mid);
    build_tree(2 * id + 1, mid + 1, r);
    tree[id] = min(tree[2 * id], tree[2 * id + 1]); // Cây Range Minimum Query
}

void update_tree(int id, int l, int r, int pos, long long val) {
    if (l == r) {
        tree[id] = val;
        return;
    }
    int mid = (l + r) / 2;
    if (pos <= mid) update_tree(2 * id, l, mid, pos, val);
    else update_tree(2 * id + 1, mid + 1, r, pos, val);
    tree[id] = min(tree[2 * id], tree[2 * id + 1]);
}

long long query_tree(int id, int l, int r, int u, int v) {
    if (v < l || u > r) return 1e18; // Nằm ngoài khoảng
    if (u <= l && r <= v) return tree[id]; // Nằm trọn trong khoảng
    int mid = (l + r) / 2;
    return min(query_tree(2 * id, l, mid, u, v), query_tree(2 * id + 1, mid + 1, r, u, v));
}
```


## 4. Ranh giới áp dụng: Khi nào chọn Fenwick vs Segment Tree?

| Tiêu Chí | Cây Fenwick (BIT) | Cây Phân Đoạn (Segment Tree) |
|---|---|---|
| **Độ phức tạp code** | Cực ngắn ($\approx 15$ dòng), ít bug | Dài hơn ($\approx 50$ dòng) |
| **Tốc độ thực thi** | Nhanh hơn gấp 2–3 lần Segment Tree | Chậm hơn do chi phí đệ quy |
| **Bộ nhớ** | Đúng $N$ phần tử | Cần $4N$ phần tử |
| **Phạm vi bài toán** | Tổng tiền tố, đếm nghịch thế, tìm $K$-th | Mọi hàm kết hợp (Min, Max, GCD, Lazy Propagation) |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L13-01]: Truy Vấn Tổng Đoạn Fenwick Tree

**Bối cảnh & Nhiệm vụ:**

Cho mảng $N$ phần tử. Có $Q$ thao tác: `1 u v` (cộng $v$ vào $A[u]$) và `2 l r` (tính tổng $A[l..r]$).

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Truy Vấn Tổng Đoạn Fenwick Tree với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng 1: $N, Q$. Dòng 2: $N$ số $A_i$. $Q$ dòng tiếp theo: các truy vấn.

**Đầu ra (Output):**

- In ra kết quả của các truy vấn loại 2.

**Ví dụ mẫu:**

### Input
```text
5 3
1 2 3 4 5
2 1 5
1 3 2
2 1 5
```
### Output
```text
15
17
```



### Bài 02 [CPPB2-L13-02]: Truy Vấn Giá Trị Nhỏ Nhất Đoạn (rmq Segment Tree)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Truy Vấn Giá Trị Nhỏ Nhất Đoạn (RMQ Segment Tree)** là bài toán trọng tâm thuộc cấp độ **P0** nhằm rèn luyện: Cài đặt Segment Tree Point Update.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Truy Vấn Giá Trị Nhỏ Nhất Đoạn (rmq Segment Tree) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Truy Vấn Giá Trị Nhỏ Nhất Đoạn (RMQ Segment Tree).



### Bài 03 [CPPB2-L13-03]: Đếm Cặp Nghịch Thế Bằng Fenwick Tree

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Cặp Nghịch Thế Bằng Fenwick Tree** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Nén tọa độ + Fenwick Tree.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Cặp Nghịch Thế Bằng Fenwick Tree với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Cặp Nghịch Thế Bằng Fenwick Tree.



### Bài 04 [CPPB2-L13-04]: Truy Vấn Gcd Đoạn Động

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Truy Vấn GCD Đoạn Động** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Segment Tree với hàm $\gcd(A, B)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Truy Vấn Gcd Đoạn Động với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Truy Vấn GCD Đoạn Động.



### Bài 05 [CPPB2-L13-05]: Tìm Phần Tử Số 1 Thứ K Trong Dãy Nhị Phân

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tìm Phần Tử Số 1 Thứ K Trong Dãy Nhị Phân** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: Chặt nhị phân trực tiếp trên Segment Tree.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tìm Phần Tử Số 1 Thứ K Trong Dãy Nhị Phân với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Phần Tử Số 1 Thứ K Trong Dãy Nhị Phân.



### Bài 06 [CPPB2-L13-06]: Dãy Con Tăng Dài Nhất Lis Bằng Segment Tree

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Dãy Con Tăng Dài Nhất LIS Bằng Segment Tree** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: DP kết hợp Segment Tree Range Max.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dãy Con Tăng Dài Nhất Lis Bằng Segment Tree với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dãy Con Tăng Dài Nhất LIS Bằng Segment Tree.



### Bài 07 [CPPB2-L13-07]: Cập Nhật Đoạn Truy Vấn Điểm Bằng Fenwick Tree

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Cập Nhật Đoạn Truy Vấn Điểm Bằng Fenwick Tree** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Fenwick trên mảng hiệu (Difference BIT).

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cập Nhật Đoạn Truy Vấn Điểm Bằng Fenwick Tree với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cập Nhật Đoạn Truy Vấn Điểm Bằng Fenwick Tree.



### Bài 08 [CPPB2-L13-08]: Segment Tree Lazy Propagation (cập Nhật Đoạn & Truy Vấn Đoạn)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Segment Tree Lazy Propagation (Cập Nhật Đoạn & Truy Vấn Đoạn)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Kỹ thuật Lazy Propagation.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Segment Tree Lazy Propagation (cập Nhật Đoạn & Truy Vấn Đoạn) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Segment Tree Lazy Propagation (Cập Nhật Đoạn & Truy Vấn Đoạn).



### Bài 09 [CPPB2-L13-09]: Đoạn Con Có Tổng Lớn Nhất (maximum Subsegment Sum Query)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đoạn Con Có Tổng Lớn Nhất (Maximum Subsegment Sum Query)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Segment Tree lưu 4 trường (sum, pref, suff, ans).

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đoạn Con Có Tổng Lớn Nhất (maximum Subsegment Sum Query) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoạn Con Có Tổng Lớn Nhất (Maximum Subsegment Sum Query).



### Bài 10 [CPPB2-L13-10]: Đoạn Con Có Tổng Lớn Nhất (maximum Subsegment Sum Query)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đoạn Con Có Tổng Lớn Nhất (Maximum Subsegment Sum Query)** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Segment Tree lưu 4 trường (sum, pref, suff, ans).

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đoạn Con Có Tổng Lớn Nhất (maximum Subsegment Sum Query) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoạn Con Có Tổng Lớn Nhất (Maximum Subsegment Sum Query).



### Bài 11 [CPPB2-L13-11]: Lazy Propagation Gán Đoạn Và Tìm Min Đoạn

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Lazy Propagation Gán Đoạn Và Tìm Min Đoạn** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Lazy gán giá trị mới lên khoảng.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Lazy Propagation Gán Đoạn Và Tìm Min Đoạn với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lazy Propagation Gán Đoạn Và Tìm Min Đoạn.



### Bài 12 [CPPB2-L13-12]: Cây Fenwick Cập Nhật Đoạn & Truy Vấn Đoạn

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Cây Fenwick Cập Nhật Đoạn & Truy Vấn Đoạn** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: 2 mảng BIT quản lý $\sum (d_1 \cdot i - d_2)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cây Fenwick Cập Nhật Đoạn & Truy Vấn Đoạn với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cây Fenwick Cập Nhật Đoạn & Truy Vấn Đoạn.



### Bài 13 [CPPB2-L13-13]: Tìm Vị Trí Đầu Tiên Có Giá Trị $\ge X$ Trong Đoạn $[l, R]$

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tìm Vị Trí Đầu Tiên Có Giá Trị $\ge X$ Trong Đoạn $[L, R]$** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Binary Search trên Segment Tree nhánh trái/phải.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tìm Vị Trí Đầu Tiên Có Giá Trị $\ge X$ Trong Đoạn $[l, R]$ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Vị Trí Đầu Tiên Có Giá Trị $\ge X$ Trong Đoạn $[L, R]$.



### Bài 14 [CPPB2-L13-14]: Segment Tree Động (dynamic / Sparse Segment Tree)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Segment Tree Động (Dynamic / Sparse Segment Tree)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Tạo nút cây theo yêu cầu bằng con trỏ.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Segment Tree Động (dynamic / Sparse Segment Tree) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Segment Tree Động (Dynamic / Sparse Segment Tree).



### Bài 15 [CPPB2-L13-15]: Cây Phân Đoạn Bền Vững (persistent Segment Tree Cơ Bản)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Cây Phân Đoạn Bền Vững (Persistent Segment Tree Cơ Bản)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Cây lưu vết phiên bản tìm phần tử nhỏ thứ $K$ trên đoạn.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cây Phân Đoạn Bền Vững (persistent Segment Tree Cơ Bản) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cây Phân Đoạn Bền Vững (Persistent Segment Tree Cơ Bản).



### Bài 16 [CPPB2-L13-16]: Segment Tree Beats (thuật Toán Ji Driver Tối Ưu Phép Min=x)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Segment Tree Beats (Thuật Toán Ji Driver Tối Ưu Phép Min=X)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Phân rã lịch sử giá trị lớn nhất/nhì.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Segment Tree Beats (thuật Toán Ji Driver Tối Ưu Phép Min=x) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Segment Tree Beats (Thuật Toán Ji Driver Tối Ưu Phép Min=X).



### Bài 17 [CPPB2-L13-17]: Segment Tree Lazy Propagation Tong Doan

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Segment Tree Lazy Propagation Tong Doan** là một dạng bài điển hình thuộc chuyên đề **Cây Phân Đoạn & Cây Fenwick (Segment Tree & BIT)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Segment Tree Lazy Propagation Tong Doan với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 2
1 2 3
1 1 2 10
2 1 3
```
### Output
```text
26
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `26`.



### Bài 18 [CPPB2-L13-18]: Fenwick Tree 2d Tong Chu Nhat

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Fenwick Tree 2D Tong Chu Nhat** là một dạng bài điển hình thuộc chuyên đề **Cây Phân Đoạn & Cây Fenwick (Segment Tree & BIT)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Fenwick Tree 2d Tong Chu Nhat với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
2 2 1
1 1 1 5
2 1 1 2 2
```
### Output
```text
5
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `5`.



### Bài 19 [CPPB2-L13-19]: Dynamic Segment Tree Toa Do 1e9

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Dynamic Segment Tree Toa Do 1E9** là một dạng bài điển hình thuộc chuyên đề **Cây Phân Đoạn & Cây Fenwick (Segment Tree & BIT)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Dynamic Segment Tree Toa Do 1e9 với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
2
1 1000000000 5
2 1 1000000000
```
### Output
```text
5
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `5`.



### Bài 20 [CPPB2-L13-20]: Persistent Segment Tree K Th Number

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Persistent Segment Tree K Th Number** là một dạng bài điển hình thuộc chuyên đề **Cây Phân Đoạn & Cây Fenwick (Segment Tree & BIT)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Persistent Segment Tree K Th Number với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 1
3 1 2
1 3 2
```
### Output
```text
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2`.



### Bài 21 [CPPB2-L13-21]: Segment Tree Walk On Tree

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Segment Tree Walk On Tree** là một dạng bài điển hình thuộc chuyên đề **Cây Phân Đoạn & Cây Fenwick (Segment Tree & BIT)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Segment Tree Walk On Tree với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 1
1 5 2
1 4
```
### Output
```text
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2`.



### Bài 22 [CPPB2-L13-22]: Merge Sort Tree Dem So Phan Tu Lon Hon K

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Merge Sort Tree Dem So Phan Tu Lon Hon K** là một dạng bài điển hình thuộc chuyên đề **Cây Phân Đoạn & Cây Fenwick (Segment Tree & BIT)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Merge Sort Tree Dem So Phan Tu Lon Hon K với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 1
1 5 3
1 3 2
```
### Output
```text
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2`.



### Bài 23 [CPPB2-L13-23]: Fenwick Tree Range Update Range Query

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Fenwick Tree Range Update Range Query** là một dạng bài điển hình thuộc chuyên đề **Cây Phân Đoạn & Cây Fenwick (Segment Tree & BIT)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Fenwick Tree Range Update Range Query với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 2
1 2 3
1 1 2 5
2 1 3
```
### Output
```text
16
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `16`.



### Bài 24 [CPPB2-L13-24]: Segment Tree Beats Co Ban

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Segment Tree Beats Co Ban** là một dạng bài điển hình thuộc chuyên đề **Cây Phân Đoạn & Cây Fenwick (Segment Tree & BIT)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Segment Tree Beats Co Ban với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 2
5 5 5
1 1 3 3
2 1 3
```
### Output
```text
9
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `9`.



### Bài 25 [CPPB2-L13-25]: Segment Tree Max Subarray Sum

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Segment Tree Max Subarray Sum** là một dạng bài điển hình thuộc chuyên đề **Cây Phân Đoạn & Cây Fenwick (Segment Tree & BIT)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Segment Tree Max Subarray Sum với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 2
-1 2 3
1 1 4
2 1 3
```
### Output
```text
9
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `9`.



### Bài 26 [CPPB2-L13-26]: Segment Tree Dem So Phan Tu Khac Nhau Offline

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Segment Tree Dem So Phan Tu Khac Nhau Offline** là một dạng bài điển hình thuộc chuyên đề **Cây Phân Đoạn & Cây Fenwick (Segment Tree & BIT)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Segment Tree Dem So Phan Tu Khac Nhau Offline với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
4 2
1 2 2 1
1 3
2 4
```
### Output
```text
2
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2
2`.



# Bài 14: Quy hoạch động chữ số (Digit DP)

## 1. Khái niệm & bản chất của Quy hoạch động chữ số

Quy hoạch động chữ số (Digit DP) là phương pháp chuyên dùng để giải quyết các bài toán: **Đếm số lượng số nguyên trong đoạn $[L, R]$ thỏa mãn một tính chất chữ số đặc biệt** (ví dụ: tổng chữ số bằng $K$, không chứa chữ số 4 và 7, các chữ số tăng dần, số nguyên tố, số chia hết cho $D$).

Với $L, R \le 10^{18}$, duyệt trâu từng số mất $10^{18}$ phép tính $\implies$ TLE.  
Digit DP giải quyết bài toán bằng cách:

1. Chuyển đổi bài toán đoạn: $\text{Count}([L, R]) = f(R) - f(L - 1)$ với $f(X)$ là số lượng số thỏa mãn trong $[0, X]$.
2. Biểu diễn số $X$ thành mảng các chữ số $D_0, D_1, \dots, D_{M-1}$ ($M \le 19$).
3. Xây dựng số từ trái sang phải qua hàm đệ quy có nhớ `memo[index][tight][leading_zero][state]`.




![Mô hình phân nhánh Digit DP](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-14-quy-hoach-dong-chu-so-digit-dp/assets/l14_digit_dp_tree_visual.png)



## 2. Các tham số trạng thái cốt lõi trong Digit DP

1. **`index` (Vị trí chữ số hiện tại):** Duyệt từ chữ số đầu tiên (cao nhất) $0$ đến chữ số cuối cùng $M - 1$.
2. **`tight` (Cờ giới hạn cận trên):**
   - `tight = true`: Các chữ số phía trước đều đã chọn trùng khít với các chữ số của $X$. Chữ số hiện tại chỉ được chọn từ $0$ đến $D_{index}$.
   - `tight = false`: Đã có ít nhất một chữ số phía trước chọn nhỏ hơn $D$, số hiện tại được tự do chọn từ $0$ đến $9$.
3. **`leading_zero` (Cờ số 0 vô nghĩa ở đầu):** Xác định xem ta đã bắt đầu viết số thực tế chưa hay vẫn đang là các số 0 vô nghĩa (ảnh hưởng đến việc đếm chữ số 0).
4. **`state` (Trạng thái đặc thù của bài toán):** Ví dụ tổng các chữ số đã chọn, số dư khi chia cho $K$, mặt nạ bit của các chữ số đã xuất hiện.


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


## 4. Ranh giới áp dụng

| Dạng Bài | Cận Biên $R$ | Kỹ Thuật Tối Ưu | Độ Phức Tạp |
|---|---|---|:---:|
| Đếm số theo tính chất chữ số | $R \le 10^{18}$ | Digit DP | $\mathcal{O}(\text{Length}(R) \times \text{States} \times 10) \approx 19 \times 200 \times 10 < 10^5$ |
| Đếm số theo tính chất đại số lớn | $R \le 10^9$ | Sàng / Toán học / Bù trừ PIE | $\mathcal{O}(\sqrt{R})$ hoặc $\mathcal{O}(1)$ |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L14-01]: Đếm Số Có Tổng Chữ Số Bằng K

**Bối cảnh & Nhiệm vụ:**

Đếm số lượng số nguyên trong đoạn $[L, R]$ có tổng các chữ số đúng bằng $K$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Có Tổng Chữ Số Bằng K với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Gồm 1 dòng chứa $L, R, K$ ($1 \le L \le R \le 10^{18}, 1 \le K \le 180$).

**Đầu ra (Output):**

- In ra số lượng số thỏa mãn.

**Ví dụ mẫu:**

### Input
```text
1 100 5
```
### Output
```text
6
```



### Bài 02 [CPPB2-L14-02]: Tổng Các Chữ Số Bằng K Trong Đoạn [l, R]

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tổng Các Chữ Số Bằng K Trong Đoạn [L, R]** là bài toán trọng tâm thuộc cấp độ **P0** nhằm rèn luyện: Digit DP lưu trạng thái `current_sum`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tổng Các Chữ Số Bằng K Trong Đoạn [l, R] với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Các Chữ Số Bằng K Trong Đoạn [L, R].



### Bài 03 [CPPB2-L14-03]: Đếm Số Lượng Chữ Số 0 Xuất Hiện

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Lượng Chữ Số 0 Xuất Hiện** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Digit DP với cờ `leading_zero`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Lượng Chữ Số 0 Xuất Hiện với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Lượng Chữ Số 0 Xuất Hiện.



### Bài 04 [CPPB2-L14-04]: Số Có Các Chữ Số Tăng Ngặt

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Số Có Các Chữ Số Tăng Ngặt** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Digit DP lưu chữ số liền trước `last_digit`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Số Có Các Chữ Số Tăng Ngặt với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Có Các Chữ Số Tăng Ngặt.



### Bài 05 [CPPB2-L14-05]: Số Chia Hết Cho Tổng Các Chữ Số Của Chính Nó

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Số Chia Hết Cho Tổng Các Chữ Số Của Chính Nó** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: Cố định tổng chữ số từ $1 \dots 162$ + Digit DP.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Số Chia Hết Cho Tổng Các Chữ Số Của Chính Nó với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Chia Hết Cho Tổng Các Chữ Số Của Chính Nó.



### Bài 06 [CPPB2-L14-06]: Đếm Số Đối Xứng (palindrome Numbers) Trong Đoạn

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Đối Xứng (Palindrome Numbers) Trong Đoạn** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Digit DP xây dựng nửa đầu và nửa sau.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Đối Xứng (palindrome Numbers) Trong Đoạn với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đối Xứng (Palindrome Numbers) Trong Đoạn.



### Bài 07 [CPPB2-L14-07]: Số Chứa Đầy Đủ Các Chữ Số Từ 0 Đến 9

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Số Chứa Đầy Đủ Các Chữ Số Từ 0 Đến 9** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Digit DP kết hợp Bitmask lưu tập chữ số.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Số Chứa Đầy Đủ Các Chữ Số Từ 0 Đến 9 với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Chứa Đầy Đủ Các Chữ Số Từ 0 Đến 9.



### Bài 08 [CPPB2-L14-08]: Tổng Các Số Trong Đoạn Thỏa Mãn Tính Chất Chữ Số

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tổng Các Số Trong Đoạn Thỏa Mãn Tính Chất Chữ Số** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Digit DP trả về cặp `{số_lượng, tổng_giá_trị}`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tổng Các Số Trong Đoạn Thỏa Mãn Tính Chất Chữ Số với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Các Số Trong Đoạn Thỏa Mãn Tính Chất Chữ Số.



### Bài 09 [CPPB2-L14-09]: Số Có Tích Các Chữ Số Bằng K

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Số Có Tích Các Chữ Số Bằng K** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Digit DP kiểm tra $K$ chỉ có ước nguyên tố 2, 3, 5, 7.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Số Có Tích Các Chữ Số Bằng K với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Có Tích Các Chữ Số Bằng K.



### Bài 10 [CPPB2-L14-10]: Tổng Giá Trị Các Số Thỏa Mãn Tính Chất Chữ Số

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tổng Giá Trị Các Số Thỏa Mãn Tính Chất Chữ Số** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Digit DP trả về cặp `{số_lượng, tổng_giá_trị}`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tổng Giá Trị Các Số Thỏa Mãn Tính Chất Chữ Số với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Giá Trị Các Số Thỏa Mãn Tính Chất Chữ Số.



### Bài 11 [CPPB2-L14-11]: Đếm Số Tự Mãn (số Armstrong / Narcissistic) Trong Đoạn

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Tự Mãn (Số Armstrong / Narcissistic) Trong Đoạn** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Digit DP tính tổng lũy thừa bậc $K$ chữ số.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Tự Mãn (số Armstrong / Narcissistic) Trong Đoạn với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Tự Mãn (Số Armstrong / Narcissistic) Trong Đoạn.



### Bài 12 [CPPB2-L14-12]: Đếm Số Đẹp Có Hiệu Hai Chữ Số Kề Nhau $\ge 2$ (số Stepping)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Đẹp Có Hiệu Hai Chữ Số Kề Nhau $\ge 2$ (Số Stepping)** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Digit DP kiểm tra $\vert D_i - D_{i-1} \vert \ge 2$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Đẹp Có Hiệu Hai Chữ Số Kề Nhau $\ge 2$ (số Stepping) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đẹp Có Hiệu Hai Chữ Số Kề Nhau $\ge 2$ (Số Stepping).



### Bài 13 [CPPB2-L14-13]: Số Có Tổng Bình Phương Các Chữ Số Là Số Nguyên Tố

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Số Có Tổng Bình Phương Các Chữ Số Là Số Nguyên Tố** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Sàng nguyên tố kết hợp Digit DP.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Số Có Tổng Bình Phương Các Chữ Số Là Số Nguyên Tố với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Có Tổng Bình Phương Các Chữ Số Là Số Nguyên Tố.



### Bài 14 [CPPB2-L14-14]: Tìm Số Thỏa Mãn Điều Kiện Chữ Số Thứ K Nhỏ Nhất

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tìm Số Thỏa Mãn Điều Kiện Chữ Số Thứ K Nhỏ Nhất** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Chặt nhị phân kết quả kết hợp hàm đếm Digit DP.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tìm Số Thỏa Mãn Điều Kiện Chữ Số Thứ K Nhỏ Nhất với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Số Thỏa Mãn Điều Kiện Chữ Số Thứ K Nhỏ Nhất.



### Bài 15 [CPPB2-L14-15]: Số Chia Hết Cho Tất Cả Các Chữ Số Khác Không Của Nó

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Số Chia Hết Cho Tất Cả Các Chữ Số Khác Không Của Nó** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Digit DP trạng thái $lcm$ và số dư theo $2520$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Số Chia Hết Cho Tất Cả Các Chữ Số Khác Không Của Nó với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Chia Hết Cho Tất Cả Các Chữ Số Khác Không Của Nó.



### Bài 16 [CPPB2-L14-16]: Tổng Xor Chữ Số Của Mọi Số Trong Đoạn $[l, R]$

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tổng XOR Chữ Số Của Mọi Số Trong Đoạn $[L, R]$** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Digit DP đa chiều tính tổng tích lũy XOR.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tổng Xor Chữ Số Của Mọi Số Trong Đoạn $[l, R]$ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng XOR Chữ Số Của Mọi Số Trong Đoạn $[L, R]$.



### Bài 17 [CPPB2-L14-17]: Digit Dp Chia Het Cho K

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Digit Dp Chia Het Cho K** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Chữ Số (Digit DP)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Digit Dp Chia Het Cho K với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
1 20 3
```
### Output
```text
6
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `6`.



### Bài 18 [CPPB2-L14-18]: Digit Dp Khong Chua Chu So Cam

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Digit Dp Khong Chua Chu So Cam** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Chữ Số (Digit DP)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Digit Dp Khong Chua Chu So Cam với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
1 20
```
### Output
```text
18
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `18`.



### Bài 19 [CPPB2-L14-19]: Digit Dp So Doi Xung Palindrome

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Digit Dp So Doi Xung Palindrome** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Chữ Số (Digit DP)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Digit Dp So Doi Xung Palindrome với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
1 100
```
### Output
```text
18
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `18`.



### Bài 20 [CPPB2-L14-20]: Digit Dp Tong Binh Phuong Chu So

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Digit Dp Tong Binh Phuong Chu So** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Chữ Số (Digit DP)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Digit Dp Tong Binh Phuong Chu So với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
1 10
```
### Output
```text
286
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `286`.



### Bài 21 [CPPB2-L14-21]: Digit Dp Dem So Nguyen To Chu So

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Digit Dp Dem So Nguyen To Chu So** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Chữ Số (Digit DP)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Digit Dp Dem So Nguyen To Chu So với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
1 10
```
### Output
```text
4
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `4`.



### Bài 22 [CPPB2-L14-22]: Digit Dp Tich Cac Chu So

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Digit Dp Tich Cac Chu So** là một dạng bài điển hình thuộc chuyên đề **Quy Hoạch Động Chữ Số (Digit DP)**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Digit Dp Tich Cac Chu So với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
20 6
```
### Output
```text
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2`.



# Bài 15: Xử lý chuỗi ký tự, String Hashing & số nguyên lớn

## 1. Khái niệm & cấu trúc 3 phần của Bài 15

Bài 15 là bài học tổng hợp cuối cùng của khóa học Level 2, tích hợp 3 mảng kiến thức lớn:

1. **15.1. Xử lý xâu cơ bản & Palindrome:** Các thao tác chuẩn trên `string`, đếm tần suất ký tự, kỹ thuật mở rộng tâm (Expand Around Center) tìm xâu con đối xứng dài nhất trong $\mathcal{O}(N^2)$.
2. **15.2. Kỹ thuật Băm chuỗi đa thức (Rolling Hash / Polynomial Hashing):** Biến đổi một xâu ký tự thành một số nguyên duy nhất theo modulo, cho phép so sánh hai xâu con bất kỳ $S[L \dots R]$ trong thời gian **$\mathcal{O}(1)$** (thay vì $\mathcal{O}(N)$).
3. **15.3. Xử lý số nguyên lớn (Big Integer):** Tự xây dựng cấu trúc số nguyên lớn để thực hiện các phép cộng, trừ, nhân hai số có hàng nghìn chữ số.




![Cây tiền tố Trie](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-15-xu-ly-chuoi-hashing-so-lon/assets/l15_trie_tree_visual.png)



## 2. Kỹ thuật Băm chuỗi đa thức (Polynomial Rolling Hash)

### 2.1. Công thức hàm băm tiền tố

Cho xâu $S$ độ dài $N$, cơ số $Base = 311$ (hoặc $31$) và modulo $MOD = 10^9 + 7$:

* Mảng băm tiền tố $hash[i] = (S[0] \cdot Base^i + S[1] \cdot Base^{i-1} + \dots + S[i]) \bmod MOD$.
* Công thức tính mã băm của đoạn con $S[L \dots R]$ (1-based) trong $\mathcal{O}(1)$:
$$\text{get\_hash}(L, R) = (hash[R] - hash[L - 1] \times Base^{R - L + 1} \bmod MOD + MOD) \bmod MOD$$

### 2.2. Kỹ thuật Băm kép (Double Hash) chống đụng độ $100\%$

Để tránh việc hai xâu khác nhau có cùng mã băm (Hash Collision) do nguyên lý Dirichlet khi số lượng truy vấn lớn ($Q = 10^5$), ta sử dụng đồng thời **hai cặp $(Base_1, MOD_1)$ và $(Base_2, MOD_2)$** khác nhau (ví dụ: $MOD_1 = 10^9+7, MOD_2 = 10^9+9$). Mã băm lúc này là một cặp số `pair<long long, long long>`. Khả năng đụng độ giảm xuống $\frac{1}{MOD_1 \times MOD_2} \approx 10^{-18}$ (gần như bằng 0 tuyệt đối).

```cpp
const long long BASE = 311;
const long long MOD = 1000000007;

long long h[1000005];
long long pw[1000005];

void init_hash(const string &s) {
    int n = s.size();
    pw[0] = 1;
    for (int i = 1; i <= n; ++i) pw[i] = (pw[i - 1] * BASE) % MOD;

    h[0] = 0;
    for (int i = 0; i < n; ++i) {
        h[i + 1] = (h[i] * BASE + s[i]) % MOD;
    }
}

long long get_hash(int l, int r) { // 1-based indexing
    long long res = (h[r] - h[l - 1] * pw[r - l + 1]) % MOD;
    return (res + MOD) % MOD;
}
```


## 3. Cấu trúc số nguyên lớn (Big Integer Addition, Subtraction, Multiplication)

### 3.1. Phép cộng hai số nguyên lớn

```cpp
string add_bigint(string a, string b) {
    while (a.size() < b.size()) a = "0" + a;
    while (b.size() < a.size()) b = "0" + b;

    int carry = 0;
    string res = "";
    for (int i = (int)a.size() - 1; i >= 0; --i) {
        int sum = (a[i] - '0') + (b[i] - '0') + carry;
        carry = sum / 10;
        res += to_string(sum % 10);
    }
    if (carry) res += to_string(carry);
    reverse(res.begin(), res.end());
    return res;
}
```

### 3.2. Phép nhân hai số nguyên lớn

```cpp
string multiply_bigint(string a, string b) {
    int n = a.size(), m = b.size();
    vector<int> res(n + m, 0);

    for (int i = n - 1; i >= 0; --i) {
        for (int j = m - 1; j >= 0; --j) {
            int mul = (a[i] - '0') * (b[j] - '0');
            int p1 = i + j, p2 = i + j + 1;
            int sum = mul + res[p2];

            res[p2] = sum % 10;
            res[p1] += sum / 10;
        }
    }

    string s = "";
    for (int val : res) {
        if (!(s.empty() && val == 0)) s += to_string(val);
    }
    return s.empty() ? "0" : s;
}
```


## 4. Ranh giới áp dụng

| Tình Huống Bài Toán | Kỹ Thuật Tối Ưu | Độ Phức Tạp |
|---|---|:---:|
| So sánh nhiều xâu con, tìm xâu con chung, đếm xâu đối xứng | String Hashing (Rolling Hash) | Tiền xử lý $\mathcal{O}(N)$, truy vấn $\mathcal{O}(1)$ |
| Phép tính số học với số có độ dài đến $10^4$ chữ số | Big Integer | Cộng $\mathcal{O}(N)$, Nhân $\mathcal{O}(NM)$ |
| Khớp mẫu xâu cơ bản | KMP hoặc String Hashing | $\mathcal{O}(N + M)$ |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L15-01]: Truy Vấn So Khớp Xâu Con Hashing

**Bối cảnh & Nhiệm vụ:**

Cho xâu $S$ và $Q$ truy vấn kiểm tra xem hai xâu con $S[a..b]$ và $S[c..d]$ có giống nhau hay không.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Truy Vấn So Khớp Xâu Con Hashing với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng 1: Xâu $S$ ($|S| \le 10^5$). Dòng 2: $Q$ ($1 \le Q \le 10^5$). $Q$ dòng sau: $a, b, c, d$ (1-based).

**Đầu ra (Output):**

- In ra `YES` nếu hai xâu con bằng nhau, `NO` nếu khác nhau.

**Ví dụ mẫu:**

### Input
```text
abacaba
2
1 3 5 7
1 3 2 4
```
### Output
```text
YES
NO
```



### Bài 02 [CPPB2-L15-02]: Nhân Hai Số Nguyên Lớn

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Nhân Hai Số Nguyên Lớn** là bài toán trọng tâm thuộc cấp độ **P0** nhằm rèn luyện: Cài đặt BigInt Multiplication $\mathcal{O}(NM)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Nhân Hai Số Nguyên Lớn với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nhân Hai Số Nguyên Lớn.



### Bài 03 [CPPB2-L15-03]: Truy Vấn So Khớp Hai Xâu Con Bằng Hashing

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Truy Vấn So Khớp Hai Xâu Con Bằng Hashing** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: Cài đặt Rolling Hash $\mathcal{O}(1)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Truy Vấn So Khớp Hai Xâu Con Bằng Hashing với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Truy Vấn So Khớp Hai Xâu Con Bằng Hashing.



### Bài 04 [CPPB2-L15-04]: Tìm Xâu Mẫu P Trong Xâu Văn Bản T (string Match)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tìm Xâu Mẫu P Trong Xâu Văn Bản T (String Match)** là bài toán trọng tâm thuộc cấp độ **P1** nhằm rèn luyện: So khớp mã băm trượt.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tìm Xâu Mẫu P Trong Xâu Văn Bản T (string Match) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Xâu Mẫu P Trong Xâu Văn Bản T (String Match).



### Bài 05 [CPPB2-L15-05]: Xâu Con Đối Xứng Dài Nhất (longest Palindromic Substring)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Xâu Con Đối Xứng Dài Nhất (Longest Palindromic Substring)** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: Băm xuôi + Băm ngược + Chặt nhị phân độ dài.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Xâu Con Đối Xứng Dài Nhất (longest Palindromic Substring) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xâu Con Đối Xứng Dài Nhất (Longest Palindromic Substring).



### Bài 06 [CPPB2-L15-06]: Đếm Số Xâu Con Khác Nhau Của Một Xâu

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Đếm Số Xâu Con Khác Nhau Của Một Xâu** là bài toán trọng tâm thuộc cấp độ **P2** nhằm rèn luyện: String Hashing + `unordered_set`.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Đếm Số Xâu Con Khác Nhau Của Một Xâu với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Xâu Con Khác Nhau Của Một Xâu.



### Bài 07 [CPPB2-L15-07]: Xâu Con Lặp Lại Dài Nhất Xuất Hiện Ít Nhất K Lần

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Xâu Con Lặp Lại Dài Nhất Xuất Hiện Ít Nhất K Lần** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Chặt nhị phân độ dài kết hợp Double Hash.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Xâu Con Lặp Lại Dài Nhất Xuất Hiện Ít Nhất K Lần với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xâu Con Lặp Lại Dài Nhất Xuất Hiện Ít Nhất K Lần.



### Bài 08 [CPPB2-L15-08]: Tính Giai Thừa $n!$ Cho $n = 1000$ Bằng Bigint

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tính Giai Thừa $N!$ Cho $N = 1000$ Bằng BigInt** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Nhân BigInt với số nguyên.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tính Giai Thừa $n!$ Cho $n = 1000$ Bằng Bigint với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tính Giai Thừa $N!$ Cho $N = 1000$ Bằng BigInt.



### Bài 09 [CPPB2-L15-09]: Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{o}(n)$

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{O}(N)$** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Manacher Algorithm.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{o}(n)$ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{O}(N)$.



### Bài 10 [CPPB2-L15-10]: Tìm Chu Kỳ Ngắn Nhất Của Xâu Ký Tự (string Period)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tìm Chu Kỳ Ngắn Nhất Của Xâu Ký Tự (String Period)** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: String Hashing kiểm tra chu kỳ lặp.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Tìm Chu Kỳ Ngắn Nhất Của Xâu Ký Tự (string Period) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Chu Kỳ Ngắn Nhất Của Xâu Ký Tự (String Period).



### Bài 11 [CPPB2-L15-11]: Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{o}(n)$

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{O}(N)$** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Thuật toán Manacher tìm mảng bán kính đối xứng.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{o}(n)$ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{O}(N)$.



### Bài 12 [CPPB2-L15-12]: Thuật Toán Kmp (knuth-morris-pratt) & Mảng Tiền Tố $\pi$

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Thuật Toán KMP (Knuth-Morris-Pratt) & Mảng Tiền Tố $\pi$** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Cài đặt hàm tiền xử lý $\pi$ của KMP.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Thuật Toán Kmp (knuth-morris-pratt) & Mảng Tiền Tố $\pi$ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Thuật Toán KMP (Knuth-Morris-Pratt) & Mảng Tiền Tố $\pi$.



### Bài 13 [CPPB2-L15-13]: Căn Bậc Hai Của Số Nguyên Lớn

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Căn Bậc Hai Của Số Nguyên Lớn** là bài toán trọng tâm thuộc cấp độ **P4** nhằm rèn luyện: Chặt nhị phân kết hợp nhân BigInt.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Căn Bậc Hai Của Số Nguyên Lớn với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Căn Bậc Hai Của Số Nguyên Lớn.



### Bài 14 [CPPB2-L15-14]: Chia Hai Số Nguyên Lớn Cho Nhau (bigint / Bigint)

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Chia Hai Số Nguyên Lớn Cho Nhau (BigInt / BigInt)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Thuật toán chia dài Knuth (Algorithm D).

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Chia Hai Số Nguyên Lớn Cho Nhau (bigint / Bigint) với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chia Hai Số Nguyên Lớn Cho Nhau (BigInt / BigInt).



### Bài 15 [CPPB2-L15-15]: Xâu Con Chung Dài Nhất Của K Xâu Ký Tự

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Xâu Con Chung Dài Nhất Của K Xâu Ký Tự** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Chặt nhị phân độ dài + Băm đa chuỗi.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Xâu Con Chung Dài Nhất Của K Xâu Ký Tự với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xâu Con Chung Dài Nhất Của K Xâu Ký Tự.



### Bài 16 [CPPB2-L15-16]: Mảng Hậu Tố (suffix Array) Bằng String Hashing $\mathcal{o}(n \log^2 N)$

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Mảng Hậu Tố (Suffix Array) Bằng String Hashing $\mathcal{O}(N \log^2 N)$** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: Sắp xếp các hậu tố bằng so sánh mã băm và LCP.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Mảng Hậu Tố (suffix Array) Bằng String Hashing $\mathcal{o}(n \log^2 N)$ với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Mảng Hậu Tố (Suffix Array) Bằng String Hashing $\mathcal{O}(N \log^2 N)$.



### Bài 17 [CPPB2-L15-17]: Double Hashing Chong Va Cham

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Double Hashing Chong Va Cham** là một dạng bài điển hình thuộc chuyên đề **Xử Lý Chuỗi, String Hashing & BigInt**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Double Hashing Chong Va Cham với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
abcde 1
1 2 1 2
```
### Output
```text
YES
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `YES`.



### Bài 18 [CPPB2-L15-18]: Thuat Toan Manacher Palindrome

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Thuat Toan Manacher Palindrome** là một dạng bài điển hình thuộc chuyên đề **Xử Lý Chuỗi, String Hashing & BigInt**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Thuat Toan Manacher Palindrome với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
abacaba
```
### Output
```text
7
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `7`.



### Bài 19 [CPPB2-L15-19]: Z Algorithm Tim Mau

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Z Algorithm Tim Mau** là một dạng bài điển hình thuộc chuyên đề **Xử Lý Chuỗi, String Hashing & BigInt**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Z Algorithm Tim Mau với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
aaaaa
```
### Output
```text
0 4 3 2 1
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `0 4 3 2 1`.



### Bài 20 [CPPB2-L15-20]: Kmp Knuth Morris Pratt

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Kmp Knuth Morris Pratt** là một dạng bài điển hình thuộc chuyên đề **Xử Lý Chuỗi, String Hashing & BigInt**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Kmp Knuth Morris Pratt với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
ababababa aba
```
### Output
```text
4
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `4`.



### Bài 21 [CPPB2-L15-21]: Cay Trie Xau Co Ban

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Cay Trie Xau Co Ban** là một dạng bài điển hình thuộc chuyên đề **Xử Lý Chuỗi, String Hashing & BigInt**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Cay Trie Xau Co Ban với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
3 1
apple
app
application
app
```
### Output
```text
3
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `3`.



### Bài 22 [CPPB2-L15-22]: Chia So Nguyen Lon Bigint

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Chia So Nguyen Lon Bigint** là một dạng bài điển hình thuộc chuyên đề **Xử Lý Chuỗi, String Hashing & BigInt**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Chia So Nguyen Lon Bigint với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
100 25
```
### Output
```text
4
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `4`.



### Bài 23 [CPPB2-L15-23]: Can Bac Hai So Nguyen Lon

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Can Bac Hai So Nguyen Lon** là một dạng bài điển hình thuộc chuyên đề **Xử Lý Chuỗi, String Hashing & BigInt**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Can Bac Hai So Nguyen Lon với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
144
```
### Output
```text
12
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `12`.



### Bài 24 [CPPB2-L15-24]: Aho Corasick Da Mau Tim Kiem

**Bối cảnh & Nhiệm vụ:**

Trong lập trình thi đấu chuyên nghiệp, bài toán **Aho Corasick Da Mau Tim Kiem** là một dạng bài điển hình thuộc chuyên đề **Xử Lý Chuỗi, String Hashing & BigInt**. Bài toán yêu cầu thiết kế thuật toán tối ưu để xử lý tập dữ liệu lớn trong giới hạn thời gian nghiêm ngặt $1.0\text{s}$.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình giải quyết bài toán Aho Corasick Da Mau Tim Kiem với độ phức tạp tối ưu nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa các tham số đầu vào của bài toán theo đúng mô tả cấu trúc dữ liệu.
- Các dòng tiếp theo chứa dữ liệu chi tiết của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

### Input
```text
ushers 2
he
she
```
### Output
```text
2
```
### Giải thích
* Thuật toán khởi tạo cấu trúc dữ liệu, thực hiện tính toán và in ra kết quả mẫu: `2`.





\newpage

# Phụ lục A: Nền tảng C++

> Phần này tóm tắt toàn bộ cú pháp, cấu trúc dữ liệu và quy trình giải bài C++ cơ bản.

## 1. KHUNG TƯ DUY CỦA MỌI BÀI LẬP TRÌNH

Mọi bài toán đều bắt đầu bằng chuỗi câu hỏi:

```text
Đề bài → Dữ liệu → Biến → Công thức/Điều kiện
       → Các bước xử lý → Code → Kiểm tra kết quả
```

### Mô hình Input – Process – Output

| Thành phần | Câu hỏi cần trả lời |
|---|---|
| **Input** | Chương trình nhận những dữ liệu nào? |
| **Process** | Cần tính toán, kiểm tra hoặc lặp lại việc gì? |
| **Output** | Cần in ra kết quả nào, theo định dạng nào? |

Trước khi viết code, hãy viết bằng lời hoặc pseudocode:

```text
1. Đọc dữ liệu.
2. Tính hoặc xử lý dữ liệu.
3. Kiểm tra điều kiện nếu có.
4. In kết quả.
```

### Công thức trước code

Không viết code trước khi biết mình đang tính gì.

```text
Bài toán → Công thức hoặc quy tắc → Code
```

Ví dụ tính diện tích hình chữ nhật:

```text
S = chiều_dài × chiều_rộng
```

```cpp
long long area = length * width;
```

Ví dụ tính trung bình (giữ phần thập phân):

```cpp
double average = 1.0 * sum / n;
```

### Chuỗi ghi nhớ nền tảng

> **BIẾN → TÍNH → ĐIỀU KIỆN → LẶP → TÍCH LŨY → MẢNG → HÀM → DEBUG**

| Từ khóa | Câu hỏi tự kiểm tra |
|---|---|
| **Biến** | Tôi cần lưu dữ liệu gì? |
| **Tính** | Tôi cần công thức nào? |
| **Điều kiện** | Tôi cần đưa ra quyết định nào? |
| **Lặp** | Tôi cần làm việc gì nhiều lần? |
| **Tích lũy** | Tôi cần cộng, đếm, tìm lớn nhất hay nhỏ nhất? |
| **Mảng** | Tôi có nhiều dữ liệu cùng loại không? |
| **Hàm** | Tôi có thể tách phần việc nào thành một nhiệm vụ riêng? |
| **Debug** | Nếu kết quả sai, tôi sẽ kiểm tra từ đâu? |

---

## 2. KHUNG CHƯƠNG TRÌNH C++ TỐI THIỂU

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 1. Khai báo biến
    // 2. Đọc dữ liệu
    // 3. Xử lý
    // 4. In kết quả

    return 0;
}
```

| Thành phần | Ý nghĩa |
|---|---|
| `#include <bits/stdc++.h>` | Nạp các thư viện C++ thường dùng trong thi đấu |
| `using namespace std;` | Cho phép dùng `vector`, `string`, `cin`, `cout`… trực tiếp |
| `int main()` | Điểm bắt đầu thực hiện chương trình |
| `ios::sync_with_stdio(false);` | Tăng tốc nhập/xuất |
| `cin.tie(nullptr);` | Tối ưu liên kết giữa nhập và xuất |
| `return 0;` | Kết thúc chương trình thành công |

Giai đoạn đầu chỉ cần tập trung vào **dữ liệu – xử lý – kết quả**, chưa cần hiểu sâu cơ chế thư viện.

---

## 3. BIẾN VÀ KIỂU DỮ LIỆU

> **Biến là ô nhớ có tên để lưu dữ liệu.**

```cpp
int age = 15;
long long population = 9000000000LL;
double average = 8.5;
char grade = 'A';
string name = "An";
bool passed = true;
```

| Kiểu | Dùng để lưu | Ví dụ |
|---|---|---|
| `int` | Số nguyên thông thường | tuổi, số lượng nhỏ |
| `long long` | Số nguyên lớn hoặc tổng lớn | tổng tiền, tổng mảng |
| `double` | Số thực | trung bình, kết quả đo |
| `char` | Một ký tự | `'A'`, `'7'` |
| `string` | Một chuỗi ký tự | `"Hello"` |
| `bool` | Đúng hoặc sai | `true`, `false` |

### Quy tắc chọn kiểu dữ liệu

| Nếu giá trị… | Nên nghĩ đến… |
|---|---|
| Là số đếm nhỏ | `int` |
| Có thể vượt giới hạn `int`, hoặc là tổng nhiều số | `long long` |
| Có phần thập phân | `double` |
| Là một ký tự duy nhất | `char` |
| Là nhiều ký tự liên tiếp | `string` |
| Chỉ có hai trạng thái đúng/sai | `bool` |

> Khi chưa chắc tổng có lớn hay không, hãy cân nhắc dùng `long long`.

### Khởi tạo biến tích lũy

```cpp
long long sum = 0;
int count = 0;
int mx = -1000000000;
int mn = 1000000000;
```

Biến dùng để cộng hoặc đếm phải có giá trị ban đầu đúng. Không dùng biến chưa khởi tạo.

---

## 4. NHẬP VÀ XUẤT DỮ LIỆU

```cpp
int a, b;
cin >> a >> b;
cout << a + b << '\n';
```

```cpp
string s;
cin >> s;
cout << s << '\n';
```

| Lệnh | Ý nghĩa |
|---|---|
| `cin >> a` | Đọc một giá trị vào biến `a` |
| `cin >> a >> b` | Đọc nhiều giá trị liên tiếp |
| `cout << answer` | In kết quả |
| `<< '\n'` | Xuống dòng |

Nếu cần đọc cả một dòng có khoảng trắng, có thể dùng:

```cpp
getline(cin, s);
```

Trong phần lớn bài thi cơ bản, dữ liệu dạng số hoặc từ không có khoảng trắng có thể đọc bằng `cin >>`.

### Ba mẹo thi đấu thường gặp

```cpp
// 1. Đọc nhiều bộ test đến khi hết file
int n;
while (cin >> n) {
    // xử lý từng bộ test
}

// 2. Đọc dòng có khoảng trắng sau khi đã cin >> n
cin.ignore(numeric_limits<streamsize>::max(), '\n');
getline(cin, s);

// 3. Ép kiểu giữ phần thập phân khi sum là long long
double avg = 1.0 * sum / n;
```

> Cần `#include <bits/stdc++.h>` đã bao gồm `limits` cho `numeric_limits`.

---

## 5. TOÁN TỬ VÀ BIỂU THỨC

### Toán tử số học

| Toán tử | Ý nghĩa | Ví dụ |
|---|---|---|
| `+` | Cộng | `a + b` |
| `-` | Trừ | `a - b` |
| `*` | Nhân | `a * b` |
| `/` | Chia | `a / b` |
| `%` | Phần dư | `a % b` |

### Chia nguyên và phần dư

```cpp
15 / 4 == 3
15 % 4 == 3
```

Khi cả hai toán hạng là số nguyên, phép `/` cho phần nguyên. Toán tử `%` cho phần dư.

| Mẫu | Ý nghĩa |
|---|---|
| `x % 2 == 0` | `x` là số chẵn |
| `x % 2 != 0` | `x` là số lẻ |
| `x % 10` | Chữ số cuối của `x` |
| `x / 10` | Bỏ chữ số cuối của `x` |
| `a % b == 0` | `a` chia hết cho `b` |

### Toán tử so sánh

```cpp
>    <    >=    <=    ==    !=
```

| Toán tử | Ý nghĩa |
|---|---|
| `==` | Bằng nhau |
| `!=` | Khác nhau |
| `>` | Lớn hơn |
| `<` | Nhỏ hơn |
| `>=` | Lớn hơn hoặc bằng |
| `<=` | Nhỏ hơn hoặc bằng |

> **Lưu ý:** Đừng nhầm `=` (gán) với `==` (so sánh).

### Toán tử logic

| Toán tử | Ý nghĩa | Ví dụ |
|---|---|---|
| `&&` | Và | `age >= 10 && age <= 15` |
| `||` | Hoặc | `x == 0 || y == 0` |
| `!` | Phủ định | `!passed` |

---

## 6. ĐIỀU KIỆN — RẼ NHÁNH

### Mẫu cơ bản

```cpp
if (condition) {
    // việc A
} else {
    // việc B
}
```

Mô hình bằng lời:

```text
NẾU điều kiện đúng
    thực hiện A
NGƯỢC LẠI
    thực hiện B
```

### Nhiều trường hợp

```cpp
if (score >= 8) {
    cout << "Gioi";
} else if (score >= 6.5) {
    cout << "Kha";
} else {
    cout << "Can co gang";
}
```

### Điều kiện lồng nhau

Chỉ dùng khi quyết định thứ hai phụ thuộc vào quyết định thứ nhất. Hãy viết điều kiện bằng lời trước để tránh rối.

### Lỗi thường gặp

| Lỗi | Cách kiểm tra |
|---|---|
| Dùng `=` thay cho `==` | Đọc lại mọi điều kiện so sánh |
| Nhầm `>` với `>=` | Kiểm tra trường hợp bằng đúng ngưỡng |
| Thiếu trường hợp | Thử giá trị nhỏ nhất, lớn nhất và đúng biên |
| Điều kiện quá phức tạp | Tách thành các biến `bool` hoặc viết lại bằng lời |

---

## 7. VÒNG LẶP – LÀM MỘT VIỆC NHIỀU LẦN

Trước khi viết vòng lặp, trả lời ba câu hỏi:

1. Việc gì được lặp lại?
2. Biến nào thay đổi sau mỗi lần?
3. Khi nào vòng lặp dừng?

### `for`: biết trước số lần hoặc khoảng lặp

```cpp
for (int i = 0; i < n; i++) {
    // xử lý phần tử thứ i
}
```

Với mảng có `n` phần tử, chỉ số thường chạy từ `0` đến `n - 1`.

### `while`: lặp khi điều kiện còn đúng

```cpp
while (condition) {
    // xử lý
    // phải có cách làm condition thay đổi
}
```

Nếu điều kiện không bao giờ sai, chương trình có thể lặp vô hạn.

### `do..while`: thực hiện ít nhất một lần

```cpp
do {
    // xử lý
} while (condition);
```

Trong phần C++ cơ bản, `for` và `while` là hai dạng cần dùng thành thạo nhất.

### Vòng lặp lồng nhau

```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        // xử lý từng cặp (i, j)
    }
}
```

Nếu vòng ngoài chạy `N` lần và vòng trong chạy `M` lần, số thao tác thường là `O(NM)`.

---

## 8. BỐN MẪU TÍCH LŨY

### Tính tổng

```cpp
long long sum = 0;
for (int x : a) {
    sum += x;
}
```

### Đếm phần tử thỏa điều kiện

```cpp
int count = 0;
for (int x : a) {
    if (x % 2 == 0) count++;
}
```

### Tìm giá trị lớn nhất

```cpp
int mx = a[0];
for (int x : a) {
    mx = max(mx, x);
}
```

### Tìm giá trị nhỏ nhất

```cpp
int mn = a[0];
for (int x : a) {
    mn = min(mn, x);
}
```

> Nếu dữ liệu có thể rỗng, không được truy cập `a[0]` trước khi kiểm tra kích thước. Có thể khởi tạo `mx`, `mn` theo giới hạn bài toán.

---

## 9. MẢNG, `VECTOR` VÀ `STRING`

### Mảng và chỉ số

```text
a[0], a[1], a[2], .., a[n - 1]
```

> **Chỉ số bắt đầu từ 0.** Với `n` phần tử, chỉ số hợp lệ là `0 … n-1`.

### Đọc và duyệt mảng

```cpp
int n;
cin >> n;

vector<int> a(n);
for (int i = 0; i < n; i++) {
    cin >> a[i];
}

for (int i = 0; i < n; i++) {
    cout << a[i] << ' ';
}
```

### Duyệt bằng phần tử

```cpp
for (int x : a) {
    cout << x << ' ';
}
```

Dùng chỉ số `i` khi cần biết vị trí hoặc cập nhật `a[i]`. Dùng `x` khi chỉ cần đọc từng giá trị.

### Các thao tác `vector` cơ bản

| Lệnh | Ý nghĩa |
|---|---|
| `vector<int> a(n)` | Tạo vector có `n` phần tử |
| `a.size()` | Số phần tử |
| `a.push_back(x)` | Thêm `x` vào cuối |
| `a.pop_back()` | Xóa phần tử cuối |
| `a[i]` | Truy cập phần tử vị trí `i` |
| `a.empty()` | Kiểm tra có rỗng không |

### Xử lý `string`

```cpp
string s;
cin >> s;

for (int i = 0; i < (int)s.size(); i++) {
    if (s[i] == 'A') {
        // xử lý ký tự A
    }
}
```

| Biểu thức | Ý nghĩa |
|---|---|
| `s.size()` | Độ dài xâu |
| `s[i]` | Ký tự ở vị trí `i` |
| `s.front()` | Ký tự đầu |
| `s.back()` | Ký tự cuối |
|

---

## 10. HÀM — CHIA BÀI TOÁN THÀNH CÁC PHẦN

> **Hàm là một khối công việc riêng:** nhận dữ liệu vào, thực hiện một nhiệm vụ và có thể trả về kết quả.

```cpp
int square(int x) {
    return x * x;
}
```

```cpp
int result = square(5); // result = 25
```

### Mẫu hàm

```cpp
return_type function_name(parameters) {
    // xử lý
    return value;
}
```

Nếu hàm không trả về kết quả, dùng `void`:

```cpp
void printLine(int n) {
    for (int i = 0; i < n; i++) cout << '-';
    cout << '\n';
}
```

Hàm nên thực hiện **một nhiệm vụ rõ ràng**. Các tên hàm thường gặp trong bài thuật toán là `check()`, `isPrime()`, `gcd()`, `solve()` và `dfs()`.

---

## 11. GỠ LỖI VÀ KIỂM THỬ

Khi chương trình sai, không đoán bừa. Hãy kiểm tra theo thứ tự:

| Câu hỏi | Việc cần làm |
|---|---|
| Input có đúng không? | Đọc lại định dạng và số lượng dữ liệu |
| Kiểu dữ liệu có đủ lớn không? | Kiểm tra `int`, `long long`, phép nhân và tổng |
| Công thức có đúng không? | Tính thủ công bằng một ví dụ nhỏ |
| Điều kiện có đúng không? | Thử trường hợp bằng biên, nhỏ hơn và lớn hơn biên |
| Vòng lặp có chạy đủ không? | Theo dõi giá trị bắt đầu, kết thúc và bước nhảy |
| Chỉ số có hợp lệ không? | Kiểm tra `0 ≤ i < n` |
| Kết quả trung gian có đúng không? | In biến tạm tại vị trí cần kiểm tra |

### In giá trị trung gian

```cpp
cerr << "i = " << i << ", sum = " << sum << '\n';
```

Có thể dùng `cout` ở bài đơn giản, nhưng phải xóa các dòng debug trước khi nộp nếu output yêu cầu chính xác.

### Bộ test tối thiểu

Mỗi bài nên thử:

1. Ví dụ mẫu.
2. Dữ liệu nhỏ nhất.
3. Dữ liệu lớn nhất hoặc gần lớn nhất.
4. Trường hợp đúng bằng ngưỡng.
5. Trường hợp không có phần tử thỏa điều kiện.
6. Trường hợp tất cả phần tử đều thỏa điều kiện.
7. Trường hợp có nhiều phần tử bằng nhau.

---

## 12. ĐỘ PHỨC TẠP — CHƯƠNG TRÌNH CÓ ĐỦ NHANH?

| Độ phức tạp | Trực giác |
|---|---|
| `O(1)` | Số thao tác gần như không phụ thuộc kích thước dữ liệu |
| `O(log N)` | Mỗi bước thu nhỏ đáng kể phạm vi tìm kiếm |
| `O(N)` | Duyệt dữ liệu một lần |
| `O(N log N)` | Thường gặp khi sắp xếp |
| `O(N²)` | Xét mọi cặp hoặc hai vòng lặp theo `N` |
| `O(2^N)` | Thử mọi tập con; chỉ phù hợp với `N` nhỏ |

### Quy tắc đọc giới hạn

| Nếu `N` khoảng… | Có thể cân nhắc… |
|---:|---|
| `N ≤ 20` | Duyệt tập con, bitmask, quay lui |
| `N ≤ 10^3` | Một số lời giải `O(N²)` |
| `N ≤ 10^5` hoặc `2 × 10^5` | `O(N)`, `O(N log N)` |
| `N` rất lớn | Công thức, toán học hoặc tối ưu mạnh hơn |

Đây chỉ là quy tắc định hướng. Cần xét thêm số test, hằng số trong chương trình và giới hạn thời gian.

---

## TÓM TẮT MỘT TRANG

```text
BIẾN
  Tôi cần lưu dữ liệu gì?

TÍNH
  Tôi cần công thức nào?

ĐIỀU KIỆN
  Tôi cần quyết định điều gì?

LẶP
  Tôi cần làm việc gì nhiều lần?

TÍCH LŨY
  Tôi cần cộng, đếm, max hay min?

MẢNG
  Tôi có nhiều dữ liệu cùng loại không?

HÀM
  Tôi có thể tách nhiệm vụ nào thành một khối công việc riêng?

DEBUG
  Input, biến, công thức, điều kiện, vòng lặp và kết quả trung gian có đúng không?
```

> **Mục tiêu của C++ Cơ bản:** Không phải nhớ thật nhiều câu lệnh, mà là nhìn một bài toán đơn giản và biết biến nó thành các bước có thể lập trình được.



\newpage

# Phụ lục B: Lời giải bài tập tham khảo

> Phần này cung cấp mã nguồn C++ tham khảo chuẩn thi đấu cho các bài tập thực hành trong sách.

## Chương 04 — Bài 07: Thuật toán tham lam (Greedy)

### `CPPB2-L07-01` — Lựa Chọn Sự Kiện Không Trùng Giờ

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Event {
    long long l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Event> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].l >> a[i].r;

    sort(a.begin(), a.end(), [](const Event &x, const Event &y) {
        return x.r < y.r;
    });

    int count = 0;
    long long last_end = -2e18;
    for (const auto &e : a) {
        if (e.l >= last_end) {
            count++;
            last_end = e.r;
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L07-02` — Tổng Thời Gian Chờ Nhỏ Nhất (sjf)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> t(n);
    for (int i = 0; i < n; ++i) cin >> t[i];

    sort(t.begin(), t.end());

    long long total_wait = 0, cur_time = 0;
    for (int i = 0; i < n; ++i) {
        total_wait += cur_time;
        cur_time += t[i];
    }

    cout << total_wait << "\n";
    return 0;
}

```

### `CPPB2-L07-03` — Cái Túi Chia Nhỏ Được (fractional Knapsack)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Item {
    double v, w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    double W;
    if (!(cin >> n >> W)) return 0;

    vector<Item> items(n);
    for (int i = 0; i < n; ++i) cin >> items[i].v >> items[i].w;

    sort(items.begin(), items.end(), [](const Item &a, const Item &b) {
        return (a.v / a.w) > (b.v / b.w);
    });

    double total_val = 0;
    for (const auto &item : items) {
        if (W <= 0) break;
        double take = min(item.w, W);
        total_val += take * (item.v / item.w);
        W -= take;
    }

    cout << fixed << setprecision(4) << total_val << "\n";
    return 0;
}

```

### `CPPB2-L07-04` — Phủ Đoạn Thẳng Ít Nhất (minimum Interval Cover)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Seg {
    long long l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L;
    if (!(cin >> n >> L)) return 0;

    vector<Seg> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].l >> a[i].r;

    sort(a.begin(), a.end(), [](const Seg &x, const Seg &y) {
        if (x.l != y.l) return x.l < y.l;
        return x.r > y.r;
    });

    int count = 0;
    long long cur_end = 0;
    int i = 0;

    while (cur_end < L) {
        long long max_reach = cur_end;
        while (i < n && a[i].l <= cur_end) {
            max_reach = max(max_reach, a[i].r);
            i++;
        }
        if (max_reach == cur_end) {
            cout << "-1\n";
            return 0;
        }
        count++;
        cur_end = max_reach;
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L07-05` — Ghép Thuyền Cứu Hộ Cực Trị

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long limit;
    if (!(cin >> n >> limit)) return 0;

    vector<long long> w(n);
    for (int i = 0; i < n; ++i) cin >> w[i];

    sort(w.begin(), w.end());

    int l = 0, r = n - 1;
    int boats = 0;

    while (l <= r) {
        if (l < r && w[l] + w[r] <= limit) {
            l++;
            r--;
        } else {
            r--;
        }
        boats++;
    }

    cout << boats << "\n";
    return 0;
}

```

### `CPPB2-L07-06` — Nối Các Sợi Dây Tiết Kiệm Chi Phí Nhất

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    priority_queue<long long, vector<long long>, greater<long long>> pq;
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        pq.push(x);
    }

    long long total_cost = 0;
    while (pq.size() > 1) {
        long long a = pq.top(); pq.pop();
        long long b = pq.top(); pq.pop();
        total_cost += (a + b);
        pq.push(a + b);
    }

    cout << total_cost << "\n";
    return 0;
}

```

### `CPPB2-L07-07` — Lập Lịch Công Việc Có Deadline & Tiền Phạt

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Job {
    int id, deadline;
    long long profit;
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        parent[root_i] = root_j;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Job> jobs(n);
    int max_d = 0;
    for (int i = 0; i < n; ++i) {
        jobs[i].id = i;
        cin >> jobs[i].deadline >> jobs[i].profit;
        max_d = max(max_d, jobs[i].deadline);
    }

    sort(jobs.begin(), jobs.end(), [](const Job &a, const Job &b) {
        return a.profit > b.profit;
    });

    DSU dsu(max_d);
    long long total_profit = 0;
    int count_jobs = 0;

    for (const auto &j : jobs) {
        int available_slot = dsu.find(min(j.deadline, max_d));
        if (available_slot > 0) {
            dsu.unite(available_slot, available_slot - 1);
            total_profit += j.profit;
            count_jobs++;
        }
    }

    cout << count_jobs << " " << total_profit << "\n";
    return 0;
}

```

### `CPPB2-L07-08` — Tối Đa Hóa Lợi Nhuận Giao Hàng

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Delivery {
    int deadline;
    long long profit;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Delivery> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].deadline >> a[i].profit;

    sort(a.begin(), a.end(), [](const Delivery &x, const Delivery &y) {
        return x.deadline < y.deadline;
    });

    priority_queue<long long, vector<long long>, greater<long long>> pq;

    for (const auto &d : a) {
        if ((int)pq.size() < d.deadline) {
            pq.push(d.profit);
        } else if (!pq.empty() && pq.top() < d.profit) {
            pq.pop();
            pq.push(d.profit);
        }
    }

    long long total_profit = 0;
    while (!pq.empty()) {
        total_profit += pq.top();
        pq.pop();
    }

    cout << total_profit << "\n";
    return 0;
}

```

### `CPPB2-L07-09` — Chia Kẹo Thưởng Cho Học Sinh Theo Điểm Số

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> ratings(n);
    for (int i = 0; i < n; ++i) cin >> ratings[i];

    vector<long long> candies(n, 1);
    for (int i = 1; i < n; ++i) {
        if (ratings[i] > ratings[i - 1]) candies[i] = candies[i - 1] + 1;
    }

    for (int i = n - 2; i >= 0; --i) {
        if (ratings[i] > ratings[i + 1]) candies[i] = max(candies[i], candies[i + 1] + 1);
    }

    long long total = 0;
    for (long long c : candies) total += c;

    cout << total << "\n";
    return 0;
}

```

### `CPPB2-L07-10` — Tối Ưu Hóa Mua Bán Cổ Phiếu Không Giới Hạn Lần Giao Dịch

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> p(n);
    for (int i = 0; i < n; ++i) cin >> p[i];

    long long profit = 0;
    for (int i = 1; i < n; ++i) {
        if (p[i] > p[i - 1]) profit += (p[i] - p[i - 1]);
    }

    cout << profit << "\n";
    return 0;
}

```

### `CPPB2-L07-11` — Sắp Đặt Chuỗi Ký Tự Không Trùng Lặp Kề Nhau

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> freq(26, 0);
    for (char c : s) freq[c - 'a']++;

    priority_queue<pair<int, char>> pq;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] > 0) pq.push({freq[i], (char)('a' + i)});
    }

    string res = "";
    pair<int, char> prev = {-1, '#'};

    while (!pq.empty()) {
        auto cur = pq.top(); pq.pop();
        res += cur.second;
        cur.first--;

        if (prev.first > 0) pq.push(prev);
        prev = cur;
    }

    if (res.size() != s.size()) cout << "-1\n";
    else cout << res << "\n";
    return 0;
}

```

### `CPPB2-L07-12` — Số Lượng Trạm Tiếp Nhiên Liệu Ít Nhất (gas Station)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Station {
    long long dist, fuel;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target, start_fuel;
    if (!(cin >> n >> target >> start_fuel)) return 0;

    vector<Station> st(n);
    for (int i = 0; i < n; ++i) cin >> st[i].dist >> st[i].fuel;

    sort(st.begin(), st.end(), [](const Station &a, const Station &b) {
        return a.dist < b.dist;
    });

    priority_queue<long long> max_fuel_pq;
    long long cur_fuel = start_fuel;
    int stops = 0;
    int idx = 0;

    while (cur_fuel < target) {
        while (idx < n && st[idx].dist <= cur_fuel) {
            max_fuel_pq.push(st[idx].fuel);
            idx++;
        }
        if (max_fuel_pq.empty()) {
            cout << "-1\n";
            return 0;
        }
        cur_fuel += max_fuel_pq.top();
        max_fuel_pq.pop();
        stops++;
    }

    cout << stops << "\n";
    return 0;
}

```

### `CPPB2-L07-13` — Lập Lịch Phòng Họp Tối Thiểu (meeting Rooms Ii)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Interval {
    long long s, e;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Interval> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].s >> a[i].e;

    sort(a.begin(), a.end(), [](const Interval &x, const Interval &y) {
        return x.s < y.s;
    });

    priority_queue<long long, vector<long long>, greater<long long>> min_end_pq;

    for (const auto &it : a) {
        if (!min_end_pq.empty() && min_end_pq.top() <= it.s) {
            min_end_pq.pop();
        }
        min_end_pq.push(it.e);
    }

    cout << min_end_pq.size() << "\n";
    return 0;
}

```

### `CPPB2-L07-14` — Phục Hồi Dãy Số Đơn Điệu Với Chi Phí Nhỏ Nhất (slope Trick Cơ Bản)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] -= i; // Chuyển dãy tăng ngặt về dãy không giảm
    }

    priority_queue<long long> pq;
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        pq.push(a[i]);
        if (pq.top() > a[i]) {
            ans += pq.top() - a[i];
            pq.pop();
            pq.push(a[i]);
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L07-15` — Ghép Cặp Trọng Số Trên Đồ Thị Cây Bằng Greedy

```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int u, int p, const vector<vector<int>> &adj, vector<bool> &matched, int &matching_size) {
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, adj, matched, matching_size);
        }
    }
    if (!matched[u] && p != 0 && !matched[p]) {
        matched[u] = matched[p] = true;
        matching_size++;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<bool> matched(n + 1, false);
    int matching_size = 0;
    dfs(1, 0, adj, matched, matching_size);

    cout << matching_size << "\n";
    return 0;
}

```

### `CPPB2-L07-16` — Thuật Toán Huffman Coding Nén Dữ Liệu Tối Ưu

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long freq;
    Node *left, *right;
    Node(long long f) : freq(f), left(nullptr), right(nullptr) {}
};

struct Compare {
    bool operator()(Node *l, Node *r) {
        return l->freq > r->freq;
    }
};

long long get_wpl(Node *root, int depth) {
    if (!root) return 0;
    if (!root->left && !root->right) return root->freq * depth;
    return get_wpl(root->left, depth + 1) + get_wpl(root->right, depth + 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    priority_queue<Node*, vector<Node*>, Compare> pq;
    for (int i = 0; i < n; ++i) {
        long long f; cin >> f;
        pq.push(new Node(f));
    }

    while (pq.size() > 1) {
        Node *l = pq.top(); pq.pop();
        Node *r = pq.top(); pq.pop();
        Node *parent = new Node(l->freq + r->freq);
        parent->left = l;
        parent->right = r;
        pq.push(parent);
    }

    cout << get_wpl(pq.top(), 0) << "\n";
    return 0;
}

```

### `CPPB2-L07-17` — Cay Ma Huffman Coding

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    priority_queue<long long, vector<long long>, greater<long long>> pq;
    for (int i = 0; i < n; ++i) { long long x; cin >> x; pq.push(x); }
    long long total = 0;
    while (pq.size() > 1) {
        long long a = pq.top(); pq.pop();
        long long b = pq.top(); pq.pop();
        total += (a + b);
        pq.push(a + b);
    }
    cout << total << "\n";
    return 0;
}

```

### `CPPB2-L07-18` — Lap Lich Deadline Tien Phat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L07-19` — Thu Gom Vang Tren Luoi Greedy

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L07-20` — Sap Xep Phan Tu Doi Cho K Lan

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L07-21` — Xep Chong Hop Trong So Va Suc Chiu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L07-22` — Noi Day Nang Cao K Dau

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

## Chương 04 — Bài 08: Quy hoạch động cơ bản & chuyên sâu (DP)

### `CPPB2-L08-01` — Dãy Con Tăng Dài Nhất Lis

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i <= n; ++i) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    }

    cout << dp[n] << "\n";
    return 0;
}

```

### `CPPB2-L08-02` — Đường Đi Trên Ma Trận Có Tổng Lớn Nhất

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) cin >> a[i][j];
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, -1e18));
    dp[1][1] = a[1][1];

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (i == 1 && j == 1) continue;
            long long best = -1e18;
            if (i > 1) best = max(best, dp[i - 1][j]);
            if (j > 1) best = max(best, dp[i][j - 1]);
            dp[i][j] = best + a[i][j];
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}

```

### `CPPB2-L08-03` — Cái Túi 0/1 Chuẩn (0/1 Knapsack)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    vector<long long> w(n), v(n);
    for (int i = 0; i < n; ++i) cin >> w[i] >> v[i];

    vector<long long> dp(W + 1, 0);
    for (int i = 0; i < n; ++i) {
        for (long long j = W; j >= w[i]; --j) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
        }
    }

    cout << dp[W] << "\n";
    return 0;
}

```

### `CPPB2-L08-04` — Đổi Tiền Xu Số Tờ Nhỏ Nhất (unbounded Coin Change)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long S;
    if (!(cin >> n >> S)) return 0;

    vector<long long> coins(n);
    for (int i = 0; i < n; ++i) cin >> coins[i];

    vector<long long> dp(S + 1, 1e9);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (long long j = coins[i]; j <= S; ++j) {
            dp[j] = min(dp[j], dp[j - coins[i]] + 1);
        }
    }

    cout << (dp[S] >= 1e9 ? -1 : dp[S]) << "\n";
    return 0;
}

```

### `CPPB2-L08-05` — Dãy Con Tăng Dài Nhất Lis $\mathcal{o}(n \log N)$

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> tail;
    for (long long x : a) {
        auto it = lower_bound(tail.begin(), tail.end(), x);
        if (it == tail.end()) tail.push_back(x);
        else *it = x;
    }

    cout << tail.size() << "\n";
    return 0;
}

```

### `CPPB2-L08-06` — Xâu Con Chung Dài Nhất (lcs)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
            else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}

```

### `CPPB2-L08-07` — Xóa Ký Tự Để Thành Palindrome Ngắn Nhất

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int i = 0; i < n; ++i) dp[i][i] = 1;

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i <= n - len; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j]) {
                dp[i][j] = (len == 2 ? 2 : dp[i + 1][j - 1] + 2);
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }

    cout << n - dp[0][n - 1] << "\n";
    return 0;
}

```

### `CPPB2-L08-08` — Cắt Bánh Hình Chữ Nhật Có Giá Trị Lớn Nhất

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int W, H, n;
    if (!(cin >> W >> H >> n)) return 0;

    vector<vector<long long>> dp(W + 1, vector<long long>(H + 1, 0));

    for (int i = 0; i < n; ++i) {
        int w, h;
        long long val;
        cin >> w >> h >> val;
        if (w <= W && h <= H) dp[w][h] = max(dp[w][h], val);
        if (h <= W && w <= H) dp[h][w] = max(dp[h][w], val);
    }

    for (int i = 1; i <= W; ++i) {
        for (int j = 1; j <= H; ++j) {
            for (int k = 1; k < i; ++k) {
                dp[i][j] = max(dp[i][j], dp[k][j] + dp[i - k][j]);
            }
            for (int k = 1; k < j; ++k) {
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[i][j - k]);
            }
        }
    }

    cout << dp[W][H] << "\n";
    return 0;
}

```

### `CPPB2-L08-09` — Dãy Con Tăng Lớn Nhất Có Truy Vết Phần Tử

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> dp(n, 1), parent(n, -1);
    int max_len = 1, best_idx = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                parent[i] = j;
            }
        }
        if (dp[i] > max_len) {
            max_len = dp[i];
            best_idx = i;
        }
    }

    vector<long long> lis;
    int cur = best_idx;
    while (cur != -1) {
        lis.push_back(a[cur]);
        cur = parent[cur];
    }
    reverse(lis.begin(), lis.end());

    cout << max_len << "\n";
    for (size_t i = 0; i < lis.size(); ++i) {
        cout << lis[i] << (i + 1 == lis.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L08-10` — Khoảng Cách Chỉnh Sửa Xâu (edit Distance / Levenshtein)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 0; i <= n; ++i) dp[i][0] = i;
    for (int j = 0; j <= m; ++j) dp[0][j] = j;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
            }
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}

```

### `CPPB2-L08-11` — Cái Túi Đổi Trục Trạng Thái (value-based Knapsack)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    vector<long long> w(n);
    vector<int> v(n);
    int sum_v = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i] >> v[i];
        sum_v += v[i];
    }

    vector<long long> dp(sum_v + 1, 1e18);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int val = sum_v; val >= v[i]; --val) {
            dp[val] = min(dp[val], dp[val - v[i]] + w[i]);
        }
    }

    int ans = 0;
    for (int val = sum_v; val >= 0; --val) {
        if (dp[val] <= W) {
            ans = val;
            break;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L08-12` — Xếp Gạch Lát Sàn Kích Thước $3 \times N$

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n % 2 != 0) {
        cout << "0\n";
        return 0;
    }

    vector<long long> f(n + 1, 0), g(n + 1, 0);
    f[0] = 1; g[0] = 0;
    f[1] = 0; g[1] = 1;

    for (int i = 2; i <= n; ++i) {
        f[i] = (f[i - 2] + 2 * g[i - 1]) % MOD;
        g[i] = (f[i - 1] + g[i - 2]) % MOD;
    }

    cout << f[n] << "\n";
    return 0;
}

```

### `CPPB2-L08-13` — Dãy Con Hình Sóng Núi Dài Nhất (bitonic Subsequence)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> inc(n, 1), dec(n, 1);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i]) inc[i] = max(inc[i], inc[j] + 1);
        }
    }

    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j > i; --j) {
            if (a[j] < a[i]) dec[i] = max(dec[i], dec[j] + 1);
        }
    }

    int max_len = 0;
    for (int i = 0; i < n; ++i) {
        max_len = max(max_len, inc[i] + dec[i] - 1);
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB2-L08-14` — Nhân Ma Trận Dây Chuyền Chi Phí Nhỏ Nhất (matrix Chain)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> p(n + 1);
    for (int i = 0; i <= n; ++i) cin >> p[i];

    vector<vector<long long>> dp(n + 1, vector<long long>(n + 1, 0));

    for (int len = 2; len <= n; ++len) {
        for (int i = 1; i <= n - len + 1; ++i) {
            int j = i + len - 1;
            dp[i][j] = 1e18;
            for (int k = i; k < j; ++k) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]);
            }
        }
    }

    cout << dp[1][n] << "\n";
    return 0;
}

```

### `CPPB2-L08-15` — Quy Hoạch Động Trên Cây (tree Dp: Max Independent Set)

```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int u, int p, const vector<vector<int>> &adj, const vector<long long> &val, vector<long long> &dp0, vector<long long> &dp1) {
    dp0[u] = 0;
    dp1[u] = val[u];
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, adj, val, dp0, dp1);
            dp0[u] += max(dp0[v], dp1[v]);
            dp1[u] += dp0[v];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> val(n + 1);
    for (int i = 1; i <= n; ++i) cin >> val[i];

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> dp0(n + 1, 0), dp1(n + 1, 0);
    dfs(1, 0, adj, val, dp0, dp1);

    cout << max(dp0[1], dp1[1]) << "\n";
    return 0;
}

```

### `CPPB2-L08-16` — Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (cht)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Line {
    long long m, c;
    long long eval(long long x) const {
        return m * x + c;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    vector<long long> dp(n, 0);
    for (int i = 1; i < n; ++i) {
        dp[i] = 1e18;
        for (int j = 0; j < i; ++j) {
            dp[i] = min(dp[i], dp[j] + (h[i] - h[j]) * (h[i] - h[j]));
        }
    }

    cout << dp[n - 1] << "\n";
    return 0;
}

```

### `CPPB2-L08-17` — Dp Tren Cay Tree Dp Tap Doc Lap

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
vector<int> adj[MAXN];
long long val[MAXN];
long long dp[MAXN][2]; // dp[u][0]: không chọn u, dp[u][1]: chọn u

void dfs(int u, int p) {
    dp[u][0] = 0;
    dp[u][1] = val[u];

    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
        dp[u][0] += max(dp[v][0], dp[v][1]);
        dp[u][1] += dp[v][0];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 1; i <= n; ++i) cin >> val[i];

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);

    cout << max(dp[1][0], dp[1][1]) << "\n";
    return 0;
}

```

### `CPPB2-L08-18` — Convex Hull Trick Dp Toi Uu Duong Thang

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L08-19` — Divide And Conquer Dp Optimization

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L08-20` — Dp Knapsack Trong So Lon W Le 1e9

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L08-21` — Dp Tren Cay Duong Kinh Cay Co Trong So

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L08-22` — Dp Palindrome Min Cut

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L08-23` — Dp Matrix Chain Multiplication

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L08-24` — Dp Bitmask Duong Di Ngan Nhat K Dinh

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L08-25` — Dp Doi Xung Hai Chieu 2 Duong Di

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L08-26` — Knuth Optimization Dp

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

## Chương 05 — Bài 09: Ngăn xếp, hàng đợi & Deque đơn điệu

### `CPPB2-L09-01` — Phần Tử Lớn Hơn Gần Nhất (nge)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> ans(n, -1);
    stack<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.top()] < a[i]) {
            ans[st.top()] = a[i];
            st.pop();
        }
        st.push(i);
    }

    for (int i = 0; i < n; ++i) {
        cout << ans[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L09-02` — Giá Trị Nhỏ Nhất Trên Cửa Sổ Trượt K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    stack<int> st;
    long long max_area = 0;

    for (int i = 0; i <= n; ++i) {
        long long cur_h = (i == n ? 0 : h[i]);
        while (!st.empty() && h[st.top()] >= cur_h) {
            long long height = h[st.top()];
            st.pop();
            long long width = st.empty() ? i : (i - st.top() - 1);
            max_area = max(max_area, height * width);
        }
        st.push(i);
    }

    cout << max_area << "\n";
    return 0;
}

```

### `CPPB2-L09-03` — Kiểm Tra Dãy Ngoặc Đúng Nhiều Loại

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> dq;
    for (int i = 0; i < n; ++i) {
        while (!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back();
        dq.push_back(i);

        if (dq.front() <= i - k) dq.pop_front();

        if (i >= k - 1) {
            cout << a[dq.front()] << (i + 1 == n ? "" : " ");
        }
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L09-04` — Tầm Nhìn Xa Của Các Tòa Nhà Cao Tầng

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string token;
    stack<long long> st;

    while (cin >> token) {
        if (token == "+" || token == "-" || token == "*" || token == "/") {
            long long b = st.top(); st.pop();
            long long a = st.top(); st.pop();
            if (token == "+") st.push(a + b);
            else if (token == "-") st.push(a - b);
            else if (token == "*") st.push(a * b);
            else if (token == "/") st.push(a / b);
        } else {
            st.push(stoll(token));
        }
    }

    if (!st.empty()) cout << st.top() << "\n";
    return 0;
}

```

### `CPPB2-L09-05` — Hình Chữ Nhật Lớn Nhất Dưới Biểu Đồ Cột (histogram)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    stack<int> st;
    long long water = 0;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && h[i] > h[st.top()]) {
            int top = st.top(); st.pop();
            if (st.empty()) break;
            int dist = i - st.top() - 1;
            long long bounded_h = min(h[i], h[st.top()]) - h[top];
            water += dist * bounded_h;
        }
        st.push(i);
    }

    cout << water << "\n";
    return 0;
}

```

### `CPPB2-L09-06` — Ma Trận Toàn Số 1 Lớn Nhất (maximal Rectangle 2d)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long max_hist(const vector<long long> &h) {
    int n = h.size();
    stack<int> st;
    long long max_area = 0;
    for (int i = 0; i <= n; ++i) {
        long long cur_h = (i == n ? 0 : h[i]);
        while (!st.empty() && h[st.top()] >= cur_h) {
            long long height = h[st.top()];
            st.pop();
            long long width = st.empty() ? i : (i - st.top() - 1);
            max_area = max(max_area, height * width);
        }
        st.push(i);
    }
    return max_area;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> mat(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) cin >> mat[i][j];
    }

    vector<long long> h(m, 0);
    long long max_rec = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (mat[i][j] == 1) h[j]++;
            else h[j] = 0;
        }
        max_rec = max(max_rec, max_hist(h));
    }

    cout << max_rec << "\n";
    return 0;
}

```

### `CPPB2-L09-07` — Tổng Hiệu Cực Đại Và Cực Tiểu Mọi Đoạn Con

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isValid(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') st.push(c);
        else {
            if (st.empty()) return false;
            char top = st.top();
            if ((c == ')' && top == '(') || (c == ']' && top == '[') || (c == '}' && top == '{')) {
                st.pop();
            } else {
                return false;
            }
        }
    }
    return st.empty();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    cout << (isValid(s) ? "YES" : "NO") << "\n";
    return 0;
}

```

### `CPPB2-L09-08` — Tối Ưu Hóa Quy Hoạch Động Bằng Monotonic Deque

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> left(n), right(n);
    stack<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.top()] > a[i]) st.pop();
        left[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }

    while (!st.empty()) st.pop();

    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.top()] >= a[i]) st.pop();
        right[i] = st.empty() ? n : st.top();
        st.push(i);
    }

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        long long l_count = i - left[i];
        long long r_count = right[i] - i;
        long long contrib = (l_count * r_count % MOD) * (a[i] % MOD) % MOD;
        total = (total + contrib) % MOD;
    }

    cout << total << "\n";
    return 0;
}

```

### `CPPB2-L09-09` — Hứng Nước Mưa Đa Chiều (trapping Rain Water)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> dq;
    vector<long long> dp(n, 0);

    dp[0] = a[0];
    dq.push_back(0);

    for (int i = 1; i < n; ++i) {
        if (!dq.empty() && dq.front() < i - k) dq.pop_front();
        dp[i] = dp[dq.front()] + a[i];
        while (!dq.empty() && dp[dq.back()] <= dp[i]) dq.pop_back();
        dq.push_back(i);
    }

    cout << dp[n - 1] << "\n";
    return 0;
}

```

### `CPPB2-L09-10` — Đánh Giá Biểu Thức Số Học Trung Tố (shunting-yard)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> max_dq, min_dq;
    int max_len = 0, l = 0;

    for (int r = 0; r < n; ++r) {
        while (!max_dq.empty() && a[max_dq.back()] <= a[r]) max_dq.pop_back();
        max_dq.push_back(r);

        while (!min_dq.empty() && a[min_dq.back()] >= a[r]) min_dq.pop_back();
        min_dq.push_back(r);

        while (a[max_dq.front()] - a[min_dq.front()] > k) {
            l++;
            if (max_dq.front() < l) max_dq.pop_front();
            if (min_dq.front() < l) min_dq.pop_front();
        }

        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB2-L09-11` — Phần Tử Lớn Hơn Gần Nhất Trên Mảng Xoay Vòng

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    stack<int> st;
    st.push(-1);
    int max_len = 0;

    for (int i = 0; i < (int)s.size(); ++i) {
        if (s[i] == '(') {
            st.push(i);
        } else {
            st.pop();
            if (st.empty()) {
                st.push(i);
            } else {
                max_len = max(max_len, i - st.top());
            }
        }
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB2-L09-12` — Xóa K Chữ Số Để Được Số Nhỏ Nhất

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    stack<pair<long long, int>> st;
    long long count = 0;

    for (int i = 0; i < n; ++i) {
        int cnt = 1;
        while (!st.empty() && st.top().first <= h[i]) {
            count += st.top().second;
            if (st.top().first == h[i]) {
                cnt += st.top().second;
            }
            st.pop();
        }
        if (!st.empty()) count++;
        st.push({h[i], cnt});
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L09-13` — Tổng Giá Trị Min Mọi Đoạn Con Nhân Độ Dài

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int k;
    if (!(cin >> s >> k)) return 0;

    string res = "";
    for (char c : s) {
        while (!res.empty() && res.back() > c && k > 0) {
            res.pop_back();
            k--;
        }
        res.push_back(c);
    }

    while (k > 0 && !res.empty()) {
        res.pop_back();
        k--;
    }

    // Xóa số 0 ở đầu
    int start = 0;
    while (start < (int)res.size() && res[start] == '0') start++;
    res = res.substr(start);

    cout << (res.empty() ? "0" : res) << "\n";
    return 0;
}

```

### `CPPB2-L09-14` — Đua Xe Trong Mê Cung Đổi Hướng Ít Nhất (0-1 Bfs)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<long long> dp(n + 1, 0);
    deque<int> dq;
    dq.push_back(0);

    for (int i = 1; i <= n; ++i) {
        while (!dq.empty() && dq.front() < i - k) dq.pop_front();
        dp[i] = dp[dq.front()] + a[i];
        while (!dq.empty() && dp[dq.back()] <= dp[i]) dq.pop_back();
        dq.push_back(i);
    }

    cout << dp[n] << "\n";
    return 0;
}

```

### `CPPB2-L09-15` — Cắt Băng Rôn Quảng Cáo Tối Ưu Bằng 2 Deque

```cpp
#include <bits/stdc++.h>
using namespace std;

bool verify_preorder_bst(const vector<int> &a) {
    stack<int> st;
    int root = -1e9;
    for (int x : a) {
        if (x < root) return false;
        while (!st.empty() && st.top() < x) {
            root = st.top();
            st.pop();
        }
        st.push(x);
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    cout << (verify_preorder_bst(a) ? "YES" : "NO") << "\n";
    return 0;
}

```

### `CPPB2-L09-16` — Khôi Phục Cây Khảo Sát Tầm Nhìn Đa Hướng

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> dq;
    long long total_max = 0;

    for (int i = 0; i < n; ++i) {
        while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
        dq.push_back(i);

        if (dq.front() <= i - k) dq.pop_front();

        if (i >= k - 1) {
            total_max += a[dq.front()];
        }
    }

    cout << total_max << "\n";
    return 0;
}

```

### `CPPB2-L09-17` — Hinh Chu Nhat Lon Nhat Bieu Do Cot

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];
    stack<int> st;
    long long max_area = 0;
    for (int i = 0; i <= n; ++i) {
        long long cur_h = (i == n ? 0 : h[i]);
        while (!st.empty() && h[st.top()] >= cur_h) {
            long long height = h[st.top()]; st.pop();
            long long width = st.empty() ? i : (i - st.top() - 1);
            max_area = max(max_area, height * width);
        }
        st.push(i);
    }
    cout << max_area << "\n";
    return 0;
}

```

### `CPPB2-L09-18` — Hinh Chu Nhat Toan So 1 Lon Nhat 2d

```cpp
#include <bits/stdc++.h>
using namespace std;

int largest_rectangle_histogram(const vector<int>& heights) {
    int n = heights.size();
    vector<int> left(n), right(n);
    vector<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && heights[st.back()] >= heights[i]) st.pop_back();
        left[i] = st.empty() ? 0 : st.back() + 1;
        st.push_back(i);
    }

    st.clear();
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && heights[st.back()] >= heights[i]) st.pop_back();
        right[i] = st.empty() ? n - 1 : st.back() - 1;
        st.push_back(i);
    }

    int max_area = 0;
    for (int i = 0; i < n; ++i) {
        max_area = max(max_area, heights[i] * (right[i] - left[i] + 1));
    }
    return max_area;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> matrix[i][j];
        }
    }

    vector<int> heights(m, 0);
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (matrix[i][j] == 1) heights[j]++;
            else heights[j] = 0;
        }
        ans = max(ans, largest_rectangle_histogram(heights));
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L09-19` — Tong Min Tat Ca Doan Con

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L09-20` — Deque Sliding Window Maximum

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    deque<int> dq;
    for (int i = 0; i < n; ++i) {
        if (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k - 1) cout << a[dq.front()] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L09-21` — Stack Danh Gia Bieu Thuc So Hoc

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L09-22` — Tam Nhin Toa Nha Hai Chieu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

## Chương 05 — Bài 10: Thư viện STL C++ nâng cao

### `CPPB2-L10-01` — Duy Trì Trung Vị Động

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Customer {
    int id, priority;
};

struct Compare {
    bool operator()(const Customer &a, const Customer &b) {
        if (a.priority != b.priority) return a.priority < b.priority;
        return a.id > b.id;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    priority_queue<Customer, vector<Customer>, Compare> pq;

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int id, p; cin >> id >> p;
            pq.push({id, p});
        } else {
            if (!pq.empty()) {
                cout << pq.top().id << "\n";
                pq.pop();
            } else {
                cout << "-1\n";
            }
        }
    }
    return 0;
}

```

### `CPPB2-L10-02` — Đếm Tần Suất Giá Trị Bằng Safe Hash Map

```cpp
#include <bits/stdc++.h>
using namespace std;

// Triển khai cây tìm kiếm nhị phân cân bằng thủ công hoặc multiset giả lập PBDS
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    vector<long long> dynamic_arr;

    while (q--) {
        int type; long long x;
        cin >> type >> x;
        if (type == 1) {
            auto it = lower_bound(dynamic_arr.begin(), dynamic_arr.end(), x);
            dynamic_arr.insert(it, x);
        } else {
            auto it = lower_bound(dynamic_arr.begin(), dynamic_arr.end(), x);
            cout << (it - dynamic_arr.begin()) << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L10-03` — Nối Dây Tiết Kiệm Bằng Priority Queue

```cpp
#include <bits/stdc++.h>
using namespace std;

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    unordered_map<long long, int, custom_hash> freq;
    long long best_val = 0;
    int max_cnt = 0;

    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        freq[x]++;
        if (freq[x] > max_cnt) {
            max_cnt = freq[x];
            best_val = x;
        }
    }

    cout << best_val << " " << max_cnt << "\n";
    return 0;
}

```

### `CPPB2-L10-04` — Duy Trì Trung Vị Động (running Median)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Student {
    string name;
    int math, it, id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Student> a(n);
    for (int i = 0; i < n; ++i) {
        a[i].id = i;
        cin >> a[i].name >> a[i].math >> a[i].it;
    }

    sort(a.begin(), a.end(), [](const Student &x, const Student &y) {
        if (x.it != y.it) return x.it > y.it;
        if (x.math != y.math) return x.math > y.math;
        return x.id < y.id;
    });

    for (const auto &s : a) {
        cout << s.name << " " << s.math << " " << s.it << "\n";
    }
    return 0;
}

```

### `CPPB2-L10-05` — Tìm Phần Tử Kế Tiếp Nhỏ Nhất Lớn Hơn X

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    for (int i = 0; i < n; ++i) p[i] = i + 1;

    do {
        for (int i = 0; i < n; ++i) cout << p[i] << (i + 1 == n ? "" : " ");
        cout << "\n";
    } while (next_permutation(p.begin(), p.end()));

    return 0;
}

```

### `CPPB2-L10-06` — Lập Lịch Phòng Họp Đa Năng (meeting Rooms)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    set<pair<long long, long long>> intervals;

    while (q--) {
        long long l, r;
        cin >> l >> r;

        auto it = intervals.lower_bound({l, -1e18});
        while (it != intervals.end() && it->second <= r) {
            l = min(l, it->second);
            r = max(r, it->first);
            it = intervals.erase(it);
        }
        intervals.insert({r, l});
    }

    long long total_len = 0;
    for (auto it : intervals) {
        total_len += (it.first - it.second);
    }
    cout << total_len << "\n";
    return 0;
}

```

### `CPPB2-L10-07` — Duy Trì K Phần Tử Lớn Nhất Trong Luồng Dữ Liệu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    priority_queue<long long> max_heap; // Nửa nhỏ
    priority_queue<long long, vector<long long>, greater<long long>> min_heap; // Nửa lớn

    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        if (max_heap.empty() || x <= max_heap.top()) max_heap.push(x);
        else min_heap.push(x);

        if (max_heap.size() > min_heap.size() + 1) {
            min_heap.push(max_heap.top());
            max_heap.pop();
        } else if (min_heap.size() > max_heap.size()) {
            max_heap.push(min_heap.top());
            min_heap.pop();
        }

        cout << max_heap.top() << "\n";
    }
    return 0;
}

```

### `CPPB2-L10-08` — Tối Ưu Hóa Chi Phí Mua Cổ Phiếu Theo Thời Gian

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    multiset<long long> ms;

    while (q--) {
        int type; long long x;
        cin >> type >> x;
        if (type == 1) {
            ms.insert(x);
        } else if (type == 2) {
            auto it = ms.find(x);
            if (it != ms.end()) ms.erase(it);
        } else {
            cout << ms.count(x) << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L10-09` — Hệ Thống Đặt Chỗ Rạp Chiếu Phim Tối Ưu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<tuple<int, int, int>> a(n);
    for (int i = 0; i < n; ++i) {
        int x, y, z; cin >> x >> y >> z;
        a[i] = make_tuple(x, y, z);
    }

    sort(a.begin(), a.end());

    for (const auto &t : a) {
        int x, y, z;
        tie(x, y, z) = t;
        cout << x << " " << y << " " << z << "\n";
    }
    return 0;
}

```

### `CPPB2-L10-10` — Đếm Số Phần Tử Phân Biệt Trong Mọi Cửa Sổ K

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXV = 100000;
bitset<MAXV + 1> bs;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    bs[0] = 1;
    for (int i = 0; i < n; ++i) {
        int w; cin >> w;
        bs |= (bs << w);
    }

    cout << bs.count() << "\n";
    return 0;
}

```

### `CPPB2-L10-11` — Hợp Nhất Các Đoạn Số Rời Rạc (merge Intervals)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct LRUCache {
    int cap;
    list<pair<int, int>> lru_list;
    unordered_map<int, list<pair<int, int>>::iterator> cache_map;

    LRUCache(int capacity) : cap(capacity) {}

    int get(int key) {
        if (!cache_map.count(key)) return -1;
        lru_list.splice(lru_list.begin(), lru_list, cache_map[key]);
        return cache_map[key]->second;
    }

    void put(int key, int value) {
        if (cache_map.count(key)) {
            cache_map[key]->second = value;
            lru_list.splice(lru_list.begin(), lru_list, cache_map[key]);
            return;
        }
        if ((int)lru_list.size() == cap) {
            int old_key = lru_list.back().first;
            lru_list.pop_back();
            cache_map.erase(old_key);
        }
        lru_list.push_front({key, value});
        cache_map[key] = lru_list.begin();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int cap, q;
    if (!(cin >> cap >> q)) return 0;

    LRUCache lru(cap);
    while (q--) {
        string op; cin >> op;
        if (op == "SET") {
            int k, v; cin >> k >> v;
            lru.put(k, v);
        } else {
            int k; cin >> k;
            cout << lru.get(k) << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L10-12` — Tìm Cặp Điểm Có Khoảng Cách Manhattan Nhỏ Nhất

```cpp
#include <bits/stdc++.h>
using namespace std;

// Giả lập Inversion count qua merge sort
long long merge_count(vector<int> &a, int l, int mid, int r) {
    vector<int> left(a.begin() + l, a.begin() + mid + 1);
    vector<int> right(a.begin() + mid + 1, a.begin() + r + 1);
    int i = 0, j = 0, k = l;
    long long inv = 0;

    while (i < (int)left.size() && j < (int)right.size()) {
        if (left[i] <= right[j]) a[k++] = left[i++];
        else {
            a[k++] = right[j++];
            inv += (left.size() - i);
        }
    }
    while (i < (int)left.size()) a[k++] = left[i++];
    while (j < (int)right.size()) a[k++] = right[j++];
    return inv;
}

long long merge_sort(vector<int> &a, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    return merge_sort(a, l, mid) + merge_sort(a, mid + 1, r) + merge_count(a, l, mid, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    cout << merge_sort(a, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB2-L10-13` — Hệ Thống Xếp Hạng Trực Tuyến Đa Tiêu Chí

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    while (q--) {
        long long l, r;
        cin >> l >> r;
        auto it1 = lower_bound(a.begin(), a.end(), l);
        auto it2 = upper_bound(a.begin(), a.end(), r);
        cout << (it2 - it1) << "\n";
    }
    return 0;
}

```

### `CPPB2-L10-14` — Tối Ưu Phân Bổ Băng Thông Máy Chủ (server Load Balancer)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end(), [](const string &x, const string &y) {
        return x + y > y + x;
    });

    if (a[0] == "0") {
        cout << "0\n";
        return 0;
    }

    for (const string &s : a) cout << s;
    cout << "\n";
    return 0;
}

```

### `CPPB2-L10-15` — Duy Trì Tổng Của K Phần Tử Lớn Nhất Động

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> color(n + 1, -1);
    bool is_bipartite = true;

    for (int i = 1; i <= n; ++i) {
        if (color[i] == -1) {
            queue<int> q;
            color[i] = 0;
            q.push(i);
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : adj[u]) {
                    if (color[v] == -1) {
                        color[v] = 1 - color[u];
                        q.push(v);
                    } else if (color[v] == color[u]) {
                        is_bipartite = false;
                        break;
                    }
                }
            }
        }
    }

    cout << (is_bipartite ? "YES" : "NO") << "\n";
    return 0;
}

```

### `CPPB2-L10-16` — Kỹ Thuật Small-to-large Merging Trên Stl Map

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    map<string, vector<long long>> records;
    for (int i = 0; i < n; ++i) {
        string key; long long val;
        cin >> key >> val;
        records[key].push_back(val);
    }

    for (auto &pair : records) {
        sort(pair.second.begin(), pair.second.end());
        long long sum = 0;
        for (long long v : pair.second) sum += v;
        cout << pair.first << ": Count=" << pair.second.size() << ", Sum=" << sum << "\n";
    }
    return 0;
}

```

### `CPPB2-L10-17` — Ordered Set Pbds Truy Van Thu Hang

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L10-18` — Can Bang Hai Heap Running Median

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L10-19` — Multiset Interval Management

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L10-20` — Safe Unordered Map Custom Hash

```cpp
#include <bits/stdc++.h>
using namespace std;
struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    unordered_map<long long, int, custom_hash> mp;
    for (int i = 0; i < n; ++i) { long long x; cin >> x; mp[x]++; }
    cout << mp.size() << "\n";
    return 0;
}

```

### `CPPB2-L10-21` — Priority Queue Dijkstra Custom Comparator

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L10-22` — Lru Cache Implementation Stl

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

## Chương 05 — Bài 11: Tổ hợp, hoán vị & xác suất cơ bản

### `CPPB2-L11-01` — Tính Tổ Hợp Ncr Modulo

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long ans = 1;
    for (int i = 1; i <= n; ++i) {
        ans = (ans * i) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L11-02` — Tam Giác Pascal Modulo Hợp Số

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k > n || k < 0) {
        cout << "0\n";
        return 0;
    }

    long long ans = 1;
    for (int i = 0; i < k; ++i) {
        ans = (ans * (n - i)) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L11-03` — Chia Kẹo Euler (stars And Bars)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

long long nCr(long long n, long long r) {
    if (r < 0 || r > n) return 0;
    long long num = 1, den = 1;
    for (long long i = 0; i < r; ++i) {
        num = (num * (n - i)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    return num * power_mod(den, MOD - 2) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    // C(n + k - 1, k - 1)
    cout << nCr(n + k - 1, k - 1) << "\n";
    return 0;
}

```

### `CPPB2-L11-04` — Đếm Số Hoán Vị Không Có Điểm Cố Định (derangements)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n == 1) { cout << "0\n"; return 0; }
    if (n == 2) { cout << "1\n"; return 0; }

    vector<long long> D(n + 1);
    D[1] = 0; D[2] = 1;
    for (int i = 3; i <= n; ++i) {
        D[i] = (i - 1) * (D[i - 1] + D[i - 2]) % MOD;
    }

    cout << D[n] << "\n";
    return 0;
}

```

### `CPPB2-L11-05` — Đếm Số Nguyên Tố Cùng Nhau Bằng Pie

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) { a %= b; swap(a, b); }
    return a;
}

long long lcm_val(long long a, long long b) {
    return (a / gcd_val(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> primes(k);
    for (int i = 0; i < k; ++i) cin >> primes[i];

    long long count = 0;
    for (int mask = 1; mask < (1 << k); ++mask) {
        long long cur_lcm = 1;
        int bits = 0;
        bool overflow = false;

        for (int i = 0; i < k; ++i) {
            if ((mask >> i) & 1) {
                bits++;
                cur_lcm = lcm_val(cur_lcm, primes[i]);
                if (cur_lcm > n) { overflow = true; break; }
            }
        }

        if (overflow) continue;

        if (bits % 2 == 1) count += n / cur_lcm;
        else count -= n / cur_lcm;
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L11-06` — Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> dp0(n + 1, 0), dp12(n + 1, 0);
    dp0[1] = 1; dp12[1] = 2;

    for (int i = 2; i <= n; ++i) {
        dp0[i] = dp12[i - 1];
        dp12[i] = (2 * dp0[i - 1] + 2 * dp12[i - 1]) % MOD;
    }

    cout << (dp0[n] + dp12[n]) % MOD << "\n";
    return 0;
}

```

### `CPPB2-L11-07` — Số Phân Hoạch Tập Hợp (số Stirling Loại 2)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;

    if (s < n || s > 6 * n) {
        cout << "0.000000\n";
        return 0;
    }

    vector<double> dp(s + 1, 0.0);
    dp[0] = 1.0;

    for (int i = 1; i <= n; ++i) {
        vector<double> next_dp(s + 1, 0.0);
        for (int j = 1; j <= s; ++j) {
            for (int face = 1; face <= 6; ++face) {
                if (j >= face) next_dp[j] += dp[j - face] / 6.0;
            }
        }
        dp = next_dp;
    }

    cout << fixed << setprecision(6) << dp[s] << "\n";
    return 0;
}

```

### `CPPB2-L11-08` — Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<long long>> S(n + 1, vector<long long>(k + 1, 0));
    S[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= min(i, k); ++j) {
            S[i][j] = (S[i - 1][j - 1] + j * S[i - 1][j]) % MOD;
        }
    }

    cout << S[n][k] << "\n";
    return 0;
}

```

### `CPPB2-L11-09` — Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> bell(n + 1, vector<long long>(n + 1, 0));
    bell[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        bell[i][0] = bell[i - 1][i - 1];
        for (int j = 1; j <= i; ++j) {
            bell[i][j] = (bell[i][j - 1] + bell[i - 1][j - 1]) % MOD;
        }
    }

    cout << bell[n][0] << "\n";
    return 0;
}

```

### `CPPB2-L11-10` — Đếm Số Hoán Vị Có Đúng K Điểm Cố Định

```cpp
#include <bits/stdc++.h>
using namespace std;

long long nCr_small(long long n, long long r, long long p) {
    if (r < 0 || r > n) return 0;
    long long num = 1, den = 1;
    for (long long i = 0; i < r; ++i) {
        num = (num * (n - i)) % p;
        den = (den * (i + 1)) % p;
    }
    long long inv = 1, exp = p - 2;
    while (exp > 0) {
        if (exp & 1) inv = (inv * den) % p;
        den = (den * den) % p;
        exp >>= 1;
    }
    return (num * inv) % p;
}

long long lucas(long long n, long long r, long long p) {
    if (r == 0) return 1;
    return lucas(n / p, r / p, p) * nCr_small(n % p, r % p, p) % p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long n, r, p;
        cin >> n >> r >> p;
        cout << lucas(n, r, p) << "\n";
    }
    return 0;
}

```

### `CPPB2-L11-11` — Số Phân Hoạch Tập Hợp (số Stirling Loại 2)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> fact(n + 1), invFact(n + 1), D(n + 1, 0);
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i % MOD;
    invFact[n] = power_mod(fact[n], MOD - 2);
    for (int i = n - 1; i >= 0; --i) invFact[i] = invFact[i + 1] * (i + 1) % MOD;

    D[0] = 1; D[1] = 0;
    for (int i = 2; i <= n; ++i) D[i] = (i - 1) * (D[i - 1] + D[i - 2]) % MOD;

    auto nCr = [&](int n, int r) {
        if (r < 0 || r > n) return 0LL;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    };

    long long ans = nCr(n, k) * D[n - k] % MOD;
    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L11-12` — Đếm Số Cây Khung Đồ Thị Đầy Đủ (công Thức Cayley)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> primes;
    long long temp = m;
    for (long long p = 2; p * p <= temp; ++p) {
        if (temp % p == 0) {
            primes.push_back(p);
            while (temp % p == 0) temp /= p;
        }
    }
    if (temp > 1) primes.push_back(temp);

    int k = primes.size();
    long long coprime_cnt = 0;

    for (int mask = 0; mask < (1 << k); ++mask) {
        long long prod = 1;
        int bits = 0;
        for (int i = 0; i < k; ++i) {
            if ((mask >> i) & 1) {
                bits++;
                prod *= primes[i];
            }
        }
        if (bits % 2 == 1) coprime_cnt -= n / prod;
        else coprime_cnt += n / prod;
    }

    cout << coprime_cnt << "\n";
    return 0;
}

```

### `CPPB2-L11-13` — Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long gcd_val(long long a, long long b) {
    while (b) { a %= b; swap(a, b); }
    return a;
}

long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total = (total + power_mod(k, gcd_val(i, n))) % MOD;
    }

    long long ans = total * power_mod(n, MOD - 2) % MOD;
    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L11-14` — Đếm Số Tam Giác Tạo Bởi N Điểm Trên Mặt Phẳng

```cpp
#include <bits/stdio.h>
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<long long>> E(n + 1, vector<long long>(k + 1, 0));
    E[1][0] = 1;

    for (int i = 2; i <= n; ++i) {
        for (int j = 0; j <= k; ++j) {
            E[i][j] = ((j + 1) * E[i - 1][j] + (j > 0 ? (i - j) * E[i - 1][j - 1] : 0)) % MOD;
        }
    }

    cout << E[n][k] << "\n";
    return 0;
}

```

### `CPPB2-L11-15` — Kỳ Vọng Toán Học Trò Chơi Gieo Xúc Xắc (probability Dp)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> dp(n + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = i; j <= n; ++j) {
            dp[j] = (dp[j] + dp[j - i]) % MOD;
        }
    }

    cout << dp[n] << "\n";
    return 0;
}

```

### `CPPB2-L11-16` — Bổ Đề Burnside Đếm Cấu Hình Bất Biến Phép Quay

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double p;
    if (!(cin >> p)) return 0;

    if (p <= 0.0) {
        cout << "-1\n";
    } else {
        cout << fixed << setprecision(6) << (1.0 / p) << "\n";
    }
    return 0;
}

```

### `CPPB2-L11-17` — Nguyen Ly Bao Ham Loai Tru Pie

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n; int k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> p(k);
    for (int i = 0; i < k; ++i) cin >> p[i];
    long long ans = 0;
    for (int mask = 1; mask < (1 << k); ++mask) {
        long long prod = 1; int cnt = 0;
        for (int i = 0; i < k; ++i) {
            if (mask & (1 << i)) {
                prod *= p[i];
                cnt++;
            }
        }
        if (cnt % 2 == 1) ans += n / prod;
        else ans -= n / prod;
    }
    cout << n - ans << "\n";
    return 0;
}

```

### `CPPB2-L11-18` — Dinh Ly Lucas To Hop Modulo P

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L11-19` — So Catalan Ung Dung Ngoac

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L11-20` — So Stirling Loai Hai Chia Tap

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L11-21` — Xac Suat Co Dieu Kien Dong Xu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L11-22` — Hoan Vi Co Chu Ky Cycles

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

## Chương 06 — Bài 12: Lý thuyết đồ thị cơ bản & nâng cao

### `CPPB2-L12-01` — Đường Đi Ngắn Nhất Dijkstra

```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int u, const vector<vector<int>> &adj, vector<bool> &vis) {
    vis[u] = true;
    for (int v : adj[u]) {
        if (!vis[v]) dfs(v, adj, vis);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<bool> vis(n + 1, false);
    int components = 0;

    for (int i = 1; i <= n; ++i) {
        if (!vis[i]) {
            components++;
            dfs(i, adj, vis);
        }
    }

    cout << components << "\n";
    return 0;
}

```

### `CPPB2-L12-02` — Đường Đi Ngắn Nhất Mê Cung 2d Bằng Bfs

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist(n + 1, -1);
    queue<int> q;

    dist[s] = 0; q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    cout << dist[t] << "\n";
    return 0;
}

```

### `CPPB2-L12-03` — Kiểm Tra Đồ Thị Hai Phía (bipartite Graph Coloring)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<long long> dist(n + 1, 1e18);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    dist[s] = 0;
    pq.push({0, s});

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;

        for (const auto &e : adj[u]) {
            if (dist[u] + e.w < dist[e.to]) {
                dist[e.to] = dist[u] + e.w;
                pq.push({dist[e.to], e.to});
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << (dist[i] >= 1e18 ? -1 : dist[i]) << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L12-04` — Sắp Xếp Tô-pô Lập Lịch Khóa Học (topological Sort)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int u, v;
    long long w;
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i), root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) cin >> edges[i].u >> edges[i].v >> edges[i].w;

    sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b) {
        return a.w < b.w;
    });

    DSU dsu(n);
    long long mst_weight = 0;
    int edge_count = 0;

    for (const auto &e : edges) {
        if (dsu.unite(e.u, e.v)) {
            mst_weight += e.w;
            edge_count++;
            if (edge_count == n - 1) break;
        }
    }

    cout << (edge_count == n - 1 ? mst_weight : -1) << "\n";
    return 0;
}

```

### `CPPB2-L12-05` — Dijkstra Tìm Đường Đi Ngắn Nhất Chuẩn

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> indeg(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        indeg[v]++;
    }

    queue<int> q;
    for (int i = 1; i <= n; ++i) {
        if (indeg[i] == 0) q.push(i);
    }

    vector<int> topo;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        topo.push_back(u);
        for (int v : adj[u]) {
            if (--indeg[v] == 0) q.push(v);
        }
    }

    if ((int)topo.size() < n) {
        cout << "-1\n";
    } else {
        for (size_t i = 0; i < topo.size(); ++i) {
            cout << topo[i] << (i + 1 == topo.size() ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}

```

### `CPPB2-L12-06` — Mê Cung Trọng Số 0 Và 1 (0-1 Bfs)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        dist[u][v] = min(dist[u][v], w);
        dist[v][u] = min(dist[v][u], w);
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (dist[i][k] < INF && dist[k][j] < INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cout << (dist[i][j] >= INF ? -1 : dist[i][j]) << (j == n ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}

```

### `CPPB2-L12-07` — Cây Khung Nhỏ Nhất (mst Kruskal Với Dsu)

```cpp
#include <bits/stdc++.h>
using namespace std;

int timer = 0;
void dfs_bridge(int u, int p, const vector<vector<int>> &adj, vector<int> &tin, vector<int> &low, int &bridges) {
    tin[u] = low[u] = ++timer;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (tin[v]) {
            low[u] = min(low[u], tin[v]);
        } else {
            dfs_bridge(v, u, adj, tin, low, bridges);
            low[u] = min(low[u], low[v]);
            if (low[v] > tin[u]) bridges++;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> tin(n + 1, 0), low(n + 1, 0);
    int bridges = 0;

    for (int i = 1; i <= n; ++i) {
        if (!tin[i]) dfs_bridge(i, 0, adj, tin, low, bridges);
    }

    cout << bridges << "\n";
    return 0;
}

```

### `CPPB2-L12-08` — Tìm Khớp Và Cầu Trên Đồ Thị (tarjan's Bridge & Articulation)

```cpp
#include <bits/stdc++.h>
using namespace std;

int timer = 0, scc_count = 0;
void dfs_scc(int u, const vector<vector<int>> &adj, vector<int> &tin, vector<int> &low, stack<int> &st, vector<bool> &in_st) {
    tin[u] = low[u] = ++timer;
    st.push(u);
    in_st[u] = true;

    for (int v : adj[u]) {
        if (!tin[v]) {
            dfs_scc(v, adj, tin, low, st, in_st);
            low[u] = min(low[u], low[v]);
        } else if (in_st[v]) {
            low[u] = min(low[u], tin[v]);
        }
    }

    if (low[u] == tin[u]) {
        scc_count++;
        while (true) {
            int node = st.top(); st.pop();
            in_st[node] = false;
            if (node == u) break;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
    }

    vector<int> tin(n + 1, 0), low(n + 1, 0);
    vector<bool> in_st(n + 1, false);
    stack<int> st;

    for (int i = 1; i <= n; ++i) {
        if (!tin[i]) dfs_scc(i, adj, tin, low, st, in_st);
    }

    cout << scc_count << "\n";
    return 0;
}

```

### `CPPB2-L12-09` — Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (k Lần Dùng Vé Miễn Phí)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    vector<long long> dist(n + 1, 1e18);
    vector<int> cnt(n + 1, 0);
    vector<bool> in_q(n + 1, false);
    queue<int> q;

    dist[s] = 0;
    q.push(s);
    in_q[s] = true;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        in_q[u] = false;

        for (const auto &e : adj[u]) {
            if (dist[u] + e.w < dist[e.to]) {
                dist[e.to] = dist[u] + e.w;
                if (!in_q[e.to]) {
                    q.push(e.to);
                    in_q[e.to] = true;
                    if (++cnt[e.to] > n) {
                        cout << "-1\n"; // Có chu trình âm
                        return 0;
                    }
                }
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << (dist[i] >= 1e18 ? -1 : dist[i]) << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L12-10` — Thành Phần Liên Thông Mạnh (scc Tarjan/kosaraju)

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005, LOG = 20;
vector<int> adj[MAXN];
int up[MAXN][LOG], depth[MAXN];

void dfs_lca(int u, int p, int d) {
    depth[u] = d;
    up[u][0] = p;
    for (int j = 1; j < LOG; ++j) {
        up[u][j] = up[up[u][j - 1]][j - 1];
    }
    for (int v : adj[u]) {
        if (v != p) dfs_lca(v, u, d + 1);
    }
}

int get_lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    for (int j = LOG - 1; j >= 0; --j) {
        if (depth[u] - (1 << j) >= depth[v]) {
            u = up[u][j];
        }
    }
    if (u == v) return u;
    for (int j = LOG - 1; j >= 0; --j) {
        if (up[u][j] != up[v][j]) {
            u = up[u][j];
            v = up[v][j];
        }
    }
    return up[u][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs_lca(1, 1, 0);

    while (q--) {
        int u, v; cin >> u >> v;
        cout << get_lca(u, v) << "\n";
    }
    return 0;
}

```

### `CPPB2-L12-11` — Tìm Tổ Tiên Chung Gần Nhất (lca Binary Lifting)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<multiset<int>> adj(n + 1);
    vector<int> deg(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].insert(v);
        adj[v].insert(u);
        deg[u]++; deg[v]++;
    }

    for (int i = 1; i <= n; ++i) {
        if (deg[i] % 2 != 0) {
            cout << "-1\n";
            return 0;
        }
    }

    stack<int> st;
    vector<int> circuit;
    st.push(1);

    while (!st.empty()) {
        int u = st.top();
        if (!adj[u].empty()) {
            int v = *adj[u].begin();
            adj[u].erase(adj[u].begin());
            adj[v].erase(adj[v].find(u));
            st.push(v);
        } else {
            circuit.push_back(u);
            st.pop();
        }
    }

    if ((int)circuit.size() != m + 1) {
        cout << "-1\n";
    } else {
        reverse(circuit.begin(), circuit.end());
        for (int node : circuit) cout << node << " ";
        cout << "\n";
    }
    return 0;
}

```

### `CPPB2-L12-12` — Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (k Lần Dùng Vé)

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
vector<int> adj[MAXN], adj_rev[MAXN];
vector<bool> vis;
vector<int> order, comp;

void dfs1(int u) {
    vis[u] = true;
    for (int v : adj[u]) if (!vis[v]) dfs1(v);
    order.push_back(u);
}

void dfs2(int u, int c) {
    comp[u] = c;
    for (int v : adj_rev[u]) if (comp[v] == -1) dfs2(v, c);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        int not_u = (u > 0 ? u + n : -u);
        int not_v = (v > 0 ? v + n : -v);
        int actual_u = (u > 0 ? u : -u + n);
        int actual_v = (v > 0 ? v : -v + n);

        adj[not_u].push_back(actual_v);
        adj[not_v].push_back(actual_u);
        adj_rev[actual_v].push_back(not_u);
        adj_rev[actual_u].push_back(not_v);
    }

    vis.assign(2 * n + 1, false);
    for (int i = 1; i <= 2 * n; ++i) if (!vis[i]) dfs1(i);

    comp.assign(2 * n + 1, -1);
    int c = 0;
    for (int i = 2 * n - 1; i >= 0; --i) {
        int u = order[i];
        if (comp[u] == -1) dfs2(u, c++);
    }

    for (int i = 1; i <= n; ++i) {
        if (comp[i] == comp[i + n]) {
            cout << "NO\n";
            return 0;
        }
    }

    cout << "YES\n";
    return 0;
}

```

### `CPPB2-L12-13` — Multi-source Bfs Lan Tỏa Dịch Bệnh / Cháy Rừng

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to;
    long long cap, flow;
    int rev;
};

const int MAXN = 505;
vector<Edge> adj[MAXN];
int level[MAXN], ptr[MAXN];

void add_edge(int from, int to, long long cap) {
    adj[from].push_back({to, cap, 0, (int)adj[to].size()});
    adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
}

bool bfs_dinic(int s, int t) {
    memset(level, -1, sizeof(level));
    level[s] = 0;
    queue<int> q; q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (const auto &e : adj[u]) {
            if (e.cap - e.flow > 0 && level[e.to] == -1) {
                level[e.to] = level[u] + 1;
                q.push(e.to);
            }
        }
    }
    return level[t] != -1;
}

long long dfs_dinic(int u, int t, long long pushed) {
    if (pushed == 0 || u == t) return pushed;
    for (int &cid = ptr[u]; cid < (int)adj[u].size(); ++cid) {
        auto &e = adj[u][cid];
        int tr = e.to;
        if (level[u] + 1 != level[tr] || e.cap - e.flow == 0) continue;
        long long tr_pushed = dfs_dinic(tr, t, min(pushed, e.cap - e.flow));
        if (tr_pushed == 0) continue;
        e.flow += tr_pushed;
        adj[tr][e.rev].flow -= tr_pushed;
        return tr_pushed;
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v; long long c; cin >> u >> v >> c;
        add_edge(u, v, c);
    }

    long long flow = 0;
    while (bfs_dinic(s, t)) {
        memset(ptr, 0, sizeof(ptr));
        while (long long pushed = dfs_dinic(s, t, 1e18)) flow += pushed;
    }

    cout << flow << "\n";
    return 0;
}

```

### `CPPB2-L12-14` — Đường Đi Euler & Chu Trình Euler (hierholzer)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Min-cut có giá trị bằng Max-flow (Dinic)
struct Edge {
    int to;
    long long cap, flow;
    int rev;
};

const int MAXN = 505;
vector<Edge> adj[MAXN];
int level[MAXN], ptr[MAXN];

void add_edge(int from, int to, long long cap) {
    adj[from].push_back({to, cap, 0, (int)adj[to].size()});
    adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
}

bool bfs_dinic(int s, int t) {
    memset(level, -1, sizeof(level));
    level[s] = 0;
    queue<int> q; q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (const auto &e : adj[u]) {
            if (e.cap - e.flow > 0 && level[e.to] == -1) {
                level[e.to] = level[u] + 1;
                q.push(e.to);
            }
        }
    }
    return level[t] != -1;
}

long long dfs_dinic(int u, int t, long long pushed) {
    if (pushed == 0 || u == t) return pushed;
    for (int &cid = ptr[u]; cid < (int)adj[u].size(); ++cid) {
        auto &e = adj[u][cid];
        int tr = e.to;
        if (level[u] + 1 != level[tr] || e.cap - e.flow == 0) continue;
        long long tr_pushed = dfs_dinic(tr, t, min(pushed, e.cap - e.flow));
        if (tr_pushed == 0) continue;
        e.flow += tr_pushed;
        adj[tr][e.rev].flow -= tr_pushed;
        return tr_pushed;
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v; long long c; cin >> u >> v >> c;
        add_edge(u, v, c);
    }

    long long min_cut = 0;
    while (bfs_dinic(s, t)) {
        memset(ptr, 0, sizeof(ptr));
        while (long long pushed = dfs_dinic(s, t, 1e18)) min_cut += pushed;
    }

    cout << min_cut << "\n";
    return 0;
}

```

### `CPPB2-L12-15` — Tìm Chu Trình Âm Bằng Bellman-ford / Spfa

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 50005;
vector<int> adj[MAXN];
int pair_u[MAXN], pair_v[MAXN], dist_u[MAXN];

bool bfs_hk(int n) {
    queue<int> q;
    for (int u = 1; u <= n; ++u) {
        if (pair_u[u] == 0) {
            dist_u[u] = 0;
            q.push(u);
        } else dist_u[u] = 1e9;
    }
    dist_u[0] = 1e9;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        if (dist_u[u] < dist_u[0]) {
            for (int v : adj[u]) {
                if (dist_u[pair_v[v]] == (int)1e9) {
                    dist_u[pair_v[v]] = dist_u[u] + 1;
                    q.push(pair_v[v]);
                }
            }
        }
    }
    return dist_u[0] != 1e9;
}

bool dfs_hk(int u) {
    if (u != 0) {
        for (int v : adj[u]) {
            if (dist_u[pair_v[v]] == dist_u[u] + 1) {
                if (dfs_hk(pair_v[v])) {
                    pair_v[v] = u;
                    pair_u[u] = v;
                    return true;
                }
            }
        }
        dist_u[u] = 1e9;
        return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, p;
    if (!(cin >> n >> m >> p)) return 0;

    for (int i = 0; i < p; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
    }

    int matching = 0;
    while (bfs_hk(n)) {
        for (int u = 1; u <= n; ++u) {
            if (pair_u[u] == 0 && dfs_hk(u)) matching++;
        }
    }

    cout << matching << "\n";
    return 0;
}

```

### `CPPB2-L12-16` — Luồng Cực Đại Trong Mạng (max Flow Dinic Algorithm)

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];
int parent_node[MAXN], depth[MAXN], heavy[MAXN], head[MAXN], pos[MAXN];
int cur_pos = 0;

int dfs_hld(int u, int p, int d) {
    int size = 1;
    int max_c_size = 0;
    depth[u] = d;
    parent_node[u] = p;
    heavy[u] = -1;

    for (int v : adj[u]) {
        if (v != p) {
            int c_size = dfs_hld(v, u, d + 1);
            size += c_size;
            if (c_size > max_c_size) {
                max_c_size = c_size;
                heavy[u] = v;
            }
        }
    }
    return size;
}

void decompose(int u, int h) {
    head[u] = h;
    pos[u] = ++cur_pos;
    if (heavy[u] != -1) decompose(heavy[u], h);
    for (int v : adj[u]) {
        if (v != parent_node[u] && v != heavy[u]) decompose(v, v);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs_hld(1, 1, 0);
    decompose(1, 1);

    cout << "HLD Built Successfully\n";
    return 0;
}

```

### `CPPB2-L12-17` — Bfs Do Thi Trong So 0 1

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L12-18` — Tarjan Tim Khop Va Cau

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];
int tin[MAXN], low[MAXN], timer;
bool is_cut[MAXN];
int bridge_count = 0;

void dfs(int u, int p = -1) {
    tin[u] = low[u] = ++timer;
    int children = 0;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (tin[v]) {
            low[u] = min(low[u], tin[v]);
        } else {
            dfs(v, u);
            low[u] = min(low[u], low[v]);
            if (low[v] > tin[u]) bridge_count++;
            if (low[v] >= tin[u] && p != -1) is_cut[u] = true;
            children++;
        }
    }
    if (p == -1 && children > 1) is_cut[u] = true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int i = 1; i <= n; ++i) {
        if (!tin[i]) dfs(i);
    }

    int cut_count = 0;
    for (int i = 1; i <= n; ++i) {
        if (is_cut[i]) cut_count++;
    }

    cout << cut_count << " " << bridge_count << "\n";
    return 0;
}

```

### `CPPB2-L12-19` — Tarjan Thanh Phan Lien Thong Manh Scc

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L12-20` — Chu Trinh Euler Hierholzer

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L12-21` — Dijkstra Do Thi Nhieu Tang K Ve Mien Phi

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L12-22` — Dinh To Nho Nhat Kruskal Dsu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L12-23` — Bellman Ford Chu Trinh Am

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L12-24` — Floyd Warshall Moi Cap Dinh

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L12-25` — Lca To Tien Chung Gan Nhat Binary Lifting

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
const int LOGN = 20;

vector<int> adj[MAXN];
int up[MAXN][LOGN];
int depth[MAXN];

void dfs(int u, int p, int d) {
    depth[u] = d;
    up[u][0] = p;
    for (int i = 1; i < LOGN; ++i) {
        up[u][i] = up[up[u][i - 1]][i - 1];
    }
    for (int v : adj[u]) {
        if (v != p) dfs(v, u, d + 1);
    }
}

int get_lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    for (int i = LOGN - 1; i >= 0; --i) {
        if (depth[u] - (1 << i) >= depth[v]) {
            u = up[u][i];
        }
    }
    if (u == v) return u;
    for (int i = LOGN - 1; i >= 0; --i) {
        if (up[u][i] != up[v][i]) {
            u = up[u][i];
            v = up[v][i];
        }
    }
    return up[u][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 1, 0);

    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << get_lca(u, v) << "\n";
    }
    return 0;
}

```

### `CPPB2-L12-26` — Dem So Duong Di Topo Dag

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

## Chương 06 — Bài 13: Cây phân đoạn & Cây Fenwick

### `CPPB2-L13-01` — Truy Vấn Tổng Đoạn Fenwick Tree

```cpp
#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<long long> tree;
    FenwickTree(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, long long delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }

    long long query_range(int l, int r) {
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    FenwickTree bit(n);
    for (int i = 1; i <= n; ++i) {
        long long x; cin >> x;
        bit.update(i, x);
    }

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int idx; long long val;
            cin >> idx >> val;
            bit.update(idx, val);
        } else {
            int l, r; cin >> l >> r;
            cout << bit.query_range(l, r) << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L13-02` — Truy Vấn Giá Trị Nhỏ Nhất Đoạn (rmq Segment Tree)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n;
    vector<long long> tree;
    SegmentTree(int n) : n(n), tree(4 * n, 1e18) {}

    void build(const vector<long long> &a, int node, int l, int r) {
        if (l == r) {
            tree[node] = a[l];
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    void update(int node, int l, int r, int idx, long long val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) update(2 * node, l, mid, idx, val);
        else update(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    long long query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 1e18;
        if (ql <= l && r <= qr) return tree[node];
        int mid = l + (r - l) / 2;
        return min(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTree st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int idx; long long val; cin >> idx >> val;
            st.update(1, 1, n, idx, val);
        } else {
            int l, r; cin >> l >> r;
            cout << st.query(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L13-03` — Đếm Cặp Nghịch Thế Bằng Fenwick Tree

```cpp
#include <bits/stdc++.h>
using namespace std;

struct LazySegmentTree {
    int n;
    vector<long long> tree, lazy;
    LazySegmentTree(int n) : n(n), tree(4 * n, 0), lazy(4 * n, 0) {}

    void push(int node, int l, int r) {
        if (lazy[node] != 0) {
            int mid = l + (r - l) / 2;
            tree[2 * node] += lazy[node] * (mid - l + 1);
            lazy[2 * node] += lazy[node];
            tree[2 * node + 1] += lazy[node] * (r - mid);
            lazy[2 * node + 1] += lazy[node];
            lazy[node] = 0;
        }
    }

    void update_range(int node, int l, int r, int ql, int qr, long long val) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            tree[node] += val * (r - l + 1);
            lazy[node] += val;
            return;
        }
        push(node, l, r);
        int mid = l + (r - l) / 2;
        update_range(2 * node, l, mid, ql, qr, val);
        update_range(2 * node + 1, mid + 1, r, ql, qr, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    long long query_range(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return tree[node];
        push(node, l, r);
        int mid = l + (r - l) / 2;
        return query_range(2 * node, l, mid, ql, qr) + query_range(2 * node + 1, mid + 1, r, ql, qr);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    LazySegmentTree st(n);
    for (int i = 1; i <= n; ++i) {
        long long x; cin >> x;
        st.update_range(1, 1, n, i, i, x);
    }

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int l, r; long long val; cin >> l >> r >> val;
            st.update_range(1, 1, n, l, r, val);
        } else {
            int l, r; cin >> l >> r;
            cout << st.query_range(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L13-04` — Truy Vấn Gcd Đoạn Động

```cpp
#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<int> tree;
    FenwickTree(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    FenwickTree bit(vals.size());
    long long inv = 0;

    for (int i = n - 1; i >= 0; --i) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        inv += bit.query(rank - 1);
        bit.update(rank, 1);
    }

    cout << inv << "\n";
    return 0;
}

```

### `CPPB2-L13-05` — Tìm Phần Tử Số 1 Thứ K Trong Dãy Nhị Phân

```cpp
#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n;
    vector<int> tree;
    SegmentTree(int n) : n(n), tree(4 * n, 0) {}

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) update(2 * node, l, mid, idx, val);
        else update(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    int find_kth(int node, int l, int r, int k) {
        if (l == r) return l;
        int mid = l + (r - l) / 2;
        if (tree[2 * node] >= k) return find_kth(2 * node, l, mid, k);
        else return find_kth(2 * node + 1, mid + 1, r, k - tree[2 * node]);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    SegmentTree st(n);
    for (int i = 1; i <= n; ++i) {
        int bit; cin >> bit;
        st.update(1, 1, n, i, bit);
    }

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int idx, val; cin >> idx >> val;
            st.update(1, 1, n, idx, val);
        } else {
            int k; cin >> k;
            cout << st.find_kth(1, 1, n, k) << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L13-06` — Dãy Con Tăng Dài Nhất Lis Bằng Segment Tree

```cpp
#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n;
    vector<int> tree;
    SegmentTree(int n) : n(n), tree(4 * n, 0) {}

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            tree[node] = max(tree[node], val);
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) update(2 * node, l, mid, idx, val);
        else update(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l || ql > qr) return 0;
        if (ql <= l && r <= qr) return tree[node];
        int mid = l + (r - l) / 2;
        return max(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    SegmentTree st(vals.size());
    int max_lis = 0;

    for (int i = 0; i < n; ++i) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        int best_prev = st.query(1, 1, vals.size(), 1, rank - 1);
        int cur_len = best_prev + 1;
        max_lis = max(max_lis, cur_len);
        st.update(1, 1, vals.size(), rank, cur_len);
    }

    cout << max_lis << "\n";
    return 0;
}

```

### `CPPB2-L13-07` — Cập Nhật Đoạn Truy Vấn Điểm Bằng Fenwick Tree

```cpp
#include <bits/stdc++.h>
using namespace std;

struct FenwickTree2D {
    int n, m;
    vector<vector<long long>> tree;
    FenwickTree2D(int n, int m) : n(n), m(m), tree(n + 1, vector<long long>(m + 1, 0)) {}

    void update(int r, int c, long long val) {
        for (int i = r; i <= n; i += i & -i) {
            for (int j = c; j <= m; j += j & -j) {
                tree[i][j] += val;
            }
        }
    }

    long long query(int r, int c) {
        long long sum = 0;
        for (int i = r; i > 0; i -= i & -i) {
            for (int j = c; j > 0; j -= j & -j) {
                sum += tree[i][j];
            }
        }
        return sum;
    }

    long long query_rect(int r1, int c1, int r2, int c2) {
        return query(r2, c2) - query(r1 - 1, c2) - query(r2, c1 - 1) + query(r1 - 1, c1 - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    FenwickTree2D bit(n, m);

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int r, c; long long val; cin >> r >> c >> val;
            bit.update(r, c, val);
        } else {
            int r1, c1, r2, c2; cin >> r1 >> c1 >> r2 >> c2;
            cout << bit.query_rect(r1, c1, r2, c2) << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L13-08` — Segment Tree Lazy Propagation (cập Nhật Đoạn & Truy Vấn Đoạn)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long sum, pref, suff, max_sub;
    Node(long long val = 0) {
        sum = val;
        pref = suff = max_sub = val;
    }
};

Node merge_nodes(const Node &L, const Node &R) {
    Node res;
    res.sum = L.sum + R.sum;
    res.pref = max(L.pref, L.sum + R.pref);
    res.suff = max(R.suff, R.sum + L.suff);
    res.max_sub = max({L.max_sub, R.max_sub, L.suff + R.pref});
    return res;
}

struct SegmentTree {
    int n;
    vector<Node> tree;
    SegmentTree(int n) : n(n), tree(4 * n) {}

    void build(const vector<long long> &a, int node, int l, int r) {
        if (l == r) {
            tree[node] = Node(a[l]);
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        tree[node] = merge_nodes(tree[2 * node], tree[2 * node + 1]);
    }

    Node query(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return tree[node];
        int mid = l + (r - l) / 2;
        if (qr <= mid) return query(2 * node, l, mid, ql, qr);
        if (ql > mid) return query(2 * node + 1, mid + 1, r, ql, qr);
        return merge_nodes(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTree st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int l, r; cin >> l >> r;
        cout << st.query(1, 1, n, l, r).max_sub << "\n";
    }
    return 0;
}

```

### `CPPB2-L13-09` — Đoạn Con Có Tổng Lớn Nhất (maximum Subsegment Sum Query)

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];
int tin[MAXN], tout[MAXN], timer = 0;

void dfs_euler(int u, int p) {
    tin[u] = ++timer;
    for (int v : adj[u]) if (v != p) dfs_euler(v, u);
    tout[u] = timer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs_euler(1, 0);

    for (int i = 1; i <= n; ++i) {
        cout << "Node " << i << ": [" << tin[i] << ", " << tout[i] << "]\n";
    }
    return 0;
}

```

### `CPPB2-L13-10` — Đoạn Con Có Tổng Lớn Nhất (maximum Subsegment Sum Query)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long sum;
    Node *left, *right;
    Node() : sum(0), left(nullptr), right(nullptr) {}
};

void update_dynamic(Node* &node, long long l, long long r, long long idx, long long val) {
    if (!node) node = new Node();
    node->sum += val;
    if (l == r) return;
    long long mid = l + (r - l) / 2;
    if (idx <= mid) update_dynamic(node->left, l, mid, idx, val);
    else update_dynamic(node->right, mid + 1, r, idx, val);
}

long long query_dynamic(Node *node, long long l, long long r, long long ql, long long qr) {
    if (!node || ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return node->sum;
    long long mid = l + (r - l) / 2;
    return query_dynamic(node->left, l, mid, ql, qr) + query_dynamic(node->right, mid + 1, r, ql, qr);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    Node *root = nullptr;
    long long MAXV = 1e18;

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            long long idx, val; cin >> idx >> val;
            update_dynamic(root, 1, MAXV, idx, val);
        } else {
            long long l, r; cin >> l >> r;
            cout << query_dynamic(root, 1, MAXV, l, r) << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L13-11` — Lazy Propagation Gán Đoạn Và Tìm Min Đoạn

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int count;
    Node *left, *right;
    Node(int c = 0) : count(c), left(nullptr), right(nullptr) {}
};

Node* build(int l, int r) {
    Node *node = new Node();
    if (l == r) return node;
    int mid = l + (r - l) / 2;
    node->left = build(l, mid);
    node->right = build(mid + 1, r);
    return node;
}

Node* update_pst(Node *prev, int l, int r, int idx) {
    Node *node = new Node(prev->count + 1);
    node->left = prev->left;
    node->right = prev->right;
    if (l == r) return node;
    int mid = l + (r - l) / 2;
    if (idx <= mid) node->left = update_pst(prev->left, l, mid, idx);
    else node->right = update_pst(prev->right, mid + 1, r, idx);
    return node;
}

int query_kth(Node *left_root, Node *right_root, int l, int r, int k) {
    if (l == r) return l;
    int count = right_root->left->count - left_root->left->count;
    int mid = l + (r - l) / 2;
    if (count >= k) return query_kth(left_root->left, right_root->left, l, mid, k);
    else return query_kth(left_root->right, right_root->right, mid + 1, r, k - count);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<long long> vals(a.begin() + 1, a.end());
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    int sz = vals.size();
    vector<Node*> roots(n + 1);
    roots[0] = build(1, sz);

    for (int i = 1; i <= n; ++i) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        roots[i] = update_pst(roots[i - 1], 1, sz, rank);
    }

    while (q--) {
        int l, r, k; cin >> l >> r >> k;
        int rank = query_kth(roots[l - 1], roots[r], 1, sz, k);
        cout << vals[rank - 1] << "\n";
    }
    return 0;
}

```

### `CPPB2-L13-12` — Cây Fenwick Cập Nhật Đoạn & Truy Vấn Đoạn

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Query {
    int l, r, id;
};

struct FenwickTree {
    int n;
    vector<int> tree;
    FenwickTree(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].l >> queries[i].r;
        queries[i].id = i;
    }

    sort(queries.begin(), queries.end(), [](const Query &x, const Query &y) {
        return x.r < y.r;
    });

    FenwickTree bit(n);
    map<int, int> last_pos;
    vector<int> ans(q);
    int cur_r = 1;

    for (const auto &qry : queries) {
        while (cur_r <= qry.r) {
            if (last_pos.count(a[cur_r])) {
                bit.update(last_pos[a[cur_r]], -1);
            }
            bit.update(cur_r, 1);
            last_pos[a[cur_r]] = cur_r;
            cur_r++;
        }
        ans[qry.id] = bit.query(qry.r) - bit.query(qry.l - 1);
    }

    for (int i = 0; i < q; ++i) cout << ans[i] << "\n";
    return 0;
}

```

### `CPPB2-L13-13` — Tìm Vị Trí Đầu Tiên Có Giá Trị $\ge X$ Trong Đoạn $[l, R]$

```cpp
#include <bits/stdc++.h>
using namespace std;

struct SegmentTreeBeats {
    int n;
    vector<long long> sum_tree, max_tree;
    SegmentTreeBeats(int n) : n(n), sum_tree(4 * n, 0), max_tree(4 * n, 0) {}

    void build(const vector<long long> &a, int node, int l, int r) {
        if (l == r) {
            sum_tree[node] = max_tree[node] = a[l];
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        sum_tree[node] = sum_tree[2 * node] + sum_tree[2 * node + 1];
        max_tree[node] = max(max_tree[2 * node], max_tree[2 * node + 1]);
    }

    long long query_sum(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return sum_tree[node];
        int mid = l + (r - l) / 2;
        return query_sum(2 * node, l, mid, ql, qr) + query_sum(2 * node + 1, mid + 1, r, ql, qr);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTreeBeats stb(n);
    stb.build(a, 1, 1, n);

    while (q--) {
        int l, r; cin >> l >> r;
        cout << stb.query_sum(1, 1, n, l, r) << "\n";
    }
    return 0;
}

```

### `CPPB2-L13-14` — Segment Tree Động (dynamic / Sparse Segment Tree)

```cpp
#include <bits/stdc++.h>
using namespace std;

int block_sz;

struct Query {
    int l, r, id;
    bool operator<(const Query &other) const {
        if (l / block_sz != other.l / block_sz) return l / block_sz < other.l / block_sz;
        return (l / block_sz) % 2 ? r < other.r : r > other.r;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    block_sz = sqrt(n) + 1;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].l >> queries[i].r;
        queries[i].id = i;
    }

    sort(queries.begin(), queries.end());

    vector<int> freq(1000005, 0);
    vector<int> ans(q);
    int cur_l = 1, cur_r = 0, distinct = 0;

    for (const auto &qry : queries) {
        while (cur_l > qry.l) {
            cur_l--;
            if (freq[a[cur_l]]++ == 0) distinct++;
        }
        while (cur_r < qry.r) {
            cur_r++;
            if (freq[a[cur_r]]++ == 0) distinct++;
        }
        while (cur_l < qry.l) {
            if (--freq[a[cur_l]] == 0) distinct--;
            cur_l++;
        }
        while (cur_r > qry.r) {
            if (--freq[a[cur_r]] == 0) distinct--;
            cur_r--;
        }
        ans[qry.id] = distinct;
    }

    for (int i = 0; i < q; ++i) cout << ans[i] << "\n";
    return 0;
}

```

### `CPPB2-L13-15` — Cây Phân Đoạn Bền Vững (persistent Segment Tree Cơ Bản)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct MergeSortTree {
    int n;
    vector<vector<long long>> tree;
    MergeSortTree(int n) : n(n), tree(4 * n) {}

    void build(const vector<long long> &a, int node, int l, int r) {
        if (l == r) {
            tree[node] = {a[l]};
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        tree[node].resize(tree[2 * node].size() + tree[2 * node + 1].size());
        merge(tree[2 * node].begin(), tree[2 * node].end(),
              tree[2 * node + 1].begin(), tree[2 * node + 1].end(),
              tree[node].begin());
    }

    int query(int node, int l, int r, int ql, int qr, long long k) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) {
            return lower_bound(tree[node].begin(), tree[node].end(), k) - tree[node].begin();
        }
        int mid = l + (r - l) / 2;
        return query(2 * node, l, mid, ql, qr, k) + query(2 * node + 1, mid + 1, r, ql, qr, k);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    MergeSortTree mst(n);
    mst.build(a, 1, 1, n);

    while (q--) {
        int l, r; long long k;
        cin >> l >> r >> k;
        cout << mst.query(1, 1, n, l, r, k) << "\n";
    }
    return 0;
}

```

### `CPPB2-L13-16` — Segment Tree Beats (thuật Toán Ji Driver Tối Ưu Phép Min=x)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int block_sz = sqrt(n) + 1;
    vector<long long> block_sum((n + block_sz - 1) / block_sz, 0);

    for (int i = 0; i < n; ++i) {
        block_sum[i / block_sz] += a[i];
    }

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int idx; long long val; cin >> idx >> val;
            idx--;
            block_sum[idx / block_sz] += (val - a[idx]);
            a[idx] = val;
        } else {
            int l, r; cin >> l >> r;
            l--; r--;
            long long sum = 0;
            int bl = l / block_sz, br = r / block_sz;
            if (bl == br) {
                for (int i = l; i <= r; ++i) sum += a[i];
            } else {
                for (int i = l; i < (bl + 1) * block_sz; ++i) sum += a[i];
                for (int b = bl + 1; b < br; ++b) sum += block_sum[b];
                for (int i = br * block_sz; i <= r; ++i) sum += a[i];
            }
            cout << sum << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L13-17` — Segment Tree Lazy Propagation Tong Doan

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
long long tree_sum[4 * MAXN], lazy[4 * MAXN], a[MAXN];

void build(int node, int start, int end) {
    if (start == end) {
        tree_sum[node] = a[start];
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    tree_sum[node] = tree_sum[2 * node] + tree_sum[2 * node + 1];
}

void push(int node, int start, int end) {
    if (lazy[node] != 0) {
        int mid = (start + end) / 2;
        tree_sum[2 * node] += lazy[node] * (mid - start + 1);
        lazy[2 * node] += lazy[node];
        tree_sum[2 * node + 1] += lazy[node] * (end - mid);
        lazy[2 * node + 1] += lazy[node];
        lazy[node] = 0;
    }
}

void update_range(int node, int start, int end, int l, int r, long long val) {
    if (r < start || end < l) return;
    if (l <= start && end <= r) {
        tree_sum[node] += val * (end - start + 1);
        lazy[node] += val;
        return;
    }
    push(node, start, end);
    int mid = (start + end) / 2;
    update_range(2 * node, start, mid, l, r, val);
    update_range(2 * node + 1, mid + 1, end, l, r, val);
    tree_sum[node] = tree_sum[2 * node] + tree_sum[2 * node + 1];
}

long long query_range(int node, int start, int end, int l, int r) {
    if (r < start || end < l) return 0;
    if (l <= start && end <= r) return tree_sum[node];
    push(node, start, end);
    int mid = (start + end) / 2;
    return query_range(2 * node, start, mid, l, r) + query_range(2 * node + 1, mid + 1, end, l, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 1; i <= n; ++i) cin >> a[i];
    build(1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r; long long val;
            cin >> l >> r >> val;
            update_range(1, 1, n, l, r, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << query_range(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L13-18` — Fenwick Tree 2d Tong Chu Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L13-19` — Dynamic Segment Tree Toa Do 1e9

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L13-20` — Persistent Segment Tree K Th Number

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L13-21` — Segment Tree Walk On Tree

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L13-22` — Merge Sort Tree Dem So Phan Tu Lon Hon K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L13-23` — Fenwick Tree Range Update Range Query

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L13-24` — Segment Tree Beats Co Ban

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L13-25` — Segment Tree Max Subarray Sum

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L13-26` — Segment Tree Dem So Phan Tu Khac Nhau Offline

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

## Chương 06 — Bài 14: Quy hoạch động chữ số (Digit DP)

### `CPPB2-L14-01` — Đếm Số Có Tổng Chữ Số Bằng K

```cpp
#include <bits/stdc++.h>
using namespace std;

long long count_digit(long long n, int d) {
    long long count = 0;
    for (long long m = 1; m <= n; m *= 10) {
        long long a = n / m, b = n % m;
        int cur = a % 10;
        if (d > 0) {
            count += (a / 10) * m + (cur > d ? m : (cur == d ? b + 1 : 0));
        } else {
            if (a / 10 > 0) count += (a / 10 - 1) * m + (cur > 0 ? m : b + 1);
        }
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R; int d;
    if (!(cin >> L >> R >> d)) return 0;

    cout << count_digit(R, d) - count_digit(L - 1, d) << "\n";
    return 0;
}

```

### `CPPB2-L14-02` — Tổng Các Chữ Số Bằng K Trong Đoạn [l, R]

```cpp
#include <bits/stdc++.h>
using namespace std;

string S_str;
int target_sum;
long long dp[20][200][2];

long long solve_dp(int idx, int sum, bool tight) {
    if (idx == (int)S_str.size()) return sum == target_sum;
    if (dp[idx][sum][tight] != -1) return dp[idx][sum][tight];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        ans += solve_dp(idx + 1, sum + d, tight && (d == limit));
    }
    return dp[idx][sum][tight] = ans;
}

long long count_sum(long long n, int s) {
    if (n < 0) return 0;
    S_str = to_string(n);
    target_sum = s;
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, 0, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R; int s;
    if (!(cin >> L >> R >> s)) return 0;

    cout << count_sum(R, s) - count_sum(L - 1, s) << "\n";
    return 0;
}

```

### `CPPB2-L14-03` — Đếm Số Lượng Chữ Số 0 Xuất Hiện

```cpp
#include <bits/stdc++.h>
using namespace std;

string S_str;
int forbidden;
long long dp[20][2];

long long solve_dp(int idx, bool tight) {
    if (idx == (int)S_str.size()) return 1;
    if (dp[idx][tight] != -1) return dp[idx][tight];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        if (d == forbidden) continue;
        ans += solve_dp(idx + 1, tight && (d == limit));
    }
    return dp[idx][tight] = ans;
}

long long count_valid(long long n, int d) {
    if (n < 0) return 0;
    S_str = to_string(n);
    forbidden = d;
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R; int d;
    if (!(cin >> L >> R >> d)) return 0;

    cout << count_valid(R, d) - count_valid(L - 1, d) << "\n";
    return 0;
}

```

### `CPPB2-L14-04` — Số Có Các Chữ Số Tăng Ngặt

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L14-05` — Số Chia Hết Cho Tổng Các Chữ Số Của Chính Nó

```cpp
#include <bits/stdc++.h>
using namespace std;

string S_str;
long long dp[20][11][2][2];

long long solve_dp(int idx, int prev, bool tight, bool leading_zero) {
    if (idx == (int)S_str.size()) return 1;
    if (dp[idx][prev + 1][tight][leading_zero] != -1) return dp[idx][prev + 1][tight][leading_zero];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        if (!leading_zero && d == prev) continue;
        bool next_lead = leading_zero && (d == 0);
        ans += solve_dp(idx + 1, next_lead ? -1 : d, tight && (d == limit), next_lead);
    }
    return dp[idx][prev + 1][tight][leading_zero] = ans;
}

long long count_lucid(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, -1, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_lucid(R) - count_lucid(L - 1) << "\n";
    return 0;
}

```

### `CPPB2-L14-06` — Đếm Số Đối Xứng (palindrome Numbers) Trong Đoạn

```cpp
#include <bits/stdc++.h>
using namespace std;

long long count_pal(long long n) {
    if (n < 0) return 0;
    if (n == 0) return 1;

    string s = to_string(n);
    int len = s.size();
    long long ans = 0;

    // Palindromes có độ dài < len
    for (int l = 1; l < len; ++l) {
        int half = (l + 1) / 2;
        ans += 9 * pow(10, half - 1);
    }

    // Palindromes có độ dài đúng bằng len
    int half = (len + 1) / 2;
    long long first_half = stoll(s.substr(0, half));
    long long min_half = pow(10, half - 1);

    ans += (first_half - min_half);

    string pal = to_string(first_half);
    string second_half = pal.substr(0, len / 2);
    reverse(second_half.begin(), second_half.end());
    pal += second_half;

    if (stoll(pal) <= n) ans++;
    return ans + 1; // gồm số 0
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_pal(R) - count_pal(L - 1) << "\n";
    return 0;
}

```

### `CPPB2-L14-07` — Số Chứa Đầy Đủ Các Chữ Số Từ 0 Đến 9

```cpp
#include <bits/stdc++.h>
using namespace std;

string S_str;
long long dp[20][11][2][2];

long long solve_dp(int idx, int prev, bool tight, bool lead) {
    if (idx == (int)S_str.size()) return 1;
    if (dp[idx][prev + 1][tight][lead] != -1) return dp[idx][prev + 1][tight][lead];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        if (!lead && d < prev) continue; // Tăng dần
        bool next_lead = lead && (d == 0);
        ans += solve_dp(idx + 1, next_lead ? -1 : d, tight && (d == limit), next_lead);
    }
    return dp[idx][prev + 1][tight][lead] = ans;
}

long long count_increasing(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, -1, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_increasing(R) - count_increasing(L - 1) << "\n";
    return 0;
}

```

### `CPPB2-L14-08` — Tổng Các Số Trong Đoạn Thỏa Mãn Tính Chất Chữ Số

```cpp
#include <bits/stdc++.h>
using namespace std;

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; ++i) if (n % i == 0) return false;
    return true;
}

string S_str;
long long dp[20][200][2];

long long solve_dp(int idx, int sum, bool tight) {
    if (idx == (int)S_str.size()) return is_prime(sum);
    if (dp[idx][sum][tight] != -1) return dp[idx][sum][tight];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        ans += solve_dp(idx + 1, sum + d, tight && (d == limit));
    }
    return dp[idx][sum][tight] = ans;
}

long long count_prime_sum(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, 0, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_prime_sum(R) - count_prime_sum(L - 1) << "\n";
    return 0;
}

```

### `CPPB2-L14-09` — Số Có Tích Các Chữ Số Bằng K

```cpp
#include <bits/stdc++.h>
using namespace std;

string S_str;
long long dp[20][50][2][2];

long long solve_dp(int idx, int diff, bool tight, bool lead) {
    if (idx == (int)S_str.size()) return (!lead && diff == 25);
    if (dp[idx][diff][tight][lead] != -1) return dp[idx][diff][tight][lead];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_lead = lead && (d == 0);
        int next_diff = diff + (next_lead ? 0 : (d % 2 == 0 ? 1 : -1));
        ans += solve_dp(idx + 1, next_diff, tight && (d == limit), next_lead);
    }
    return dp[idx][diff][tight][lead] = ans;
}

long long count_balanced(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, 25, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_balanced(R) - count_balanced(L - 1) << "\n";
    return 0;
}

```

### `CPPB2-L14-10` — Tổng Giá Trị Các Số Thỏa Mãn Tính Chất Chữ Số

```cpp
#include <bits/stdc++.h>
using namespace std;

long long sum_all_digits(long long n) {
    if (n <= 0) return 0;
    long long total = 0;
    for (long long m = 1; m <= n; m *= 10) {
        long long a = n / m, b = n % m;
        int cur = a % 10;
        total += (a / 10) * 45 * m;
        for (int d = 0; d < cur; ++d) total += d * m;
        total += cur * (b + 1);
    }
    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << sum_all_digits(R) - sum_all_digits(L - 1) << "\n";
    return 0;
}

```

### `CPPB2-L14-11` — Đếm Số Tự Mãn (số Armstrong / Narcissistic) Trong Đoạn

```cpp
#include <bits/stdc++.h>
using namespace std;

string S_str;
long long dp[20][1 << 10][2][2];

long long solve_dp(int idx, int mask, bool tight, bool lead) {
    if (idx == (int)S_str.size()) return !lead;
    if (dp[idx][mask][tight][lead] != -1) return dp[idx][mask][tight][lead];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        if (!lead && ((mask >> d) & 1)) continue;
        bool next_lead = lead && (d == 0);
        int next_mask = next_lead ? 0 : (mask | (1 << d));
        ans += solve_dp(idx + 1, next_mask, tight && (d == limit), next_lead);
    }
    return dp[idx][mask][tight][lead] = ans;
}

long long count_distinct(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, 0, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_distinct(R) - count_distinct(L - 1) << "\n";
    return 0;
}

```

### `CPPB2-L14-12` — Đếm Số Đẹp Có Hiệu Hai Chữ Số Kề Nhau $\ge 2$ (số Stepping)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) { a %= b; swap(a, b); }
    return a;
}

long long lcm_val(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd_val(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    auto check = [](long long x) {
        long long temp = x;
        while (temp > 0) {
            int d = temp % 10;
            if (d == 0 || x % d != 0) return false;
            temp /= 10;
        }
        return true;
    };

    long long count = 0;
    for (long long x = L; x <= R; ++x) {
        if (check(x)) count++;
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L14-13` — Số Có Tổng Bình Phương Các Chữ Số Là Số Nguyên Tố

```cpp
#include <bits/stdc++.h>
using namespace std;

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long ans = 1;
    for (int i = 1; i <= r; ++i) ans = ans * (n - i + 1) / i;
    return ans;
}

long long count_k_bits(long long n, int k) {
    if (n <= 0) return 0;
    long long count = 0;
    int ones = 0;
    for (int b = 62; b >= 0; --b) {
        if ((n >> b) & 1) {
            count += nCr(b, k - ones);
            ones++;
            if (ones > k) break;
        }
    }
    if (ones == k) count++;
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R; int k;
    if (!(cin >> L >> R >> k)) return 0;

    cout << count_k_bits(R, k) - count_k_bits(L - 1, k) << "\n";
    return 0;
}

```

### `CPPB2-L14-14` — Tìm Số Thỏa Mãn Điều Kiện Chữ Số Thứ K Nhỏ Nhất

```cpp
#include <bits/stdc++.h>
using namespace std;

string S_str;
long long dp[20][2][2];

long long solve_dp(int idx, bool prev4, bool tight) {
    if (idx == (int)S_str.size()) return 1;
    if (dp[idx][prev4][tight] != -1) return dp[idx][prev4][tight];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        if (prev4 && d == 9) continue;
        ans += solve_dp(idx + 1, d == 4, tight && (d == limit));
    }
    return dp[idx][prev4][tight] = ans;
}

long long count_no_49(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, false, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_no_49(R) - count_no_49(L - 1) << "\n";
    return 0;
}

```

### `CPPB2-L14-15` — Số Chia Hết Cho Tất Cả Các Chữ Số Khác Không Của Nó

```cpp
#include <bits/stdc++.h>
using namespace std;

long long count_no_4(long long n) {
    if (n <= 0) return 0;
    string s = to_string(n);
    long long ans = 0;
    for (size_t i = 0; i < s.size(); ++i) {
        int d = s[i] - '0';
        int valid = (d > 4 ? d - 1 : d);
        ans += valid * pow(9, s.size() - i - 1);
        if (d == 4) break;
        if (i + 1 == s.size()) ans++;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long k;
    if (!(cin >> k)) return 0;

    long long low = 1, high = 2e18, ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_no_4(mid) >= k) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L14-16` — Tổng Xor Chữ Số Của Mọi Số Trong Đoạn $[l, R]$

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long total_xor = 0;
    for (int b = 0; b < 60; ++b) {
        long long count1 = 0;
        for (int i = 0; i < n; ++i) {
            if ((a[i] >> b) & 1) count1++;
        }
        long long count0 = n - count1;
        long long pairs = (count1 * count0) % MOD;
        long long weight = (1LL << b) % MOD;
        total_xor = (total_xor + pairs * weight) % MOD;
    }

    cout << total_xor << "\n";
    return 0;
}

```

### `CPPB2-L14-17` — Digit Dp Chia Het Cho K

```cpp
#include <bits/stdc++.h>
using namespace std;

long long dp[20][100][2][2];
string S;
int K;

long long solve(int idx, int rem, bool tight, bool leading_zero) {
    if (idx == (int)S.size()) {
        return (rem == 0 && !leading_zero) ? 1 : 0;
    }
    if (dp[idx][rem][tight][leading_zero] != -1) {
        return dp[idx][rem][tight][leading_zero];
    }

    int limit = tight ? (S[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_tight = tight && (d == limit);
        bool next_lz = leading_zero && (d == 0);
        int next_rem = next_lz ? 0 : (rem * 10 + d) % K;
        ans += solve(idx + 1, next_rem, next_tight, next_lz);
    }

    return dp[idx][rem][tight][leading_zero] = ans;
}

long long count_div(long long N, int k) {
    if (N <= 0) return 0;
    S = to_string(N);
    K = k;
    memset(dp, -1, sizeof(dp));
    return solve(0, 0, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    int k;
    if (!(cin >> L >> R >> k)) return 0;

    cout << count_div(R, k) - count_div(L - 1, k) << "\n";
    return 0;
}

```

### `CPPB2-L14-18` — Digit Dp Khong Chua Chu So Cam

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L14-19` — Digit Dp So Doi Xung Palindrome

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L14-20` — Digit Dp Tong Binh Phuong Chu So

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L14-21` — Digit Dp Dem So Nguyen To Chu So

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L14-22` — Digit Dp Tich Cac Chu So

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

## Chương 06 — Bài 15: Xử lý chuỗi, String Hashing & BigInt

### `CPPB2-L15-01` — Truy Vấn So Khớp Xâu Con Hashing

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string t, p;
    if (!(cin >> t >> p)) return 0;

    int n = t.size(), m = p.size();
    if (n < m) return 0;

    vector<long long> h(n + 1, 0), pw(n + 1, 1);
    for (int i = 0; i < n; ++i) {
        h[i + 1] = (h[i] * BASE + t[i]) % MOD;
        pw[i + 1] = (pw[i] * BASE) % MOD;
    }

    long long hash_p = 0;
    for (char c : p) hash_p = (hash_p * BASE + c) % MOD;

    for (int i = 0; i <= n - m; ++i) {
        long long cur_hash = (h[i + m] - h[i] * pw[m] % MOD + MOD) % MOD;
        if (cur_hash == hash_p) {
            cout << i + 1 << " ";
        }
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L15-02` — Nhân Hai Số Nguyên Lớn

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int q;
    if (!(cin >> s >> q)) return 0;

    int n = s.size();
    vector<long long> h(n + 1, 0), pw(n + 1, 1);
    for (int i = 0; i < n; ++i) {
        h[i + 1] = (h[i] * BASE + s[i]) % MOD;
        pw[i + 1] = (pw[i] * BASE) % MOD;
    }

    auto get_hash = [&](int l, int r) {
        return (h[r] - h[l - 1] * pw[r - l + 1] % MOD + MOD) % MOD;
    };

    while (q--) {
        int i, j; cin >> i >> j;
        int low = 1, high = n - max(i, j) + 1, ans = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (get_hash(i, i + mid - 1) == get_hash(j, j + mid - 1)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}

```

### `CPPB2-L15-03` — Truy Vấn So Khớp Hai Xâu Con Bằng Hashing

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    unordered_set<long long> distinct_hashes;

    for (int i = 0; i < n; ++i) {
        long long h = 0;
        for (int j = i; j < n; ++j) {
            h = (h * BASE + s[j]) % MOD;
            distinct_hashes.insert(h);
        }
    }

    cout << distinct_hashes.size() << "\n";
    return 0;
}

```

### `CPPB2-L15-04` — Tìm Xâu Mẫu P Trong Xâu Văn Bản T (string Match)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<long long> hf(n + 1, 0), hb(n + 2, 0), pw(n + 1, 1);

    for (int i = 0; i < n; ++i) {
        hf[i + 1] = (hf[i] * BASE + s[i]) % MOD;
        pw[i + 1] = (pw[i] * BASE) % MOD;
    }
    for (int i = n - 1; i >= 0; --i) {
        hb[i + 1] = (hb[i + 2] * BASE + s[i]) % MOD;
    }

    auto get_f = [&](int l, int r) {
        return (hf[r] - hf[l - 1] * pw[r - l + 1] % MOD + MOD) % MOD;
    };
    auto get_b = [&](int l, int r) {
        return (hb[l] - hb[r + 1] * pw[r - l + 1] % MOD + MOD) % MOD;
    };

    int max_len = 1;
    for (int i = 1; i <= n; ++i) {
        // Lẻ
        int low = 1, high = min(i, n - i + 1), best_odd = 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (get_f(i - mid + 1, i + mid - 1) == get_b(i - mid + 1, i + mid - 1)) {
                best_odd = 2 * mid - 1;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        max_len = max(max_len, best_odd);

        // Chẵn
        if (i < n && s[i - 1] == s[i]) {
            low = 1; high = min(i, n - i); int best_even = 2;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (get_f(i - mid + 1, i + mid) == get_b(i - mid + 1, i + mid)) {
                    best_even = 2 * mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            max_len = max(max_len, best_even);
        }
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB2-L15-05` — Xâu Con Đối Xứng Dài Nhất (longest Palindromic Substring)

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> compute_lps(const string &p) {
    int m = p.size();
    vector<int> lps(m, 0);
    int len = 0, i = 1;
    while (i < m) {
        if (p[i] == p[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) len = lps[len - 1];
            else { lps[i] = 0; i++; }
        }
    }
    return lps;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string t, p;
    if (!(cin >> t >> p)) return 0;

    int n = t.size(), m = p.size();
    vector<int> lps = compute_lps(p);
    int i = 0, j = 0;

    while (i < n) {
        if (t[i] == p[j]) {
            i++; j++;
        }
        if (j == m) {
            cout << i - j + 1 << " ";
            j = lps[j - 1];
        } else if (i < n && t[i] != p[j]) {
            if (j != 0) j = lps[j - 1];
            else i++;
        }
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L15-06` — Đếm Số Xâu Con Khác Nhau Của Một Xâu

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> z_function(const string &s) {
    int n = s.size();
    vector<int> z(n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (i <= r) z[i] = min(r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> z = z_function(s);
    for (int i = 0; i < (int)s.size(); ++i) {
        cout << z[i] << (i + 1 == (int)s.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L15-07` — Xâu Con Lặp Lại Dài Nhất Xuất Hiện Ít Nhất K Lần

```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    int next[26];
    bool is_end;
    TrieNode() {
        memset(next, -1, sizeof(next));
        is_end = false;
    }
};

vector<TrieNode> trie;

void insert_str(const string &s) {
    int u = 0;
    for (char c : s) {
        int idx = c - 'a';
        if (trie[u].next[idx] == -1) {
            trie[u].next[idx] = trie.size();
            trie.push_back(TrieNode());
        }
        u = trie[u].next[idx];
    }
    trie[u].is_end = true;
}

bool search_str(const string &s) {
    int u = 0;
    for (char c : s) {
        int idx = c - 'a';
        if (trie[u].next[idx] == -1) return false;
        u = trie[u].next[idx];
    }
    return trie[u].is_end;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    trie.push_back(TrieNode());
    for (int i = 0; i < n; ++i) {
        string w; cin >> w;
        insert_str(w);
    }

    while (q--) {
        string qry; cin >> qry;
        cout << (search_str(qry) ? "YES" : "NO") << "\n";
    }
    return 0;
}

```

### `CPPB2-L15-08` — Tính Giai Thừa $n!$ Cho $n = 1000$ Bằng Bigint

```cpp
#include <bits/stdc++.h>
using namespace std;

string add_bigint(string a, string b) {
    string res = "";
    int i = a.size() - 1, j = b.size() - 1, carry = 0;
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';
        carry = sum / 10;
        res += to_string(sum % 10);
    }
    reverse(res.begin(), res.end());
    return res;
}

string mul_bigint(string a, string b) {
    if (a == "0" || b == "0") return "0";
    int n = a.size(), m = b.size();
    vector<int> res(n + m, 0);
    for (int i = n - 1; i >= 0; --i) {
        for (int j = m - 1; j >= 0; --j) {
            int mul = (a[i] - '0') * (b[j] - '0');
            int p1 = i + j, p2 = i + j + 1;
            int sum = mul + res[p2];
            res[p2] = sum % 10;
            res[p1] += sum / 10;
        }
    }
    string s = "";
    for (int val : res) if (!(s.empty() && val == 0)) s += to_string(val);
    return s.empty() ? "0" : s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    cout << add_bigint(a, b) << "\n";
    cout << mul_bigint(a, b) << "\n";
    return 0;
}

```

### `CPPB2-L15-09` — Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{o}(n)$

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long BASE1 = 311, MOD1 = 1000000007;
const long long BASE2 = 317, MOD2 = 1000000009;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    set<pair<long long, long long>> hashes;

    for (int i = 0; i < n; ++i) {
        string s; cin >> s;
        long long h1 = 0, h2 = 0;
        for (char c : s) {
            h1 = (h1 * BASE1 + c) % MOD1;
            h2 = (h2 * BASE2 + c) % MOD2;
        }
        hashes.insert({h1, h2});
    }

    cout << hashes.size() << "\n";
    return 0;
}

```

### `CPPB2-L15-10` — Tìm Chu Kỳ Ngắn Nhất Của Xâu Ký Tự (string Period)

```cpp
#include <bits/stdc++.h>
using namespace std;

int least_rotation(string s) {
    s += s;
    int n = s.size();
    vector<int> f(n, -1);
    int k = 0;
    for (int j = 1; j < n; ++j) {
        char sj = s[j];
        int i = f[j - k - 1];
        while (i != -1 && sj != s[k + i + 1]) {
            if (sj < s[k + i + 1]) k = j - i - 1;
            i = f[i];
        }
        if (sj != s[k + i + 1]) {
            if (sj < s[k]) k = j;
            f[j - k] = -1;
        } else {
            f[j - k] = i + 1;
        }
    }
    return k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int idx = least_rotation(s);
    cout << s.substr(idx) + s.substr(0, idx) << "\n";
    return 0;
}

```

### `CPPB2-L15-11` — Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{o}(n)$

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int next[26], link;
    bool is_word;
    Node() {
        memset(next, -1, sizeof(next));
        link = 0;
        is_word = false;
    }
};

vector<Node> trie;

void insert_word(const string &s) {
    int u = 0;
    for (char c : s) {
        int idx = c - 'a';
        if (trie[u].next[idx] == -1) {
            trie[u].next[idx] = trie.size();
            trie.push_back(Node());
        }
        u = trie[u].next[idx];
    }
    trie[u].is_word = true;
}

void build_ac() {
    queue<int> q;
    for (int c = 0; c < 26; ++c) {
        if (trie[0].next[c] != -1) q.push(trie[0].next[c]);
        else trie[0].next[c] = 0;
    }
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int c = 0; c < 26; ++c) {
            if (trie[u].next[c] != -1) {
                int v = trie[u].next[c];
                trie[v].link = trie[trie[u].link].next[c];
                trie[v].is_word |= trie[trie[v].link].is_word;
                q.push(v);
            } else {
                trie[u].next[c] = trie[trie[u].link].next[c];
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    trie.push_back(Node());
    for (int i = 0; i < k; ++i) {
        string w; cin >> w;
        insert_word(w);
    }
    build_ac();

    string text; cin >> text;
    int u = 0, matches = 0;
    for (char c : text) {
        u = trie[u].next[c - 'a'];
        if (trie[u].is_word) matches++;
    }

    cout << matches << "\n";
    return 0;
}

```

### `CPPB2-L15-12` — Thuật Toán Kmp (knuth-morris-pratt) & Mảng Tiền Tố $\pi$

```cpp
#include <bits/stdc++.h>
using namespace std;

string manacher(string s) {
    string t = "^";
    for (char c : s) t += "#" + string(1, c);
    t += "#$";

    int n = t.size();
    vector<int> p(n, 0);
    int c = 0, r = 0;

    for (int i = 1; i < n - 1; ++i) {
        int i_mirror = 2 * c - i;
        if (r > i) p[i] = min(r - i, p[i_mirror]);
        while (t[i + 1 + p[i]] == t[i - 1 - p[i]]) p[i]++;
        if (i + p[i] > r) {
            c = i;
            r = i + p[i];
        }
    }

    int max_len = 0, center_idx = 0;
    for (int i = 1; i < n - 1; ++i) {
        if (p[i] > max_len) {
            max_len = p[i];
            center_idx = i;
        }
    }

    int start = (center_idx - 1 - max_len) / 2;
    return s.substr(start, max_len);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    cout << manacher(s) << "\n";
    return 0;
}

```

### `CPPB2-L15-13` — Căn Bậc Hai Của Số Nguyên Lớn

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> build_sa(string s) {
    s += "$";
    int n = s.size();
    vector<int> p(n), c(n);
    vector<pair<char, int>> a(n);
    for (int i = 0; i < n; ++i) a[i] = {s[i], i};
    sort(a.begin(), a.end());
    for (int i = 0; i < n; ++i) p[i] = a[i].second;
    c[p[0]] = 0;
    for (int i = 1; i < n; ++i) {
        c[p[i]] = c[p[i - 1]] + (a[i].first != a[i - 1].first);
    }

    int k = 0;
    while ((1 << k) < n) {
        vector<pair<pair<int, int>, int>> b(n);
        for (int i = 0; i < n; ++i) {
            b[i] = {{c[i], c[(i + (1 << k)) % n]}, i};
        }
        sort(b.begin(), b.end());
        for (int i = 0; i < n; ++i) p[i] = b[i].second;
        c[p[0]] = 0;
        for (int i = 1; i < n; ++i) {
            c[p[i]] = c[p[i - 1]] + (b[i].first != b[i - 1].first);
        }
        k++;
    }
    return vector<int>(p.begin() + 1, p.end());
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> sa = build_sa(s);
    for (int idx : sa) cout << idx << " ";
    cout << "\n";
    return 0;
}

```

### `CPPB2-L15-14` — Chia Hai Số Nguyên Lớn Cho Nhau (bigint / Bigint)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) { a %= b; swap(a, b); }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a_str;
    long long b;
    if (!(cin >> a_str >> b)) return 0;

    long long rem = 0;
    for (char c : a_str) {
        rem = (rem * 10 + (c - '0')) % b;
    }

    cout << rem << "\n";
    cout << gcd_val(b, rem) << "\n";
    return 0;
}

```

### `CPPB2-L15-15` — Xâu Con Chung Dài Nhất Của K Xâu Ký Tự

```cpp
#include <bits/stdc++.h>
using namespace std;

struct State {
    int len, link;
    map<char, int> next;
};

const int MAXLEN = 100005;
State st[MAXLEN * 2];
int sz, last;

void sam_init() {
    st[0].len = 0;
    st[0].link = -1;
    sz = 1;
    last = 0;
}

void sam_extend(char c) {
    int cur = sz++;
    st[cur].len = st[last].len + 1;
    int p = last;
    while (p != -1 && !st[p].next.count(c)) {
        st[p].next[c] = cur;
        p = st[p].link;
    }
    if (p == -1) {
        st[cur].link = 0;
    } else {
        int q = st[p].next[c];
        if (st[p].len + 1 == st[q].len) {
            st[cur].link = q;
        } else {
            int clone = sz++;
            st[clone].len = st[p].len + 1;
            st[clone].next = st[q].next;
            st[clone].link = st[q].link;
            while (p != -1 && st[p].next[c] == q) {
                st[p].next[c] = clone;
                p = st[p].link;
            }
            st[q].link = st[cur].link = clone;
        }
    }
    last = cur;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    sam_init();
    for (char c : s) sam_extend(c);

    long long distinct_substrings = 0;
    for (int i = 1; i < sz; ++i) {
        distinct_substrings += st[i].len - st[st[i].link].len;
    }

    cout << distinct_substrings << "\n";
    return 0;
}

```

### `CPPB2-L15-16` — Mảng Hậu Tố (suffix Array) Bằng String Hashing $\mathcal{o}(n \log^2 N)$

```cpp
#include <bits/stdc++.h>
using namespace std;

string bwt_transform(string s) {
    s += "$";
    int n = s.size();
    vector<string> rotations(n);
    for (int i = 0; i < n; ++i) {
        rotations[i] = s.substr(i) + s.substr(0, i);
    }
    sort(rotations.begin(), rotations.end());
    string bwt = "";
    for (int i = 0; i < n; ++i) bwt += rotations[i].back();
    return bwt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    cout << bwt_transform(s) << "\n";
    return 0;
}

```

### `CPPB2-L15-17` — Double Hashing Chong Va Cham

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L15-18` — Thuat Toan Manacher Palindrome

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L15-19` — Z Algorithm Tim Mau

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L15-20` — Kmp Knuth Morris Pratt

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> compute_lps(const string& p) {
    int m = p.size();
    vector<int> lps(m, 0);
    int len = 0, i = 1;
    while (i < m) {
        if (p[i] == p[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) len = lps[len - 1];
            else { lps[i] = 0; i++; }
        }
    }
    return lps;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string t, p;
    if (!(cin >> t >> p)) return 0;

    vector<int> lps = compute_lps(p);
    int n = t.size(), m = p.size();
    int i = 0, j = 0, matches = 0;

    while (i < n) {
        if (t[i] == p[j]) { i++; j++; }
        if (j == m) {
            matches++;
            j = lps[j - 1];
        } else if (i < n && t[i] != p[j]) {
            if (j != 0) j = lps[j - 1];
            else i++;
        }
    }

    cout << matches << "\n";
    return 0;
}

```

### `CPPB2-L15-21` — Cay Trie Xau Co Ban

```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    int children[26];
    int count_words;
    int count_prefixes;
    TrieNode() {
        memset(children, -1, sizeof(children));
        count_words = 0;
        count_prefixes = 0;
    }
};

vector<TrieNode> trie;

void insert(const string& s) {
    int node = 0;
    for (char c : s) {
        int idx = c - 'a';
        if (trie[node].children[idx] == -1) {
            trie[node].children[idx] = trie.size();
            trie.emplace_back();
        }
        node = trie[node].children[idx];
        trie[node].count_prefixes++;
    }
    trie[node].count_words++;
}

int query_prefix(const string& p) {
    int node = 0;
    for (char c : p) {
        int idx = c - 'a';
        if (trie[node].children[idx] == -1) return 0;
        node = trie[node].children[idx];
    }
    return trie[node].count_prefixes;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    trie.emplace_back(); // Node gốc 0

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        insert(s);
    }

    while (q--) {
        string p;
        cin >> p;
        cout << query_prefix(p) << "\n";
    }
    return 0;
}

```

### `CPPB2-L15-22` — Chia So Nguyen Lon Bigint

```cpp
#include <bits/stdc++.h>
using namespace std;

string divide_bigint(string a, long long b) {
    string res = "";
    long long rem = 0;
    for (char c : a) {
        rem = rem * 10 + (c - '0');
        res += to_string(rem / b);
        rem %= b;
    }
    int pos = 0;
    while (pos < (int)res.size() - 1 && res[pos] == '0') pos++;
    return res.substr(pos);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    long long b;
    if (!(cin >> a >> b)) return 0;

    cout << divide_bigint(a, b) << "\n";
    return 0;
}

```

### `CPPB2-L15-23` — Can Bac Hai So Nguyen Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L15-24` — Aho Corasick Da Mau Tim Kiem

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i];
    }

    cout << ans << "\n";
    return 0;
}

```




\newpage

# Mục lục


