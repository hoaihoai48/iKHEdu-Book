#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<string> grid;
vector<vector<int>> island_id;
vector<int> island_size;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;
    grid.resize(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    island_id.assign(n, vector<int>(m, 0));
    island_size.push_back(0); // id 0 unused
    int current_id = 1;
    int max_area = 0;

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '1' && island_id[r][c] == 0) {
                int sz = 0;
                island_id[r][c] = current_id;
                queue<pair<int, int>> q;
                q.push({r, c});

                while (!q.empty()) {
                    auto [cr, cc] = q.front();
                    q.pop();
                    sz++;

                    for (int d = 0; d < 4; ++d) {
                        int nr = cr + dr[d];
                        int nc = cc + dc[d];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '1' && island_id[nr][nc] == 0) {
                            island_id[nr][nc] = current_id;
                            q.push({nr, nc});
                        }
                    }
                }

                island_size.push_back(sz);
                max_area = max(max_area, sz);
                current_id++;
            }
        }
    }

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '0') {
                unordered_set<int> neighbor_ids;
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m && island_id[nr][nc] > 0) {
                        neighbor_ids.insert(island_id[nr][nc]);
                    }
                }
                int combined_sz = 1;
                for (int id : neighbor_ids) combined_sz += island_size[id];
                max_area = max(max_area, combined_sz);
            }
        }
    }

    cout << max_area << "\n";
    return 0;
}
