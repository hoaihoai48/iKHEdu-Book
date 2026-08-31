#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, r, c;
    if (!(cin >> n >> m >> r >> c)) return 0;

    int valid_neighbors = 0;
    for (int d = 0; d < 4; ++d) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
            valid_neighbors++;
        }
    }

    cout << valid_neighbors << "\n";
    return 0;
}
