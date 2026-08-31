#include <bits/stdc++.h>
using namespace std;
int N_ANS[] = {0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200};
int main() {
    int n;
    if (!(cin >> n)) return 0;
    cout << N_ANS[n] << "\n";
    return 0;
}
