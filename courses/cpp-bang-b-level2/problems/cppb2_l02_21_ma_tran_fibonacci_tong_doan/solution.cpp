#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B) {
    Matrix C = {{0, 0}, {0, 0}};
    for (int i = 0; i < 2; ++i)
        for (int k = 0; k < 2; ++k)
            for (int j = 0; j < 2; ++j)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
}

Matrix matPow(Matrix A, long long k) {
    Matrix res = {{1, 0}, {0, 1}};
    while (k > 0) {
        if (k & 1) res = multiply(res, A);
        A = multiply(A, A);
        k >>= 1;
    }
    return res;
}

long long getFib(long long n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    Matrix T = {{1, 1}, {1, 0}};
    Matrix Tn = matPow(T, n - 1);
    return Tn[0][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long l, r;
    if (!(cin >> l >> r)) return 0;
    long long sumR = (getFib(r + 2) - 1 + MOD) % MOD;
    long long sumL = (getFib(l + 1) - 1 + MOD) % MOD;
    cout << (sumR - sumL + MOD) % MOD << "\n";
    return 0;
}
