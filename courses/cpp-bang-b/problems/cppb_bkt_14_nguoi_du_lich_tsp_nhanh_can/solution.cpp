#include <bits/stdc++.h>
using namespace std;

int n;
long long c[15][15];
bool visited[15];
long long min_edge = 1e9;
long long best_cost = 1e18;

void branchAndBound(int u, int count, long long current_cost) {
    // Optimality Pruning
    if (current_cost + (n - count + 1) * min_edge >= best_cost) return;

    if (count == n) {
        best_cost = min(best_cost, current_cost + c[u][1]);
        return;
    }

    for (int v = 2; v <= n; ++v) {
        if (!visited[v]) {
            visited[v] = true;
            branchAndBound(v, count + 1, current_cost + c[u][v]);
            visited[v] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> c[i][j];
            if (i != j) min_edge = min(min_edge, c[i][j]);
        }
    }
    memset(visited, false, sizeof(visited));
    visited[1] = true;
    branchAndBound(1, 1, 0);
    cout << best_cost << "\n";
    return 0;
}
