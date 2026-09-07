#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string p;
    if (!(cin >> p)) return 0;
    int n = (int)p.size();
    vector<int> pi(n, 0);
    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j > 0 && p[i] != p[j]) j = pi[j - 1];
        if (p[i] == p[j]) j++;
        pi[i] = j;
    }
    for (int i = 0; i < n; i++) { if (i) cout << ' '; cout << pi[i]; }
    cout << "\n";
    return 0;
}
