#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) { a %= b; swap(a, b); }
    return a;
}

long long lcm_val(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd_val(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    auto check = [](long long x) {
        long long temp = x;
        while (temp > 0) {
            int d = temp % 10;
            if (d == 0 || x % d != 0) return false;
            temp /= 10;
        }
        return true;
    };

    long long count = 0;
    for (long long x = L; x <= R; ++x) {
        if (check(x)) count++;
    }

    cout << count << "\n";
    return 0;
}
