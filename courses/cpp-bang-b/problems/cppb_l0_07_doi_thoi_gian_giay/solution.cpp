#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long t;
    if (!(cin >> t)) return 0;

    long long h = t / 3600;
    long long rem = t % 3600;
    long long m = rem / 60;
    long long s = rem % 60;

    cout << h << ':' << m << ':' << s << '\n';
    return 0;
}
