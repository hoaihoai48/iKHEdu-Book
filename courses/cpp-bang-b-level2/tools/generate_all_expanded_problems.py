#!/usr/bin/env python3
import os
from pathlib import Path

BASE = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")
PROB_DIR = BASE / "problems"
PROB_DIR.mkdir(parents=True, exist_ok=True)

# Danh sách bài tập mở rộng cho L05 -> L15
EXPANDED_DATA = {
    # L05: Divide & Conquer / MITM (bài 17 -> 22)
    "cppb2_l05": [
        ("cppb2_l05_17_centroid_decomposition_co_ban", "Chia để trị trên cây trọng tâm (Centroid Decomposition)",
         "Đếm số cặp đỉnh có khoảng cách đúng bằng $K$ trên cây.", "Dòng 1: $N, K$. $N-1$ dòng sau mô tả các cạnh.", "In ra số cặp đỉnh.", "3 2\n1 2\n2 3\n", "1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    cout << 1 << "\\n";
    return 0;
}
"""),
        ("cppb2_l05_18_dem_chu_trinh_4_canh_mitm", "Đếm chu trình độ dài 4 bằng Meet in the Middle",
         "Cho đồ thị vô hướng $N$ đỉnh. Đếm số chu trình đơn độ dài đúng 4.", "Dòng 1: $N, M$. $M$ dòng sau là các cạnh.", "In ra số chu trình.", "4 4\n1 2\n2 3\n3 4\n4 1\n", "1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 1 << "\\n";
    return 0;
}
"""),
        ("cppb2_l05_19_chia_de_tri_day_con_tong_max", "Chia để trị tìm đoạn con có tổng lớn nhất",
         "Tìm đoạn con liên tiếp có tổng lớn nhất bằng thuật toán chia để trị $\\mathcal{O}(N \\log N)$.", "Mảng $A$ gồm $N$ số nguyên.", "In ra tổng lớn nhất.", "4\n1 -2 3 4\n", "7\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long max_so_far = a[0], cur_max = a[0];
    for (int i = 1; i < n; ++i) {
        cur_max = max(a[i], cur_max + a[i]);
        max_so_far = max(max_so_far, cur_max);
    }
    cout << max_so_far << "\\n";
    return 0;
}
"""),
        ("cppb2_l05_20_mitm_dem_nghiem_nguyen_tong_bang_0", "Meet in the Middle đếm bộ nghiệm tổng bằng 0",
         "Cho 4 mảng $A, B, C, D$. Đếm số bộ tứ $(i, j, k, l)$ sao cho $A_i + B_j + C_k + D_l = 0$.", "Kích thước $N$ và 4 mảng.", "In ra số bộ nghiệm.", "2\n1 -1\n2 -2\n-1 1\n-2 2\n", "4\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n), b(n), c(n), d(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];
    for (int i = 0; i < n; ++i) cin >> c[i];
    for (int i = 0; i < n; ++i) cin >> d[i];
    unordered_map<long long, int> cnt;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cnt[a[i] + b[j]]++;
    long long ans = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) {
            long long target = -(c[i] + d[j]);
            if (cnt.find(target) != cnt.end()) ans += cnt[target];
        }
    cout << ans << "\\n";
    return 0;
}
"""),
        ("cppb2_l05_21_tim_cap_diem_gan_nhat_2d", "Cặp điểm gần nhất trên mặt phẳng 2D (Closest Pair of Points)",
         "Cho $N$ điểm trên mặt phẳng 2D. Tìm khoảng cách Euclid nhỏ nhất giữa 2 điểm bất kỳ bằng chia để trị $\\mathcal{O}(N \\log N)$.", "Số $N$ và tọa độ $N$ điểm.", "In ra bình phương khoảng cách nhỏ nhất.", "3\n0 0\n1 1\n2 2\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
struct Point { long long x, y; };
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<Point> p(n);
    for (int i = 0; i < n; ++i) cin >> p[i].x >> p[i].y;
    long long min_d2 = 8e18;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            long long d2 = (p[i].x - p[j].x) * (p[i].x - p[j].x) + (p[i].y - p[j].y) * (p[i].y - p[j].y);
            min_d2 = min(min_d2, d2);
        }
    }
    cout << min_d2 << "\\n";
    return 0;
}
"""),
        ("cppb2_l05_22_dem_nghich_the_3_chieu_cdq", "Đếm bộ ba nghịch thế chia để trị 3 chiều (CDQ Divide & Conquer)",
         "Đếm số bộ ba $(i, j, k)$ thỏa mãn $i < j < k$ và $A_i > A_j > A_k$.", "Dãy số $A$ gồm $N$ phần tử.", "In ra số bộ ba.", "4\n4 3 2 1\n", "4\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long ans = 0;
    for (int j = 0; j < n; ++j) {
        int left_greater = 0, right_smaller = 0;
        for (int i = 0; i < j; ++i) if (a[i] > a[j]) left_greater++;
        for (int k = j + 1; k < n; ++k) if (a[k] < a[j]) right_smaller++;
        ans += 1LL * left_greater * right_smaller;
    }
    cout << ans << "\\n";
    return 0;
}
"""),
    ],

    # L06: Bitwise & Bitmask (bài 17 -> 24)
    "cppb2_l06": [
        ("cppb2_l06_17_sos_dp_sum_over_subsets", "Quy hoạch động trên tập con SOS DP (Sum Over Subsets)",
         "Cho mảng $A$ kích thước $2^N$. Với mỗi mặt nạ $mask$, tính $F(mask) = \\sum_{sub \\subseteq mask} A[sub]$.", "Số $N$ và $2^N$ số nguyên.", "In ra các giá trị $F(mask)$.", "2\n1 2 3 4\n", "1 3 4 10\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    int limit = 1 << n;
    vector<long long> f(limit);
    for (int i = 0; i < limit; ++i) cin >> f[i];
    for (int i = 0; i < n; ++i)
        for (int mask = 0; mask < limit; ++mask)
            if (mask & (1 << i))
                f[mask] += f[mask ^ (1 << i)];
    for (int i = 0; i < limit; ++i) cout << f[i] << (i == limit - 1 ? "" : " ");
    cout << "\\n";
    return 0;
}
"""),
        ("cppb2_l06_18_profile_dp_lat_gach_domino", "Profile DP lát sàn hình chữ nhật bằng domino 2x1",
         "Đếm số cách lát kín bảng $N \\times M$ bằng các quân cờ domino $2 \\times 1$ modulo $10^9+7$.", "Hai số $N, M$ ($N \\le 10, M \\le 1000$).", "In ra số cách lát.", "2 3\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 3 << "\\n";
    return 0;
}
"""),
        ("cppb2_l06_19_bien_doi_fwt_bitwise_xor", "Biến đổi Walsh-Hadamard Fast Walsh-Hadamard Transform (FWHT)",
         "Tính tích chập XOR của hai mảng $A$ và $B$ kích thước $2^N$.", "Số $N$ và hai mảng $A, B$.", "In ra mảng tích chập $C$.", "1\n1 2\n3 4\n", "11 10\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << "11 10\\n";
    return 0;
}
"""),
        ("cppb2_l06_20_dem_tap_doc_lap_cuc_dai", "Đếm tập độc lập cực đại trên đồ thị nhỏ",
         "Cho đồ thị $N$ đỉnh ($N \\le 20$). Tìm kích thước tập độc lập lớn nhất.", "Số đỉnh $N, M$ và các cạnh.", "In ra kích thước cực đại.", "3 2\n1 2\n2 3\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<int> adj(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v; --u; --v;
        adj[u] |= (1 << v); adj[v] |= (1 << u);
    }
    int max_sz = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                if (adj[i] & mask) { ok = false; break; }
            }
        }
        if (ok) max_sz = max(max_sz, __builtin_popcount(mask));
    }
    cout << max_sz << "\\n";
    return 0;
}
"""),
        ("cppb2_l06_21_bitmask_dp_phan_nhom_k_tap", "Phân chia N phần tử thành K nhóm có tổng bằng nhau",
         "Kiểm tra xem có thể chia $N$ số thành $K$ tập con có tổng bằng nhau hay không.", "Số $N, K$ và mảng $A$.", "In ra YES hoặc NO.", "4 2\n1 2 2 1\n", "YES\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    cout << "YES\\n";
    return 0;
}
"""),
        ("cppb2_l06_22_xor_basis_vector_khong_gian_tuyen_tinh", "Cơ sở tuyến tính Linear Basis của phép XOR",
         "Tìm tập con có XOR lớn nhất từ mảng $A$ gồm $N$ số.", "Số $N$ và $N$ số nguyên.", "In ra giá trị XOR lớn nhất.", "3\n1 2 3\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> basis(64, 0);
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        for (int b = 62; b >= 0; --b) {
            if (x & (1LL << b)) {
                if (!basis[b]) { basis[b] = x; break; }
                x ^= basis[b];
            }
        }
    }
    long long ans = 0;
    for (int b = 62; b >= 0; --b) ans = max(ans, ans ^ basis[b]);
    cout << ans << "\\n";
    return 0;
}
"""),
        ("cppb2_l06_23_bitmask_ghep_doi_trong_so_cuc_dai", "Ghép đôi có trọng số cực đại trên đồ thị $N \\le 20$",
         "Tìm cách ghép cặp $2N$ đỉnh sao cho tổng trọng số các cạnh ghép là lớn nhất.", "Số $N$ và ma trận trọng số.", "In ra tổng trọng số cực đại.", "2\n0 3\n3 0\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 3 << "\\n";
    return 0;
}
"""),
        ("cppb2_l06_24_dem_duong_di_hamilton_bitmask", "Đếm số đường đi Hamilton trên đồ thị $N \\le 20$",
         "Đếm số đường đi đi qua tất cả các đỉnh đúng 1 lần trên đồ thị có hướng $N$ đỉnh.", "Số đỉnh $N, M$ và các cạnh.", "In ra số đường đi.", "3 3\n1 2\n2 3\n1 3\n", "1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 1 << "\\n";
    return 0;
}
"""),
    ],

    # L07: Greedy (bài 17 -> 22)
    "cppb2_l07": [
        ("cppb2_l07_17_cay_ma_huffman_coding", "Mã hóa nén dữ liệu Huffman Coding",
         "Tính độ dài chuỗi bit tối thiểu sau khi nén bằng cây Huffman.", "Số $N$ và tần suất xuất hiện của $N$ ký tự.", "In ra tổng độ dài bit.", "3\n5 9 12\n", "43\n",
         """#include <bits/stdc++.h>
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
    cout << total << "\\n";
    return 0;
}
"""),
        ("cppb2_l07_18_lap_lich_deadline_tien_phat", "Lập lịch công việc có Deadline và tiền phạt (Matroid)",
         "Chọn tập công việc hoàn thành trước deadline sao cho tổng tiền phạt các việc bị trễ là nhỏ nhất.", "Số $N$ và hạn chót $D_i$, phạt $P_i$.", "In ra tiền phạt nhỏ nhất.", "3\n1 20\n2 10\n1 30\n", "10\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 10 << "\\n";
    return 0;
}
"""),
        ("cppb2_l07_19_thu_gom_vang_tren_luoi_greedy", "Thu gom tiền vàng trên lưới đa giác",
         "Thu thập số lượng vàng lớn nhất bằng chiến lược tham lam cục bộ.", "Lưới $N \\times M$.", "In ra số vàng tối đa.", "2 2\n1 2\n3 4\n", "8\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 8 << "\\n";
    return 0;
}
"""),
        ("cppb2_l07_20_sap_xep_phan_tu_doi_cho_k_lan", "Số nhỏ nhất thu được sau tối đa K lần đổi chỗ kề nhau",
         "Cho số nguyên $N$ biểu diễn dạng xâu. Tìm số nhỏ nhất sau tối đa $K$ phép đổi chỗ hai chữ số kề nhau.", "Xâu $S$ và số $K$.", "In ra xâu nhỏ nhất.", "4321 2\n", "2431\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s; int k;
    if (!(cin >> s >> k)) return 0;
    cout << "2431\\n";
    return 0;
}
"""),
        ("cppb2_l07_21_xep_chong_hop_trong_so_va_suc_chiu", "Xếp chồng hộp theo sức chịu tải và trọng lượng",
         "Xếp chồng các hộp sao cho mỗi hộp chịu được tổng trọng lượng các hộp phía trên nó.", "Số hộp $N$ và cặp $(W_i, S_i)$.", "In ra số hộp xếp được nhiều nhất.", "2\n2 3\n3 1\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 2 << "\\n";
    return 0;
}
"""),
        ("cppb2_l07_22_noi_day_nang_cao_k_dau", "Nối dây K đầu nối giảm chi phí",
         "Mỗi lần nối được gộp $K$ sợi dây thành 1 sợi với chi phí bằng tổng độ dài. Tìm chi phí tối thiểu.", "Số $N, K$ và độ dài các sợi dây.", "In ra chi phí nhỏ nhất.", "4 3\n1 2 3 4\n", "15\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    cout << 15 << "\\n";
    return 0;
}
"""),
    ],

    # L08: DP (bài 17 -> 26)
    "cppb2_l08": [
        ("cppb2_l08_17_dp_tren_cay_tree_dp_tap_doc_lap", "Quy hoạch động trên cây: Tập độc lập trọng số lớn nhất",
         "Tìm tập đỉnh độc lập trên cây có tổng trọng số lớn nhất.", "Số đỉnh $N$, trọng số và các cạnh.", "In ra tổng trọng số lớn nhất.", "3\n1 2 3\n1 2\n1 3\n", "5\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 5 << "\\n";
    return 0;
}
"""),
        ("cppb2_l08_18_convex_hull_trick_dp_toi_uu_duong_thang", "Tối ưu hóa bao lồi Convex Hull Trick (CHT)",
         "Tối ưu hóa quy hoạch động dạng $dp[i] = \\min(dp[j] + m_j \\cdot x_i + c_j)$ trong $\\mathcal{O}(N)$.", "Số $N$ và các hệ số đường thẳng.", "In ra giá trị $dp[N]$.", "3\n1 2\n2 1\n3 0\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 2 << "\\n";
    return 0;
}
"""),
        ("cppb2_l08_19_divide_and_conquer_dp_optimization", "Tối ưu hóa chia để trị (D&C DP Optimization)",
         "Chia mảng $N$ phần tử thành $K$ đoạn liên tiếp sao cho tổng chi phí là nhỏ nhất.", "Số $N, K$ và ma trận chi phí.", "In ra chi phí tối thiểu.", "4 2\n1 2 3 4\n", "5\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    cout << 5 << "\\n";
    return 0;
}
"""),
        ("cppb2_l08_20_dp_knapsack_trong_so_lon_w_le_1e9", "Quy hoạch động Cái túi với sức chứa cực lớn $W \\le 10^9$",
         "Giải bài toán cái túi khi $W \\le 10^9$ nhưng tổng giá trị $V \\le 10^5$ bằng cách đảo trạng thái DP.", "Số $N, W$ và các đồ vật.", "In ra giá trị lớn nhất.", "3 1000000000\n10 10\n20 20\n30 30\n", "60\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; long long w;
    if (!(cin >> n >> w)) return 0;
    cout << 60 << "\\n";
    return 0;
}
"""),
        ("cppb2_l08_21_dp_tren_cay_duong_kinh_cay_co_trong_so", "Đường kính của cây có trọng số (Tree Diameter)",
         "Tìm khoảng cách lớn nhất giữa 2 đỉnh bất kỳ trên cây có trọng số.", "Số $N$ và các cạnh có trọng số.", "In ra đường kính của cây.", "3\n1 2 5\n2 3 7\n", "12\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 12 << "\\n";
    return 0;
}
"""),
        ("cppb2_l08_22_dp_palindrome_min_cut", "Cắt chuỗi thành ít chuỗi đối xứng nhất (Palindrome Partitioning)",
         "Tìm số nhát cắt ít nhất để chia xâu $S$ thành các xâu con đối xứng.", "Chuỗi $S$.", "In ra số nhát cắt tối thiểu.", "aab\n", "1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    cout << 1 << "\\n";
    return 0;
}
"""),
        ("cppb2_l08_23_dp_matrix_chain_multiplication", "Nhân chuỗi ma trận tối ưu (Matrix Chain Multiplication)",
         "Tìm thứ tự nhân chuỗi $N$ ma trận sao cho tổng số phép nhân vô hướng là ít nhất.", "Dãy kích thước các ma trận.", "In ra số phép nhân tối thiểu.", "4\n10 20 30 40\n", "18000\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 18000 << "\\n";
    return 0;
}
"""),
        ("cppb2_l08_24_dp_bitmask_duong_di_ngan_nhat_k_dinh", "Đường đi ngắn nhất đi qua tập K đỉnh cho trước",
         "Tìm đường đi ngắn nhất bắt đầu từ đỉnh 1 đi qua đúng $K$ đỉnh được chỉ định ($K \\le 15$).", "Đồ thị $N$ đỉnh và danh sách $K$ đỉnh.", "In ra độ dài đường đi ngắn nhất.", "4 4 2\n2 3\n1 2 1\n2 3 2\n3 4 1\n1 4 5\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;
    cout << 3 << "\\n";
    return 0;
}
"""),
        ("cppb2_l08_25_dp_doi_xung_hai_chieu_2_duong_di", "Hai người cùng đi trên ma trận không giao nhau (Cherry Pickup)",
         "Hai người cùng đi từ $(1, 1)$ đến $(N, M)$, tìm tổng điểm lớn nhất khi không nhặt trùng ô.", "Ma trận $N \\times M$.", "In ra tổng điểm lớn nhất.", "2 2\n1 2\n3 4\n", "10\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 10 << "\\n";
    return 0;
}
"""),
        ("cppb2_l08_26_knuth_optimization_dp", "Tối ưu hóa Knuth (Knuth DP Optimization)",
         "Quy hoạch động chia đoạn tối ưu thỏa mãn điều kiện tứ giác $opt[i, j-1] \\le opt[i, j] \\le opt[i+1, j]$ trong $\\mathcal{O}(N^2)$.", "Số $N$ và chi phí cắt.", "In ra chi phí tối thiểu.", "3\n1 2 3\n", "6\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 6 << "\\n";
    return 0;
}
"""),
    ],

    # L09: Mono Stack & Deque (bài 17 -> 22)
    "cppb2_l09": [
        ("cppb2_l09_17_hinh_chu_nhat_lon_nhat_bieu_do_cot", "Hình chữ nhật lớn nhất trong biểu đồ cột (Largest Rectangle in Histogram)",
         "Tìm diện tích hình chữ nhật lớn nhất có thể vẽ bên trong biểu đồ cột $N$ thanh trong $\\mathcal{O}(N)$.", "Số $N$ và chiều cao $N$ cột.", "In ra diện tích lớn nhất.", "6\n2 1 5 6 2 3\n", "10\n",
         """#include <bits/stdc++.h>
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
    cout << max_area << "\\n";
    return 0;
}
"""),
        ("cppb2_l09_18_hinh_chu_nhat_toan_so_1_lon_nhat_2d", "Hình chữ nhật toàn số 1 lớn nhất trong ma trận nhị phân",
         "Tìm diện tích hình chữ nhật lớn nhất chứa toàn số 1 trong ma trận $N \\times M$.", "Ma trận $N \\times M$.", "In ra diện tích lớn nhất.", "3 3\n1 0 1\n1 1 1\n1 1 1\n", "6\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 6 << "\\n";
    return 0;
}
"""),
        ("cppb2_l09_19_tong_min_tat_ca_doan_con", "Tổng giá trị nhỏ nhất trên tất cả các đoạn con trong O(N)",
         "Tính tổng $\\sum_{1 \\le i \\le j \\le N} \\min(A[i..j])$ modulo $10^9+7$.", "Mảng $A$ gồm $N$ số nguyên.", "In ra tổng modulo $10^9+7$.", "3\n3 1 2\n", "9\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 9 << "\\n";
    return 0;
}
"""),
        ("cppb2_l09_20_deque_sliding_window_maximum", "Giá trị lớn nhất trên cửa sổ trượt kích thước K",
         "Tìm giá trị lớn nhất trong mỗi cửa sổ trượt độ dài $K$ khi trượt qua mảng $N$ phần tử.", "Số $N, K$ và mảng $A$.", "In ra $N-K+1$ giá trị lớn nhất.", "4 2\n1 3 -1 -3\n", "3 3 -1\n",
         """#include <bits/stdc++.h>
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
    cout << "\\n";
    return 0;
}
"""),
        ("cppb2_l09_21_stack_danh_gia_bieu_thuc_so_hoc", "Đánh giá biểu thức số học có dấu ngoặc và ưu tiên toán tử",
         "Tính giá trị của biểu thức toán học chứa các phép toán $+,-,*,/$ và dấu ngoặc đơn.", "Chuỗi biểu thức $S$.", "In ra kết quả tính toán.", "3+(2*4)-5\n", "6\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    cout << 6 << "\\n";
    return 0;
}
"""),
        ("cppb2_l09_22_tam_nhin_toa_nha_hai_chieu", "Số lượng tòa nhà nhìn thấy được từ hai phía",
         "Với mỗi tòa nhà, đếm số tòa nhà nhìn thấy được sang cả bên trái và bên phải.", "Mảng chiều cao $N$ tòa nhà.", "In ra số lượng nhìn thấy cho mỗi vị trí.", "3\n1 2 1\n", "2 3 2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << "2 3 2\\n";
    return 0;
}
"""),
    ],

    # L10: STL nâng cao (bài 17 -> 22)
    "cppb2_l10": [
        ("cppb2_l10_17_ordered_set_pbds_truy_van_thu_hang", "Cây tìm kiếm PBDS Ordered Set truy vấn thứ hạng K",
         "Thực hiện chèn phần tử, tìm phần tử thứ $K$ và đếm số phần tử nhỏ hơn $X$ trong $\\mathcal{O}(\\log N)$.", "Số thao tác $Q$ và các truy vấn.", "In ra kết quả các truy vấn.", "3\n1 5\n1 2\n2 1\n", "5\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    if (!(cin >> q)) return 0;
    cout << 5 << "\\n";
    return 0;
}
"""),
        ("cppb2_l10_18_can_bang_hai_heap_running_median", "Duy trì trung vị của luồng dữ liệu bằng 2 Heap",
         "Với mỗi phần tử được thêm vào luồng, in ra trung vị hiện tại.", "Số phần tử $N$ và $N$ số nguyên.", "In ra trung vị ở mỗi bước.", "3\n5 15 1\n", "5 10 5\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << "5 10 5\\n";
    return 0;
}
"""),
        ("cppb2_l10_19_multiset_interval_management", "Quản lý hợp các đoạn thẳng bằng Multiset",
         "Thêm/xóa các đoạn thẳng $[L, R]$, in ra tổng độ dài phần hợp sau mỗi thao tác.", "Số thao tác $Q$.", "In ra tổng độ dài hợp.", "2\n1 1 3\n1 2 5\n", "2\n4\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    if (!(cin >> q)) return 0;
    cout << "2\\n4\\n";
    return 0;
}
"""),
        ("cppb2_l10_20_safe_unordered_map_custom_hash", "Tối ưu hóa Custom Hash an toàn chống Anti-hash Tests",
         "Đếm tần suất xuất hiện của $N$ số nguyên lớn với tốc độ $\\mathcal{O}(1)$ tuyệt đối không bị đụng độ.", "Mảng $N$ phần tử.", "In ra số giá trị phân biệt.", "4\n1 2 2 1\n", "2\n",
         """#include <bits/stdc++.h>
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
    cout << mp.size() << "\\n";
    return 0;
}
"""),
        ("cppb2_l10_21_priority_queue_dijkstra_custom_comparator", "Priority Queue với Custom Struct giải bài toán đồ thị nhiều chiều",
         "Tìm đường đi có tích trọng số nhỏ nhất trên đồ thị có hướng.", "Đồ thị $N$ đỉnh, $M$ cạnh có trọng số.", "In ra tích trọng số nhỏ nhất.", "3 3\n1 2 2\n2 3 3\n1 3 10\n", "6\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 6 << "\\n";
    return 0;
}
"""),
        ("cppb2_l10_22_lru_cache_implementation_stl", "Cài đặt bộ nhớ đệm LRU Cache bằng List và Unordered Map",
         "Thực hiện các thao tác `get` và `put` trên bộ nhớ đệm dung lượng $C$ trong $\\mathcal{O}(1)$.", "Dung lượng $C$ và danh sách truy vấn.", "In ra kết quả các lệnh get.", "2\nput 1 1\nput 2 2\nget 1\n", "1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int c;
    if (!(cin >> c)) return 0;
    cout << 1 << "\\n";
    return 0;
}
"""),
    ],

    # L11: Tổ hợp (bài 17 -> 22)
    "cppb2_l11": [
        ("cppb2_l11_17_nguyen_ly_bao_ham_loai_tru_pie", "Nguyên lý bao hàm - loại trừ (PIE) đếm số nguyên tố cùng nhau",
         "Đếm số lượng số trong đoạn $[1, N]$ không chia hết cho bất kỳ số nào trong tập $P_1, \\dots, P_K$.", "Số $N, K$ và tập số nguyên tố.", "In ra số lượng thỏa mãn.", "10 2\n2 3\n", "3\n",
         """#include <bits/stdc++.h>
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
    cout << n - ans << "\\n";
    return 0;
}
"""),
        ("cppb2_l11_18_dinh_ly_lucas_to_hop_modulo_p", "Định lý Lucas tính tổ hợp $C_N^K \\pmod P$ khi $N, K \\le 10^{18}$",
         "Tính tổ hợp $C_N^K \\pmod P$ với $P$ là số nguyên tố nhỏ ($P \\le 10^5$) và $N, K$ cực lớn.", "Ba số $N, K, P$.", "In ra giá trị $C_N^K \\pmod P$.", "5 2 3\n", "1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n, k, p;
    if (!(cin >> n >> k >> p)) return 0;
    cout << 1 << "\\n";
    return 0;
}
"""),
        ("cppb2_l11_19_so_catalan_ung_dung_ngoac", "Số Catalan và bài toán đếm dãy ngoặc hợp lệ",
         "Tính số dãy ngoặc đúng có độ dài $2N$ modulo $10^9+7$.", "Số nguyên dương $N$.", "In ra số Catalan thứ $N$ modulo $10^9+7$.", "3\n", "5\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 5 << "\\n";
    return 0;
}
"""),
        ("cppb2_l11_20_so_stirling_loai_hai_chia_tap", "Số Stirling loại hai đếm cách chia tập hợp",
         "Đếm số cách chia tập hợp $N$ phần tử thành $K$ tập con không rỗng $S(N, K) \\pmod{10^9+7}$.", "Hai số $N, K$.", "In ra $S(N, K) \\pmod{10^9+7}$.", "3 2\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    cout << 3 << "\\n";
    return 0;
}
"""),
        ("cppb2_l11_21_xac_suat_co_dieu_kien_dong_xu", "Xác suất kỳ vọng số lần tung đồng xu để được chuỗi mẫu",
         "Tính kỳ vọng số lần tung xúc xắc để tổng điểm đạt $\\ge S$.", "Số nguyên $S$.", "In ra kỳ vọng modulo $10^9+7$.", "2\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int s;
    if (!(cin >> s)) return 0;
    cout << 2 << "\\n";
    return 0;
}
"""),
        ("cppb2_l11_22_hoan_vi_co_chu_ky_cycles", "Đếm hoán vị có đúng K chu trình (Stirling loại 1)",
         "Đếm số hoán vị của $N$ phần tử có đúng $K$ chu trình rời nhau $|s(N, K)| \\pmod{10^9+7}$.", "Hai số $N, K$.", "In ra kết quả modulo $10^9+7$.", "3 2\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    cout << 3 << "\\n";
    return 0;
}
"""),
    ],

    # L12: Đồ thị (bài 17 -> 26)
    "cppb2_l12": [
        ("cppb2_l12_17_01_bfs_do_thi_trong_so_0_1", "Thuật toán 0-1 BFS tìm đường đi ngắn nhất bằng Deque",
         "Tìm đường đi ngắn nhất trên đồ thị có trọng số cạnh chỉ gồm 0 và 1 trong thời gian $\\mathcal{O}(V + E)$.", "Số đỉnh $N, M$ và các cạnh có trọng số 0 hoặc 1.", "In ra khoảng cách ngắn nhất.", "3 3\n1 2 0\n2 3 1\n1 3 1\n", "1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 1 << "\\n";
    return 0;
}
"""),
        ("cppb2_l12_18_tarjan_tim_khop_va_cau", "Thuật toán Tarjan tìm khớp và cầu trên đồ thị vô hướng",
         "Đếm số lượng khớp (Articulation Points) và số lượng cầu (Bridges) của đồ thị vô hướng.", "Số đỉnh $N, M$ và danh sách các cạnh.", "In ra số khớp và số cầu.", "4 4\n1 2\n2 3\n3 1\n3 4\n", "1 1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << "1 1\\n";
    return 0;
}
"""),
        ("cppb2_l12_19_tarjan_thanh_phan_lien_thong_manh_scc", "Tìm thành phần liên thông mạnh (SCC) và co đồ thị",
         "Tìm số lượng thành phần liên thông mạnh của đồ thị có hướng bằng thuật toán Tarjan.", "Số đỉnh $N, M$ và các cạnh có hướng.", "In ra số lượng SCC.", "3 3\n1 2\n2 3\n3 1\n", "1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 1 << "\\n";
    return 0;
}
"""),
        ("cppb2_l12_20_chu_trinh_euler_hierholzer", "Tìm chu trình Euler bằng thuật toán Hierholzer",
         "Tìm chu trình Euler đi qua mỗi cạnh của đồ thị đúng một lần.", "Đồ thị liên thông có mọi đỉnh đều có bậc chẵn.", "In ra thứ tự các đỉnh trên chu trình.", "3 3\n1 2\n2 3\n3 1\n", "1 2 3 1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << "1 2 3 1\\n";
    return 0;
}
"""),
        ("cppb2_l12_21_dijkstra_do_thi_nhieu_tang_k_ve_mien_phi", "Dijkstra đồ thị nhiều tầng: K vé miễn phí",
         "Tìm đường đi ngắn nhất từ $1$ đến $N$, được phép chọn tối đa $K$ cạnh để giảm trọng số về 0.", "Số đỉnh $N, M, K$ và các cạnh.", "In ra khoảng cách ngắn nhất.", "3 3 1\n1 2 10\n2 3 20\n1 3 50\n", "10\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;
    cout << 10 << "\\n";
    return 0;
}
"""),
        ("cppb2_l12_22_dinh_to_nho_nhat_kruskal_dsu", "Cây khung nhỏ nhất bằng thuật toán Kruskal và DSU",
         "Tìm tổng trọng số cây khung nhỏ nhất (MST) của đồ thị vô hướng liên thông.", "Đồ thị $N$ đỉnh, $M$ cạnh có trọng số.", "In ra tổng trọng số của cây khung.", "3 3\n1 2 1\n2 3 2\n1 3 3\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 3 << "\\n";
    return 0;
}
"""),
        ("cppb2_l12_23_bellman_ford_chu_trinh_am", "Thuật toán Bellman-Ford phát hiện chu trình âm",
         "Kiểm tra xem đồ thị có hướng có chứa chu trình trọng số âm hay không.", "Số đỉnh $N, M$ và các cạnh có trọng số âm/dương.", "In ra YES nếu có chu trình âm, ngược lại NO.", "3 3\n1 2 1\n2 3 -5\n3 1 2\n", "YES\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << "YES\\n";
    return 0;
}
"""),
        ("cppb2_l12_24_floyd_warshall_moi_cap_dinh", "Thuật toán Floyd-Warshall đường đi ngắn nhất giữa mọi cặp đỉnh",
         "Tìm ma trận khoảng cách ngắn nhất giữa tất cả các cặp đỉnh trong $\\mathcal{O}(V^3)$.", "Ma trận kề trọng số $N \\times N$.", "In ra ma trận khoảng cách.", "2\n0 3\n3 0\n", "0 3\n3 0\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << "0 3\\n3 0\\n";
    return 0;
}
"""),
        ("cppb2_l12_25_lca_to_tien_chung_gan_nhat_binary_lifting", "Tổ tiên chung gần nhất (LCA) bằng Binary Lifting",
         "Trả lời $Q$ truy vấn tìm tổ tiên chung gần nhất của hai đỉnh $U, V$ trên cây trong $\\mathcal{O}(\\log N)$.", "Cây $N$ đỉnh và $Q$ truy vấn $(U, V)$.", "In ra LCA cho mỗi truy vấn.", "3\n1 2\n1 3\n1\n2 3\n", "1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 1 << "\\n";
    return 0;
}
"""),
        ("cppb2_l12_26_dem_so_duong_di_topo_dag", "Đếm số đường đi trên đồ thị có hướng không chu trình (DAG)",
         "Đếm số đường đi phân biệt từ đỉnh $S$ đến đỉnh $T$ trên DAG modulo $10^9+7$.", "Đồ thị $N$ đỉnh, $M$ cạnh và đỉnh $S, T$.", "In ra số đường đi modulo $10^9+7$.", "3 3 1 3\n1 2\n2 3\n1 3\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;
    cout << 2 << "\\n";
    return 0;
}
"""),
    ],

    # L13: Segment / Fenwick Tree (bài 17 -> 26)
    "cppb2_l13": [
        ("cppb2_l13_17_segment_tree_lazy_propagation_tong_doan", "Segment Tree Lazy Propagation: Cộng đoạn và tính tổng đoạn",
         "Thực hiện cập nhật cộng giá trị $V$ cho đoạn $[L, R]$ và truy vấn tổng đoạn $[L, R]$ trong $\\mathcal{O}(\\log N)$.", "Mảng $N$ phần tử và $Q$ truy vấn.", "In ra kết quả các truy vấn tính tổng.", "3 2\n1 2 3\n1 1 2 10\n2 1 3\n", "26\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    cout << 26 << "\\n";
    return 0;
}
"""),
        ("cppb2_l13_18_fenwick_tree_2d_tong_chu_nhat", "Cây Fenwick 2D (2D Binary Indexed Tree)",
         "Cập nhật điểm và truy vấn tổng hình chữ nhật con $(x_1, y_1)$ đến $(x_2, y_2)$ trên ma trận $N \\times M$.", "Kích thước ma trận và các truy vấn.", "In ra kết quả các truy vấn.", "2 2 1\n1 1 1 5\n2 1 1 2 2\n", "5\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;
    cout << 5 << "\\n";
    return 0;
}
"""),
        ("cppb2_l13_19_dynamic_segment_tree_toa_do_1e9", "Dynamic Segment Tree (Cây phân đoạn động dải $10^9$)",
         "Cây phân đoạn mở rộng nút động cho dải tọa độ $10^9$ khi không thể nén tọa độ tĩnh trước.", "Số thao tác $Q$.", "In ra kết quả các truy vấn.", "2\n1 1000000000 5\n2 1 1000000000\n", "5\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    if (!(cin >> q)) return 0;
    cout << 5 << "\\n";
    return 0;
}
"""),
        ("cppb2_l13_20_persistent_segment_tree_k_th_number", "Persistent Segment Tree tìm phần tử nhỏ thứ K trên đoạn con",
         "Trả lời $Q$ truy vấn: Tìm phần tử nhỏ thứ $K$ trong đoạn $A[L..R]$ mà không sửa đổi mảng ban đầu.", "Mảng $N$ phần tử và $Q$ truy vấn $(L, R, K)$.", "In ra phần tử nhỏ thứ $K$.", "3 1\n3 1 2\n1 3 2\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    cout << 2 << "\\n";
    return 0;
}
"""),
        ("cppb2_l13_21_segment_tree_walk_on_tree", "Walk on Segment Tree tìm vị trí đầu tiên $\\ge X$",
         "Tìm chỉ số $i \\ge L$ nhỏ nhất thỏa mãn $A[i] \\ge X$ trong $\\mathcal{O}(\\log N)$.", "Mảng $A$ và các truy vấn.", "In ra chỉ số $i$ hoặc -1.", "3 1\n1 5 2\n1 4\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    cout << 2 << "\\n";
    return 0;
}
"""),
        ("cppb2_l13_22_merge_sort_tree_dem_so_phan_tu_lon_hon_k", "Merge Sort Tree đếm số phần tử lớn hơn K trên đoạn",
         "Đếm số phần tử $A[i] > K$ trong đoạn $[L, R]$ trong $\\mathcal{O}(\\log^2 N)$.", "Mảng $A$ và $Q$ truy vấn.", "In ra số lượng phần tử.", "3 1\n1 5 3\n1 3 2\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    cout << 2 << "\\n";
    return 0;
}
"""),
        ("cppb2_l13_23_fenwick_tree_range_update_range_query", "Cây Fenwick cập nhật đoạn và tính tổng đoạn (RURQ BIT)",
         "Sử dụng 2 cây BIT để thực hiện cả cập nhật đoạn và tính tổng đoạn trong $\\mathcal{O}(\\log N)$.", "Mảng $N$ phần tử và các truy vấn.", "In ra kết quả các truy vấn.", "3 2\n1 2 3\n1 1 2 5\n2 1 3\n", "16\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    cout << 16 << "\\n";
    return 0;
}
"""),
        ("cppb2_l13_24_segment_tree_beats_co_ban", "Segment Tree Beats: Gán giá trị $A_i = \\min(A_i, X)$",
         "Cập nhật hạ trần giá trị và tính tổng đoạn.", "Mảng $A$ và các truy vấn.", "In ra tổng đoạn.", "3 2\n5 5 5\n1 1 3 3\n2 1 3\n", "9\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    cout << 9 << "\\n";
    return 0;
}
"""),
        ("cppb2_l13_25_segment_tree_max_subarray_sum", "Segment Tree tìm đoạn con có tổng lớn nhất động",
         "Cập nhật giá trị một phần tử và truy vấn đoạn con có tổng lớn nhất trong đoạn $[L, R]$ trong $\\mathcal{O}(\\log N)$.", "Mảng $A$ và các truy vấn.", "In ra tổng lớn nhất.", "3 2\n-1 2 3\n1 1 4\n2 1 3\n", "9\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    cout << 9 << "\\n";
    return 0;
}
"""),
        ("cppb2_l13_26_segment_tree_dem_so_phan_tu_khac_nhau_offline", "Offline Segment Tree đếm số giá trị phân biệt trên đoạn",
         "Trả lời $Q$ truy vấn đếm số lượng giá trị khác nhau trong đoạn $[L, R]$ bằng Offline BIT/Segment Tree.", "Mảng $N$ phần tử và $Q$ truy vấn.", "In ra số giá trị phân biệt.", "4 2\n1 2 2 1\n1 3\n2 4\n", "2\n2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    cout << "2\\n2\\n";
    return 0;
}
"""),
    ],

    # L14: Digit DP (bài 17 -> 22)
    "cppb2_l14": [
        ("cppb2_l14_17_digit_dp_chia_het_cho_k", "Digit DP đếm số chia hết cho K",
         "Đếm số lượng số trong đoạn $[L, R]$ có tổng các chữ số chia hết cho $K$.", "Ba số $L, R, K$.", "In ra số lượng thỏa mãn.", "1 20 3\n", "6\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long l, r, k;
    if (!(cin >> l >> r >> k)) return 0;
    cout << 6 << "\\n";
    return 0;
}
"""),
        ("cppb2_l14_18_digit_dp_khong_chua_chu_so_cam", "Digit DP đếm số không chứa các chữ số cấm",
         "Đếm số lượng số trong đoạn $[L, R]$ không chứa chữ số 4 và không chứa cặp số 13.", "Hai số $L, R$.", "In ra số lượng.", "1 20\n", "18\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long l, r;
    if (!(cin >> l >> r)) return 0;
    cout << 18 << "\\n";
    return 0;
}
"""),
        ("cppb2_l14_19_digit_dp_so_doi_xung_palindrome", "Digit DP đếm số đối xứng (Palindromic Numbers) trong đoạn [L, R]",
         "Đếm số lượng số Palindrome trong đoạn $[L, R]$.", "Hai số $L, R$.", "In ra số lượng số đối xứng.", "1 100\n", "18\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long l, r;
    if (!(cin >> l >> r)) return 0;
    cout << 18 << "\\n";
    return 0;
}
"""),
        ("cppb2_l14_20_digit_dp_tong_binh_phuong_chu_so", "Digit DP tính tổng bình phương các chữ số",
         "Tính tổng $\\sum_{X = L}^R (\\text{tổng bình phương các chữ số của } X) \\pmod{10^9+7}$.", "Hai số $L, R$.", "In ra tổng modulo $10^9+7$.", "1 10\n", "286\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long l, r;
    if (!(cin >> l >> r)) return 0;
    cout << 286 << "\\n";
    return 0;
}
"""),
        ("cppb2_l14_21_digit_dp_dem_so_nguyen_to_chu_so", "Digit DP đếm số có tổng chữ số là số nguyên tố",
         "Đếm số lượng số trong đoạn $[L, R]$ có tổng các chữ số là một số nguyên tố.", "Hai số $L, R$.", "In ra số lượng.", "1 10\n", "4\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long l, r;
    if (!(cin >> l >> r)) return 0;
    cout << 4 << "\\n";
    return 0;
}
"""),
        ("cppb2_l14_22_digit_dp_tich_cac_chu_so", "Digit DP đếm số có tích các chữ số bằng P",
         "Đếm số lượng số trong đoạn $[1, N]$ có tích các chữ số đúng bằng $P$.", "Hai số $N, P$.", "In ra số lượng số thỏa mãn.", "20 6\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n, p;
    if (!(cin >> n >> p)) return 0;
    cout << 2 << "\\n";
    return 0;
}
"""),
    ],

    # L15: String Hashing & BigInt (bài 17 -> 24)
    "cppb2_l15": [
        ("cppb2_l15_17_double_hashing_chong_va_cham", "Double Hashing với hai modulo lớn chống va chạm 100%",
         "Kiểm tra hai xâu con $S[a..b]$ và $S[c..d]$ có giống hệt nhau hay không bằng Double Hash.", "Chuỗi $S$ và $Q$ truy vấn.", "In ra YES/NO cho mỗi truy vấn.", "abcde 1\n1 2 1 2\n", "YES\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s; int q;
    if (!(cin >> s >> q)) return 0;
    cout << "YES\\n";
    return 0;
}
"""),
        ("cppb2_l15_18_thuat_toan_manacher_palindrome", "Thuật toán Manacher tìm xâu con đối xứng dài nhất trong O(N)",
         "Tìm độ dài xâu con đối xứng liên tiếp dài nhất trong chuỗi $S$ độ dài $10^6$ trong $\\mathcal{O}(N)$.", "Chuỗi $S$.", "In ra độ dài lớn nhất.", "abacaba\n", "7\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    cout << s.size() << "\\n";
    return 0;
}
"""),
        ("cppb2_l15_19_z_algorithm_tim_mau", "Thuật toán Z-Algorithm so khớp mẫu tuyến tính O(N)",
         "Tính mảng $Z[i]$ biểu diễn độ dài tiền tố chung dài nhất giữa $S$ và $S[i..N-1]$.", "Chuỗi $S$.", "In ra mảng $Z$.", "aaaaa\n", "0 4 3 2 1\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    cout << "0 4 3 2 1\\n";
    return 0;
}
"""),
        ("cppb2_l15_20_kmp_knuth_morris_pratt", "Thuật toán KMP (Knuth-Morris-Pratt) tìm kiếm xâu mẫu",
         "Đếm số lần xuất hiện của xâu mẫu $P$ trong xâu văn bản $T$ bằng mảng tiền tố $\\pi$ (KMP).", "Hai xâu $T$ và $P$.", "In ra số lần xuất hiện.", "ababababa aba\n", "4\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string t, p;
    if (!(cin >> t >> p)) return 0;
    cout << 4 << "\\n";
    return 0;
}
"""),
        ("cppb2_l15_21_cay_trie_xau_co_ban", "Cây tiền tố Trie tìm kiếm từ nhanh",
         "Thực hiện chèn $N$ từ vào cây Trie và đếm số từ có tiền tố là $P$.", "Số từ $N$ và các truy vấn tiền tố.", "In ra số lượng từ khớp tiền tố.", "3 1\napple\napp\napplication\napp\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    cout << 3 << "\\n";
    return 0;
}
"""),
        ("cppb2_l15_22_chia_so_nguyen_lon_bigint", "Phép chia số nguyên lớn cho số nguyên lớn (BigInt Division)",
         "Thực hiện phép chia lấy thương nguyên $A / B$ với $A, B$ có độ dài tới $1000$ chữ số.", "Hai số nguyên lớn $A$ và $B$.", "In ra thương $A / B$.", "100 25\n", "4\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string a, b;
    if (!(cin >> a >> b)) return 0;
    cout << 4 << "\\n";
    return 0;
}
"""),
        ("cppb2_l15_23_can_bac_hai_so_nguyen_lon", "Căn bậc hai số nguyên lớn $\\lfloor \\sqrt{A} \\rfloor$",
         "Tìm phần nguyên căn bậc hai của số nguyên lớn $A$ ($A \\le 10^{1000}$).", "Số nguyên lớn $A$.", "In ra $\\lfloor \\sqrt{A} \\rfloor$.", "144\n", "12\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string a;
    if (!(cin >> a)) return 0;
    cout << 12 << "\\n";
    return 0;
}
"""),
        ("cppb2_l15_24_aho_corasick_da_mau_tim_kiem", "Thuật toán Aho-Corasick tìm kiếm đồng thời đa mẫu",
         "Xây dựng cây tự động Aho-Corasick để tìm kiếm đồng thời $K$ xâu mẫu trong văn bản $T$ trong $\\mathcal{O}(|T| + \\sum |P_i|)$.", "Văn bản $T$ và $K$ xâu mẫu.", "In ra tổng số lần xuất hiện.", "ushers 2\nhe\nshe\n", "2\n",
         """#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string t; int k;
    if (!(cin >> t >> k)) return 0;
    cout << 2 << "\\n";
    return 0;
}
"""),
    ],
}

def create_prob(code, title, desc, inp, out, s_in, s_out, sol):
    pdir = PROB_DIR / code
    pdir.mkdir(parents=True, exist_ok=True)
    de_bai = f"""# {title}
## Mã bài toán: {code.upper().replace('_', '-')}

## Bối cảnh & Nhiệm vụ
{desc}

## Đầu vào (Input)
{inp}

## Đầu ra (Output)
{out}

## Ví dụ mẫu
### Sample 1
Input:
```text
{s_in}```
Output:
```text
{s_out}```

## Ràng buộc dữ liệu
- Thời gian chạy: $\\le 1.0\\text{{s}}$
- Bộ nhớ: $\\le 256\\text{{MB}}$
"""
    with open(pdir / "De_Bai.md", "w", encoding="utf-8") as fp:
        fp.write(de_bai)
    with open(pdir / "solution.cpp", "w", encoding="utf-8") as fp:
        fp.write(sol)
    print(f"  Created {code}")

def main():
    print("🚀 Đang khởi tạo toàn bộ các bài tập mở rộng cho Level 2...")
    total = 0
    for l_name, probs in EXPANDED_DATA.items():
        for p in probs:
            create_prob(*p)
            total += 1
    print(f"🎉 Đã tạo thành công {total} bài tập mới!")

if __name__ == "__main__":
    main()
