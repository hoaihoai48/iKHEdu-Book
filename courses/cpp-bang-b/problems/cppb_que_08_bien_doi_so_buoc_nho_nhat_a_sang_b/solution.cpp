#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    if (!(cin >> a >> b)) return 0;

    if (a >= b) {
        cout << a - b << "\n";
        return 0;
    }

    vector<int> dist(20005, -1);
    queue<int> q;

    dist[a] = 0;
    q.push(a);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (u == b) {
            cout << dist[b] << "\n";
            return 0;
        }

        // Thao tác 1: u * 2
        if (u * 2 <= 20000 && dist[u * 2] == -1) {
            dist[u * 2] = dist[u] + 1;
            q.push(u * 2);
        }

        // Thao tác 2: u - 1
        if (u - 1 > 0 && dist[u - 1] == -1) {
            dist[u - 1] = dist[u] + 1;
            q.push(u - 1);
        }
    }

    return 0;
}
