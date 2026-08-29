#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(2));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0];
        a[i][1] = i + 1;
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << "\n";
    }
    return 0;
}
