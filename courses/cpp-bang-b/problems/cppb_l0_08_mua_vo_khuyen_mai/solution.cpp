#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, p;
    if (!(cin >> n >> p)) return 0;

    long long groups = n / 6;
    long long rem = n % 6;

    long long to_buy = groups * 5 + min(rem, 5LL);
    long long total_cost = to_buy * p;

    cout << total_cost << '\n';
    return 0;
}
