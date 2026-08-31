#include <bits/stdc++.h>
using namespace std;

int V, E, K;
vector<int> adj[15];
int color[15];
bool possible = false;

bool isSafe(int u, int c) {
    for (int v : adj[u]) {
        if (color[v] == c) return false;
    }
    return true;
}

void backtrack(int u) {
    if (possible) return;
    if (u > V) {
        possible = true;
        return;
    }
    for (int c = 1; c <= K; ++c) {
        if (isSafe(u, c)) {
            color[u] = c;
            backtrack(u + 1);
            color[u] = 0;
            if (possible) return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> V >> E >> K)) return 0;
    for (int i = 0; i < E; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    memset(color, 0, sizeof(color));
    backtrack(1);
    cout << (possible ? "YES\n" : "NO\n");
    return 0;
}
