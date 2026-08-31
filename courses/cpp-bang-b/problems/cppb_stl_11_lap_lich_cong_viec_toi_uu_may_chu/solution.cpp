#include <bits/stdc++.h>
using namespace std;

struct Job {
    long long s, e;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<Job> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].s >> a[i].e;

    sort(a.begin(), a.end(), [](const Job& x, const Job& y) {
        if (x.s != y.s) return x.s < y.s;
        return x.e < y.e;
    });

    priority_queue<long long, vector<long long>, greater<long long>> servers;

    for (int i = 0; i < n; ++i) {
        if (!servers.empty() && servers.top() <= a[i].s) {
            servers.pop();
        }
        servers.push(a[i].e);
    }

    cout << servers.size() << "\n";
    return 0;
}
