#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        string s = "";
        for (int i = n - 1; i >= 0; --i) s.push_back((mask & (1 << i)) ? '1' : '0');
        cout << s << "\n";
    }
    return 0;
}
