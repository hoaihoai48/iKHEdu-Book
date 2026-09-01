#include <bits/stdc++.h>
using namespace std;

struct Rect {
    long long x1, y1, x2, y2;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Rect> rects(n);
    vector<long long> X, Y;
    for (int i = 0; i < n; ++i) {
        cin >> rects[i].x1 >> rects[i].y1 >> rects[i].x2 >> rects[i].y2;
        X.push_back(rects[i].x1); X.push_back(rects[i].x2);
        Y.push_back(rects[i].y1); Y.push_back(rects[i].y2);
    }

    sort(X.begin(), X.end()); X.erase(unique(X.begin(), X.end()), X.end());
    sort(Y.begin(), Y.end()); Y.erase(unique(Y.begin(), Y.end()), Y.end());

    int nx = X.size(), ny = Y.size();
    vector<vector<int>> grid(nx, vector<int>(ny, 0));

    for (const auto &r : rects) {
        int ix1 = lower_bound(X.begin(), X.end(), r.x1) - X.begin();
        int ix2 = lower_bound(X.begin(), X.end(), r.x2) - X.begin();
        int iy1 = lower_bound(Y.begin(), Y.end(), r.y1) - Y.begin();
        int iy2 = lower_bound(Y.begin(), Y.end(), r.y2) - Y.begin();

        for (int i = ix1; i < ix2; ++i) {
            for (int j = iy1; j < iy2; ++j) {
                grid[i][j] = 1;
            }
        }
    }

    long long total_area = 0;
    for (int i = 0; i < nx - 1; ++i) {
        for (int j = 0; j < ny - 1; ++j) {
            if (grid[i][j]) {
                total_area += (X[i + 1] - X[i]) * (Y[j + 1] - Y[j]);
            }
        }
    }

    cout << total_area << "\n";
    return 0;
}
