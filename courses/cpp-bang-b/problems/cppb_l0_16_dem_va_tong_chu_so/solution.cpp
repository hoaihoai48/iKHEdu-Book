#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    if (n == 0) {
        cout << "1 0\n";
        return 0;
    }

    int count_digits = 0;
    long long sum_digits = 0;

    while (n > 0) {
        sum_digits += n % 10;
        count_digits++;
        n /= 10;
    }

    cout << count_digits << ' ' << sum_digits << '\n';
    return 0;
}
