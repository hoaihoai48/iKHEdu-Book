#include <bits/stdc++.h>
using namespace std;

struct Event {
    long long l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Event> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].l >> a[i].r;

    sort(a.begin(), a.end(), [](const Event &x, const Event &y) {
        return x.r < y.r;
    });

    int count = 0;
    long long last_end = -2e18;
    for (const auto &e : a) {
        if (e.l >= last_end) {
            count++;
            last_end = e.r;
        }
    }

    cout << count << "\n";
    return 0;
}
