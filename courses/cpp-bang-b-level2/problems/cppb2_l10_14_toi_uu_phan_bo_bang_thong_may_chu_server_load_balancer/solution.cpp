#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end(), [](const string &x, const string &y) {
        return x + y > y + x;
    });

    if (a[0] == "0") {
        cout << "0\n";
        return 0;
    }

    for (const string &s : a) cout << s;
    cout << "\n";
    return 0;
}
