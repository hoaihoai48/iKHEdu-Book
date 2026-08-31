#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n + 1);
    long long total_sum = 0;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        total_sum += a[i];
    }

    // dp[i]: tổng nhỏ nhất các phần tử bị loại bỏ kết thúc tại i sao cho không có k+1 phần tử liền kề nào được chọn
    vector<long long> dp(n + 1, 0);
    deque<int> dq;
    dq.push_back(0);

    for (int i = 1; i <= n; ++i) {
        while (!dq.empty() && dq.front() < i - k - 1) dq.pop_front();
        dp[i] = dp[dq.front()] + a[i];
        while (!dq.empty() && dp[dq.back()] >= dp[i]) dq.pop_back();
        dq.push_back(i);
    }

    long long min_dropped = LLONG_MAX;
    for (int i = n - k; i <= n; ++i) {
        if (i >= 0) min_dropped = min(min_dropped, dp[i]);
    }

    cout << total_sum - min_dropped << "\n";
    return 0;
}
