#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    long long k;
    if (!(cin >> s >> k)) return 0;
    string res;
    for (char c : s) {
        while (!res.empty() && res.back() > c && k > 0) {
            res.pop_back();
            --k;
        }
        res.push_back(c);
    }
    while (k > 0 && !res.empty()) {
        res.pop_back();
        --k;
    }
    size_t p = 0;
    while (p < res.size() && res[p] == '0') ++p;
    res = res.substr(p);
    if (res.empty()) res = "0";
    cout << res << "\n";
    return 0;
}
