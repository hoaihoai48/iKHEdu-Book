#include <bits/stdc++.h>
using namespace std;

// Đếm số chu trình 4 đỉnh C4 bằng Meet in the Middle O(M * sqrt(M))
const int MAXN = 50005;
vector<int> adj[MAXN];
int cnt[MAXN];

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

    long long ans = 0;
    for (int u = 1; u <= n; ++u) {
        for (int v : adj[u]) {
            for (int w : adj[v]) {
                if (w != u && w > u) { // Đảm bảo đếm không lặp
                    ans += cnt[w];
                    cnt[w]++;
                }
            }
        }
        for (int v : adj[u]) {
            for (int w : adj[v]) {
                if (w != u && w > u) {
                    cnt[w] = 0; // Reset
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
