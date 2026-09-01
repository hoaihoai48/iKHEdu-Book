#include <bits/stdc++.h>
using namespace std;

// Floyd-Warshall tìm đường đi ngắn nhất mọi cặp đỉnh O(N^3)
const long long INF = 1e18;
long long dist_mat[505][505];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (i == j) dist_mat[i][j] = 0;
            else dist_mat[i][j] = INF;
        }
    }

    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        dist_mat[u][v] = min(dist_mat[u][v], w);
        dist_mat[v][u] = min(dist_mat[v][u], w);
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (dist_mat[i][k] < INF && dist_mat[k][j] < INF) {
                    dist_mat[i][j] = min(dist_mat[i][j], dist_mat[i][k] + dist_mat[k][j]);
                }
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cout << (dist_mat[i][j] == INF ? -1 : dist_mat[i][j]) << " ";
        }
        cout << "\n";
    }
    return 0;
}
