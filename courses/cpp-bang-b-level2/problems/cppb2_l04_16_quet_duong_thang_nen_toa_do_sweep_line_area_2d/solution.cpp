#include <bits/stdc++.h>
using namespace std;

struct Event {
    long long x, y1, y2;
    int type;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Event> events;
    vector<long long> Y;
    for (int i = 0; i < n; ++i) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        events.push_back({x1, y1, y2, 1});
        events.push_back({x2, y1, y2, -1});
        Y.push_back(y1);
        Y.push_back(y2);
    }

    sort(Y.begin(), Y.end());
    Y.erase(unique(Y.begin(), Y.end()), Y.end());

    sort(events.begin(), events.end(), [](const Event &a, const Event &b) {
        return a.x < b.x;
    });

    vector<int> cnt(Y.size(), 0);
    long long total_area = 0;

    for (size_t i = 0; i + 1 < events.size(); ++i) {
        int y1_idx = lower_bound(Y.begin(), Y.end(), events[i].y1) - Y.begin();
        int y2_idx = lower_bound(Y.begin(), Y.end(), events[i].y2) - Y.begin();

        for (int j = y1_idx; j < y2_idx; ++j) {
            cnt[j] += events[i].type;
        }

        long long covered_y = 0;
        for (size_t j = 0; j + 1 < Y.size(); ++j) {
            if (cnt[j] > 0) covered_y += (Y[j + 1] - Y[j]);
        }

        total_area += covered_y * (events[i + 1].x - events[i].x);
    }

    cout << total_area << "\n";
    return 0;
}
