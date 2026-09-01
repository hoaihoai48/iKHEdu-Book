#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B) {
    Matrix C(3, vector<long long>(3, 0));
    for (int i = 0; i < 3; ++i)
        for (int k = 0; k < 3; ++k)
            for (int j = 0; j < 3; ++j)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
}

Matrix matPow(Matrix A, long long k) {
    Matrix res(3, vector<long long>(3, 0));
    for (int i = 0; i < 3; ++i) res[i][i] = 1;
    while (k > 0) {
        if (k & 1) res = multiply(res, A);
        A = multiply(A, A);
        k >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    if (n == 0) { cout << 0 << "\n"; return 0; }
    if (n == 1 || n == 2) { cout << 1 << "\n"; return 0; }

    Matrix T = {
        {1, 1, 1},
        {1, 0, 0},
        {0, 1, 0}
    };
    Matrix Tn = matPow(T, n - 2);
    long long ans = (Tn[0][0] * 1 + Tn[0][1] * 1 + Tn[0][2] * 0) % MOD;
    cout << ans << "\n";
    return 0;
}
