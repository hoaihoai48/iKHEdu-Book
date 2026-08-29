#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long r;
    if (!(cin >> n >> r)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    int i = 0;
    int count = 0;

    while (i < n) {
        ++count;
        long long loc = x[i];
        while (i < n && x[i] - loc <= r) ++i;
        long long tower = x[i - 1];
        while (i < n && x[i] - tower <= r) ++i;
    }

    cout << count << "\n";
    return 0;
}
