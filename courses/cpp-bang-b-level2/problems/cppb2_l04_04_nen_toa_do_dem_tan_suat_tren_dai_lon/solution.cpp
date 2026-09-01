#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    vector<int> freq(vals.size(), 0);
    for (long long x : a) {
        int idx = lower_bound(vals.begin(), vals.end(), x) - vals.begin();
        freq[idx]++;
    }

    for (size_t i = 0; i < vals.size(); ++i) {
        cout << vals[i] << ": " << freq[i] << "\n";
    }
    return 0;
}
