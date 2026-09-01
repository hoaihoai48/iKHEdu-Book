#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B, int k) {
    Matrix C(k, vector<long long>(k, 0));
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            for (int p = 0; p < k; ++p) {
                C[i][j] = (C[i][j] + A[i][p] * B[p][j]) % MOD;
            }
        }
    }
    return C;
}

Matrix power_mat(Matrix A, long long p, int k) {
    Matrix res(k, vector<long long>(k, 0));
    for (int i = 0; i < k; ++i) res[i][i] = 1;
    while (p > 0) {
        if (p & 1) res = multiply(res, A, k);
        A = multiply(A, A, k);
        p >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    long long n;
    if (!(cin >> k >> n)) return 0;

    Matrix A(k, vector<long long>(k));
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) cin >> A[i][j];
    }

    Matrix An = power_mat(A, n, k);
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            cout << An[i][j] << (j + 1 == k ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}
