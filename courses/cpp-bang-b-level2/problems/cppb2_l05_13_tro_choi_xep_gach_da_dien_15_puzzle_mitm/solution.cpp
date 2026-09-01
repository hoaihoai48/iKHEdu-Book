#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string start_state = "", target_state = "123456780";
    for (int i = 0; i < 9; ++i) {
        int val; cin >> val;
        start_state += to_string(val);
    }

    unordered_map<string, int> dist_f, dist_b;
    queue<string> q_f, q_b;

    dist_f[start_state] = 0; q_f.push(start_state);
    dist_b[target_state] = 0; q_b.push(target_state);

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    auto expand = [&](queue<string> &q, unordered_map<string, int> &d_cur, unordered_map<string, int> &d_other) {
        int sz = q.size();
        while (sz--) {
            string u = q.front(); q.pop();
            if (d_other.count(u)) return d_cur[u] + d_other[u];

            int pos = u.find('0');
            int r = pos / 3, c = pos % 3;
            for (int k = 0; k < 4; ++k) {
                int nr = r + dx[k], nc = c + dy[k];
                if (nr >= 0 && nr < 3 && nc >= 0 && nc < 3) {
                    string v = u;
                    swap(v[pos], v[nr * 3 + nc]);
                    if (!d_cur.count(v)) {
                        d_cur[v] = d_cur[u] + 1;
                        q.push(v);
                    }
                }
            }
        }
        return -1;
    };

    while (!q_f.empty() && !q_b.empty()) {
        int res;
        if (q_f.size() <= q_b.size()) res = expand(q_f, dist_f, dist_b);
        else res = expand(q_b, dist_b, dist_f);

        if (res != -1) {
            cout << res << "\n";
            return 0;
        }
    }

    cout << "-1\n";
    return 0;
}
