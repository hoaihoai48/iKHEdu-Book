#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    map<long long, int> freq;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        freq[a[i]]++;
    }
    long long ans = -1;
    for (auto &p : freq) {
        if (p.second > n / 2) { ans = p.first; break; }
    }
    cout << ans << "\n";
    return 0;
}
