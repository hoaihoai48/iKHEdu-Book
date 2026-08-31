#include <bits/stdc++.h>
using namespace std;

struct Item {
    long long w, v;
    double ratio;
};

int n;
long long max_w;
vector<Item> items;
long long best_val = 0;

double getUpperBound(int idx, long long cur_w, long long cur_v) {
    long long remain_w = max_w - cur_w;
    double bound = cur_v;
    for (int i = idx; i < n; ++i) {
        if (items[i].w <= remain_w) {
            remain_w -= items[i].w;
            bound += items[i].v;
        } else {
            bound += items[i].ratio * remain_w;
            break;
        }
    }
    return bound;
}

void branchAndBound(int idx, long long cur_w, long long cur_v) {
    if (cur_v > best_val) best_val = cur_v;
    if (idx >= n) return;

    if (getUpperBound(idx, cur_w, cur_v) <= best_val) return;

    // Nhánh 1: Chọn vật idx
    if (cur_w + items[idx].w <= max_w) {
        branchAndBound(idx + 1, cur_w + items[idx].w, cur_v + items[idx].v);
    }
    // Nhánh 2: Không chọn vật idx
    branchAndBound(idx + 1, cur_w, cur_v);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> max_w)) return 0;
    items.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> items[i].w >> items[i].v;
        items[i].ratio = (double)items[i].v / items[i].w;
    }
    sort(items.begin(), items.end(), [](const Item &a, const Item &b) {
        return a.ratio > b.ratio;
    });
    branchAndBound(0, 0, 0);
    cout << best_val << "\n";
    return 0;
}
