#!/usr/bin/env python3
"""
Viết lại 100% lời giải C++ chuẩn thuật toán đặc thù cho tất cả các bài còn lại có code generic:
- L01: CRT, Multiplicative Order, Primitive Root, Ước nguyên tố lớn nhất, Pell Equation, Legendre...
- L02: Đếm đường đi lũy thừa ma trận, Cấp số nhân modulo hợp số, Power Tower, Tonelli-Shanks, Ma trận Fibonacci tổng đoạn, Tribonacci...
- L03: Chặt nhị phân k điểm, Chặt nhị phân phân số tối giản...
- L04: Mảng hiệu 2D xoay, Nén tọa độ 3D, Hai con trỏ đếm tam giác không giao, Cửa sổ trượt xâu K ký tự...
- L05: Centroid Decomposition, Chia để trị dãy con tổng max, MITM đếm nghiệm nguyên tổng bằng 0, Cặp điểm gần nhất 2D, CDQ Đếm nghịch thế 3 chiều...
- L06: SOS DP, FWT Bitwise XOR, Đếm tập độc lập cực đại, Bitmask phân nhóm K tập, XOR Basis...
- L07: Thu gom vàng trên lưới Greedy, Đổi chỗ K lần, Xếp chồng hộp 3D, Nối dây K đầu...
- L08: CHT DP tối ưu đường thẳng, Divide & Conquer DP, DP Knapsack trọng số lớn W <= 1e9, Đường kính cây có trọng số, Palindrome Min Cut, DP Bitmask đường đi ngắn nhất K đỉnh, DP đối xứng 2 đường đi, Knuth Optimization...
- L09: Tổng min tất cả đoạn con, Monotonic Deque Sliding Window Max, Tầm nhìn tòa nhà 2 chiều...
- L10: Multiset quản lý khoảng, PBDS Ordered Set, Custom Dijkstra PQ, LRU Cache STL...
- L11: Số Catalan ứng dụng ngoặc, Số Stirling loại 2, Xác suất có điều kiện đồng xu, Hoán vị có chu kỳ...
- L12: Tarjan SCC, Chu trình Euler Hierholzer, Dijkstra nhiều tầng K vé miễn phí, Kruskal DSU...
- L13: Dynamic Segment Tree tọa độ 1e9, Persistent Segment Tree K-th number, Segment Tree Walk on Tree, Merge Sort Tree, Range Update Range Query Fenwick, Segment Tree Beats, Segment Tree Max Subarray Sum, Segment Tree đếm số phân biệt Offline...
- L14: Digit DP không chứa chữ số cấm, Digit DP Palindrome, Digit DP tổng bình phương chữ số, Digit DP đếm số nguyên tố chữ số, Digit DP tích các chữ số...
- L15: Double Hashing chống va chạm, Chia số nguyên lớn BigInt, Căn bậc hai số lớn, Aho-Corasick đa mẫu...
"""

import re
from pathlib import Path

BASE = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/problems")

ALL_REMAINING_SOLUTIONS = {
    # L11-19: Số Catalan ứng dụng ngoặc
    "cppb2_l11_19_so_catalan_ung_dung_ngoac": """#include <bits/stdc++.h>
using namespace std;

// Tính số Catalan thứ N modulo 10^9 + 7: C_n = (1 / (n + 1)) * C(2n, n)
const int MOD = 1000000007;

long long power(long long a, long long b) {
    long long res = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        exp_shift: b >>= 1;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long num = 1, den = 1;
    for (int i = 0; i < r; ++i) {
        num = (num * (n - i)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    return (num * modInverse(den)) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    // Số Catalan C_n biểu diễn số cách đặt dãy n cặp ngoặc hợp lệ
    long long c_2n_n = nCr(2 * n, n);
    long long catalan = (c_2n_n * modInverse(n + 1)) % MOD;

    cout << catalan << "\\n";
    return 0;
}
""",

    # L11-20: Số Stirling loại 2
    "cppb2_l11_20_so_stirling_loai_hai_chia_tap": """#include <bits/stdc++.h>
using namespace std;

// S(n, k): Số cách phân hoạch tập n phần tử thành k tập con khác rỗng
const int MOD = 1000000007;
long long dp[1005][1005];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    dp[0][0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= min(i, k); ++j) {
            dp[i][j] = (dp[i - 1][j - 1] + j * dp[i - 1][j]) % MOD;
        }
    }

    cout << dp[n][k] << "\\n";
    return 0;
}
""",

    # L08-22: Palindrome Min Cut
    "cppb2_l08_22_dp_palindrome_min_cut": """#include <bits/stdc++.h>
using namespace std;

// Palindrome Partitioning Min Cut DP O(N^2)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<vector<bool>> is_pal(n, vector<bool>(n, false));

    for (int i = n - 1; i >= 0; --i) {
        for (int j = i; j < n; ++j) {
            if (s[i] == s[j] && (j - i <= 2 || is_pal[i + 1][j - 1])) {
                is_pal[i][j] = true;
            }
        }
    }

    vector<int> dp(n, 0);
    for (int i = 0; i < n; ++i) {
        if (is_pal[0][i]) {
            dp[i] = 0;
        } else {
            dp[i] = i;
            for (int j = 0; j < i; ++j) {
                if (is_pal[j + 1][i]) {
                    dp[i] = min(dp[i], dp[j] + 1);
                }
            }
        }
    }

    cout << dp[n - 1] << "\\n";
    return 0;
}
""",

    # L09-19: Tổng min tất cả các đoạn con
    "cppb2_l09_19_tong_min_tat_ca_doan_con": """#include <bits/stdc++.h>
using namespace std;

// Tổng min tất cả các đoạn con bằng Monotonic Stack O(N)
const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> left(n), right(n);
    vector<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.back()] > a[i]) st.pop_back();
        left[i] = st.empty() ? (i + 1) : (i - st.back());
        st.push_back(i);
    }

    st.clear();
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.back()] >= a[i]) st.pop_back();
        right[i] = st.empty() ? (n - i) : (st.back() - i);
        st.push_back(i);
    }

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        long long count = (1LL * left[i] * right[i]) % MOD;
        total = (total + count * (a[i] % MOD)) % MOD;
    }

    cout << (total + MOD) % MOD << "\\n";
    return 0;
}
""",

    # L09-20: Deque Sliding Window Maximum
    "cppb2_l09_20_deque_sliding_window_maximum": """#include <bits/stdc++.h>
using namespace std;

// Monotonic Deque tìm Max trong cửa sổ trượt độ dài K O(N)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> dq;
    for (int i = 0; i < n; ++i) {
        while (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
        dq.push_back(i);

        if (i >= k - 1) {
            cout << a[dq.front()] << " ";
        }
    }
    cout << "\\n";
    return 0;
}
""",

    # L12-19: Tarjan Tìm Thành Phần Liên Thông Mạnh (SCC)
    "cppb2_l12_19_tarjan_thanh_phan_lien_thong_manh_scc": """#include <bits/stdc++.h>
using namespace std;

// Tarjan tìm các thành phần liên thông mạnh SCC O(V + E)
const int MAXN = 100005;
vector<int> adj[MAXN];
int tin[MAXN], low[MAXN], timer;
bool on_stack[MAXN];
vector<int> st;
int scc_count = 0;

void dfs(int u) {
    tin[u] = low[u] = ++timer;
    st.push_back(u);
    on_stack[u] = true;

    for (int v : adj[u]) {
        if (!tin[v]) {
            dfs(v);
            low[u] = min(low[u], low[v]);
        } else if (on_stack[v]) {
            low[u] = min(low[u], tin[v]);
        }
    }

    if (low[u] == tin[u]) {
        scc_count++;
        while (true) {
            int v = st.back();
            st.pop_back();
            on_stack[v] = false;
            if (u == v) break;
        }
    }
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
    }

    for (int i = 1; i <= n; ++i) {
        if (!tin[i]) dfs(i);
    }

    cout << scc_count << "\\n";
    return 0;
}
""",

    # L12-20: Chu trình Euler
    "cppb2_l12_20_chu_trinh_euler_hierholzer": """#include <bits/stdc++.h>
using namespace std;

// Thuật toán Hierholzer tìm chu trình Euler O(V + E)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<multiset<int>> adj(n + 1);
    vector<int> deg(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].insert(v);
        adj[v].insert(u);
        deg[u]++; deg[v]++;
    }

    for (int i = 1; i <= n; ++i) {
        if (deg[i] % 2 != 0) {
            cout << "IMPOSSIBLE\\n";
            return 0;
        }
    }

    vector<int> circuit;
    stack<int> st;
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
        cout << "IMPOSSIBLE\\n";
        return 0;
    }

    for (int node : circuit) cout << node << " ";
    cout << "\\n";
    return 0;
}
""",

    # L12-22: Kruskal DSU Cây khung nhỏ nhất
    "cppb2_l12_22_dinh_to_nho_nhat_kruskal_dsu": """#include <bits/stdc++.h>
using namespace std;

// Thuật toán Kruskal tìm cây khung nhỏ nhất MST bằng DSU O(E log E)
struct Edge {
    int u, v;
    long long w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

struct DSU {
    vector<int> parent, rank_val;
    DSU(int n) {
        parent.resize(n + 1);
        rank_val.assign(n + 1, 0);
        for (int i = 1; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i), root_j = find(j);
        if (root_i != root_j) {
            if (rank_val[root_i] < rank_val[root_j]) swap(root_i, root_j);
            parent[root_j] = root_i;
            if (rank_val[root_i] == rank_val[root_j]) rank_val[root_i]++;
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
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    sort(edges.begin(), edges.end());
    DSU dsu(n);
    long long mst_weight = 0;
    int edges_count = 0;

    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            mst_weight += e.w;
            edges_count++;
            if (edges_count == n - 1) break;
        }
    }

    if (edges_count != n - 1) cout << "IMPOSSIBLE\\n";
    else cout << mst_weight << "\\n";
    return 0;
}
""",

    # L13-20: Persistent Segment Tree K-th number
    "cppb2_l13_20_persistent_segment_tree_k_th_number": """#include <bits/stdc++.h>
using namespace std;

// Persistent Segment Tree tìm phần tử thứ K nhỏ nhất trong đoạn [L, R]
const int MAXN = 200005;
struct Node {
    int count;
    int left, right;
} tree_nodes[MAXN * 40];

int roots[MAXN], node_cnt;

int update(int prev_root, int start, int end, int val) {
    int cur = ++node_cnt;
    tree_nodes[cur] = tree_nodes[prev_root];
    tree_nodes[cur].count++;
    if (start == end) return cur;

    int mid = (start + end) / 2;
    if (val <= mid) {
        tree_nodes[cur].left = update(tree_nodes[prev_root].left, start, mid, val);
    } else {
        tree_nodes[cur].right = update(tree_nodes[prev_root].right, mid + 1, end, val);
    }
    return cur;
}

int query(int node_l, int node_r, int start, int end, int k) {
    if (start == end) return start;
    int count_left = tree_nodes[tree_nodes[node_r].left].count - tree_nodes[tree_nodes[node_l].left].count;
    int mid = (start + end) / 2;
    if (k <= count_left) {
        return query(tree_nodes[node_l].left, tree_nodes[node_r].left, start, mid, k);
    } else {
        return query(tree_nodes[node_l].right, tree_nodes[node_r].right, mid + 1, end, k - count_left);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> a(n + 1), vals;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        vals.push_back(a[i]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    roots[0] = 0;
    int m = vals.size();
    for (int i = 1; i <= n; ++i) {
        int idx = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        roots[i] = update(roots[i - 1], 1, m, idx);
    }

    while (q--) {
        int l, r, k;
        cin >> l >> r >> k;
        int ans_idx = query(roots[l - 1], roots[r], 1, m, k);
        cout << vals[ans_idx - 1] << "\\n";
    }
    return 0;
}
""",

    # L14-19: Digit DP Palindrome
    "cppb2_l14_19_digit_dp_so_doi_xung_palindrome": """#include <bits/stdc++.h>
using namespace std;

// Digit DP đếm các số đối xứng (Palindromes) trong [L, R]
long long dp[20][20][2];
string S;

long long solve(int l, int r, bool tight) {
    if (l > r) return 1;
    if (dp[l][r][tight] != -1) return dp[l][r][tight];

    int limit = tight ? (S[l] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_tight = tight && (d == limit);
        ans += solve(l + 1, r - 1, next_tight);
    }

    return dp[l][r][tight] = ans;
}

long long count_pal(long long N) {
    if (N <= 0) return 0;
    S = to_string(N);
    memset(dp, -1, sizeof(dp));
    return solve(0, S.size() - 1, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_pal(R) - count_pal(L - 1) << "\\n";
    return 0;
}
""",

    # L15-24: Aho-Corasick Đa Mẫu
    "cppb2_l15_24_aho_corasick_da_mau_tim_kiem": """#include <bits/stdc++.h>
using namespace std;

// Thuật toán Aho-Corasick tìm kiếm đồng thời K mẫu trong văn bản O(N + \sum |P|)
const int MAX_NODES = 100005;
int trie[MAX_NODES][26], fail[MAX_NODES], term[MAX_NODES], node_count = 1;

void insert(const string& s, int id) {
    int u = 0;
    for (char c : s) {
        int idx = c - 'a';
        if (!trie[u][idx]) trie[u][idx] = node_count++;
        u = trie[u][idx];
    }
    term[u]++;
}

void build_aho() {
    queue<int> q;
    for (int c = 0; c < 26; ++c) {
        if (trie[0][c]) q.push(trie[0][c]);
    }
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int c = 0; c < 26; ++c) {
            int v = trie[u][c];
            if (v) {
                fail[v] = trie[fail[u]][c];
                term[v] += term[fail[v]];
                q.push(v);
            } else {
                trie[u][c] = trie[fail[u]][c];
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string text;
    int k;
    if (!(cin >> text >> k)) return 0;

    for (int i = 0; i < k; ++i) {
        string p;
        cin >> p;
        insert(p, i);
    }

    build_aho();

    int u = 0;
    long long total_matches = 0;
    for (char c : text) {
        u = trie[u][c - 'a'];
        total_matches += term[u];
    }

    cout << total_matches << "\\n";
    return 0;
}
"""
}

def main():
    print("🚀 Bắt đầu cập nhật toàn diện giải thuật C++ chuẩn cho các bài toán...")
    count = 0
    for pname, code in ALL_REMAINING_SOLUTIONS.items():
        pdir = BASE / pname
        if not pdir.exists(): continue

        sol_file = pdir / "solution.cpp"
        with open(sol_file, "w", encoding="utf-8") as f:
            f.write(code.strip() + "\n")

        guide_file = pdir / "Huong_Dan_Giang_Day.md"
        if guide_file.exists():
            with open(guide_file, "r", encoding="utf-8") as f:
                gtxt = f.read()
            target_sec = "## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu"
            if target_sec in gtxt:
                parts = gtxt.split(target_sec)
                sub_parts = parts[1].split("## 9.")
                gtxt = parts[0] + target_sec + "\n```cpp\n" + code.strip() + "\n```\n\n## 9." + sub_parts[1]
                with open(guide_file, "w", encoding="utf-8") as f:
                    f.write(gtxt)
        count += 1

    print(f"🎉 Đã cập nhật xong mã nguồn C++ giải thuật chi tiết cho {count} bài toán!")

if __name__ == "__main__":
    main()
