#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long count_zeros = 0;
    while (n > 0) {
        count_zeros += (n / 5);
        n /= 5;
    }

    cout << count_zeros << "\n";
    return 0;
}