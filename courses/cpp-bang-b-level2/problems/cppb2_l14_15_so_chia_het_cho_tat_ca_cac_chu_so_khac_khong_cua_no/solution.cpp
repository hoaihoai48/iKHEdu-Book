#include <bits/stdc++.h>
using namespace std;

long long count_no_4(long long n) {
    if (n <= 0) return 0;
    string s = to_string(n);
    long long ans = 0;
    for (size_t i = 0; i < s.size(); ++i) {
        int d = s[i] - '0';
        int valid = (d > 4 ? d - 1 : d);
        ans += valid * pow(9, s.size() - i - 1);
        if (d == 4) break;
        if (i + 1 == s.size()) ans++;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long k;
    if (!(cin >> k)) return 0;

    long long low = 1, high = 2e18, ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_no_4(mid) >= k) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
