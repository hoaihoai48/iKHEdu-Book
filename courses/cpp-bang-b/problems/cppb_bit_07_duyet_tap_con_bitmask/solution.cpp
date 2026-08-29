#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int total_masks = (1 << n);
    for (int mask = 0; mask < total_masks; ++mask) {
        bool first = true;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if (!first) cout << " ";
                cout << a[i];
                first = false;
            }
        }
        cout << "\n";
    }

    return 0;
}
