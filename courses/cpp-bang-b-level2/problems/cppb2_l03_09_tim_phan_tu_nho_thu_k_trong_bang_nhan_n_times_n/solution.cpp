#include <bits/stdc++.h>
using namespace std;

long long count_le(long long x, long long n) {
    long long cnt = 0;
    for (long long i = 1; i <= n; ++i) {
        cnt += min(n, x / i);
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    long long low = 1, high = n * n;
    long long ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_le(mid, n) >= k) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
