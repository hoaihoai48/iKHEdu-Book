#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> p(n);
    for (int i = 0; i < n; ++i) cin >> p[i];

    long long profit = 0;
    for (int i = 1; i < n; ++i) {
        if (p[i] > p[i - 1]) profit += (p[i] - p[i - 1]);
    }

    cout << profit << "\n";
    return 0;
}
