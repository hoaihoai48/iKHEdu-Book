#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long max_xor = 0;
    long long mask = 0;

    for (int bit = 30; bit >= 0; --bit) {
        mask |= (1LL << bit);
        vector<long long> prefixes;
        prefixes.reserve(n);
        for (long long x : a) {
            prefixes.push_back(x & mask);
        }
        sort(prefixes.begin(), prefixes.end());
        prefixes.erase(unique(prefixes.begin(), prefixes.end()), prefixes.end());

        long long candidate = max_xor | (1LL << bit);
        bool found = false;

        for (long long p : prefixes) {
            long long target = p ^ candidate;
            if (binary_search(prefixes.begin(), prefixes.end(), target)) {
                found = true;
                break;
            }
        }

        if (found) {
            max_xor = candidate;
        }
    }

    cout << max_xor << "\n";
    return 0;
}
