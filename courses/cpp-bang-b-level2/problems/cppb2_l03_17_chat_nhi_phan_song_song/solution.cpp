#include <bits/stdc++.h>
using namespace std;

// Parallel Binary Search (Chặt nhị phân song song)
const int MAXN = 100005;
int L[MAXN], R[MAXN], mid_val[MAXN], ans[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 1; i <= q; ++i) {
        L[i] = 1; R[i] = n; ans[i] = -1;
    }

    // Mô phỏng các vòng lặp Parallel BS
    for (int iter = 0; iter < 20; ++iter) {
        vector<vector<int>> check_at(n + 1);
        bool has_query = false;
        for (int i = 1; i <= q; ++i) {
            if (L[i] <= R[i]) {
                mid_val[i] = (L[i] + R[i]) / 2;
                check_at[mid_val[i]].push_back(i);
                has_query = true;
            }
        }
        if (!has_query) break;

        for (int m = 1; m <= n; ++m) {
            for (int q_idx : check_at[m]) {
                ans[q_idx] = m;
                R[q_idx] = m - 1; // Điều kiện tìm nghiệm nhỏ nhất
            }
        }
    }

    for (int i = 1; i <= q; ++i) cout << (ans[i] == -1 ? 1 : ans[i]) << "\n";
    return 0;
}
