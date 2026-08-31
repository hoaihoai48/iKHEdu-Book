#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    long long lower, upper;
    if (!(cin >> n >> lower >> upper)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long cnt = 0;
    for (int i = 0; i < n; ++i) {
        long long sum = 0;
        for (int j = i; j < n; ++j) {
            sum += a[j];
            if (sum >= lower && sum <= upper) cnt++;
        }
    }
    cout << cnt << "\n";
    return 0;
}
