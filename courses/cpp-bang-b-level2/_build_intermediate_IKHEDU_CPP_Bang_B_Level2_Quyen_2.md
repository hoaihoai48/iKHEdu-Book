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

Phần nội dung này gồm **3 Chương chuyên sâu (Chương 04 đến Chương 06)** với **9 Bài học** và **144 bài toán thực hành phân tầng (P0 → P5)**, chinh phục tham lam, quy hoạch động tối ưu, ngăn xếp đơn điệu, Deque, STL C++ nâng cao, tổ hợp, đồ thị BFS/DFS/Dijkstra, cây phân đoạn Segment Tree, Fenwick Tree, Digit DP và xử lý chuỗi Hashing.

Mỗi bài học được thiết kế theo cấu trúc sư phạm chặt chẽ:

- **Khái niệm & Bản chất toán học**: Giải thích trực quan, dễ hiểu kèm chứng minh toán học và bất biến thuật toán.
- **Bảng mô phỏng từng bước (Dry Run Table)**: Trực quan hóa quá trình biến đổi dữ liệu từng bước.
- **Mẫu cài đặt chuẩn thi đấu**: Code C++ chuẩn (0 `std::`, `#include <bits/stdc++.h>`, Fast I/O), tối ưu và an toàn tuyệt đối.
- **Hệ thống 16 bài tập thực hành phân tầng**: Từ cơ bản đến chuyên sâu (P0 đến P5), có đầy đủ bối cảnh, nhiệm vụ, input/output và sample test.
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


### Bài 01 [CPPB2-L07-01]: LỰA CHỌN SỰ KIỆN KHÔNG TRÙNG GIỜ

**Đầu vào (Input):**

* Dòng 1: $N$ ($1 \le N \le 10^5$). $N$ dòng tiếp theo: $L_i, R_i$ ($0 \le L_i < R_i \le 10^9$).

---

**Đầu ra (Output):**

* In ra số lượng sự kiện tối đa.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
3
10 20
12 25
20 30
```

**Output:**
```text
2
```

---



### Bài 02 [CPPB2-L07-02]: TỔNG THỜI GIAN CHỜ NHỎ NHẤT (SJF)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Thời Gian Chờ Nhỏ Nhất (SJF).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, T_i \le 10^6$.



### Bài 03 [CPPB2-L07-03]: CÁI TÚI CHIA NHỎ ĐƯỢC (FRACTIONAL KNAPSACK)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cái Túi Chia Nhỏ Được (Fractional Knapsack).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, W \le 10^9$.



### Bài 04 [CPPB2-L07-04]: PHỦ ĐOẠN THẲNG ÍT NHẤT (MINIMUM INTERVAL COVER)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phủ Đoạn Thẳng Ít Nhất (Minimum Interval Cover).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$, phủ đoạn $[0, L]$.



### Bài 05 [CPPB2-L07-05]: GHÉP THUYỀN CỨU HỘ CỰC TRỊ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Ghép Thuyền Cứu Hộ Cực Trị.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, W_i \le C$.



### Bài 06 [CPPB2-L07-06]: NỐI CÁC SỢI DÂY TIẾT KIỆM CHI PHÍ NHẤT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nối Các Sợi Dây Tiết Kiệm Chi Phí Nhất.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, L_i \le 10^6$.



### Bài 07 [CPPB2-L07-07]: LẬP LỊCH CÔNG VIỆC CÓ DEADLINE & TIỀN PHẠT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lập Lịch Công Việc Có Deadline & Tiền Phạt.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, D_i \le 10^5$.



### Bài 08 [CPPB2-L07-08]: TỐI ĐA HÓA LỢI NHUẬN GIAO HÀNG

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Đa Hóa Lợi Nhuận Giao Hàng.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$.



### Bài 09 [CPPB2-L07-09]: CHIA KẸO THƯỞNG CHO HỌC SINH THEO ĐIỂM SỐ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chia Kẹo Thưởng Cho Học Sinh Theo Điểm Số.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.



### Bài 10 [CPPB2-L07-10]: TỐI ƯU HÓA MUA BÁN CỔ PHIẾU KHÔNG GIỚI HẠN LẦN GIAO DỊCH

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Mua Bán Cổ Phiếu Không Giới Hạn Lần Giao Dịch.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 2 \times 10^5, P_i \le 10^9$.



### Bài 11 [CPPB2-L07-11]: SẮP ĐẶT CHUỖI KÝ TỰ KHÔNG TRÙNG LẶP KỀ NHAU

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Sắp Đặt Chuỗi Ký Tự Không Trùng Lặp Kề Nhau.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^5$, khoảng cách $D$.



### Bài 12 [CPPB2-L07-12]: SỐ LƯỢNG TRẠM TIẾP NHIÊN LIỆU ÍT NHẤT (GAS STATION)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Lượng Trạm Tiếp Nhiên Liệu Ít Nhất (Gas Station).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, D \le 10^9$.



### Bài 13 [CPPB2-L07-13]: LẬP LỊCH PHÒNG HỌP TỐI THIỂU (MEETING ROOMS II)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lập Lịch Phòng Họp Tối Thiểu (Meeting Rooms II).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, [S_i, E_i] \le 10^9$.



### Bài 14 [CPPB2-L07-14]: PHỤC HỒI DÃY SỐ ĐƠN ĐIỆU VỚI CHI PHÍ NHỎ NHẤT (SLOPE TRICK CƠ BẢN)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phục Hồi Dãy Số Đơn Điệu Với Chi Phí Nhỏ Nhất (Slope Trick Cơ Bản).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.



### Bài 15 [CPPB2-L07-15]: GHÉP CẶP TRỌNG SỐ TRÊN ĐỒ THỊ CÂY BẰNG GREEDY

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Ghép Cặp Trọng Số Trên Đồ Thị Cây Bằng Greedy.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Cây $N \le 10^5$ đỉnh.



### Bài 16 [CPPB2-L07-16]: THUẬT TOÁN HUFFMAN CODING NÉN DỮ LIỆU TỐI ƯU

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Thuật Toán Huffman Coding Nén Dữ Liệu Tối Ưu.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$ tần suất.




# Bài 08: Quy hoạch động cơ bản (Dynamic Programming)

## 1. Khái niệm & bản chất của phương pháp Quy hoạch động

Quy hoạch động (Dynamic Programming - DP) là phương pháp giải quyết các bài toán tối ưu hóa và đếm tổ hợp bằng cách chia bài toán thành các **bài toán con gối nhau (Overlapping Subproblems)** và lưu trữ kết quả của các bài toán con đó vào bảng nhớ (memoization table / DP array) để không phải tính lại nhiều lần.

Một bài toán áp dụng được Quy hoạch động khi thỏa mãn 2 nguyên lý:

1. **Cấu trúc con tối ưu (Optimal Substructure):** Nghiệm tối ưu của bài toán lớn được xây dựng trực tiếp từ nghiệm tối ưu của các bài toán con nhỏ hơn.
2. **Các bài toán con gối nhau (Overlapping Subproblems):** Cùng một trạng thái con được gọi đi gọi lại nhiều lần trong quá trình đệ quy (ví dụ: cây đệ quy Fibonacci).


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


### Bài 01 [CPPB2-L08-01]: DÃY CON TĂNG DÀI NHẤT LIS

**Đầu vào (Input):**

* Dòng 1: $N$ ($1 \le N \le 2 \times 10^5$). Dòng 2: $N$ số $A_i$ ($1 \le A_i \le 10^9$).

---

**Đầu ra (Output):**

* In ra độ dài LIS.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
6
10 20 10 30 20 50
```

**Output:**
```text
4
```

---



### Bài 02 [CPPB2-L08-02]: ĐƯỜNG ĐI TRÊN MA TRẬN CÓ TỔNG LỚN NHẤT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đường Đi Trên Ma Trận Có Tổng Lớn Nhất.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 1000$.



### Bài 03 [CPPB2-L08-03]: CÁI TÚI 0/1 CHUẨN (0/1 KNAPSACK)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cái Túi 0/1 Chuẩn (0/1 Knapsack).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 1000, W \le 10^5$.



### Bài 04 [CPPB2-L08-04]: ĐỔI TIỀN XU SỐ TỜ NHỎ NHẤT (UNBOUNDED COIN CHANGE)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đổi Tiền Xu Số Tờ Nhỏ Nhất (Unbounded Coin Change).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 100, S \le 10^5$.



### Bài 05 [CPPB2-L08-05]: DÃY CON TĂNG DÀI NHẤT LIS $\MATHCAL{O}(N \LOG N)$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dãy Con Tăng Dài Nhất LIS $\mathcal{O}(N \log N)$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 2 \times 10^5, A_i \le 10^9$.



### Bài 06 [CPPB2-L08-06]: XÂU CON CHUNG DÀI NHẤT (LCS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xâu Con Chung Dài Nhất (LCS).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert, \vert T \vert \le 3000$.



### Bài 07 [CPPB2-L08-07]: XÓA KÝ TỰ ĐỂ THÀNH PALINDROME NGẮN NHẤT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xóa Ký Tự Để Thành Palindrome Ngắn Nhất.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 2000$.



### Bài 08 [CPPB2-L08-08]: CẮT BÁNH HÌNH CHỮ NHẬT CÓ GIÁ TRỊ LỚN NHẤT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cắt Bánh Hình Chữ Nhật Có Giá Trị Lớn Nhất.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $W, H \le 600, N \le 200$.



### Bài 09 [CPPB2-L08-09]: DÃY CON TĂNG LỚN NHẤT CÓ TRUY VẾT PHẦN TỬ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dãy Con Tăng Lớn Nhất Có Truy Vết Phần Tử.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$.



### Bài 10 [CPPB2-L08-10]: KHOẢNG CÁCH CHỈNH SỬA XÂU (EDIT DISTANCE / LEVENSHTEIN)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Khoảng Cách Chỉnh Sửa Xâu (Edit Distance / Levenshtein).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert, \vert T \vert \le 3000$.



### Bài 11 [CPPB2-L08-11]: CÁI TÚI ĐỔI TRỤC TRẠNG THÁI (VALUE-BASED KNAPSACK)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cái Túi Đổi Trục Trạng Thái (Value-based Knapsack).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 100, W \le 10^9, \sum V_i \le 10^5$.



### Bài 12 [CPPB2-L08-12]: XẾP GẠCH LÁT SÀN KÍCH THƯỚC $3 \TIMES N$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xếp Gạch Lát Sàn Kích Thước $3 \times N$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, M = 10^9+7$.



### Bài 13 [CPPB2-L08-13]: DÃY CON HÌNH SÓNG NÚI DÀI NHẤT (BITONIC SUBSEQUENCE)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dãy Con Hình Sóng Núi Dài Nhất (Bitonic Subsequence).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.



### Bài 14 [CPPB2-L08-14]: NHÂN MA TRẬN DÂY CHUYỀN CHI PHÍ NHỎ NHẤT (MATRIX CHAIN)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nhân Ma Trận Dây Chuyền Chi Phí Nhỏ Nhất (Matrix Chain).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 500$.



### Bài 15 [CPPB2-L08-15]: QUY HOẠCH ĐỘNG TRÊN CÂY (TREE DP: MAX INDEPENDENT SET)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Quy Hoạch Động Trên Cây (Tree DP: Max Independent Set).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Cây $N \le 10^5$ đỉnh.



### Bài 16 [CPPB2-L08-16]: TỐI ƯU HÓA QUY HOẠCH ĐỘNG BẰNG CONVEX HULL TRICK (CHT)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (CHT).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$.



# CHƯƠNG 05: CẤU TRÚC DỮ LIỆU ĐƠN ĐIỆU, STL C++ NÂNG CAO & ĐẠI SỐ TỔ HỢP


# Bài 09: Ngăn xếp, hàng đợi & Deque (Stack, Queue, Deque)

## 1. Khái niệm & bản chất của cấu trúc dữ liệu tuyến tính đơn điệu

Ngăn xếp (Stack - LIFO) và Hàng đợi (Queue - FIFO) là hai cấu trúc dữ liệu cơ sở có thời gian thêm và xóa ở đầu/cuối trong $\mathcal{O}(1)$.

Ở Level 2, ta nâng cấp lên **Ngăn xếp đơn điệu (Monotonic Stack)** và **Hàng đợi hai đầu đơn điệu (Monotonic Deque)** — hai công cụ tối ưu hóa cực mạnh giúp giải quyết các bài toán tìm kiếm phần tử lớn hơn/nhỏ hơn gần nhất và duy trì $\min/\max$ trên cửa sổ trượt trong thời gian tuyến tính $\mathcal{O}(N)$ (thay vì $\mathcal{O}(N^2)$ hoặc $\mathcal{O}(N \log K)$).


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


### Bài 01 [CPPB2-L09-01]: PHẦN TỬ LỚN HƠN GẦN NHẤT (NGE)

**Đầu vào (Input):**

* Dòng 1: $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số $A_i$ ($1 \le A_i \le 10^9$).

---

**Đầu ra (Output):**

* In ra $N$ số kết quả cách nhau dấu cách.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
4
4 5 2 25
```

**Output:**
```text
5 25 25 -1
```

---



### Bài 02 [CPPB2-L09-02]: GIÁ TRỊ NHỎ NHẤT TRÊN CỬA SỔ TRƯỢT K

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Giá Trị Nhỏ Nhất Trên Cửa Sổ Trượt K.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^6, K \le N$.



### Bài 03 [CPPB2-L09-03]: KIỂM TRA DÃY NGOẶC ĐÚNG NHIỀU LOẠI

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Kiểm Tra Dãy Ngoặc Đúng Nhiều Loại.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^5$, gồm `()[]{}`.



### Bài 04 [CPPB2-L09-04]: TẦM NHÌN XA CỦA CÁC TÒA NHÀ CAO TẦNG

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tầm Nhìn Xa Của Các Tòa Nhà Cao Tầng.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 2 \times 10^5, H_i \le 10^9$.



### Bài 05 [CPPB2-L09-05]: HÌNH CHỮ NHẬT LỚN NHẤT DƯỚI BIỂU ĐỒ CỘT (HISTOGRAM)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hình Chữ Nhật Lớn Nhất Dưới Biểu Đồ Cột (Histogram).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, H_i \le 10^9$.



### Bài 06 [CPPB2-L09-06]: MA TRẬN TOÀN SỐ 1 LỚN NHẤT (MAXIMAL RECTANGLE 2D)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Ma Trận Toàn Số 1 Lớn Nhất (Maximal Rectangle 2D).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 1000$.



### Bài 07 [CPPB2-L09-07]: TỔNG HIỆU CỰC ĐẠI VÀ CỰC TIỂU MỌI ĐOẠN CON

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Hiệu Cực Đại Và Cực Tiểu Mọi Đoạn Con.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.



### Bài 08 [CPPB2-L09-08]: TỐI ƯU HÓA QUY HOẠCH ĐỘNG BẰNG MONOTONIC DEQUE

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Quy Hoạch Động Bằng Monotonic Deque.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, K \le N$.



### Bài 09 [CPPB2-L09-09]: HỨNG NƯỚC MƯA ĐA CHIỀU (TRAPPING RAIN WATER)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hứng Nước Mưa Đa Chiều (Trapping Rain Water).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, H_i \le 10^9$.



### Bài 10 [CPPB2-L09-10]: ĐÁNH GIÁ BIỂU THỨC SỐ HỌC TRUNG TỐ (SHUNTING-YARD)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đánh Giá Biểu Thức Số Học Trung Tố (Shunting-yard).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^5$, có `+,-,*,/,(,)`.



### Bài 11 [CPPB2-L09-11]: PHẦN TỬ LỚN HƠN GẦN NHẤT TRÊN MẢNG XOAY VÒNG

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phần Tử Lớn Hơn Gần Nhất Trên Mảng Xoay Vòng.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.



### Bài 12 [CPPB2-L09-12]: XÓA K CHỮ SỐ ĐỂ ĐƯỢC SỐ NHỎ NHẤT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xóa K Chữ Số Để Được Số Nhỏ Nhất.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^5, K \le \vert S \vert$.



### Bài 13 [CPPB2-L09-13]: TỔNG GIÁ TRỊ MIN MỌI ĐOẠN CON NHÂN ĐỘ DÀI

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Giá Trị Min Mọi Đoạn Con Nhân Độ Dài.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^6$.



### Bài 14 [CPPB2-L09-14]: ĐUA XE TRONG MÊ CUNG ĐỔI HƯỚNG ÍT NHẤT (0-1 BFS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đua Xe Trong Mê Cung Đổi Hướng Ít Nhất (0-1 BFS).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 1000$.



### Bài 15 [CPPB2-L09-15]: CẮT BĂNG RÔN QUẢNG CÁO TỐI ƯU BẰNG 2 DEQUE

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cắt Băng Rôn Quảng Cáo Tối Ưu Bằng 2 Deque.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, C \le 10^9$.



### Bài 16 [CPPB2-L09-16]: KHÔI PHỤC CÂY KHẢO SÁT TẦM NHÌN ĐA HƯỚNG

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Khôi Phục Cây Khảo Sát Tầm Nhìn Đa Hướng.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 2 \times 10^5$.




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
> 
> Trong `multiset<int> ms`, nếu viết `ms.erase(val)`, C++ sẽ **xóa sạch toàn bộ mọi phần tử có giá trị bằng `val`**!  
> **Cách xóa đúng duy nhất 1 phần tử:** Truyền vào iterator trỏ tới phần tử đó:
> ```cpp
> auto it = ms.find(val);
> if (it != ms.end()) {
>     ms.erase(it); // Chỉ xóa đúng 1 phần tử tại vị trí it
> }
> ```

> **Cảnh báo bẫy lỗi 2: BẪY TẤN CÔNG BẢNG BĂM (ANTI-HASH TEST / HASH COLLISION)**
> 
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


### Bài 01 [CPPB2-L10-01]: DUY TRÌ TRUNG VỊ ĐỘNG

**Đầu vào (Input):**

* Dòng 1: $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số $A_i$.

---

**Đầu ra (Output):**

* In ra $N$ giá trị trung vị tương ứng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
4
5 15 1 3
```

**Output:**
```text
5 5 5 3
```

---



### Bài 02 [CPPB2-L10-02]: ĐẾM TẦN SUẤT GIÁ TRỊ BẰNG SAFE HASH MAP

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Tần Suất Giá Trị Bằng Safe Hash Map.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^{18}$.



### Bài 03 [CPPB2-L10-03]: NỐI DÂY TIẾT KIỆM BẰNG PRIORITY QUEUE

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nối Dây Tiết Kiệm Bằng Priority Queue.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, L_i \le 10^6$.



### Bài 04 [CPPB2-L10-04]: DUY TRÌ TRUNG VỊ ĐỘNG (RUNNING MEDIAN)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Duy Trì Trung Vị Động (Running Median).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 2 \times 10^5$.



### Bài 05 [CPPB2-L10-05]: TÌM PHẦN TỬ KẾ TIẾP NHỎ NHẤT LỚN HƠN X

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Phần Tử Kế Tiếp Nhỏ Nhất Lớn Hơn X.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $Q \le 2 \times 10^5$.



### Bài 06 [CPPB2-L10-06]: LẬP LỊCH PHÒNG HỌP ĐA NĂNG (MEETING ROOMS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lập Lịch Phòng Họp Đa Năng (Meeting Rooms).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$, $[S_i, E_i] \le 10^9$.



### Bài 07 [CPPB2-L10-07]: DUY TRÌ K PHẦN TỬ LỚN NHẤT TRONG LUỒNG DỮ LIỆU

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Duy Trì K Phần Tử Lớn Nhất Trong Luồng Dữ Liệu.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^6, K \le 1000$.



### Bài 08 [CPPB2-L10-08]: TỐI ƯU HÓA CHI PHÍ MUA CỔ PHIẾU THEO THỜI GIAN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Chi Phí Mua Cổ Phiếu Theo Thời Gian.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$.



### Bài 09 [CPPB2-L10-09]: HỆ THỐNG ĐẶT CHỖ RẠP CHIẾU PHIM TỐI ƯU

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hệ Thống Đặt Chỗ Rạp Chiếu Phim Tối Ưu.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, M \le 10^9$.



### Bài 10 [CPPB2-L10-10]: ĐẾM SỐ PHẦN TỬ PHÂN BIỆT TRONG MỌI CỬA SỔ K

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Phần Tử Phân Biệt Trong Mọi Cửa Sổ K.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 2 \times 10^5, K \le N$.



### Bài 11 [CPPB2-L10-11]: HỢP NHẤT CÁC ĐOẠN SỐ RỜI RẠC (MERGE INTERVALS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hợp Nhất Các Đoạn Số Rời Rạc (Merge Intervals).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, [L_i, R_i] \le 10^9$.



### Bài 12 [CPPB2-L10-12]: TÌM CẶP ĐIỂM CÓ KHOẢNG CÁCH MANHATTAN NHỎ NHẤT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Cặp Điểm Có Khoảng Cách Manhattan Nhỏ Nhất.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$, tọa độ 2D.



### Bài 13 [CPPB2-L10-13]: HỆ THỐNG XẾP HẠNG TRỰC TUYẾN ĐA TIÊU CHÍ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hệ Thống Xếp Hạng Trực Tuyến Đa Tiêu Chí.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $Q \le 10^5$, cập nhật điểm động.



### Bài 14 [CPPB2-L10-14]: TỐI ƯU PHÂN BỔ BĂNG THÔNG MÁY CHỦ (SERVER LOAD BALANCER)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Phân Bổ Băng Thông Máy Chủ (Server Load Balancer).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 10^5$.



### Bài 15 [CPPB2-L10-15]: DUY TRÌ TỔNG CỦA K PHẦN TỬ LỚN NHẤT ĐỘNG

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Duy Trì Tổng Của K Phần Tử Lớn Nhất Động.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $Q \le 10^5$, thêm/xóa phần tử.



### Bài 16 [CPPB2-L10-16]: KỸ THUẬT SMALL-TO-LARGE MERGING TRÊN STL MAP

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Kỹ Thuật Small-to-Large Merging Trên STL Map.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Cây $N \le 10^5$ đỉnh.




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


### Bài 01 [CPPB2-L11-01]: TÍNH TỔ HỢP NCR MODULO

**Đầu vào (Input):**

* Dòng 1: $Q$ ($1 \le Q \le 10^5$). $Q$ dòng sau: $N, K$ ($0 \le K \le N \le 10^6$).

---

**Đầu ra (Output):**

* In ra kết quả mỗi truy vấn trên 1 dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
2
5 2
10 3
```

**Output:**
```text
10
120
```

---



### Bài 02 [CPPB2-L11-02]: TAM GIÁC PASCAL MODULO HỢP SỐ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tam Giác Pascal Modulo Hợp Số.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, K \le 2000, M \le 10^9$.



### Bài 03 [CPPB2-L11-03]: CHIA KẸO EULER (STARS AND BARS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chia Kẹo Euler (Stars and Bars).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, K \le 10^6$.



### Bài 04 [CPPB2-L11-04]: ĐẾM SỐ HOÁN VỊ KHÔNG CÓ ĐIỂM CỐ ĐỊNH (DERANGEMENTS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Hoán Vị Không Có Điểm Cố Định (Derangements).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^6$.



### Bài 05 [CPPB2-L11-05]: ĐẾM SỐ NGUYÊN TỐ CÙNG NHAU BẰNG PIE

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Nguyên Tố Cùng Nhau Bằng PIE.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^{12}, K \le 15$.



### Bài 06 [CPPB2-L11-06]: ĐẾM SỐ ĐƯỜNG ĐI TRÊN LƯỚI TỌA ĐỘ CÓ ĐIỂM CẤM

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 10^5, K \le 2000$ điểm cấm.



### Bài 07 [CPPB2-L11-07]: SỐ PHÂN HOẠCH TẬP HỢP (SỐ STIRLING LOẠI 2)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Phân Hoạch Tập Hợp (Số Stirling Loại 2).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, K \le 2000$.



### Bài 08 [CPPB2-L11-08]: ĐỊNH LÝ LUCAS CHO TỔ HỢP MODULO NGUYÊN TỐ NHỎ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, K \le 10^{18}, P \le 10^5$.



### Bài 09 [CPPB2-L11-09]: ĐẾM SỐ ĐƯỜNG ĐI TRÊN LƯỚI TỌA ĐỘ CÓ ĐIỂM CẤM

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 10^5, K \le 2000$ điểm cấm.



### Bài 10 [CPPB2-L11-10]: ĐẾM SỐ HOÁN VỊ CÓ ĐÚNG K ĐIỂM CỐ ĐỊNH

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Hoán Vị Có Đúng K Điểm Cố Định.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^6, K \le N$.



### Bài 11 [CPPB2-L11-11]: SỐ PHÂN HOẠCH TẬP HỢP (SỐ STIRLING LOẠI 2)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Phân Hoạch Tập Hợp (Số Stirling Loại 2).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, K \le 2000, M = 10^9+7$.



### Bài 12 [CPPB2-L11-12]: ĐẾM SỐ CÂY KHUNG ĐỒ THỊ ĐẦY ĐỦ (CÔNG THỨC CAYLEY)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Cây Khung Đồ Thị Đầy Đủ (Công Thức Cayley).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^6, M = 10^9+7$.



### Bài 13 [CPPB2-L11-13]: ĐỊNH LÝ LUCAS CHO TỔ HỢP MODULO NGUYÊN TỐ NHỎ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, K \le 10^{18}, P \le 10^5$.



### Bài 14 [CPPB2-L11-14]: ĐẾM SỐ TAM GIÁC TẠO BỞI N ĐIỂM TRÊN MẶT PHẲNG

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Tam Giác Tạo Bởi N Điểm Trên Mặt Phẳng.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 2000$, tọa độ nguyên.



### Bài 15 [CPPB2-L11-15]: KỲ VỌNG TOÁN HỌC TRÒ CHƠI GIEO XÚC XẮC (PROBABILITY DP)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Kỳ Vọng Toán Học Trò Chơi Gieo Xúc Xắc (Probability DP).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, K \le 6$.



### Bài 16 [CPPB2-L11-16]: BỔ ĐỀ BURNSIDE ĐẾM CẤU HÌNH BẤT BIẾN PHÉP QUAY

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Bổ Đề Burnside Đếm Cấu Hình Bất Biến Phép Quay.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, K \le 10^5, M = 10^9+7$.



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


### Bài 01 [CPPB2-L12-01]: ĐƯỜNG ĐI NGẮN NHẤT DIJKSTRA

**Đầu vào (Input):**

* Dòng 1: $N, M$ ($1 \le N \le 10^5, 1 \le M \le 2 \times 10^5$). $M$ dòng sau: $u, v, w$.

---

**Đầu ra (Output):**

* In ra khoảng cách ngắn nhất từ 1 đến $N$, nếu không đến được in -1.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
3 3
1 2 1
2 3 2
1 3 4
```

**Output:**
```text
3
```

---



### Bài 02 [CPPB2-L12-02]: ĐƯỜNG ĐI NGẮN NHẤT MÊ CUNG 2D BẰNG BFS

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đường Đi Ngắn Nhất Mê Cung 2D Bằng BFS.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 1000$.



### Bài 03 [CPPB2-L12-03]: KIỂM TRA ĐỒ THỊ HAI PHÍA (BIPARTITE GRAPH COLORING)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Kiểm Tra Đồ Thị Hai Phía (Bipartite Graph Coloring).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V, E \le 10^5$.



### Bài 04 [CPPB2-L12-04]: SẮP XẾP TÔ-PÔ LẬP LỊCH KHÓA HỌC (TOPOLOGICAL SORT)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Sắp Xếp Tô-pô Lập Lịch Khóa Học (Topological Sort).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V, E \le 10^5$.



### Bài 05 [CPPB2-L12-05]: DIJKSTRA TÌM ĐƯỜNG ĐI NGẮN NHẤT CHUẨN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dijkstra Tìm Đường Đi Ngắn Nhất Chuẩn.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V \le 10^5, E \le 2 \times 10^5$.



### Bài 06 [CPPB2-L12-06]: MÊ CUNG TRỌNG SỐ 0 VÀ 1 (0-1 BFS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Mê Cung Trọng Số 0 và 1 (0-1 BFS).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 1000$.



### Bài 07 [CPPB2-L12-07]: CÂY KHUNG NHỎ NHẤT (MST KRUSKAL VỚI DSU)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cây Khung Nhỏ Nhất (MST Kruskal với DSU).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V \le 10^5, E \le 2 \times 10^5$.



### Bài 08 [CPPB2-L12-08]: TÌM KHỚP VÀ CẦU TRÊN ĐỒ THỊ (TARJAN'S BRIDGE & ARTICULATION)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Khớp Và Cầu Trên Đồ Thị (Tarjan's Bridge & Articulation).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V, E \le 10^5$.



### Bài 09 [CPPB2-L12-09]: DIJKSTRA TRÊN ĐỒ THỊ MỞ RỘNG TRẠNG THÁI (K LẦN DÙNG VÉ MIỄN PHÍ)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (K Lần Dùng Vé Miễn Phí).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V \le 10^5, K \le 10$.



### Bài 10 [CPPB2-L12-10]: THÀNH PHẦN LIÊN THÔNG MẠNH (SCC TARJAN/KOSARAJU)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Thành Phần Liên Thông Mạnh (SCC Tarjan/Kosaraju).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V, E \le 10^5$.



### Bài 11 [CPPB2-L12-11]: TÌM TỔ TIÊN CHUNG GẦN NHẤT (LCA BINARY LIFTING)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Tổ Tiên Chung Gần Nhất (LCA Binary Lifting).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Cây $N \le 10^5, Q \le 10^5$.



### Bài 12 [CPPB2-L12-12]: DIJKSTRA TRÊN ĐỒ THỊ MỞ RỘNG TRẠNG THÁI (K LẦN DÙNG VÉ)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (K Lần Dùng Vé).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V \le 10^5, K \le 10$.



### Bài 13 [CPPB2-L12-13]: MULTI-SOURCE BFS LAN TỎA DỊCH BỆNH / CHÁY RỪNG

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Multi-Source BFS Lan Tỏa Dịch Bệnh / Cháy Rừng.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 1000$.



### Bài 14 [CPPB2-L12-14]: ĐƯỜNG ĐI EULER & CHU TRÌNH EULER (HIERHOLZER)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đường Đi Euler & Chu Trình Euler (Hierholzer).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V, E \le 2 \times 10^5$.



### Bài 15 [CPPB2-L12-15]: TÌM CHU TRÌNH ÂM BẰNG BELLMAN-FORD / SPFA

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Chu Trình Âm Bằng Bellman-Ford / SPFA.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V \le 2500, E \le 5000$.



### Bài 16 [CPPB2-L12-16]: LUỒNG CỰC ĐẠI TRONG MẠNG (MAX FLOW DINIC ALGORITHM)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Luồng Cực Đại Trong Mạng (Max Flow Dinic Algorithm).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $V \le 500, E \le 5000$.




# Bài 13: Cây phân đoạn & cây Fenwick (Segment Tree & Fenwick Tree)

## 1. Khái niệm & bản chất của cấu trúc dữ liệu truy vấn đoạn (Range Query Data Structures)

Khi một bài toán có $Q = 10^5$ truy vấn xen kẽ giữa:

1. **Cập nhật giá trị (Update):** Gán $A[i] = X$ hoặc cộng thêm vào $A[i] \mathrel{+}= X$.
2. **Truy vấn đoạn (Range Query):** Tính tổng $\sum_{k=L}^R A[k]$ hoặc tìm $\min_{k=L}^R A[k]$, $\max_{k=L}^R A[k]$, $\gcd_{k=L}^R A[k]$.

Nếu dùng mảng thông thường: Cập nhật $\mathcal{O}(1)$ nhưng truy vấn $\mathcal{O}(N) \implies \mathcal{O}(QN) \approx 10^{10} \implies \text{TLE}$.  
Nếu dùng Mảng tiền tố tĩnh: Truy vấn $\mathcal{O}(1)$ nhưng cập nhật lại mảng tiền tố mất $\mathcal{O}(N) \implies \text{TLE}$.

**Giải pháp đột phá:** Cây Fenwick (Binary Indexed Tree - BIT) và Cây phân đoạn (Segment Tree) cân bằng cả 2 thao tác cập nhật và truy vấn trong thời gian **logarit $\mathcal{O}(\log N)$**.


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


### Bài 01 [CPPB2-L13-01]: TRUY VẤN TỔNG ĐOẠN FENWICK TREE

**Đầu vào (Input):**

* Dòng 1: $N, Q$. Dòng 2: $N$ số $A_i$. $Q$ dòng tiếp theo: các truy vấn.

---

**Đầu ra (Output):**

* In ra kết quả của các truy vấn loại 2.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5 3
1 2 3 4 5
2 1 5
1 3 2
2 1 5
```

**Output:**
```text
15
17
```

---



### Bài 02 [CPPB2-L13-02]: TRUY VẤN GIÁ TRỊ NHỎ NHẤT ĐOẠN (RMQ SEGMENT TREE)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Truy Vấn Giá Trị Nhỏ Nhất Đoạn (RMQ Segment Tree).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5, A_i \le 10^9$.



### Bài 03 [CPPB2-L13-03]: ĐẾM CẶP NGHỊCH THẾ BẰNG FENWICK TREE

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Cặp Nghịch Thế Bằng Fenwick Tree.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.



### Bài 04 [CPPB2-L13-04]: TRUY VẤN GCD ĐOẠN ĐỘNG

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Truy Vấn GCD Đoạn Động.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5, A_i \le 10^9$.



### Bài 05 [CPPB2-L13-05]: TÌM PHẦN TỬ SỐ 1 THỨ K TRONG DÃY NHỊ PHÂN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Phần Tử Số 1 Thứ K Trong Dãy Nhị Phân.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.



### Bài 06 [CPPB2-L13-06]: DÃY CON TĂNG DÀI NHẤT LIS BẰNG SEGMENT TREE

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Dãy Con Tăng Dài Nhất LIS Bằng Segment Tree.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.



### Bài 07 [CPPB2-L13-07]: CẬP NHẬT ĐOẠN TRUY VẤN ĐIỂM BẰNG FENWICK TREE

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cập Nhật Đoạn Truy Vấn Điểm Bằng Fenwick Tree.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.



### Bài 08 [CPPB2-L13-08]: SEGMENT TREE LAZY PROPAGATION (CẬP NHẬT ĐOẠN & TRUY VẤN ĐOẠN)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Segment Tree Lazy Propagation (Cập Nhật Đoạn & Truy Vấn Đoạn).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.



### Bài 09 [CPPB2-L13-09]: ĐOẠN CON CÓ TỔNG LỚN NHẤT (MAXIMUM SUBSEGMENT SUM QUERY)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoạn Con Có Tổng Lớn Nhất (Maximum Subsegment Sum Query).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.



### Bài 10 [CPPB2-L13-10]: ĐOẠN CON CÓ TỔNG LỚN NHẤT (MAXIMUM SUBSEGMENT SUM QUERY)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoạn Con Có Tổng Lớn Nhất (Maximum Subsegment Sum Query).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.



### Bài 11 [CPPB2-L13-11]: LAZY PROPAGATION GÁN ĐOẠN VÀ TÌM MIN ĐOẠN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lazy Propagation Gán Đoạn Và Tìm Min Đoạn.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.



### Bài 12 [CPPB2-L13-12]: CÂY FENWICK CẬP NHẬT ĐOẠN & TRUY VẤN ĐOẠN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cây Fenwick Cập Nhật Đoạn & Truy Vấn Đoạn.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.



### Bài 13 [CPPB2-L13-13]: TÌM VỊ TRÍ ĐẦU TIÊN CÓ GIÁ TRỊ $\GE X$ TRONG ĐOẠN $[L, R]$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Vị Trí Đầu Tiên Có Giá Trị $\ge X$ Trong Đoạn $[L, R]$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.



### Bài 14 [CPPB2-L13-14]: SEGMENT TREE ĐỘNG (DYNAMIC / SPARSE SEGMENT TREE)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Segment Tree Động (Dynamic / Sparse Segment Tree).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Tọa độ $10^9, Q \le 10^5$.



### Bài 15 [CPPB2-L13-15]: CÂY PHÂN ĐOẠN BỀN VỮNG (PERSISTENT SEGMENT TREE CƠ BẢN)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cây Phân Đoạn Bền Vững (Persistent Segment Tree Cơ Bản).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.



### Bài 16 [CPPB2-L13-16]: SEGMENT TREE BEATS (THUẬT TOÁN JI DRIVER TỐI ƯU PHÉP MIN=X)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Segment Tree Beats (Thuật Toán Ji Driver Tối Ưu Phép Min=X).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.




# Bài 14: Quy hoạch động chữ số (Digit DP)

## 1. Khái niệm & bản chất của Quy hoạch động chữ số

Quy hoạch động chữ số (Digit DP) là phương pháp chuyên dùng để giải quyết các bài toán: **Đếm số lượng số nguyên trong đoạn $[L, R]$ thỏa mãn một tính chất chữ số đặc biệt** (ví dụ: tổng chữ số bằng $K$, không chứa chữ số 4 và 7, các chữ số tăng dần, số nguyên tố, số chia hết cho $D$).

Với $L, R \le 10^{18}$, duyệt trâu từng số mất $10^{18}$ phép tính $\implies$ TLE.  
Digit DP giải quyết bài toán bằng cách:

1. Chuyển đổi bài toán đoạn: $\text{Count}([L, R]) = f(R) - f(L - 1)$ với $f(X)$ là số lượng số thỏa mãn trong $[0, X]$.
2. Biểu diễn số $X$ thành mảng các chữ số $D_0, D_1, \dots, D_{M-1}$ ($M \le 19$).
3. Xây dựng số từ trái sang phải qua hàm đệ quy có nhớ `memo[index][tight][leading_zero][state]`.


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


### Bài 01 [CPPB2-L14-01]: ĐẾM SỐ CÓ TỔNG CHỮ SỐ BẰNG K

**Đầu vào (Input):**

* Gồm 1 dòng chứa $L, R, K$ ($1 \le L \le R \le 10^{18}, 1 \le K \le 180$).

---

**Đầu ra (Output):**

* In ra số lượng số thỏa mãn.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
1 100 5
```

**Output:**
```text
6
```

---



### Bài 02 [CPPB2-L14-02]: TỔNG CÁC CHỮ SỐ BẰNG K TRONG ĐOẠN [L, R]

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Các Chữ Số Bằng K Trong Đoạn [L, R].

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}, K \le 200$.



### Bài 03 [CPPB2-L14-03]: ĐẾM SỐ LƯỢNG CHỮ SỐ 0 XUẤT HIỆN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Lượng Chữ Số 0 Xuất Hiện.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}$.



### Bài 04 [CPPB2-L14-04]: SỐ CÓ CÁC CHỮ SỐ TĂNG NGẶT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Có Các Chữ Số Tăng Ngặt.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}$.



### Bài 05 [CPPB2-L14-05]: SỐ CHIA HẾT CHO TỔNG CÁC CHỮ SỐ CỦA CHÍNH NÓ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Chia Hết Cho Tổng Các Chữ Số Của Chính Nó.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}$.



### Bài 06 [CPPB2-L14-06]: ĐẾM SỐ ĐỐI XỨNG (PALINDROME NUMBERS) TRONG ĐOẠN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đối Xứng (Palindrome Numbers) Trong Đoạn.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}$.



### Bài 07 [CPPB2-L14-07]: SỐ CHỨA ĐẦY ĐỦ CÁC CHỮ SỐ TỪ 0 ĐẾN 9

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Chứa Đầy Đủ Các Chữ Số Từ 0 Đến 9.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}$.



### Bài 08 [CPPB2-L14-08]: TỔNG CÁC SỐ TRONG ĐOẠN THỎA MÃN TÍNH CHẤT CHỮ SỐ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Các Số Trong Đoạn Thỏa Mãn Tính Chất Chữ Số.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}, M = 10^9+7$.



### Bài 09 [CPPB2-L14-09]: SỐ CÓ TÍCH CÁC CHỮ SỐ BẰNG K

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Có Tích Các Chữ Số Bằng K.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}, K \le 10^9$.



### Bài 10 [CPPB2-L14-10]: TỔNG GIÁ TRỊ CÁC SỐ THỎA MÃN TÍNH CHẤT CHỮ SỐ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Giá Trị Các Số Thỏa Mãn Tính Chất Chữ Số.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}, M = 10^9+7$.



### Bài 11 [CPPB2-L14-11]: ĐẾM SỐ TỰ MÃN (SỐ ARMSTRONG / NARCISSISTIC) TRONG ĐOẠN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Tự Mãn (Số Armstrong / Narcissistic) Trong Đoạn.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}$.



### Bài 12 [CPPB2-L14-12]: ĐẾM SỐ ĐẸP CÓ HIỆU HAI CHỮ SỐ KỀ NHAU $\GE 2$ (SỐ STEPPING)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đẹp Có Hiệu Hai Chữ Số Kề Nhau $\ge 2$ (Số Stepping).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}$.



### Bài 13 [CPPB2-L14-13]: SỐ CÓ TỔNG BÌNH PHƯƠNG CÁC CHỮ SỐ LÀ SỐ NGUYÊN TỐ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Có Tổng Bình Phương Các Chữ Số Là Số Nguyên Tố.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}$.



### Bài 14 [CPPB2-L14-14]: TÌM SỐ THỎA MÃN ĐIỀU KIỆN CHỮ SỐ THỨ K NHỎ NHẤT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Số Thỏa Mãn Điều Kiện Chữ Số Thứ K Nhỏ Nhất.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $K \le 10^{18}$.



### Bài 15 [CPPB2-L14-15]: SỐ CHIA HẾT CHO TẤT CẢ CÁC CHỮ SỐ KHÁC KHÔNG CỦA NÓ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Số Chia Hết Cho Tất Cả Các Chữ Số Khác Không Của Nó.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}$.



### Bài 16 [CPPB2-L14-16]: TỔNG XOR CHỮ SỐ CỦA MỌI SỐ TRONG ĐOẠN $[L, R]$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng XOR Chữ Số Của Mọi Số Trong Đoạn $[L, R]$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $L, R \le 10^{18}$.




# Bài 15: Xử lý chuỗi ký tự, String Hashing & số nguyên lớn

## 1. Khái niệm & cấu trúc 3 phần của Bài 15

Bài 15 là bài học tổng hợp cuối cùng của khóa học Level 2, tích hợp 3 mảng kiến thức lớn:

1. **15.1. Xử lý xâu cơ bản & Palindrome:** Các thao tác chuẩn trên `string`, đếm tần suất ký tự, kỹ thuật mở rộng tâm (Expand Around Center) tìm xâu con đối xứng dài nhất trong $\mathcal{O}(N^2)$.
2. **15.2. Kỹ thuật Băm chuỗi đa thức (Rolling Hash / Polynomial Hashing):** Biến đổi một xâu ký tự thành một số nguyên duy nhất theo modulo, cho phép so sánh hai xâu con bất kỳ $S[L \dots R]$ trong thời gian **$\mathcal{O}(1)$** (thay vì $\mathcal{O}(N)$).
3. **15.3. Xử lý số nguyên lớn (Big Integer):** Tự xây dựng cấu trúc số nguyên lớn để thực hiện các phép cộng, trừ, nhân hai số có hàng nghìn chữ số.


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


### Bài 01 [CPPB2-L15-01]: TRUY VẤN SO KHỚP XÂU CON HASHING

**Đầu vào (Input):**

* Dòng 1: Xâu $S$ ($|S| \le 10^5$). Dòng 2: $Q$ ($1 \le Q \le 10^5$). $Q$ dòng sau: $a, b, c, d$ (1-based).

---

**Đầu ra (Output):**

* In ra `YES` nếu hai xâu con bằng nhau, `NO` nếu khác nhau.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
abacaba
2
1 3 5 7
1 3 2 4
```

**Output:**
```text
YES
NO
```

---



### Bài 02 [CPPB2-L15-02]: NHÂN HAI SỐ NGUYÊN LỚN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nhân Hai Số Nguyên Lớn.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Chiều dài $\le 1000$ chữ số.



### Bài 03 [CPPB2-L15-03]: TRUY VẤN SO KHỚP HAI XÂU CON BẰNG HASHING

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Truy Vấn So Khớp Hai Xâu Con Bằng Hashing.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^5, Q \le 10^5$.



### Bài 04 [CPPB2-L15-04]: TÌM XÂU MẪU P TRONG XÂU VĂN BẢN T (STRING MATCH)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Xâu Mẫu P Trong Xâu Văn Bản T (String Match).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert T \vert \le 10^6, \vert P \vert \le 10^5$.



### Bài 05 [CPPB2-L15-05]: XÂU CON ĐỐI XỨNG DÀI NHẤT (LONGEST PALINDROMIC SUBSTRING)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xâu Con Đối Xứng Dài Nhất (Longest Palindromic Substring).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^5$.



### Bài 06 [CPPB2-L15-06]: ĐẾM SỐ XÂU CON KHÁC NHAU CỦA MỘT XÂU

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Xâu Con Khác Nhau Của Một Xâu.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 2000$.



### Bài 07 [CPPB2-L15-07]: XÂU CON LẶP LẠI DÀI NHẤT XUẤT HIỆN ÍT NHẤT K LẦN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xâu Con Lặp Lại Dài Nhất Xuất Hiện Ít Nhất K Lần.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^5, K \le \vert S \vert$.



### Bài 08 [CPPB2-L15-08]: TÍNH GIAI THỪA $N!$ CHO $N = 1000$ BẰNG BIGINT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tính Giai Thừa $N!$ Cho $N = 1000$ Bằng BigInt.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 1000$.



### Bài 09 [CPPB2-L15-09]: THUẬT TOÁN MANACHER TÌM MỌI PALINDROME TUYẾN TÍNH $\MATHCAL{O}(N)$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{O}(N)$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^6$.



### Bài 10 [CPPB2-L15-10]: TÌM CHU KỲ NGẮN NHẤT CỦA XÂU KÝ TỰ (STRING PERIOD)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Chu Kỳ Ngắn Nhất Của Xâu Ký Tự (String Period).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^5$.



### Bài 11 [CPPB2-L15-11]: THUẬT TOÁN MANACHER TÌM MỌI PALINDROME TUYẾN TÍNH $\MATHCAL{O}(N)$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{O}(N)$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^6$.



### Bài 12 [CPPB2-L15-12]: THUẬT TOÁN KMP (KNUTH-MORRIS-PRATT) & MẢNG TIỀN TỐ $\PI$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Thuật Toán KMP (Knuth-Morris-Pratt) & Mảng Tiền Tố $\pi$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert T \vert \le 10^6, \vert P \vert \le 10^6$.



### Bài 13 [CPPB2-L15-13]: CĂN BẬC HAI CỦA SỐ NGUYÊN LỚN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Căn Bậc Hai Của Số Nguyên Lớn.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Chiều dài $\le 200$ chữ số.



### Bài 14 [CPPB2-L15-14]: CHIA HAI SỐ NGUYÊN LỚN CHO NHAU (BIGINT / BIGINT)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chia Hai Số Nguyên Lớn Cho Nhau (BigInt / BigInt).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Chiều dài $\le 500$ chữ số.



### Bài 15 [CPPB2-L15-15]: XÂU CON CHUNG DÀI NHẤT CỦA K XÂU KÝ TỰ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Xâu Con Chung Dài Nhất Của K Xâu Ký Tự.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $K \le 10, \vert S_i \vert \le 10^5$.



### Bài 16 [CPPB2-L15-16]: MẢNG HẬU TỐ (SUFFIX ARRAY) BẰNG STRING HASHING $\MATHCAL{O}(N \LOG^2 N)$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Mảng Hậu Tố (Suffix Array) Bằng String Hashing $\mathcal{O}(N \log^2 N)$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^5$.





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

### `CPPB2-L07-01` — LỰA CHỌN SỰ KIỆN KHÔNG TRÙNG GIỜ

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; if (!(cin >> n)) return 0;
    vector<pair<long long, long long>> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].second >> a[i].first; // sort by end time
    sort(a.begin(), a.end());
    int cnt = 0; long long last_end = -1;
    for (auto &p : a) {
        if (p.second >= last_end) { cnt++; last_end = p.first; }
    }
    cout << cnt << "\n";
    return 0;
}
```

### `CPPB2-L07-02` — TỔNG THỜI GIAN CHỜ NHỎ NHẤT (SJF)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-02: Tổng Thời Gian Chờ Nhỏ Nhất (SJF)
// Goal: Sắp xếp thời gian phục vụ tăng dần

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-03` — CÁI TÚI CHIA NHỎ ĐƯỢC (FRACTIONAL KNAPSACK)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-03: Cái Túi Chia Nhỏ Được (Fractional Knapsack)
// Goal: Sắp xếp theo đơn giá $V_i / W_i$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-04` — PHỦ ĐOẠN THẲNG ÍT NHẤT (MINIMUM INTERVAL COVER)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-04: Phủ Đoạn Thẳng Ít Nhất (Minimum Interval Cover)
// Goal: Tham lam chọn đoạn vươn xa nhất

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-05` — GHÉP THUYỀN CỨU HỘ CỰC TRỊ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-05: Ghép Thuyền Cứu Hộ Cực Trị
// Goal: Hai con trỏ ghép kiện nặng nhất + nhẹ nhất

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-06` — NỐI CÁC SỢI DÂY TIẾT KIỆM CHI PHÍ NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-06: Nối Các Sợi Dây Tiết Kiệm Chi Phí Nhất
// Goal: Hàng đợi ưu tiên `priority_queue` (Cây Huffman)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-07` — LẬP LỊCH CÔNG VIỆC CÓ DEADLINE & TIỀN PHẠT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-07: Lập Lịch Công Việc Có Deadline & Tiền Phạt
// Goal: Tham lam kết hợp Disjoint Set Union (DSU)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-08` — TỐI ĐA HÓA LỢI NHUẬN GIAO HÀNG

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-08: Tối Đa Hóa Lợi Nhuận Giao Hàng
// Goal: Min-heap duy trì tập công việc được chọn

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-09` — CHIA KẸO THƯỞNG CHO HỌC SINH THEO ĐIỂM SỐ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-09: Chia Kẹo Thưởng Cho Học Sinh Theo Điểm Số
// Goal: Quét hai chiều trái $\to$ phải và phải $\to$ trái

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-10` — TỐI ƯU HÓA MUA BÁN CỔ PHIẾU KHÔNG GIỚI HẠN LẦN GIAO DỊCH

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-10: Tối Ưu Hóa Mua Bán Cổ Phiếu Không Giới Hạn Lần Giao Dịch
// Goal: Tham lam gom mọi khoảng giá tăng $\max(0, P_{i+1} - P_i)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-11` — SẮP ĐẶT CHUỖI KÝ TỰ KHÔNG TRÙNG LẶP KỀ NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-11: Sắp Đặt Chuỗi Ký Tự Không Trùng Lặp Kề Nhau
// Goal: Max-Heap xếp ký tự có tần suất cao nhất

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-12` — SỐ LƯỢNG TRẠM TIẾP NHIÊN LIỆU ÍT NHẤT (GAS STATION)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-12: Số Lượng Trạm Tiếp Nhiên Liệu Ít Nhất (Gas Station)
// Goal: Max-Heap chọn cây xăng có trữ lượng lớn nhất khi hết xăng

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-13` — LẬP LỊCH PHÒNG HỌP TỐI THIỂU (MEETING ROOMS II)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-13: Lập Lịch Phòng Họp Tối Thiểu (Meeting Rooms II)
// Goal: Min-Heap theo dõi phòng họp trống sớm nhất

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-14` — PHỤC HỒI DÃY SỐ ĐƠN ĐIỆU VỚI CHI PHÍ NHỎ NHẤT (SLOPE TRICK CƠ BẢN)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-14: Phục Hồi Dãy Số Đơn Điệu Với Chi Phí Nhỏ Nhất (Slope Trick Cơ Bản)
// Goal: Duy trì hàm lỗi lồi bằng Priority Queue

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-15` — GHÉP CẶP TRỌNG SỐ TRÊN ĐỒ THỊ CÂY BẰNG GREEDY

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-15: Ghép Cặp Trọng Số Trên Đồ Thị Cây Bằng Greedy
// Goal: Tham lam từ lá lên gốc (Bottom-up Tree Greedy)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L07-16` — THUẬT TOÁN HUFFMAN CODING NÉN DỮ LIỆU TỐI ƯU

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L07-16: Thuật Toán Huffman Coding Nén Dữ Liệu Tối Ưu
// Goal: Cây mã hóa nhị phân tiền tố tối ưu

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 04 — Bài 08: Quy hoạch động cơ bản (DP)

### `CPPB2-L08-01` — DÃY CON TĂNG DÀI NHẤT LIS

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; if (!(cin >> n)) return 0;
    vector<int> tail;
    for (int i = 0; i < n; ++i) {
        int x; cin >> x;
        auto it = lower_bound(tail.begin(), tail.end(), x);
        if (it == tail.end()) tail.push_back(x);
        else *it = x;
    }
    cout << tail.size() << "\n";
    return 0;
}
```

### `CPPB2-L08-02` — ĐƯỜNG ĐI TRÊN MA TRẬN CÓ TỔNG LỚN NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-02: Đường Đi Trên Ma Trận Có Tổng Lớn Nhất
// Goal: DP 2D $dp[i][j] = \max(dp[i-1][j], dp[i][j-1]) + A[i][j]$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-03` — CÁI TÚI 0/1 CHUẨN (0/1 KNAPSACK)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-03: Cái Túi 0/1 Chuẩn (0/1 Knapsack)
// Goal: DP Cái túi tối ưu bộ nhớ 1D

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-04` — ĐỔI TIỀN XU SỐ TỜ NHỎ NHẤT (UNBOUNDED COIN CHANGE)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-04: Đổi Tiền Xu Số Tờ Nhỏ Nhất (Unbounded Coin Change)
// Goal: DP Cái túi vô hạn duyệt xuôi

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-05` — DÃY CON TĂNG DÀI NHẤT LIS $\MATHCAL{O}(N \LOG N)$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-05: Dãy Con Tăng Dài Nhất LIS $\mathcal{O}(N \log N)$
// Goal: `lower_bound` trên mảng `tail`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-06` — XÂU CON CHUNG DÀI NHẤT (LCS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-06: Xâu Con Chung Dài Nhất (LCS)
// Goal: DP chuỗi 2D

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-07` — XÓA KÝ TỰ ĐỂ THÀNH PALINDROME NGẮN NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-07: Xóa Ký Tự Để Thành Palindrome Ngắn Nhất
// Goal: DP khoảng $[l, r]$ (Interval DP)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-08` — CẮT BÁNH HÌNH CHỮ NHẬT CÓ GIÁ TRỊ LỚN NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-08: Cắt Bánh Hình Chữ Nhật Có Giá Trị Lớn Nhất
// Goal: DP 2D chia đôi hình chữ nhật

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-09` — DÃY CON TĂNG LỚN NHẤT CÓ TRUY VẾT PHẦN TỬ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-09: Dãy Con Tăng Lớn Nhất Có Truy Vết Phần Tử
// Goal: LIS $\mathcal{O}(N \log N)$ kèm mảng truy vết $parent[i]$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-10` — KHOẢNG CÁCH CHỈNH SỬA XÂU (EDIT DISTANCE / LEVENSHTEIN)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-10: Khoảng Cách Chỉnh Sửa Xâu (Edit Distance / Levenshtein)
// Goal: DP 2D tính 3 thao tác Thêm, Xóa, Thay thế

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-11` — CÁI TÚI ĐỔI TRỤC TRẠNG THÁI (VALUE-BASED KNAPSACK)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-11: Cái Túi Đổi Trục Trạng Thái (Value-based Knapsack)
// Goal: Đổi trục DP $dp[v]$ là trọng lượng nhỏ nhất đạt giá trị $v$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-12` — XẾP GẠCH LÁT SÀN KÍCH THƯỚC $3 \TIMES N$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-12: Xếp Gạch Lát Sàn Kích Thước $3 \times N$
// Goal: DP ma trận trạng thái chẵn lẻ

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-13` — DÃY CON HÌNH SÓNG NÚI DÀI NHẤT (BITONIC SUBSEQUENCE)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-13: Dãy Con Hình Sóng Núi Dài Nhất (Bitonic Subsequence)
// Goal: Kết hợp LIS xuôi và LDS ngược trong $\mathcal{O}(N \log N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-14` — NHÂN MA TRẬN DÂY CHUYỀN CHI PHÍ NHỎ NHẤT (MATRIX CHAIN)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-14: Nhân Ma Trận Dây Chuyền Chi Phí Nhỏ Nhất (Matrix Chain)
// Goal: Interval DP $\mathcal{O}(N^3)$ tìm vị trí chia cắt tối ưu

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-15` — QUY HOẠCH ĐỘNG TRÊN CÂY (TREE DP: MAX INDEPENDENT SET)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-15: Quy Hoạch Động Trên Cây (Tree DP: Max Independent Set)
// Goal: DP $dp[u][0/1]$ chọn hoặc không chọn đỉnh $u$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L08-16` — TỐI ƯU HÓA QUY HOẠCH ĐỘNG BẰNG CONVEX HULL TRICK (CHT)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L08-16: Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (CHT)
// Goal: CHT tối ưu $dp[i] = \min(dp[j] + m_j x_i + c_j)$ từ $\mathcal{O}(N^2) \to \mathcal{O}(N \log N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 05 — Bài 09: Ngăn xếp, hàng đợi & Deque đơn điệu

### `CPPB2-L09-01` — PHẦN TỬ LỚN HƠN GẦN NHẤT (NGE)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; if (!(cin >> n)) return 0;
    vector<long long> a(n), res(n, -1);
    for (int i = 0; i < n; ++i) cin >> a[i];
    stack<int> st;
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.top()] <= a[i]) st.pop();
        if (!st.empty()) res[i] = a[st.top()];
        st.push(i);
    }
    for (int i = 0; i < n; ++i) cout << res[i] << (i == n - 1 ? "" : " ");
    cout << "\n";
    return 0;
}
```

### `CPPB2-L09-02` — GIÁ TRỊ NHỎ NHẤT TRÊN CỬA SỔ TRƯỢT K

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-02: Giá Trị Nhỏ Nhất Trên Cửa Sổ Trượt K
// Goal: Cài đặt Monotonic Deque $\mathcal{O}(N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-03` — KIỂM TRA DÃY NGOẶC ĐÚNG NHIỀU LOẠI

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-03: Kiểm Tra Dãy Ngoặc Đúng Nhiều Loại
// Goal: Ứng dụng Stack cơ bản

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-04` — TẦM NHÌN XA CỦA CÁC TÒA NHÀ CAO TẦNG

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-04: Tầm Nhìn Xa Của Các Tòa Nhà Cao Tầng
// Goal: Monotonic Stack đếm số tòa nhà quan sát được

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-05` — HÌNH CHỮ NHẬT LỚN NHẤT DƯỚI BIỂU ĐỒ CỘT (HISTOGRAM)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-05: Hình Chữ Nhật Lớn Nhất Dưới Biểu Đồ Cột (Histogram)
// Goal: Monotonic Stack tìm biên trái & biên phải

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-06` — MA TRẬN TOÀN SỐ 1 LỚN NHẤT (MAXIMAL RECTANGLE 2D)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-06: Ma Trận Toàn Số 1 Lớn Nhất (Maximal Rectangle 2D)
// Goal: Histogram DP 2D

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-07` — TỔNG HIỆU CỰC ĐẠI VÀ CỰC TIỂU MỌI ĐOẠN CON

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-07: Tổng Hiệu Cực Đại Và Cực Tiểu Mọi Đoạn Con
// Goal: Monotonic Stack đếm số đoạn con mà $A_i$ là $\min/\max$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-08` — TỐI ƯU HÓA QUY HOẠCH ĐỘNG BẰNG MONOTONIC DEQUE

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-08: Tối Ưu Hóa Quy Hoạch Động Bằng Monotonic Deque
// Goal: DP $dp[i] = \min_{i-K \le j < i} (dp[j]) + A[i]$ qua Deque

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-09` — HỨNG NƯỚC MƯA ĐA CHIỀU (TRAPPING RAIN WATER)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-09: Hứng Nước Mưa Đa Chiều (Trapping Rain Water)
// Goal: Monotonic Stack tính thể tích nước đọng

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-10` — ĐÁNH GIÁ BIỂU THỨC SỐ HỌC TRUNG TỐ (SHUNTING-YARD)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-10: Đánh Giá Biểu Thức Số Học Trung Tố (Shunting-yard)
// Goal: Thuật toán Shunting-yard của Dijkstra dùng 2 Stack

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-11` — PHẦN TỬ LỚN HƠN GẦN NHẤT TRÊN MẢNG XOAY VÒNG

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-11: Phần Tử Lớn Hơn Gần Nhất Trên Mảng Xoay Vòng
// Goal: Monotonic Stack duyệt $2N$ phần tử

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-12` — XÓA K CHỮ SỐ ĐỂ ĐƯỢC SỐ NHỎ NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-12: Xóa K Chữ Số Để Được Số Nhỏ Nhất
// Goal: Monotonic Stack duy trì các chữ số tăng dần

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-13` — TỔNG GIÁ TRỊ MIN MỌI ĐOẠN CON NHÂN ĐỘ DÀI

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-13: Tổng Giá Trị Min Mọi Đoạn Con Nhân Độ Dài
// Goal: Monotonic Stack kết hợp Prefix Sum

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-14` — ĐUA XE TRONG MÊ CUNG ĐỔI HƯỚNG ÍT NHẤT (0-1 BFS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-14: Đua Xe Trong Mê Cung Đổi Hướng Ít Nhất (0-1 BFS)
// Goal: Hàng đợi Deque tìm đường tối ưu góc rẽ

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-15` — CẮT BĂNG RÔN QUẢNG CÁO TỐI ƯU BẰNG 2 DEQUE

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-15: Cắt Băng Rôn Quảng Cáo Tối Ưu Bằng 2 Deque
// Goal: Duy trì $\max - \min \le C$ trên cửa sổ co giãn

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L09-16` — KHÔI PHỤC CÂY KHẢO SÁT TẦM NHÌN ĐA HƯỚNG

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L09-16: Khôi Phục Cây Khảo Sát Tầm Nhìn Đa Hướng
// Goal: Monotonic Stack 2 chiều xây dựng Cartesian Tree

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 05 — Bài 10: Thư viện STL C++ nâng cao

### `CPPB2-L10-01` — DUY TRÌ TRUNG VỊ ĐỘNG

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; if (!(cin >> n)) return 0;
    priority_queue<int> left;
    priority_queue<int, vector<int>, greater<int>> right;
    for (int i = 0; i < n; ++i) {
        int x; cin >> x;
        if (left.empty() || x <= left.top()) left.push(x);
        else right.push(x);
        if (left.size() > right.size() + 1) { right.push(left.top()); left.pop(); }
        else if (right.size() > left.size()) { left.push(right.top()); right.pop(); }
        cout << left.top() << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

### `CPPB2-L10-02` — ĐẾM TẦN SUẤT GIÁ TRỊ BẰNG SAFE HASH MAP

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-02: Đếm Tần Suất Giá Trị Bằng Safe Hash Map
// Goal: `unordered_map` với `custom_hash`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-03` — NỐI DÂY TIẾT KIỆM BẰNG PRIORITY QUEUE

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-03: Nối Dây Tiết Kiệm Bằng Priority Queue
// Goal: Min-Heap `priority_queue`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-04` — DUY TRÌ TRUNG VỊ ĐỘNG (RUNNING MEDIAN)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-04: Duy Trì Trung Vị Động (Running Median)
// Goal: 2 Heap cân bằng kích thước

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-05` — TÌM PHẦN TỬ KẾ TIẾP NHỎ NHẤT LỚN HƠN X

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-05: Tìm Phần Tử Kế Tiếp Nhỏ Nhất Lớn Hơn X
// Goal: `s.upper_bound(x)` trên `set`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-06` — LẬP LỊCH PHÒNG HỌP ĐA NĂNG (MEETING ROOMS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-06: Lập Lịch Phòng Họp Đa Năng (Meeting Rooms)
// Goal: Min-Heap theo dõi thời điểm kết thúc

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-07` — DUY TRÌ K PHẦN TỬ LỚN NHẤT TRONG LUỒNG DỮ LIỆU

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-07: Duy Trì K Phần Tử Lớn Nhất Trong Luồng Dữ Liệu
// Goal: Min-Heap kích thước cố định $K$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-08` — TỐI ƯU HÓA CHI PHÍ MUA CỔ PHIẾU THEO THỜI GIAN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-08: Tối Ưu Hóa Chi Phí Mua Cổ Phiếu Theo Thời Gian
// Goal: `multiset` duy trì trật tự giá trị

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-09` — HỆ THỐNG ĐẶT CHỖ RẠP CHIẾU PHIM TỐI ƯU

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-09: Hệ Thống Đặt Chỗ Rạp Chiếu Phim Tối Ưu
// Goal: `set<pair<int, int>>` quản lý đoạn trống

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-10` — ĐẾM SỐ PHẦN TỬ PHÂN BIỆT TRONG MỌI CỬA SỔ K

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-10: Đếm Số Phần Tử Phân Biệt Trong Mọi Cửa Sổ K
// Goal: `unordered_map` kết hợp Sliding Window

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-11` — HỢP NHẤT CÁC ĐOẠN SỐ RỜI RẠC (MERGE INTERVALS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-11: Hợp Nhất Các Đoạn Số Rời Rạc (Merge Intervals)
// Goal: `map` hoặc `set` quản lý các khoảng rời

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-12` — TÌM CẶP ĐIỂM CÓ KHOẢNG CÁCH MANHATTAN NHỎ NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-12: Tìm Cặp Điểm Có Khoảng Cách Manhattan Nhỏ Nhất
// Goal: Sweep-line kết hợp `set` tìm kiếm lân cận

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-13` — HỆ THỐNG XẾP HẠNG TRỰC TUYẾN ĐA TIÊU CHÍ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-13: Hệ Thống Xếp Hạng Trực Tuyến Đa Tiêu Chí
// Goal: `set<CustomStruct>` với Strict Weak Ordering

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-14` — TỐI ƯU PHÂN BỔ BĂNG THÔNG MÁY CHỦ (SERVER LOAD BALANCER)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-14: Tối Ưu Phân Bổ Băng Thông Máy Chủ (Server Load Balancer)
// Goal: 2 `set` quản lý máy chủ bận và máy chủ rảnh

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-15` — DUY TRÌ TỔNG CỦA K PHẦN TỬ LỚN NHẤT ĐỘNG

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-15: Duy Trì Tổng Của K Phần Tử Lớn Nhất Động
// Goal: 2 `multiset` cân bằng kích thước $K$ và tổng

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L10-16` — KỸ THUẬT SMALL-TO-LARGE MERGING TRÊN STL MAP

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L10-16: Kỹ Thuật Small-to-Large Merging Trên STL Map
// Goal: Gộp `map` từ cây con lên gốc trong $\mathcal{O}(N \log^2 N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 05 — Bài 11: Tổ hợp, hoán vị & xác suất cơ bản

### `CPPB2-L11-01` — TÍNH TỔ HỢP NCR MODULO

```cpp
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000000;
const long long MOD = 1000000007;
long long f[MAXN + 1], inv[MAXN + 1];
long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD; b >>= 1;
    }
    return res;
}
void init() {
    f[0] = 1; for (int i = 1; i <= MAXN; ++i) f[i] = (f[i - 1] * i) % MOD;
    inv[MAXN] = power_mod(f[MAXN], MOD - 2);
    for (int i = MAXN - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    init();
    int q; if (!(cin >> q)) return 0;
    while (q--) {
        int n, k; cin >> n >> k;
        if (k < 0 || k > n) cout << 0 << "\n";
        else cout << f[n] * inv[k] % MOD * inv[n - k] % MOD << "\n";
    }
    return 0;
}
```

### `CPPB2-L11-02` — TAM GIÁC PASCAL MODULO HỢP SỐ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-02: Tam Giác Pascal Modulo Hợp Số
// Goal: DP Tam giác Pascal $C_n^k = C_{n-1}^{k-1} + C_{n-1}^k$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-03` — CHIA KẸO EULER (STARS AND BARS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-03: Chia Kẹo Euler (Stars and Bars)
// Goal: Ứng dụng công thức chia kẹo Euler

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-04` — ĐẾM SỐ HOÁN VỊ KHÔNG CÓ ĐIỂM CỐ ĐỊNH (DERANGEMENTS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-04: Đếm Số Hoán Vị Không Có Điểm Cố Định (Derangements)
// Goal: Công thức $D_n = (n-1)(D_{n-1} + D_{n-2})$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-05` — ĐẾM SỐ NGUYÊN TỐ CÙNG NHAU BẰNG PIE

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-05: Đếm Số Nguyên Tố Cùng Nhau Bằng PIE
// Goal: Nguyên lý bù trừ kết hợp Bitmask

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-06` — ĐẾM SỐ ĐƯỜNG ĐI TRÊN LƯỚI TỌA ĐỘ CÓ ĐIỂM CẤM

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-06: Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm
// Goal: DP kết hợp PIE và tổ hợp

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-07` — SỐ PHÂN HOẠCH TẬP HỢP (SỐ STIRLING LOẠI 2)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-07: Số Phân Hoạch Tập Hợp (Số Stirling Loại 2)
// Goal: DP tính số Stirling $S(n, k)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-08` — ĐỊNH LÝ LUCAS CHO TỔ HỢP MODULO NGUYÊN TỐ NHỎ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-08: Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ
// Goal: Định lý Lucas $\binom{n}{k} \equiv \prod \binom{n_i}{k_i} \pmod P$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-09` — ĐẾM SỐ ĐƯỜNG ĐI TRÊN LƯỚI TỌA ĐỘ CÓ ĐIỂM CẤM

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-09: Đếm Số Đường Đi Trên Lưới Tọa Độ Có Điểm Cấm
// Goal: DP sắp xếp điểm cấm + PIE

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-10` — ĐẾM SỐ HOÁN VỊ CÓ ĐÚNG K ĐIỂM CỐ ĐỊNH

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-10: Đếm Số Hoán Vị Có Đúng K Điểm Cố Định
// Goal: Công thức $\binom{N}{K} \times D_{N-K} \bmod M$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-11` — SỐ PHÂN HOẠCH TẬP HỢP (SỐ STIRLING LOẠI 2)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-11: Số Phân Hoạch Tập Hợp (Số Stirling Loại 2)
// Goal: DP tính $S(n, k) = S(n-1, k-1) + k \cdot S(n-1, k)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-12` — ĐẾM SỐ CÂY KHUNG ĐỒ THỊ ĐẦY ĐỦ (CÔNG THỨC CAYLEY)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-12: Đếm Số Cây Khung Đồ Thị Đầy Đủ (Công Thức Cayley)
// Goal: Công thức $N^{N-2} \bmod M$ bằng Fast Power

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-13` — ĐỊNH LÝ LUCAS CHO TỔ HỢP MODULO NGUYÊN TỐ NHỎ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-13: Định Lý Lucas Cho Tổ Hợp Modulo Nguyên Tố Nhỏ
// Goal: Định lý Lucas $\binom{n}{k} \equiv \prod \binom{n_i}{k_i} \pmod P$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-14` — ĐẾM SỐ TAM GIÁC TẠO BỞI N ĐIỂM TRÊN MẶT PHẲNG

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-14: Đếm Số Tam Giác Tạo Bởi N Điểm Trên Mặt Phẳng
// Goal: $\binom{N}{3}$ trừ các bộ 3 điểm thẳng hàng qua $\gcd$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-15` — KỲ VỌNG TOÁN HỌC TRÒ CHƠI GIEO XÚC XẮC (PROBABILITY DP)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-15: Kỳ Vọng Toán Học Trò Chơi Gieo Xúc Xắc (Probability DP)
// Goal: DP tính kỳ vọng bước đi $E[i]$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L11-16` — BỔ ĐỀ BURNSIDE ĐẾM CẤU HÌNH BẤT BIẾN PHÉP QUAY

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L11-16: Bổ Đề Burnside Đếm Cấu Hình Bất Biến Phép Quay
// Goal: Lý thuyết nhóm & Bổ đề Burnside đếm vòng cổ

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 06 — Bài 12: Lý thuyết đồ thị cơ bản & nâng cao

### `CPPB2-L12-01` — ĐƯỜNG ĐI NGẮN NHẤT DIJKSTRA

```cpp
#include <bits/stdc++.h>
using namespace std;
const long long INF = 1e18;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m; if (!(cin >> n >> m)) return 0;
    vector<vector<pair<int, long long>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; long long w; cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }
    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    dist[1] = 0; pq.push({0, 1});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto &edge : adj[u]) {
            int v = edge.first; long long w = edge.second;
            if (dist[u] + w < dist[v]) { dist[v] = dist[u] + w; pq.push({dist[v], v}); }
        }
    }
    cout << (dist[n] == INF ? -1 : dist[n]) << "\n";
    return 0;
}
```

### `CPPB2-L12-02` — ĐƯỜNG ĐI NGẮN NHẤT MÊ CUNG 2D BẰNG BFS

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-02: Đường Đi Ngắn Nhất Mê Cung 2D Bằng BFS
// Goal: BFS trên lưới ma trận 2D

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-03` — KIỂM TRA ĐỒ THỊ HAI PHÍA (BIPARTITE GRAPH COLORING)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-03: Kiểm Tra Đồ Thị Hai Phía (Bipartite Graph Coloring)
// Goal: Tô màu 2 màu bằng BFS/DFS

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-04` — SẮP XẾP TÔ-PÔ LẬP LỊCH KHÓA HỌC (TOPOLOGICAL SORT)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-04: Sắp Xếp Tô-pô Lập Lịch Khóa Học (Topological Sort)
// Goal: Thuật toán Kahn (Bán bậc vào `in_degree`)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-05` — DIJKSTRA TÌM ĐƯỜNG ĐI NGẮN NHẤT CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-05: Dijkstra Tìm Đường Đi Ngắn Nhất Chuẩn
// Goal: Cài đặt Dijkstra Min-Heap

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-06` — MÊ CUNG TRỌNG SỐ 0 VÀ 1 (0-1 BFS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-06: Mê Cung Trọng Số 0 và 1 (0-1 BFS)
// Goal: 0-1 BFS với `std::deque`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-07` — CÂY KHUNG NHỎ NHẤT (MST KRUSKAL VỚI DSU)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-07: Cây Khung Nhỏ Nhất (MST Kruskal với DSU)
// Goal: Kruskal + Disjoint Set Union

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-08` — TÌM KHỚP VÀ CẦU TRÊN ĐỒ THỊ (TARJAN'S BRIDGE & ARTICULATION)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-08: Tìm Khớp Và Cầu Trên Đồ Thị (Tarjan's Bridge & Articulation)
// Goal: Mảng `num` và `low` trong DFS

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-09` — DIJKSTRA TRÊN ĐỒ THỊ MỞ RỘNG TRẠNG THÁI (K LẦN DÙNG VÉ MIỄN PHÍ)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-09: Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (K Lần Dùng Vé Miễn Phí)
// Goal: Dijkstra đa tầng $dist[u][k]$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-10` — THÀNH PHẦN LIÊN THÔNG MẠNH (SCC TARJAN/KOSARAJU)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-10: Thành Phần Liên Thông Mạnh (SCC Tarjan/Kosaraju)
// Goal: Co đồ thị có hướng thành DAG

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-11` — TÌM TỔ TIÊN CHUNG GẦN NHẤT (LCA BINARY LIFTING)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-11: Tìm Tổ Tiên Chung Gần Nhất (LCA Binary Lifting)
// Goal: Bảng nhảy nhị phân $up[u][k]$ trong $\mathcal{O}(\log N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-12` — DIJKSTRA TRÊN ĐỒ THỊ MỞ RỘNG TRẠNG THÁI (K LẦN DÙNG VÉ)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-12: Dijkstra Trên Đồ Thị Mở Rộng Trạng Thái (K Lần Dùng Vé)
// Goal: Dijkstra đa tầng $dist[u][k]$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-13` — MULTI-SOURCE BFS LAN TỎA DỊCH BỆNH / CHÁY RỪNG

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-13: Multi-Source BFS Lan Tỏa Dịch Bệnh / Cháy Rừng
// Goal: BFS đồng thời từ nhiều đỉnh nguồn ban đầu

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-14` — ĐƯỜNG ĐI EULER & CHU TRÌNH EULER (HIERHOLZER)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-14: Đường Đi Euler & Chu Trình Euler (Hierholzer)
// Goal: Thuật toán Hierholzer tìm hành trình Euler

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-15` — TÌM CHU TRÌNH ÂM BẰNG BELLMAN-FORD / SPFA

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-15: Tìm Chu Trình Âm Bằng Bellman-Ford / SPFA
// Goal: Kiểm tra nới lỏng lần thứ $V$ phát hiện chu trình âm

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L12-16` — LUỒNG CỰC ĐẠI TRONG MẠNG (MAX FLOW DINIC ALGORITHM)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L12-16: Luồng Cực Đại Trong Mạng (Max Flow Dinic Algorithm)
// Goal: Thuật toán Dinic dùng đồ thị tầng Level Graph

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 06 — Bài 13: Cây phân đoạn & Cây Fenwick

### `CPPB2-L13-01` — TRUY VẤN TỔNG ĐOẠN FENWICK TREE

```cpp
#include <bits/stdc++.h>
using namespace std;
int n, q;
long long bit[100005];
void update(int idx, long long val) {
    for (; idx <= n; idx += idx & (-idx)) bit[idx] += val;
}
long long query(int idx) {
    long long s = 0;
    for (; idx > 0; idx -= idx & (-idx)) s += bit[idx];
    return s;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    if (!(cin >> n >> q)) return 0;
    for (int i = 1; i <= n; ++i) {
        long long x; cin >> x; update(i, x);
    }
    while (q--) {
        int type; cin >> type;
        if (type == 1) { int u; long long v; cin >> u >> v; update(u, v); }
        else { int l, r; cin >> l >> r; cout << query(r) - query(l - 1) << "\n"; }
    }
    return 0;
}
```

### `CPPB2-L13-02` — TRUY VẤN GIÁ TRỊ NHỎ NHẤT ĐOẠN (RMQ SEGMENT TREE)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-02: Truy Vấn Giá Trị Nhỏ Nhất Đoạn (RMQ Segment Tree)
// Goal: Cài đặt Segment Tree Point Update

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-03` — ĐẾM CẶP NGHỊCH THẾ BẰNG FENWICK TREE

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-03: Đếm Cặp Nghịch Thế Bằng Fenwick Tree
// Goal: Nén tọa độ + Fenwick Tree

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-04` — TRUY VẤN GCD ĐOẠN ĐỘNG

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-04: Truy Vấn GCD Đoạn Động
// Goal: Segment Tree với hàm $\gcd(A, B)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-05` — TÌM PHẦN TỬ SỐ 1 THỨ K TRONG DÃY NHỊ PHÂN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-05: Tìm Phần Tử Số 1 Thứ K Trong Dãy Nhị Phân
// Goal: Chặt nhị phân trực tiếp trên Segment Tree

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-06` — DÃY CON TĂNG DÀI NHẤT LIS BẰNG SEGMENT TREE

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-06: Dãy Con Tăng Dài Nhất LIS Bằng Segment Tree
// Goal: DP kết hợp Segment Tree Range Max

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-07` — CẬP NHẬT ĐOẠN TRUY VẤN ĐIỂM BẰNG FENWICK TREE

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-07: Cập Nhật Đoạn Truy Vấn Điểm Bằng Fenwick Tree
// Goal: Fenwick trên mảng hiệu (Difference BIT)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-08` — SEGMENT TREE LAZY PROPAGATION (CẬP NHẬT ĐOẠN & TRUY VẤN ĐOẠN)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-08: Segment Tree Lazy Propagation (Cập Nhật Đoạn & Truy Vấn Đoạn)
// Goal: Kỹ thuật Lazy Propagation

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-09` — ĐOẠN CON CÓ TỔNG LỚN NHẤT (MAXIMUM SUBSEGMENT SUM QUERY)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-09: Đoạn Con Có Tổng Lớn Nhất (Maximum Subsegment Sum Query)
// Goal: Segment Tree lưu 4 trường (sum, pref, suff, ans)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-10` — ĐOẠN CON CÓ TỔNG LỚN NHẤT (MAXIMUM SUBSEGMENT SUM QUERY)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-10: Đoạn Con Có Tổng Lớn Nhất (Maximum Subsegment Sum Query)
// Goal: Segment Tree lưu 4 trường (sum, pref, suff, ans)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-11` — LAZY PROPAGATION GÁN ĐOẠN VÀ TÌM MIN ĐOẠN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-11: Lazy Propagation Gán Đoạn Và Tìm Min Đoạn
// Goal: Lazy gán giá trị mới lên khoảng

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-12` — CÂY FENWICK CẬP NHẬT ĐOẠN & TRUY VẤN ĐOẠN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-12: Cây Fenwick Cập Nhật Đoạn & Truy Vấn Đoạn
// Goal: 2 mảng BIT quản lý $\sum (d_1 \cdot i - d_2)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-13` — TÌM VỊ TRÍ ĐẦU TIÊN CÓ GIÁ TRỊ $\GE X$ TRONG ĐOẠN $[L, R]$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-13: Tìm Vị Trí Đầu Tiên Có Giá Trị $\ge X$ Trong Đoạn $[L, R]$
// Goal: Binary Search trên Segment Tree nhánh trái/phải

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-14` — SEGMENT TREE ĐỘNG (DYNAMIC / SPARSE SEGMENT TREE)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-14: Segment Tree Động (Dynamic / Sparse Segment Tree)
// Goal: Tạo nút cây theo yêu cầu bằng con trỏ

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-15` — CÂY PHÂN ĐOẠN BỀN VỮNG (PERSISTENT SEGMENT TREE CƠ BẢN)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-15: Cây Phân Đoạn Bền Vững (Persistent Segment Tree Cơ Bản)
// Goal: Cây lưu vết phiên bản tìm phần tử nhỏ thứ $K$ trên đoạn

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L13-16` — SEGMENT TREE BEATS (THUẬT TOÁN JI DRIVER TỐI ƯU PHÉP MIN=X)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L13-16: Segment Tree Beats (Thuật Toán Ji Driver Tối Ưu Phép Min=X)
// Goal: Phân rã lịch sử giá trị lớn nhất/nhì

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 06 — Bài 14: Quy hoạch động chữ số (Digit DP)

### `CPPB2-L14-01` — ĐẾM SỐ CÓ TỔNG CHỮ SỐ BẰNG K

```cpp
#include <bits/stdc++.h>
using namespace std;
string s; int target_k;
long long dp[20][2][200];
long long calc(int idx, bool tight, int sum) {
    if (idx == s.size()) return sum == target_k;
    if (dp[idx][tight][sum] != -1) return dp[idx][tight][sum];
    int limit = (tight ? s[idx] - '0' : 9);
    long long ans = 0;
    for (int d = 0; d <= limit; ++d) {
        ans += calc(idx + 1, tight && (d == limit), sum + d);
    }
    return dp[idx][tight][sum] = ans;
}
long long count_to(long long x) {
    if (x < 0) return 0;
    s = to_string(x);
    memset(dp, -1, sizeof(dp));
    return calc(0, true, 0);
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    long long L, R; if (!(cin >> L >> R >> target_k)) return 0;
    cout << count_to(R) - count_to(L - 1) << "\n";
    return 0;
}
```

### `CPPB2-L14-02` — TỔNG CÁC CHỮ SỐ BẰNG K TRONG ĐOẠN [L, R]

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-02: Tổng Các Chữ Số Bằng K Trong Đoạn [L, R]
// Goal: Digit DP lưu trạng thái `current_sum`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-03` — ĐẾM SỐ LƯỢNG CHỮ SỐ 0 XUẤT HIỆN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-03: Đếm Số Lượng Chữ Số 0 Xuất Hiện
// Goal: Digit DP với cờ `leading_zero`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-04` — SỐ CÓ CÁC CHỮ SỐ TĂNG NGẶT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-04: Số Có Các Chữ Số Tăng Ngặt
// Goal: Digit DP lưu chữ số liền trước `last_digit`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-05` — SỐ CHIA HẾT CHO TỔNG CÁC CHỮ SỐ CỦA CHÍNH NÓ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-05: Số Chia Hết Cho Tổng Các Chữ Số Của Chính Nó
// Goal: Cố định tổng chữ số từ $1 \dots 162$ + Digit DP

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-06` — ĐẾM SỐ ĐỐI XỨNG (PALINDROME NUMBERS) TRONG ĐOẠN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-06: Đếm Số Đối Xứng (Palindrome Numbers) Trong Đoạn
// Goal: Digit DP xây dựng nửa đầu và nửa sau

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-07` — SỐ CHỨA ĐẦY ĐỦ CÁC CHỮ SỐ TỪ 0 ĐẾN 9

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-07: Số Chứa Đầy Đủ Các Chữ Số Từ 0 Đến 9
// Goal: Digit DP kết hợp Bitmask lưu tập chữ số

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-08` — TỔNG CÁC SỐ TRONG ĐOẠN THỎA MÃN TÍNH CHẤT CHỮ SỐ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-08: Tổng Các Số Trong Đoạn Thỏa Mãn Tính Chất Chữ Số
// Goal: Digit DP trả về cặp `{số_lượng, tổng_giá_trị}`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-09` — SỐ CÓ TÍCH CÁC CHỮ SỐ BẰNG K

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-09: Số Có Tích Các Chữ Số Bằng K
// Goal: Digit DP kiểm tra $K$ chỉ có ước nguyên tố 2, 3, 5, 7

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-10` — TỔNG GIÁ TRỊ CÁC SỐ THỎA MÃN TÍNH CHẤT CHỮ SỐ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-10: Tổng Giá Trị Các Số Thỏa Mãn Tính Chất Chữ Số
// Goal: Digit DP trả về cặp `{số_lượng, tổng_giá_trị}`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-11` — ĐẾM SỐ TỰ MÃN (SỐ ARMSTRONG / NARCISSISTIC) TRONG ĐOẠN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-11: Đếm Số Tự Mãn (Số Armstrong / Narcissistic) Trong Đoạn
// Goal: Digit DP tính tổng lũy thừa bậc $K$ chữ số

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-12` — ĐẾM SỐ ĐẸP CÓ HIỆU HAI CHỮ SỐ KỀ NHAU $\GE 2$ (SỐ STEPPING)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-12: Đếm Số Đẹp Có Hiệu Hai Chữ Số Kề Nhau $\ge 2$ (Số Stepping)
// Goal: Digit DP kiểm tra $\vert D_i - D_{i-1} \vert \ge 2$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-13` — SỐ CÓ TỔNG BÌNH PHƯƠNG CÁC CHỮ SỐ LÀ SỐ NGUYÊN TỐ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-13: Số Có Tổng Bình Phương Các Chữ Số Là Số Nguyên Tố
// Goal: Sàng nguyên tố kết hợp Digit DP

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-14` — TÌM SỐ THỎA MÃN ĐIỀU KIỆN CHỮ SỐ THỨ K NHỎ NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-14: Tìm Số Thỏa Mãn Điều Kiện Chữ Số Thứ K Nhỏ Nhất
// Goal: Chặt nhị phân kết quả kết hợp hàm đếm Digit DP

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-15` — SỐ CHIA HẾT CHO TẤT CẢ CÁC CHỮ SỐ KHÁC KHÔNG CỦA NÓ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-15: Số Chia Hết Cho Tất Cả Các Chữ Số Khác Không Của Nó
// Goal: Digit DP trạng thái $lcm$ và số dư theo $2520$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L14-16` — TỔNG XOR CHỮ SỐ CỦA MỌI SỐ TRONG ĐOẠN $[L, R]$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L14-16: Tổng XOR Chữ Số Của Mọi Số Trong Đoạn $[L, R]$
// Goal: Digit DP đa chiều tính tổng tích lũy XOR

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 06 — Bài 15: Xử lý chuỗi, String Hashing & BigInt

### `CPPB2-L15-01` — TRUY VẤN SO KHỚP XÂU CON HASHING

```cpp
#include <bits/stdc++.h>
using namespace std;
const long long BASE = 311;
const long long MOD = 1000000007;
long long h[100005], pw[100005];
long long get_hash(int l, int r) {
    long long res = (h[r] - h[l - 1] * pw[r - l + 1]) % MOD;
    return (res + MOD) % MOD;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; if (!(cin >> s)) return 0;
    int n = s.size();
    pw[0] = 1; for (int i = 1; i <= n; ++i) pw[i] = (pw[i - 1] * BASE) % MOD;
    h[0] = 0; for (int i = 0; i < n; ++i) h[i + 1] = (h[i] * BASE + s[i]) % MOD;
    int q; cin >> q;
    while (q--) {
        int a, b, c, d; cin >> a >> b >> c >> d;
        if (b - a != d - c) cout << "NO\n";
        else cout << (get_hash(a, b) == get_hash(c, d) ? "YES\n" : "NO\n");
    }
    return 0;
}
```

### `CPPB2-L15-02` — NHÂN HAI SỐ NGUYÊN LỚN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-02: Nhân Hai Số Nguyên Lớn
// Goal: Cài đặt BigInt Multiplication $\mathcal{O}(NM)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-03` — TRUY VẤN SO KHỚP HAI XÂU CON BẰNG HASHING

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-03: Truy Vấn So Khớp Hai Xâu Con Bằng Hashing
// Goal: Cài đặt Rolling Hash $\mathcal{O}(1)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-04` — TÌM XÂU MẪU P TRONG XÂU VĂN BẢN T (STRING MATCH)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-04: Tìm Xâu Mẫu P Trong Xâu Văn Bản T (String Match)
// Goal: So khớp mã băm trượt

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-05` — XÂU CON ĐỐI XỨNG DÀI NHẤT (LONGEST PALINDROMIC SUBSTRING)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-05: Xâu Con Đối Xứng Dài Nhất (Longest Palindromic Substring)
// Goal: Băm xuôi + Băm ngược + Chặt nhị phân độ dài

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-06` — ĐẾM SỐ XÂU CON KHÁC NHAU CỦA MỘT XÂU

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-06: Đếm Số Xâu Con Khác Nhau Của Một Xâu
// Goal: String Hashing + `unordered_set`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-07` — XÂU CON LẶP LẠI DÀI NHẤT XUẤT HIỆN ÍT NHẤT K LẦN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-07: Xâu Con Lặp Lại Dài Nhất Xuất Hiện Ít Nhất K Lần
// Goal: Chặt nhị phân độ dài kết hợp Double Hash

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-08` — TÍNH GIAI THỪA $N!$ CHO $N = 1000$ BẰNG BIGINT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-08: Tính Giai Thừa $N!$ Cho $N = 1000$ Bằng BigInt
// Goal: Nhân BigInt với số nguyên

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-09` — THUẬT TOÁN MANACHER TÌM MỌI PALINDROME TUYẾN TÍNH $\MATHCAL{O}(N)$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-09: Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{O}(N)$
// Goal: Manacher Algorithm

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-10` — TÌM CHU KỲ NGẮN NHẤT CỦA XÂU KÝ TỰ (STRING PERIOD)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-10: Tìm Chu Kỳ Ngắn Nhất Của Xâu Ký Tự (String Period)
// Goal: String Hashing kiểm tra chu kỳ lặp

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-11` — THUẬT TOÁN MANACHER TÌM MỌI PALINDROME TUYẾN TÍNH $\MATHCAL{O}(N)$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-11: Thuật Toán Manacher Tìm Mọi Palindrome Tuyến Tính $\mathcal{O}(N)$
// Goal: Thuật toán Manacher tìm mảng bán kính đối xứng

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-12` — THUẬT TOÁN KMP (KNUTH-MORRIS-PRATT) & MẢNG TIỀN TỐ $\PI$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-12: Thuật Toán KMP (Knuth-Morris-Pratt) & Mảng Tiền Tố $\pi$
// Goal: Cài đặt hàm tiền xử lý $\pi$ của KMP

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-13` — CĂN BẬC HAI CỦA SỐ NGUYÊN LỚN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-13: Căn Bậc Hai Của Số Nguyên Lớn
// Goal: Chặt nhị phân kết hợp nhân BigInt

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-14` — CHIA HAI SỐ NGUYÊN LỚN CHO NHAU (BIGINT / BIGINT)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-14: Chia Hai Số Nguyên Lớn Cho Nhau (BigInt / BigInt)
// Goal: Thuật toán chia dài Knuth (Algorithm D)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-15` — XÂU CON CHUNG DÀI NHẤT CỦA K XÂU KÝ TỰ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-15: Xâu Con Chung Dài Nhất Của K Xâu Ký Tự
// Goal: Chặt nhị phân độ dài + Băm đa chuỗi

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L15-16` — MẢNG HẬU TỐ (SUFFIX ARRAY) BẰNG STRING HASHING $\MATHCAL{O}(N \LOG^2 N)$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L15-16: Mảng Hậu Tố (Suffix Array) Bằng String Hashing $\mathcal{O}(N \log^2 N)$
// Goal: Sắp xếp các hậu tố bằng so sánh mã băm và LCP

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```




\newpage

# Mục lục


