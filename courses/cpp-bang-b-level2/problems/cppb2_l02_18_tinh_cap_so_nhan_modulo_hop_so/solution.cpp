#include <bits/stdc++.h>
using namespace std;

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B, long long mod) {
    Matrix C(2, vector<long long>(2, 0));
    for (int i = 0; i < 2; ++i)
        for (int k = 0; k < 2; ++k)
            for (int j = 0; j < 2; ++j)
                C[i][j] = (C[i][j] + (__int128)A[i][k] * B[k][j]) % mod;
    return C;
}

Matrix matPow(Matrix A, long long k, long long mod) {
    Matrix res = {{1, 0}, {0, 1}};
    while (k > 0) {
        if (k & 1) res = multiply(res, A, mod);
        A = multiply(A, A, mod);
        k >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, n, m;
    if (!(cin >> a >> n >> m)) return 0;

    Matrix T = {{a % m, 1}, {0, 1}};
    Matrix Tn = matPow(T, n + 1, m);
    cout << (Tn[0][1] % m + m) % m << "\n";
    return 0;
}
