#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> t(n);
    for (int i = 0; i < n; ++i) cin >> t[i];

    sort(t.begin(), t.end());

    long long total_wait = 0, cur_time = 0;
    for (int i = 0; i < n; ++i) {
        total_wait += cur_time;
        cur_time += t[i];
    }

    cout << total_wait << "\n";
    return 0;
}
