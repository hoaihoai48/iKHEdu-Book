#include <bits/stdc++.h>
using namespace std;

bool cmp(const vector<long long> &a, const vector<long long> &b) {
    if (a[0] != b[0]) return a[0] < b[0];
    return a[1] > b[1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(2));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0] >> a[i][1];
    }

    stable_sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << "\n";
    }
    return 0;
}
