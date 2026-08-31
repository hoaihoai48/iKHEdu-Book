#include <bits/stdc++.h>
using namespace std;

void printBinaryRec(long long n) {
    if (n == 0) return;
    printBinaryRec(n / 2);
    cout << (n % 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    if (!(cin >> n)) return 0;
    if (n == 0) {
        cout << 0 << "\n";
    } else {
        printBinaryRec(n);
        cout << "\n";
    }
    return 0;
}
