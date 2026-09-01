#include <bits/stdc++.h>
using namespace std;

struct Event {
    long long x;
    int type; // +1: start, -1: end
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Event> events;
    for (int i = 0; i < n; ++i) {
        long long l, r;
        cin >> l >> r;
        events.push_back({l, 1});
        events.push_back({r, -1});
    }

    sort(events.begin(), events.end(), [](const Event &a, const Event &b) {
        if (a.x != b.x) return a.x < b.x;
        return a.type > b.type;
    });

    long long active = 0, overlaps = 0;
    for (const auto &e : events) {
        if (e.type == 1) {
            overlaps += active;
            active++;
        } else {
            active--;
        }
    }

    cout << overlaps << "\n";
    return 0;
}
