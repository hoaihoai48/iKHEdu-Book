#include <bits/stdc++.h>
using namespace std;
struct Mat { long long m[2][2]; };
Mat mul(Mat a, Mat b, long long mod) {
    Mat c = {{{0,0},{0,0}}};
    for (int i=0; i<2; ++i)
        for (int j=0; j<2; ++j)
            for (int k=0; k<2; ++k)
                c.m[i][j] = (c.m[i][j] + a.m[i][k] * b.m[k][j]) % mod;
    return c;
}
int main() {
    Mat A;
    if (!(cin >> A.m[0][0] >> A.m[0][1] >> A.m[1][0] >> A.m[1][1])) return 0;
    long long n, mod;
    if (!(cin >> n >> mod)) return 0;
    Mat res = {{{1%mod, 0}, {0, 1%mod}}};
    for (int i = 0; i < n; ++i) res = mul(res, A, mod);
    cout << res.m[0][0] << " " << res.m[0][1] << "\n";
    cout << res.m[1][0] << " " << res.m[1][1] << "\n";
    return 0;
}
