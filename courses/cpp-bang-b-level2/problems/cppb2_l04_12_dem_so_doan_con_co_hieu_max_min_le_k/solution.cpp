#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> max_dq, min_dq;
    long long count = 0;
    int l = 0;

    for (int r = 0; r < n; ++r) {
        while (!max_dq.empty() && a[max_dq.back()] <= a[r]) max_dq.pop_back();
        max_dq.push_back(r);

        while (!min_dq.empty() && a[min_dq.back()] >= a[r]) min_dq.pop_back();
        min_dq.push_back(r);

        while (a[max_dq.front()] - a[min_dq.front()] > k) {
            l++;
            if (max_dq.front() < l) max_dq.pop_front();
            if (min_dq.front() < l) min_dq.pop_front();
        }

        count += (r - l + 1);
    }

    cout << count << "\n";
    return 0;
}
