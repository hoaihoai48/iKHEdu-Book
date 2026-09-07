#include <bits/stdc++.h>
using namespace std;

int inv_count(const vector<int> &p) {
    int c = 0;
    for (int i = 0; i < 9; ++i) {
        if (p[i] == 0) continue;
        for (int j = i + 1; j < 9; ++j) {
            if (p[j] == 0) continue;
            if (p[i] > p[j]) ++c;
        }
    }
    return c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> s(9), t(9);
    for (int i = 0; i < 9; ++i) if (!(cin >> s[i])) return 0;
    for (int i = 0; i < 9; ++i) cin >> t[i];

    string start, goal;
    for (int x : s) start.push_back((char)('0' + x));
    for (int x : t) goal.push_back((char)('0' + x));
    if (start == goal) {
        cout << 0 << "\n";
        return 0;
    }
    if ((inv_count(s) & 1) != (inv_count(t) & 1)) {
        cout << -1 << "\n";
        return 0;
    }
    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};
    unordered_map<string, int> dS, dT;
    queue<string> qS, qT;
    dS[start] = 0; qS.push(start);
    dT[goal] = 0; qT.push(goal);
    while (!qS.empty() && !qT.empty()) {
        bool expandS = qS.size() <= qT.size();
        queue<string> &q = expandS ? qS : qT;
        unordered_map<string, int> &dC = expandS ? dS : dT;
        unordered_map<string, int> &dO = expandS ? dT : dS;
        int sz = (int)q.size();
        while (sz--) {
            string cur = q.front();
            q.pop();
            int z = (int)cur.find('0');
            int zr = z / 3, zc = z % 3;
            for (int d = 0; d < 4; ++d) {
                int nr = zr + dr[d], nc = zc + dc[d];
                if (nr < 0 || nr >= 3 || nc < 0 || nc >= 3) continue;
                string nxt = cur;
                swap(nxt[z], nxt[nr * 3 + nc]);
                if (dC.count(nxt)) continue;
                dC[nxt] = dC[cur] + 1;
                if (dO.count(nxt)) {
                    cout << dC[nxt] + dO[nxt] << "\n";
                    return 0;
                }
                q.push(nxt);
            }
        }
    }
    cout << -1 << "\n";
    return 0;
}
