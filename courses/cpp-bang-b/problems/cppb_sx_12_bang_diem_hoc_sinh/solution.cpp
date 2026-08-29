#include <bits/stdc++.h>
using namespace std;

bool cmp(const vector<long long> &a, const vector<long long> &b) {
    long long total_a = a[1] + a[2];
    long long total_b = b[1] + b[2];
    if (total_a != total_b) return total_a > total_b;
    if (a[2] != b[2]) return a[2] > b[2];
    return a[0] < b[0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(3));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0] >> a[i][1] >> a[i][2];
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << " " << a[i][2] << "\n";
    }
    return 0;
}
