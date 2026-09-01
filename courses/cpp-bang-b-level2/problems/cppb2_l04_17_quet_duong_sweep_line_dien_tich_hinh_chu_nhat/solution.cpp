#include <bits/stdc++.h>
using namespace std;

// Sweep-line dùng vector<vector<long long>> biểu diễn sự kiện: {x, type, y1, y2}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> events;
    vector<long long> Y;

    for (int i = 0; i < n; ++i) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        events.push_back({x1, 1, y1, y2});
        events.push_back({x2, -1, y1, y2});
        Y.push_back(y1);
        Y.push_back(y2);
    }

    sort(Y.begin(), Y.end());
    Y.erase(unique(Y.begin(), Y.end()), Y.end());
    sort(events.begin(), events.end());

    vector<int> count_cover(Y.size(), 0);
    long long total_area = 0;

    for (size_t i = 0; i + 1 < events.size(); ++i) {
        int y1_idx = lower_bound(Y.begin(), Y.end(), events[i][2]) - Y.begin();
        int y2_idx = lower_bound(Y.begin(), Y.end(), events[i][3]) - Y.begin();

        for (int j = y1_idx; j < y2_idx; ++j) {
            count_cover[j] += events[i][1];
        }

        long long covered_len = 0;
        for (size_t j = 0; j + 1 < Y.size(); ++j) {
            if (count_cover[j] > 0) {
                covered_len += Y[j + 1] - Y[j];
            }
        }
        total_area += covered_len * (events[i + 1][0] - events[i][0]);
    }

    cout << total_area << "\n";
    return 0;
}
