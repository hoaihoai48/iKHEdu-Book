#include <bits/stdc++.h>
using namespace std;

struct Item {
    double v, w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    double W;
    if (!(cin >> n >> W)) return 0;

    vector<Item> items(n);
    for (int i = 0; i < n; ++i) cin >> items[i].v >> items[i].w;

    sort(items.begin(), items.end(), [](const Item &a, const Item &b) {
        return (a.v / a.w) > (b.v / b.w);
    });

    double total_val = 0;
    for (const auto &item : items) {
        if (W <= 0) break;
        double take = min(item.w, W);
        total_val += take * (item.v / item.w);
        W -= take;
    }

    cout << fixed << setprecision(4) << total_val << "\n";
    return 0;
}
