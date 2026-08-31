#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    long long sum = 0;
    for (int i = 1; i <= n; ++i) {
        if (i % 2 == 1) sum += i;
        else sum -= i;
    }
    cout << sum << "\n";
    return 0;
}
