#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total += a[i];
    }

    if (total % 2 != 0) {
        cout << "NO\n";
        return 0;
    }

    long long target = total / 2;
    int mid = n / 2;

    vector<long long> s1, s2;
    for (int mask = 0; mask < (1 << mid); ++mask) {
        long long sum = 0;
        for (int i = 0; i < mid; ++i) if ((mask >> i) & 1) sum += a[i];
        s1.push_back(sum);
    }

    int rem = n - mid;
    unordered_set<long long> s2_set;
    for (int mask = 0; mask < (1 << rem); ++mask) {
        long long sum = 0;
        for (int i = 0; i < rem; ++i) if ((mask >> i) & 1) sum += a[mid + i];
        s2_set.insert(sum);
    }

    for (long long x : s1) {
        if (s2_set.count(target - x)) {
            cout << "YES\n";
            return 0;
        }
    }

    cout << "NO\n";
    return 0;
}
