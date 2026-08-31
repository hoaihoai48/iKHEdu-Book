#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0 || k <= 0 || k > n) return 0;

    priority_queue<long long, vector<long long>, greater<long long>> min_heap;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        min_heap.push(x);
        if ((int)min_heap.size() > k) {
            min_heap.pop();
        }
    }

    vector<long long> result;
    while (!min_heap.empty()) {
        result.push_back(min_heap.top());
        min_heap.pop();
    }
    sort(result.rbegin(), result.rend());

    for (int i = 0; i < k; ++i) {
        cout << result[i] << (i + 1 == k ? "" : " ");
    }
    cout << "\n";
    return 0;
}
