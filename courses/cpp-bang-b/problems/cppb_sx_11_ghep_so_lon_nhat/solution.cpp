#include <bits/stdc++.h>
using namespace std;

bool cmp(const string &a, const string &b) {
    return a + b > b + a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> s(n);
    for (int i = 0; i < n; ++i) cin >> s[i];

    sort(s.begin(), s.end(), cmp);

    if (s[0] == "0") {
        cout << 0 << "\n";
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        cout << s[i];
    }
    cout << "\n";
    return 0;
}
