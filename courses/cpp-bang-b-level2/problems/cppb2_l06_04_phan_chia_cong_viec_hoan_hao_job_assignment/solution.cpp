#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int n;
int dist_mat[20][20];
int dp[1 << 18][18];

int tsp(int mask, int u) {
    if (mask == (1 << n) - 1) return dist_mat[u][0];
    if (dp[mask][u] != -1) return dp[mask][u];

    int ans = INF;
    for (int v = 0; v < n; ++v) {
        if (!((mask >> v) & 1)) {
            ans = min(ans, dist_mat[u][v] + tsp(mask | (1 << v), v));
        }
    }
    return dp[mask][u] = ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> dist_mat[i][j];
    }

    memset(dp, -1, sizeof(dp));
    cout << tsp(1, 0) << "\n";
    return 0;
}
