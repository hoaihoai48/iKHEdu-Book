#include <bits/stdc++.h>
using namespace std;

long long solveRec(int n) {
    if (n == 1) return 1;
    long long term = (n % 2 == 1) ? n : -n;
    return solveRec(n - 1) + term;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << solveRec(n) << "\n";
    return 0;
}
