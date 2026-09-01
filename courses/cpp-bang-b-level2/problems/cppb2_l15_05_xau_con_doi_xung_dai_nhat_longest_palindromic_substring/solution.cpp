#include <bits/stdc++.h>
using namespace std;

vector<int> compute_lps(const string &p) {
    int m = p.size();
    vector<int> lps(m, 0);
    int len = 0, i = 1;
    while (i < m) {
        if (p[i] == p[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) len = lps[len - 1];
            else { lps[i] = 0; i++; }
        }
    }
    return lps;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string t, p;
    if (!(cin >> t >> p)) return 0;

    int n = t.size(), m = p.size();
    vector<int> lps = compute_lps(p);
    int i = 0, j = 0;

    while (i < n) {
        if (t[i] == p[j]) {
            i++; j++;
        }
        if (j == m) {
            cout << i - j + 1 << " ";
            j = lps[j - 1];
        } else if (i < n && t[i] != p[j]) {
            if (j != 0) j = lps[j - 1];
            else i++;
        }
    }
    cout << "\n";
    return 0;
}
