#include <bits/stdc++.h>
using namespace std;

long long getGcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    long long g = getGcd(a, b);
    long long l = (a / g) * b;

    cout << g << " " << l << "\n";
    return 0;
}