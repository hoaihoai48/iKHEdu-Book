#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0) return 0;

    map<long long, int> freq;
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        if (freq.count(x - k)) ans += freq[x - k];
        if (k != 0 && freq.count(x + k)) ans += freq[x + k];
        freq[x]++;
    }

    cout << ans << "\n";
    return 0;
}
