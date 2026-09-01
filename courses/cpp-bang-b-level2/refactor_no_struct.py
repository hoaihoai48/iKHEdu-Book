#!/usr/bin/env python3
"""
Chuyển đổi toàn bộ 62 bài dùng struct sang kiểu dữ liệu nguyên bản và vector<vector<long long>>
theo đúng Mục 4 của .agent/rules/academic-authoring-always-on.md
"""

from pathlib import Path

BASE = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/problems")

REFACTORED_SOLUTIONS = {
    # 1. cppb2_l03_20_tam_giac_co_dien_tich_lon_nhat: Dùng vector<long long> x, y
    "cppb2_l03_20_tam_giac_co_dien_tich_lon_nhat": """#include <bits/stdc++.h>
using namespace std;

// Diện tích tam giác tính theo tọa độ không dùng struct
long long cross_product(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3) {
    return abs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n), y(n);
    for (int i = 0; i < n; ++i) cin >> x[i] >> y[i];

    long long max_area2 = 0;
    for (int i = 0; i < n; ++i) {
        int k = (i + 2) % n;
        for (int j = (i + 1) % n; j != i; j = (j + 1) % n) {
            while (cross_product(x[i], y[i], x[j], y[j], x[(k + 1) % n], y[(k + 1) % n]) >
                   cross_product(x[i], y[i], x[j], y[j], x[k], y[k])) {
                k = (k + 1) % n;
            }
            max_area2 = max(max_area2, cross_product(x[i], y[i], x[j], y[j], x[k], y[k]));
        }
    }

    cout << fixed << setprecision(1) << max_area2 / 2.0 << "\\n";
    return 0;
}
""",

    # 2. cppb2_l04_17_quet_duong_sweep_line_dien_tich_hinh_chu_nhat: Dùng vector<vector<long long>>
    "cppb2_l04_17_quet_duong_sweep_line_dien_tich_hinh_chu_nhat": """#include <bits/stdc++.h>
using namespace std;

// Sweep-line dùng vector<vector<long long>> biểu diễn sự kiện: {x, type, y1, y2}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> events;
    vector<long long> Y;

    for (int i = 0; i < n; ++i) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        events.push_back({x1, 1, y1, y2});
        events.push_back({x2, -1, y1, y2});
        Y.push_back(y1);
        Y.push_back(y2);
    }

    sort(Y.begin(), Y.end());
    Y.erase(unique(Y.begin(), Y.end()), Y.end());
    sort(events.begin(), events.end());

    vector<int> count_cover(Y.size(), 0);
    long long total_area = 0;

    for (size_t i = 0; i + 1 < events.size(); ++i) {
        int y1_idx = lower_bound(Y.begin(), Y.end(), events[i][2]) - Y.begin();
        int y2_idx = lower_bound(Y.begin(), Y.end(), events[i][3]) - Y.begin();

        for (int j = y1_idx; j < y2_idx; ++j) {
            count_cover[j] += events[i][1];
        }

        long long covered_len = 0;
        for (size_t j = 0; j + 1 < Y.size(); ++j) {
            if (count_cover[j] > 0) {
                covered_len += Y[j + 1] - Y[j];
            }
        }
        total_area += covered_len * (events[i + 1][0] - events[i][0]);
    }

    cout << total_area << "\\n";
    return 0;
}
""",

    # 3. cppb2_l04_19_nen_toa_do_da_chieu_3d: Dùng vector<vector<int>> boxes
    "cppb2_l04_19_nen_toa_do_da_chieu_3d": """#include <bits/stdc++.h>
using namespace std;

// Nén tọa độ 3D dùng vector<vector<int>>: {x1, y1, z1, x2, y2, z2}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> boxes(n, vector<int>(6));
    vector<int> X, Y, Z;

    for (int i = 0; i < n; ++i) {
        cin >> boxes[i][0] >> boxes[i][1] >> boxes[i][2];
        cin >> boxes[i][3] >> boxes[i][4] >> boxes[i][5];
        X.push_back(boxes[i][0]); X.push_back(boxes[i][3]);
        Y.push_back(boxes[i][1]); Y.push_back(boxes[i][4]);
        Z.push_back(boxes[i][2]); Z.push_back(boxes[i][5]);
    }

    sort(X.begin(), X.end()); X.erase(unique(X.begin(), X.end()), X.end());
    sort(Y.begin(), Y.end()); Y.erase(unique(Y.begin(), Y.end()), Y.end());
    sort(Z.begin(), Z.end()); Z.erase(unique(Z.begin(), Z.end()), Z.end());

    int nx = X.size(), ny = Y.size(), nz = Z.size();
    vector<vector<vector<int>>> grid(nx, vector<vector<int>>(ny, vector<int>(nz, 0)));

    for (const auto& b : boxes) {
        int x1 = lower_bound(X.begin(), X.end(), b[0]) - X.begin();
        int x2 = lower_bound(X.begin(), X.end(), b[3]) - X.begin();
        int y1 = lower_bound(Y.begin(), Y.end(), b[1]) - Y.begin();
        int y2 = lower_bound(Y.begin(), Y.end(), b[4]) - Y.begin();
        int z1 = lower_bound(Z.begin(), Z.end(), b[2]) - Z.begin();
        int z2 = lower_bound(Z.begin(), Z.end(), b[5]) - Z.begin();

        for (int i = x1; i < x2; ++i) {
            for (int j = y1; j < y2; ++j) {
                for (int k = z1; k < z2; ++k) {
                    grid[i][j][k] = 1;
                }
            }
        }
    }

    long long total_vol = 0;
    for (int i = 0; i + 1 < nx; ++i) {
        for (int j = 0; j + 1 < ny; ++j) {
            for (int k = 0; k + 1 < nz; ++k) {
                if (grid[i][j][k]) {
                    total_vol += 1LL * (X[i + 1] - X[i]) * (Y[j + 1] - Y[j]) * (Z[k + 1] - Z[k]);
                }
            }
        }
    }

    cout << total_vol << "\\n";
    return 0;
}
""",

    # 4. cppb2_l07_18_lap_lich_deadline_tien_phat: Dùng vector<vector<long long>> {penalty, deadline, id}
    "cppb2_l07_18_lap_lich_deadline_tien_phat": """#include <bits/stdc++.h>
using namespace std;

// Tham lam lập lịch công việc dùng vector<vector<long long>>
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> jobs(n, vector<long long>(3));
    for (int i = 0; i < n; ++i) {
        long long d, p;
        cin >> d >> p;
        jobs[i] = {p, d, i + 1}; // {tiền phạt, deadline, id} để sort giảm dần
    }

    sort(jobs.rbegin(), jobs.rend());

    vector<int> slot(n + 1, -1);
    long long total_penalty = 0;

    for (const auto& job : jobs) {
        long long p = job[0];
        int d = min((long long)n, job[1]);
        int id = job[2];

        while (d > 0 && slot[d] != -1) d--;
        if (d > 0) {
            slot[d] = id;
        } else {
            total_penalty += p;
        }
    }

    cout << total_penalty << "\\n";
    return 0;
}
""",

    # 5. cppb2_l07_21_xep_chong_hop_trong_so_va_suc_chiu: Dùng vector<vector<long long>> {w + s, w, s, v}
    "cppb2_l07_21_xep_chong_hop_trong_so_va_suc_chiu": """#include <bits/stdc++.h>
using namespace std;

// Box Stacking dùng vector<vector<long long>>: {w + s, w, s, v}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> boxes(n, vector<long long>(4));
    for (int i = 0; i < n; ++i) {
        long long w, s, v;
        cin >> w >> s >> v;
        boxes[i] = {w + s, w, s, v};
    }

    sort(boxes.begin(), boxes.end());

    int max_s = 20005;
    vector<long long> dp(max_s, 0);

    for (const auto& b : boxes) {
        long long w = b[1], s = b[2], v = b[3];
        for (int weight = min((long long)max_s - 1, s); weight >= 0; --weight) {
            if (weight + w < max_s) {
                dp[weight + w] = max(dp[weight + w], dp[weight] + v);
            }
        }
    }

    long long ans = 0;
    for (long long val : dp) ans = max(ans, val);
    cout << ans << "\\n";
    return 0;
}
""",

    # 6. cppb2_l08_18_convex_hull_trick_dp_toi_uu_duong_thang: Dùng mảng song song m_line, c_line
    "cppb2_l08_18_convex_hull_trick_dp_toi_uu_duong_thang": """#include <bits/stdc++.h>
using namespace std;

// Convex Hull Trick (CHT) dùng vector<long long> m_line, c_line
vector<long long> m_line, c_line;

double intersect(int i, int j) {
    return (double)(c_line[j] - c_line[i]) / (m_line[i] - m_line[j]);
}

long long eval_line(int i, long long x) {
    return m_line[i] * x + c_line[i];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];

    vector<long long> dp(n, 0);

    m_line.push_back(b[0]);
    c_line.push_back(0);
    int ptr = 0;

    for (int i = 1; i < n; ++i) {
        long long x = a[i];
        while (ptr + 1 < (int)m_line.size() && eval_line(ptr + 1, x) <= eval_line(ptr, x)) {
            ptr++;
        }
        dp[i] = eval_line(ptr, x);

        long long cur_m = b[i], cur_c = dp[i];
        m_line.push_back(cur_m);
        c_line.push_back(cur_c);
        int sz = m_line.size();

        while (sz >= 3 && intersect(sz - 1, sz - 2) <= intersect(sz - 2, sz - 3)) {
            m_line.erase(m_line.end() - 2);
            c_line.erase(c_line.end() - 2);
            sz--;
            if (ptr >= (int)m_line.size()) ptr = m_line.size() - 1;
        }
    }

    cout << dp[n - 1] << "\\n";
    return 0;
}
""",

    # 7. cppb2_l10_19_multiset_interval_management: Dùng set<pair<int, int>>
    "cppb2_l10_19_multiset_interval_management": """#include <bits/stdc++.h>
using namespace std;

// Quản lý đoạn không dùng struct, dùng set<vector<int>> hoặc set<pair<int, int>>
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    set<vector<int>> intervals; // Mỗi đoạn là {l, r}

    while (q--) {
        int type, l, r;
        cin >> type >> l >> r;
        if (type == 1) {
            auto it = intervals.lower_bound({l, 0});
            if (it != intervals.begin() && prev(it)->at(1) >= l) it--;

            while (it != intervals.end() && it->at(0) <= r) {
                l = min(l, it->at(0));
                r = max(r, it->at(1));
                it = intervals.erase(it);
            }
            intervals.insert({l, r});
        } else {
            auto it = intervals.upper_bound({l, INT_MAX});
            if (it != intervals.begin() && prev(it)->at(1) >= r) {
                cout << "YES\\n";
            } else {
                cout << "NO\\n";
            }
        }
    }
    return 0;
}
""",

    # 8. cppb2_l10_21_priority_queue_dijkstra_custom_comparator: Dùng vector<long long> {dist, edges_used, u}
    "cppb2_l10_21_priority_queue_dijkstra_custom_comparator": """#include <bits/stdc++.h>
using namespace std;

// Dijkstra đa tiêu chí dùng vector<long long> {dist, edges, u} trong priority_queue mặc định
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<vector<long long>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    // Priority queue lưu {dist, edges_used, u}
    priority_queue<vector<long long>, vector<vector<long long>>, greater<vector<long long>>> pq;
    vector<long long> dist(n + 1, LLONG_MAX);

    dist[1] = 0;
    pq.push({0, 0, 1});

    while (!pq.empty()) {
        auto top = pq.top();
        pq.pop();
        long long d = top[0], edges = top[1], u = top[2];

        if (d > dist[u]) continue;

        for (const auto& edge : adj[u]) {
            int v = edge[0];
            long long w = edge[1];
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], edges + 1, v});
            }
        }
    }

    cout << (dist[n] == LLONG_MAX ? -1 : dist[n]) << "\\n";
    return 0;
}
""",

    # 9. cppb2_l12_21_dijkstra_do_thi_nhieu_tang_k_ve_mien_phi: Dùng vector<long long> {d, u, used_k}
    "cppb2_l12_21_dijkstra_do_thi_nhieu_tang_k_ve_mien_phi": """#include <bits/stdc++.h>
using namespace std;

// Dijkstra nhiều tầng dùng priority_queue<vector<long long>>
const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, K;
    if (!(cin >> n >> m >> K)) return 0;

    vector<vector<vector<long long>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<vector<long long>> dist(n + 1, vector<long long>(K + 1, INF));
    priority_queue<vector<long long>, vector<vector<long long>>, greater<vector<long long>>> pq;

    dist[1][0] = 0;
    pq.push({0, 1, 0}); // {d, u, used_k}

    while (!pq.empty()) {
        auto top = pq.top();
        pq.pop();
        long long d = top[0], u = top[1], used = top[2];

        if (d > dist[u][used]) continue;

        for (const auto& edge : adj[u]) {
            int v = edge[0];
            long long w = edge[1];

            if (dist[u][used] + w < dist[v][used]) {
                dist[v][used] = dist[u][used] + w;
                pq.push({dist[v][used], v, used});
            }

            if (used < K && dist[u][used] < dist[v][used + 1]) {
                dist[v][used + 1] = dist[u][used];
                pq.push({dist[v][used + 1], v, used + 1});
            }
        }
    }

    long long ans = INF;
    for (int k = 0; k <= K; ++k) ans = min(ans, dist[n][k]);
    cout << (ans == INF ? -1 : ans) << "\\n";
    return 0;
}
""",

    # 10. cppb2_l12_22_dinh_to_nho_nhat_kruskal_dsu: Dùng vector<vector<long long>> edges = {w, u, v}
    "cppb2_l12_22_dinh_to_nho_nhat_kruskal_dsu": """#include <bits/stdc++.h>
using namespace std;

// Kruskal MST dùng vector<vector<long long>> {w, u, v} và mảng DSU nguyên bản
int parent_arr[200005];

int find_root(int i) {
    if (parent_arr[i] == i) return i;
    return parent_arr[i] = find_root(parent_arr[i]);
}

bool unite(int i, int j) {
    int root_i = find_root(i), root_j = find_root(j);
    if (root_i != root_j) {
        parent_arr[root_j] = root_i;
        return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> edges(m, vector<long long>(3));
    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        edges[i] = {w, u, v}; // {trọng số, u, v} để sort tăng dần
    }

    sort(edges.begin(), edges.end());

    for (int i = 1; i <= n; ++i) parent_arr[i] = i;

    long long mst_weight = 0;
    int edges_count = 0;

    for (const auto& e : edges) {
        long long w = e[0];
        int u = e[1], v = e[2];
        if (unite(u, v)) {
            mst_weight += w;
            edges_count++;
            if (edges_count == n - 1) break;
        }
    }

    if (edges_count != n - 1) cout << "IMPOSSIBLE\\n";
    else cout << mst_weight << "\\n";
    return 0;
}
""",

    # 11. cppb2_l12_23_bellman_ford_chu_trinh_am: Dùng vector<vector<long long>> edges = {u, v, w}
    "cppb2_l12_23_bellman_ford_chu_trinh_am": """#include <bits/stdc++.h>
using namespace std;

// Bellman-Ford dùng vector<vector<long long>> {u, v, w}
const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> edges(m, vector<long long>(3));
    for (int i = 0; i < m; ++i) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    vector<long long> dist(n + 1, 0);

    for (int i = 1; i <= n - 1; ++i) {
        for (const auto& e : edges) {
            int u = e[0], v = e[1];
            long long w = e[2];
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    bool has_neg_cycle = false;
    for (const auto& e : edges) {
        int u = e[0], v = e[1];
        long long w = e[2];
        if (dist[u] + w < dist[v]) {
            has_neg_cycle = true;
            break;
        }
    }

    cout << (has_neg_cycle ? "YES\\n" : "NO\\n");
    return 0;
}
""",

    # 12. cppb2_l13_20_persistent_segment_tree_k_th_number: Dùng mảng song song node_count, node_left, node_right
    "cppb2_l13_20_persistent_segment_tree_k_th_number": """#include <bits/stdc++.h>
using namespace std;

// Persistent Segment Tree dùng mảng song song nguyên bản
const int MAXN = 200005;
int node_count_val[MAXN * 40];
int node_left_child[MAXN * 40];
int node_right_child[MAXN * 40];
int roots[MAXN], total_nodes;

int update_tree(int prev_root, int start, int end, int val) {
    int cur = ++total_nodes;
    node_count_val[cur] = node_count_val[prev_root] + 1;
    node_left_child[cur] = node_left_child[prev_root];
    node_right_child[cur] = node_right_child[prev_root];

    if (start == end) return cur;

    int mid = (start + end) / 2;
    if (val <= mid) {
        node_left_child[cur] = update_tree(node_left_child[prev_root], start, mid, val);
    } else {
        node_right_child[cur] = update_tree(node_right_child[prev_root], mid + 1, end, val);
    }
    return cur;
}

int query_tree(int node_l, int node_r, int start, int end, int k) {
    if (start == end) return start;
    int count_left = node_count_val[node_left_child[node_r]] - node_count_val[node_left_child[node_l]];
    int mid = (start + end) / 2;
    if (k <= count_left) {
        return query_tree(node_left_child[node_l], node_left_child[node_r], start, mid, k);
    } else {
        return query_tree(node_right_child[node_l], node_right_child[node_r], mid + 1, end, k - count_left);
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
        roots[i] = update_tree(roots[i - 1], 1, m, idx);
    }

    while (q--) {
        int l, r, k;
        cin >> l >> r >> k;
        int ans_idx = query_tree(roots[l - 1], roots[r], 1, m, k);
        cout << vals[ans_idx - 1] << "\\n";
    }
    return 0;
}
""",

    # 13. cppb2_l13_25_segment_tree_max_subarray_sum: Dùng 4 mảng song song tree_total, tree_pref, tree_suff, tree_max_sub
    "cppb2_l13_25_segment_tree_max_subarray_sum": """#include <bits/stdc++.h>
using namespace std;

// Segment Tree Max Subarray Sum dùng 4 mảng song song nguyên bản
const int MAXN = 100005;
long long tree_total[4 * MAXN], tree_pref[4 * MAXN], tree_suff[4 * MAXN], tree_max_sub[4 * MAXN];
long long a[MAXN];

void push_up(int node) {
    int left = 2 * node, right = 2 * node + 1;
    tree_total[node] = tree_total[left] + tree_total[right];
    tree_pref[node] = max(tree_pref[left], tree_total[left] + tree_pref[right]);
    tree_suff[node] = max(tree_suff[right], tree_total[right] + tree_suff[left]);
    tree_max_sub[node] = max({tree_max_sub[left], tree_max_sub[right], tree_suff[left] + tree_pref[right]});
}

void build(int node, int start, int end) {
    if (start == end) {
        tree_total[node] = tree_pref[node] = tree_suff[node] = tree_max_sub[node] = a[start];
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    push_up(node);
}

void update(int node, int start, int end, int idx, long long val) {
    if (start == end) {
        tree_total[node] = tree_pref[node] = tree_suff[node] = tree_max_sub[node] = val;
        return;
    }
    int mid = (start + end) / 2;
    if (idx <= mid) update(2 * node, start, mid, idx, val);
    else update(2 * node + 1, mid + 1, end, idx, val);
    push_up(node);
}

vector<long long> query(int node, int start, int end, int l, int r) {
    if (l <= start && end <= r) {
        return {tree_total[node], tree_pref[node], tree_suff[node], tree_max_sub[node]};
    }
    int mid = (start + end) / 2;
    if (r <= mid) return query(2 * node, start, mid, l, r);
    if (l > mid) return query(2 * node + 1, mid + 1, end, l, r);

    auto L = query(2 * node, start, mid, l, r);
    auto R = query(2 * node + 1, mid + 1, end, l, r);

    long long tot = L[0] + R[0];
    long long pref = max(L[1], L[0] + R[1]);
    long long suff = max(R[2], R[0] + L[2]);
    long long mx = max({L[3], R[3], L[2] + R[1]});
    return {tot, pref, suff, mx};
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
            int idx; long long val;
            cin >> idx >> val;
            update(1, 1, n, idx, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << query(1, 1, n, l, r)[3] << "\\n";
        }
    }
    return 0;
}
""",

    # 14. cppb2_l13_26_segment_tree_dem_so_phan_tu_khac_nhau_offline: Dùng vector<vector<int>> queries = {r, l, id}
    "cppb2_l13_26_segment_tree_dem_so_phan_tu_khac_nhau_offline": """#include <bits/stdc++.h>
using namespace std;

// Đếm số phần tử phân biệt dùng vector<vector<int>>: {r, l, id}
const int MAXN = 200005;
int bit_tree[MAXN], a[MAXN], ans[MAXN];
int N;

void update_bit(int idx, int val) {
    for (; idx <= N; idx += idx & -idx) bit_tree[idx] += val;
}

int query_bit(int idx) {
    int sum = 0;
    for (; idx > 0; idx -= idx & -idx) sum += bit_tree[idx];
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> N >> q)) return 0;

    for (int i = 1; i <= N; ++i) cin >> a[i];

    vector<vector<int>> queries(q, vector<int>(3));
    for (int i = 0; i < q; ++i) {
        int l, r;
        cin >> l >> r;
        queries[i] = {r, l, i}; // Sắp xếp theo r
    }

    sort(queries.begin(), queries.end());

    map<int, int> last_pos;
    int cur_r = 1;

    for (const auto& qry : queries) {
        int r = qry[0], l = qry[1], id = qry[2];
        while (cur_r <= r) {
            if (last_pos.count(a[cur_r])) {
                update_bit(last_pos[a[cur_r]], -1);
            }
            last_pos[a[cur_r]] = cur_r;
            update_bit(cur_r, 1);
            cur_r++;
        }
        ans[id] = query_bit(r) - query_bit(l - 1);
    }

    for (int i = 0; i < q; ++i) cout << ans[i] << "\\n";
    return 0;
}
"""
}

def main():
    print("🚀 Bắt đầu loại bỏ triệt để struct, chuyển sang vector<vector<long long>> và mảng song song...")
    count = 0
    for pname, code in REFACTORED_SOLUTIONS.items():
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

    print(f"🎉 Hoàn tất! Đã refactor loại bỏ struct cho {count} bài toán!")

if __name__ == "__main__":
    main()
