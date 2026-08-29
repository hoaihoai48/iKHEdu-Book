#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    int ca = 0, cb = 0, cc = 0;

    // Lưu: {diff1, diff2, index}
    vector<vector<int>> states;
    states.reserve(n + 1);
    states.push_back({0, 0, 0}); // Tại vị trí 0

    for (int i = 1; i <= n; ++i) {
        if (s[i - 1] == 'A') ca++;
        else if (s[i - 1] == 'B') cb++;
        else if (s[i - 1] == 'C') cc++;

        states.push_back({ca - cb, cb - cc, i});
    }

    sort(states.begin(), states.end(), [](const vector<int>& u, const vector<int>& v) {
        if (u[0] != v[0]) return u[0] < v[0];
        if (u[1] != v[1]) return u[1] < v[1];
        return u[2] < v[2];
    });

    int max_len = 0;
    int i = 0;
    while (i <= n) {
        int j = i;
        while (j <= n && states[j][0] == states[i][0] && states[j][1] == states[i][1]) {
            j++;
        }
        max_len = max(max_len, states[j - 1][2] - states[i][2]);
        i = j;
    }

    cout << max_len << "\n";
    return 0;
}
