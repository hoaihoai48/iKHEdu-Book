#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    unsigned long long L, R;
    if (!(cin >> L >> R)) return 0;
    // All Armstrong (narcissistic) numbers <= 1e18, plus 0
    unsigned long long A[] = {0,1,2,3,4,5,6,7,8,9,153,370,371,407,1634,8208,9474,
        54748,92727,93084,548834,1741725,4210818,9800817,9926315,24678050,
        24678051,88593477,146511208,472335975,534494836,912985153,4679307774ULL,
        32164049650ULL,32164049651ULL,40028394225ULL,42678290603ULL,
        44708635679ULL,49388550606ULL,82693916578ULL,94204591914ULL,
        28116440335967ULL,4338281769391370ULL,4338281769391371ULL,
        21897142587612075ULL,35641594208964132ULL,35875699062250035ULL};
    long long ans = 0;
    for (unsigned long long v : A) if (v >= L && v <= R) ans++;
    // exclude 0 when L == 0? 0 = 0^1 is Armstrong; sample 1..500 -> 13 unaffected
    cout << ans << "\n";
    return 0;
}
