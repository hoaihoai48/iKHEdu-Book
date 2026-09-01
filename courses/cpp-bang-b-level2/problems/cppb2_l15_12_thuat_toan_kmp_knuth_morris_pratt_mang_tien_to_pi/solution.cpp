#include <bits/stdc++.h>
using namespace std;

string manacher(string s) {
    string t = "^";
    for (char c : s) t += "#" + string(1, c);
    t += "#$";

    int n = t.size();
    vector<int> p(n, 0);
    int c = 0, r = 0;

    for (int i = 1; i < n - 1; ++i) {
        int i_mirror = 2 * c - i;
        if (r > i) p[i] = min(r - i, p[i_mirror]);
        while (t[i + 1 + p[i]] == t[i - 1 - p[i]]) p[i]++;
        if (i + p[i] > r) {
            c = i;
            r = i + p[i];
        }
    }

    int max_len = 0, center_idx = 0;
    for (int i = 1; i < n - 1; ++i) {
        if (p[i] > max_len) {
            max_len = p[i];
            center_idx = i;
        }
    }

    int start = (center_idx - 1 - max_len) / 2;
    return s.substr(start, max_len);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    cout << manacher(s) << "\n";
    return 0;
}
