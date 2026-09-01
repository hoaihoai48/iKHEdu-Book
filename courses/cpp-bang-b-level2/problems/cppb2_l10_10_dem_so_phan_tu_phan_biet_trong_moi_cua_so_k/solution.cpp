#include <bits/stdc++.h>
using namespace std;

const int MAXV = 100000;
bitset<MAXV + 1> bs;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    bs[0] = 1;
    for (int i = 0; i < n; ++i) {
        int w; cin >> w;
        bs |= (bs << w);
    }

    cout << bs.count() << "\n";
    return 0;
}
