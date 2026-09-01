#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    for (int i = 0; i < n; ++i) p[i] = i + 1;

    do {
        for (int i = 0; i < n; ++i) cout << p[i] << (i + 1 == n ? "" : " ");
        cout << "\n";
    } while (next_permutation(p.begin(), p.end()));

    return 0;
}
