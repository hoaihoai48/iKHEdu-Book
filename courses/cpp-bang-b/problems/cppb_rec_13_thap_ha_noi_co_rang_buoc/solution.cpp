#include <bits/stdc++.h>
using namespace std;

void moveAtoB(int n, char a, char b, char c);
void moveBtoC(int n, char b, char c, char a);

void solveConstrainedHanoi(int n, char from, char to, char aux) {
    if (n == 0) return;
    // Chuyển n-1 đĩa from -> to
    solveConstrainedHanoi(n - 1, from, to, aux);
    // Chuyển đĩa n: from -> aux
    cout << from << " -> " << aux << "\n";
    // Chuyển n-1 đĩa to -> from
    solveConstrainedHanoi(n - 1, to, from, aux);
    // Chuyển đĩa n: aux -> to
    cout << aux << " -> " << to << "\n";
    // Chuyển n-1 đĩa from -> to
    solveConstrainedHanoi(n - 1, from, to, aux);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    long long total_steps = 1;
    for (int i = 0; i < n; ++i) total_steps *= 3;
    total_steps -= 1;
    cout << total_steps << "\n";
    solveConstrainedHanoi(n, 'A', 'C', 'B');
    return 0;
}
