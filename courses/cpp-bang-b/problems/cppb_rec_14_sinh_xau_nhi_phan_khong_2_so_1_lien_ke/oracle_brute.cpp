#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    vector<string> res;
    for (int mask = 0; mask < (1 << n); ++mask) {
        if (mask & (mask >> 1)) continue;
        string s = "";
        for (int i = n - 1; i >= 0; --i) {
            s.push_back((mask & (1 << i)) ? '1' : '0');
        }
        res.push_back(s);
    }
    cout << res.size() << "\n";
    for (auto &s : res) cout << s << "\n";
    return 0;
}
