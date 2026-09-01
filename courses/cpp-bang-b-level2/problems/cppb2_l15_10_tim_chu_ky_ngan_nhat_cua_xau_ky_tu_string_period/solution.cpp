#include <bits/stdc++.h>
using namespace std;

int least_rotation(string s) {
    s += s;
    int n = s.size();
    vector<int> f(n, -1);
    int k = 0;
    for (int j = 1; j < n; ++j) {
        char sj = s[j];
        int i = f[j - k - 1];
        while (i != -1 && sj != s[k + i + 1]) {
            if (sj < s[k + i + 1]) k = j - i - 1;
            i = f[i];
        }
        if (sj != s[k + i + 1]) {
            if (sj < s[k]) k = j;
            f[j - k] = -1;
        } else {
            f[j - k] = i + 1;
        }
    }
    return k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int idx = least_rotation(s);
    cout << s.substr(idx) + s.substr(0, idx) << "\n";
    return 0;
}
