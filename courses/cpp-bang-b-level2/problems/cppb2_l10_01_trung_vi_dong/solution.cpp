#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    priority_queue<long long> lo;
    priority_queue<long long, vector<long long>, greater<long long>> hi;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        if (lo.empty() || x <= lo.top()) lo.push(x);
        else hi.push(x);

        if ((int)lo.size() > (int)hi.size() + 1) {
            hi.push(lo.top());
            lo.pop();
        } else if ((int)lo.size() < (int)hi.size()) {
            lo.push(hi.top());
            hi.pop();
        }

        if (i > 0) cout << ' ';
        cout << lo.top();
    }
    cout << "\n";
    return 0;
}
