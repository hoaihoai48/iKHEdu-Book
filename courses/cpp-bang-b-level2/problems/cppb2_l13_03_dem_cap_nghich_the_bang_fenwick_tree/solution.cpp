#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    if (!(cin >> N)) return 0;
    vector<long long> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];
    vector<long long> v = a;
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    vector<int> bit(v.size() + 2, 0);
    auto add = [&](int i) { for (; i < (int)bit.size(); i += i & -i) bit[i]++; };
    auto sum = [&](int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; };
    long long ans = 0;
    for (int i = N - 1; i >= 0; i--) {
        int r = (int)(lower_bound(v.begin(), v.end(), a[i]) - v.begin()) + 1;
        ans += sum(r - 1);
        add(r);
    }
    cout << ans << "\n";
    return 0;
}
