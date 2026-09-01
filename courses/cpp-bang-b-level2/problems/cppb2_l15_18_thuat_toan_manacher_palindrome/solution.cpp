#include <bits/stdc++.h>
using namespace std;

// Manacher Algorithm tìm xâu con đối xứng dài nhất O(N)
string transform_string(const string& s) {
    string res = "^";
    for (char c : s) {
        res += "#";
        res += c;
    }
    res += "#$";
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    string t = transform_string(s);
    int n = t.size();
    vector<int> p(n, 0);
    int c = 0, r = 0;
    int max_len = 0;

    for (int i = 1; i < n - 1; ++i) {
        int i_mirror = 2 * c - i;
        if (r > i) p[i] = min(r - i, p[i_mirror]);

        while (t[i + 1 + p[i]] == t[i - 1 - p[i]]) p[i]++;

        if (i + p[i] > r) {
            c = i;
            r = i + p[i];
        }
        max_len = max(max_len, p[i]);
    }

    cout << max_len << "\n";
    return 0;
}
