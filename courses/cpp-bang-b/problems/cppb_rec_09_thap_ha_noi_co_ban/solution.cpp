#include <bits/stdc++.h>
using namespace std;

void solveHanoi(int n, char from, char to, char aux) {
    if (n == 0) return;
    solveHanoi(n - 1, from, aux, to);
    cout << from << " -> " << to << "\n";
    solveHanoi(n - 1, aux, to, from);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << (1 << n) - 1 << "\n";
    solveHanoi(n, 'A', 'C', 'B');
    return 0;
}
