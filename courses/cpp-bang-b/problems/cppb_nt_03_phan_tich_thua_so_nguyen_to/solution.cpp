#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, int>> factors;
    for (long long i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            int cnt = 0;
            while (n % i == 0) {
                cnt++;
                n /= i;
            }
            factors.push_back({i, cnt});
        }
    }
    if (n > 1) {
        factors.push_back({n, 1});
    }

    for (int i = 0; i < (int)factors.size(); ++i) {
        cout << factors[i].first << "^" << factors[i].second;
        if (i + 1 < (int)factors.size()) cout << " * ";
    }
    cout << "\n";
    return 0;
}