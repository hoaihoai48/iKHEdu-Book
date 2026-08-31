#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long c;
    if (!(cin >> n >> c)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> min_dq, max_dq;
    int left = 0;
    int max_len = 0;

    for (int right = 0; right < n; ++right) {
        while (!min_dq.empty() && a[min_dq.back()] >= a[right]) min_dq.pop_back();
        min_dq.push_back(right);

        while (!max_dq.empty() && a[max_dq.back()] <= a[right]) max_dq.pop_back();
        max_dq.push_back(right);

        while (a[max_dq.front()] - a[min_dq.front()] > c) {
            left++;
            if (min_dq.front() < left) min_dq.pop_front();
            if (max_dq.front() < left) max_dq.pop_front();
        }

        max_len = max(max_len, right - left + 1);
    }

    cout << max_len << "\n";
    return 0;
}
