#include <bits/stdc++.h>
using namespace std;

// Nén tọa độ 3D dùng vector<vector<int>>: {x1, y1, z1, x2, y2, z2}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> boxes(n, vector<int>(6));
    vector<int> X, Y, Z;

    for (int i = 0; i < n; ++i) {
        cin >> boxes[i][0] >> boxes[i][1] >> boxes[i][2];
        cin >> boxes[i][3] >> boxes[i][4] >> boxes[i][5];
        X.push_back(boxes[i][0]); X.push_back(boxes[i][3]);
        Y.push_back(boxes[i][1]); Y.push_back(boxes[i][4]);
        Z.push_back(boxes[i][2]); Z.push_back(boxes[i][5]);
    }

    sort(X.begin(), X.end()); X.erase(unique(X.begin(), X.end()), X.end());
    sort(Y.begin(), Y.end()); Y.erase(unique(Y.begin(), Y.end()), Y.end());
    sort(Z.begin(), Z.end()); Z.erase(unique(Z.begin(), Z.end()), Z.end());

    int nx = X.size(), ny = Y.size(), nz = Z.size();
    vector<vector<vector<int>>> grid(nx, vector<vector<int>>(ny, vector<int>(nz, 0)));

    for (const auto& b : boxes) {
        int x1 = lower_bound(X.begin(), X.end(), b[0]) - X.begin();
        int x2 = lower_bound(X.begin(), X.end(), b[3]) - X.begin();
        int y1 = lower_bound(Y.begin(), Y.end(), b[1]) - Y.begin();
        int y2 = lower_bound(Y.begin(), Y.end(), b[4]) - Y.begin();
        int z1 = lower_bound(Z.begin(), Z.end(), b[2]) - Z.begin();
        int z2 = lower_bound(Z.begin(), Z.end(), b[5]) - Z.begin();

        for (int i = x1; i < x2; ++i) {
            for (int j = y1; j < y2; ++j) {
                for (int k = z1; k < z2; ++k) {
                    grid[i][j][k] = 1;
                }
            }
        }
    }

    long long total_vol = 0;
    for (int i = 0; i + 1 < nx; ++i) {
        for (int j = 0; j + 1 < ny; ++j) {
            for (int k = 0; k + 1 < nz; ++k) {
                if (grid[i][j][k]) {
                    total_vol += 1LL * (X[i + 1] - X[i]) * (Y[j + 1] - Y[j]) * (Z[k + 1] - Z[k]);
                }
            }
        }
    }

    cout << total_vol << "\n";
    return 0;
}
