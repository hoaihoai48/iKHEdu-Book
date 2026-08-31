#include <bits/stdc++.h>
using namespace std;
void h(int n, char from, char to, char aux) {
    if (n == 0) return;
    h(n - 1, from, to, aux);
    cout << from << " -> " << aux << "\n";
    h(n - 1, to, from, aux);
    cout << aux << " -> " << to << "\n";
    h(n - 1, from, to, aux);
}
int main() {
    int n;
    if (!(cin >> n)) return 0;
    long long steps = 1;
    for (int i = 0; i < n; ++i) steps *= 3;
    steps -= 1;
    cout << steps << "\n";
    h(n, 'A', 'C', 'B');
    return 0;
}
