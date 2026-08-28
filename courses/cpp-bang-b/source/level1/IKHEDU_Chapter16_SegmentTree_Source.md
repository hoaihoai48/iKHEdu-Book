# TÀI LIỆU GỐC — CHƯƠNG 16: CÂY PHÂN ĐOẠN (SEGMENT TREE)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững cấu trúc Cây phân đoạn (Segment Tree / IT) giải bài toán cập nhật phần tử đơn điểm và truy vấn tổng/Min/Max đoạn trong $\mathcal{O}(\log N)$; làm chủ kỹ thuật Cập nhật lười (Lazy Propagation) cho cập nhật trên đoạn |
| Kiến thức cần có | Cây nhị phân, chia để trị, đệ quy, mảng |
| Phạm vi | Xây dựng cây Segment Tree `build` $\mathcal{O}(N)$, Cập nhật điểm `update` $\mathcal{O}(\log N)$, Truy vấn đoạn `query` $\mathcal{O}(\log N)$, Kỹ thuật Lazy Propagation cho cập nhật đoạn |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Cài đặt hàm `build`, `update` điểm và `query` đoạn của Segment Tree trong $\mathcal{O}(\log N)$ — `LO-01`.
2. Khai báo mảng cây $4N$ phần tử không bao giờ bị tràn bộ nhớ — `LO-02`.
3. Cài đặt kỹ thuật Lazy Propagation cập nhật cộng/gán trên đoạn $[L, R]$ trong $\mathcal{O}(\log N)$ — `LO-03`.
4. Tìm vị trí phần tử đầu tiên $\ge X$ trong đoạn $[L, R]$ bằng cách đi bộ trên cây (Walk on Segment Tree) trong $\mathcal{O}(\log N)$ — `LO-04`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để vừa sửa đổi một đoạn dữ liệu, vừa tính tổng hoặc tìm giá trị lớn nhất của đoạn đó trong thời gian chỉ tốn vài chục phép tính?**

---

### Bài 16.1 — Cấu trúc Segment Tree và Thao tác Xây cây (Build)

#### 1. Khái niệm & Quy tắc mảng $4N$
- Cây nhị phân quản lý đoạn $[1, N]$. Nút $id$ quản lý $[L, R]$, nút con trái là $2 \times id$ quản lý $[L, mid]$, nút con phải là $2 \times id + 1$ quản lý $[mid + 1, R]$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 16.1: Quản Lý Biến Động Doanh Thu Siêu Thị WinMart**  
> **Bối cảnh:** Chuỗi $N$ siêu thị có doanh thu ban đầu $A_1, A_2, \dots, A_N$. Thực hiện $Q$ thao tác:  
> - `1 pos val`: Cập nhật doanh thu siêu thị `pos` thành `val`.  
> - `2 l r`: Tính tổng doanh thu các siêu thị từ `l` đến `r`.  
> **Input:** `5 3` \ `1 2 3 4 5` \ `2 1 3` \ `1 2 10` \ `2 1 3` $\implies$ **Output:** `6` \ `14`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<long long> a, treeNode;

void build(int id, int l, int r) {
    if (l == r) {
        treeNode[id] = a[l];
        return;
    }
    int mid = l + (r - l) / 2;
    build(2 * id, l, mid);
    build(2 * id + 1, mid + 1, r);
    treeNode[id] = treeNode[2 * id] + treeNode[2 * id + 1];
}

void update(int id, int l, int r, int pos, long long val) {
    if (l == r) {
        treeNode[id] = val;
        return;
    }
    int mid = l + (r - l) / 2;
    if (pos <= mid) update(2 * id, l, mid, pos, val);
    else update(2 * id + 1, mid + 1, r, pos, val);
    treeNode[id] = treeNode[2 * id] + treeNode[2 * id + 1];
}

long long query(int id, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return treeNode[id];
    int mid = l + (r - l) / 2;
    return query(2 * id, l, mid, ql, qr) + query(2 * id + 1, mid + 1, r, ql, qr);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q)) return 0;

    a.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    treeNode.assign(4 * n + 1, 0);
    build(1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            update(1, 1, n, pos, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << query(1, 1, n, l, r) << "\n";
        }
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 16.1

##### Bài 16.1.1 — Kiểm Tra Năng Lực Trạm Biến Áp
- **Bối cảnh:** $N$ trạm biến áp có công suất ban đầu. Thực hiện các truy vấn cộng thêm công suất cho trạm $P$ và tính tổng công suất vùng $[L, R]$.
- **Input:** `3 2` \ `10 20 30` \ `1 1 5` \ `2 1 2` $\implies$ **Output:** `35`

##### Bài 16.1.2 — Segment Tree Đếm Số Lượng Số Chẵn Trên Đoạn
- **Bối cảnh:** Mỗi nút Segment Tree lưu số lượng số chẵn trong đoạn quản lý. Thực hiện cập nhật điểm và truy vấn đoạn.
- **Input:** `4 1` \ `1 2 3 4` \ `1 4` $\implies$ **Output:** `2`

---

### Bài 16.2 — Cập nhật một điểm (Point Update $\mathcal{O}(\log N)$)

#### 1. Khái niệm & Thuật toán
- Rẽ nhánh trái hoặc phải theo $pos$, cập nhật giá trị nút lá rồi tính lại giá trị các nút tổ tiên trên đường đi.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 16.2: Tìm Giá Trị Lớn Nhất Trên Đoạn Sau Cập Nhật**  
> **Bối cảnh:** Tìm giá trị $\max(A[L..R])$ với các truy vấn sửa đổi giá trị tại một vị trí.  
> **Input:** `4 2` \ `1 5 2 8` \ `2 1 3` \ `1 2 10` $\implies$ **Output:** `5` (trước update).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<long long> a, treeMax;

void build(int id, int l, int r) {
    if (l == r) {
        treeMax[id] = a[l];
        return;
    }
    int mid = l + (r - l) / 2;
    build(2 * id, l, mid);
    build(2 * id + 1, mid + 1, r);
    treeMax[id] = max(treeMax[2 * id], treeMax[2 * id + 1]);
}

void update(int id, int l, int r, int pos, long long val) {
    if (l == r) {
        treeMax[id] = val;
        return;
    }
    int mid = l + (r - l) / 2;
    if (pos <= mid) update(2 * id, l, mid, pos, val);
    else update(2 * id + 1, mid + 1, r, pos, val);
    treeMax[id] = max(treeMax[2 * id], treeMax[2 * id + 1]);
}

long long queryMax(int id, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return -1e18;
    if (ql <= l && r <= qr) return treeMax[id];
    int mid = l + (r - l) / 2;
    return max(queryMax(2 * id, l, mid, ql, qr), queryMax(2 * id + 1, mid + 1, r, ql, qr));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q)) return 0;

    a.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    treeMax.assign(4 * n + 1, 0);
    build(1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            update(1, 1, n, pos, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << queryMax(1, 1, n, l, r) << "\n";
        }
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 16.2

##### Bài 16.2.1 — Tìm Giá Trị Nhỏ Nhất (RMQ) Đoạn Cập Nhật Điểm
- **Bối cảnh:** Tìm giá trị $\min(A[L..R])$ với các thao tác thay đổi giá trị $A[P] = V$.
- **Input:** `3 1` \ `4 1 7` \ `2 1 3` $\implies$ **Output:** `1`

##### Bài 16.2.2 — Tìm Ước Chung Lớn Nhất Đoạn (Range GCD)
- **Bối cảnh:** Mỗi nút cây lưu $\gcd$ của đoạn con. Cập nhật điểm và truy vấn GCD đoạn $[L, R]$.
- **Input:** `3 1` \ `6 12 18` \ `1 3` $\implies$ **Output:** `6`

---

### Bài 16.3 — Truy vấn đoạn và Cập nhật lười (Lazy Propagation)

#### 1. Khái niệm & Kỹ thuật
- Đẩy giá trị lười xuống 2 nút con (`pushDown`) khi cần thiết $\implies$ Thao tác cập nhật đoạn $[L, R]$ chỉ mất $\mathcal{O}(\log N)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 16.3: Nâng Cấp Tải Trọng Tuyến Đường Vành Đai 3**  
> **Bối cảnh:** $N$ đoạn đường vành đai. Thao tác 1: Tăng tải trọng đoạn $[L, R]$ thêm $V$ tấn. Thao tác 2: Tìm tải trọng lớn nhất trong đoạn $[L, R]$.  
> **Input:** `4 3` \ `1 2 3 4` \ `1 1 3 5` \ `2 1 2` \ `2 3 4` $\implies$ **Output:** `7` \ `8`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<long long> a, treeMax, lazyVal;

void build(int id, int l, int r) {
    if (l == r) {
        treeMax[id] = a[l];
        return;
    }
    int mid = l + (r - l) / 2;
    build(2 * id, l, mid);
    build(2 * id + 1, mid + 1, r);
    treeMax[id] = max(treeMax[2 * id], treeMax[2 * id + 1]);
}

void pushDown(int id) {
    if (lazyVal[id] != 0) {
        treeMax[2 * id] += lazyVal[id];
        lazyVal[2 * id] += lazyVal[id];
        treeMax[2 * id + 1] += lazyVal[id];
        lazyVal[2 * id + 1] += lazyVal[id];
        lazyVal[id] = 0;
    }
}

void updateRange(int id, int l, int r, int ql, int qr, long long val) {
    if (ql > r || qr < l) return;
    if (ql <= l && r <= qr) {
        treeMax[id] += val;
        lazyVal[id] += val;
        return;
    }
    pushDown(id);
    int mid = l + (r - l) / 2;
    updateRange(2 * id, l, mid, ql, qr, val);
    updateRange(2 * id + 1, mid + 1, r, ql, qr, val);
    treeMax[id] = max(treeMax[2 * id], treeMax[2 * id + 1]);
}

long long queryMax(int id, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return -1e18;
    if (ql <= l && r <= qr) return treeMax[id];
    pushDown(id);
    int mid = l + (r - l) / 2;
    return max(queryMax(2 * id, l, mid, ql, qr), queryMax(2 * id + 1, mid + 1, r, ql, qr));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q)) return 0;

    a.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    treeMax.assign(4 * n + 1, 0);
    lazyVal.assign(4 * n + 1, 0);
    build(1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long val;
            cin >> l >> r >> val;
            updateRange(1, 1, n, l, r, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << queryMax(1, 1, n, l, r) << "\n";
        }
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 16.3

##### Bài 16.3.1 — Cộng Đoạn Tính Tổng Bằng Lazy Propagation
- **Bối cảnh:** Thao tác 1: Cộng $V$ vào đoạn $[L, R]$. Thao tác 2: Tính tổng đoạn $[L, R]$.
- **Input:** `3 2` \ `1 1 1` \ `1 1 2 3` \ `2 1 3` $\implies$ **Output:** `9`

##### Bài 16.3.2 — Gán Đoạn Tính Giá Trị Lớn Nhất
- **Bối cảnh:** Thao tác 1: Gán mọi phần tử trong đoạn $[L, R]$ bằng $X$. Thao tác 2: Tìm $\max(A[L..R])$.
- **Input:** `3 2` \ `5 5 5` \ `1 1 2 10` \ `2 2 3` $\implies$ **Output:** `10`

---

### Bài 16.4 — Mở rộng: Đếm số lượng phần tử nhỏ nhất và Tìm kiếm trên cây

#### 1. Khái niệm & Kỹ thuật
- Mỗi nút lưu `{minValue, countMin}`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 16.4: Đếm Số Lượng Học Sinh Có Điểm Thấp Nhất**  
> **Bối cảnh:** Tìm giá trị nhỏ nhất và đếm số lượng học sinh đạt điểm số nhỏ nhất trong đoạn $[L, R]$.  
> **Input:** `5 1` \ `2 1 3 1 4` \ `1 5` $\implies$ **Output:** `1 2` (min là 1, xuất hiện 2 lần).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long minVal;
    int cnt;
};

int n, q;
vector<long long> a;
vector<Node> treeNode;

Node combine(Node left, Node right) {
    if (left.minVal < right.minVal) return left;
    if (right.minVal < left.minVal) return right;
    return {left.minVal, left.cnt + right.cnt};
}

void build(int id, int l, int r) {
    if (l == r) {
        treeNode[id] = {a[l], 1};
        return;
    }
    int mid = l + (r - l) / 2;
    build(2 * id, l, mid);
    build(2 * id + 1, mid + 1, r);
    treeNode[id] = combine(treeNode[2 * id], treeNode[2 * id + 1]);
}

Node query(int id, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return { (long long)1e18, 0 };
    if (ql <= l && r <= qr) return treeNode[id];
    int mid = l + (r - l) / 2;
    return combine(query(2 * id, l, mid, ql, qr), query(2 * id + 1, mid + 1, r, ql, qr));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q)) return 0;

    a.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    treeNode.resize(4 * n + 1);
    build(1, 1, n);

    while (q--) {
        int l, r;
        cin >> l >> r;
        Node res = query(1, 1, n, l, r);
        cout << res.minVal << " " << res.cnt << "\n";
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 16.4

##### Bài 16.4.1 — Tìm Vị Trí Đầu Tiên Lớn Hơn Hoặc Bằng X (Walk on Segment Tree)
- **Bối cảnh:** Tìm chỉ số $i$ nhỏ nhất trong đoạn $[L, R]$ thỏa mãn $A[i] \ge X$ trong $\mathcal{O}(\log N)$.
- **Input:** `4 1` \ `1 5 3 7` \ `1 4 4` $\implies$ **Output:** `2` (vị trí 2 có giá trị 5 $\ge 4$).

##### Bài 16.4.2 — Đếm Số Phần Tử Bằng Giá Trị Nhỏ Nhất
- **Bối cảnh:** Tìm giá trị nhỏ nhất và đếm số lần xuất hiện của nó trong đoạn $[L, R]$.
- **Input:** `4 1` \ `2 1 1 3` \ `1 4` $\implies$ **Output:** `1 2`

---

### Bài 16.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 16.5.1 — Cây Phân Đoạn Tính Tổng Điểm Thưởng
- **Bối cảnh:** $Q$ truy vấn cộng điểm cho học sinh tại vị trí $P$ và tính tổng điểm đoạn $[L, R]$.

##### Bài 16.5.2 — Tìm Giá Trị Nhỏ Nhất Trên Đoạn (RMQ)
- **Bối cảnh:** Segment Tree tìm giá trị nhỏ nhất trong đoạn $[L, R]$.

##### Bài 16.5.3 — Đếm Số Phần Tử Bằng Min Trên Đoạn
- **Bối cảnh:** Lưu cặp giá trị `{minVal, cnt}` tại mỗi nút cây Segment Tree.

##### Bài 16.5.4 — Cập Nhật Cộng Đoạn Bằng Lazy Propagation Cơ Bản
- **Bối cảnh:** Cộng thêm giá trị $V$ vào đoạn $[L, R]$ và tính tổng đoạn.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 16.5.5 — Gán Đoạn Cập Nhật Lười (Range Assignment)
- **Bối cảnh:** Gán tất cả phần tử trong đoạn $[L, R]$ bằng giá trị $X$.

##### Bài 16.5.6 — Đoạn Con Có Tổng Lớn Nhất Trên Đoạn (Maximum Subarray Query)
- **Bối cảnh:** Mỗi nút lưu `{sum, pref, suff, maxSub}` để trả lời truy vấn đoạn con tổng lớn nhất trong $\mathcal{O}(\log N)$.

##### Bài 16.5.7 — Tìm Vị Trí Đầu Tiên Lớn Hơn Hoặc Bằng X (Walk on Segment Tree)
- **Bối cảnh:** Rẽ nhánh trực tiếp trên Segment Tree tìm chỉ số đầu tiên có $A[i] \ge X$ trong đoạn $[L, R]$.

##### Bài 16.5.8 — LIS Bằng Segment Tree Trong $\mathcal{O}(N \log N)$
- **Bối cảnh:** Cập nhật giá trị độ dài LIS vào Segment Tree theo thứ tự giá trị.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 16.5.9 — Segment Tree Động Tiết Kiệm Bộ Nhớ (Dynamic Segment Tree)
- **Bối cảnh:** Quản lý dải chỉ số lên tới $N = 10^9$ bằng cấp phát nút động khi cần.

##### Bài 16.5.10 — Segment Tree Bất Biến Lưu Lịch Sử (Persistent Segment Tree)
- **Bối cảnh:** Lưu lại lịch sử cập nhật sau mỗi phiên bản để trả lời truy vấn tìm phần tử nhỏ thứ $K$ trong đoạn $[L, R]$.

##### Bài 16.5.11 — Diện Tích Hợp Các Hình Chữ Nhật Bằng Line Sweep
- **Bối cảnh:** Kết hợp thuật toán quét đường Line Sweep và Segment Tree tính diện tích hợp các hình chữ nhật.

##### Bài 16.5.12 — Cây Phân Đoạn Trên Cây (Heavy-Light Decomposition)
- **Bối cảnh:** Phân rã cây thành các chuỗi nặng-nhẹ để thực hiện cập nhật và truy vấn trên đường đi nối 2 đỉnh của cây.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Khởi tạo kích thước mảng cây nhỏ hơn $4N$ gây tràn mảng | Luôn khai báo `treeNode.assign(4 * n + 1, 0)` |
| Quên gọi `pushDown` trước khi rẽ nhánh trong Lazy Propagation | Luôn gọi `pushDown(id)` trước khi gọi đệ quy 2 con |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Cài đặt chính xác hàm Build, Update điểm và Query đoạn không lỗi tràn mảng. |
| **Vận dụng (Tầng B)** | Cài đặt thành thạo Lazy Propagation và Walk on Segment Tree. |
| **Thành thạo (Tầng C)** | Làm chủ Persistent Segment Tree và ứng dụng Line Sweep hình học. |
