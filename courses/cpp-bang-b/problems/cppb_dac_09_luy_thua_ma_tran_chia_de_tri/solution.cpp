#include <bits/stdc++.h>
using namespace std;

struct Matrix {
    long long mat[2][2];
};

Matrix multiply(const Matrix &A, const Matrix &B, long long m) {
    Matrix C;
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            C.mat[i][j] = 0;
            for (int k = 0; k < 2; ++k) {
                C.mat[i][j] = (C.mat[i][j] + (A.mat[i][k] % m) * (B.mat[k][j] % m)) % m;
            }
        }
    }
    return C;
}

Matrix powerMatrix(Matrix A, long long n, long long m) {
    Matrix res = {{{1 % m, 0}, {0, 1 % m}}};
    while (n > 0) {
        if (n & 1) res = multiply(res, A, m);
        A = multiply(A, A, m);
        n >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Matrix A;
    if (!(cin >> A.mat[0][0] >> A.mat[0][1] >> A.mat[1][0] >> A.mat[1][1])) return 0;
    long long n, m;
    if (!(cin >> n >> m)) return 0;
    Matrix ans = powerMatrix(A, n, m);
    cout << ans.mat[0][0] << " " << ans.mat[0][1] << "\n";
    cout << ans.mat[1][0] << " " << ans.mat[1][1] << "\n";
    return 0;
}
