#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> p(n);
    long long total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        total_sum += p[i];
    }

    long long min_diff = total_sum;
    int total_masks = (1 << n);

    for (int mask = 0; mask < total_masks; ++mask) {
        long long s1 = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                s1 += p[i];
            }
        }
        long long s2 = total_sum - s1;
        min_diff = min(min_diff, abs(s1 - s2));
    }

    cout << min_diff << "\n";
    return 0;
}
