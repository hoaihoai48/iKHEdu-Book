#include <bits/stdc++.h>
using namespace std;

// Box Stacking dùng vector<vector<long long>>: {w + s, w, s, v}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> boxes(n, vector<long long>(4));
    for (int i = 0; i < n; ++i) {
        long long w, s, v;
        cin >> w >> s >> v;
        boxes[i] = {w + s, w, s, v};
    }

    sort(boxes.begin(), boxes.end());

    int max_s = 20005;
    vector<long long> dp(max_s, 0);

    for (const auto& b : boxes) {
        long long w = b[1], s = b[2], v = b[3];
        for (int weight = min((long long)max_s - 1, s); weight >= 0; --weight) {
            if (weight + w < max_s) {
                dp[weight + w] = max(dp[weight + w], dp[weight] + v);
            }
        }
    }

    long long ans = 0;
    for (long long val : dp) ans = max(ans, val);
    cout << ans << "\n";
    return 0;
}
