#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B, int n) {
    Matrix C(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i)
        for (int k = 0; k < n; ++k)
            for (int j = 0; j < n; ++j)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
}

Matrix matPow(Matrix A, long long k, int n) {
    Matrix res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
    while (k > 0) {
        if (k & 1) res = multiply(res, A, n);
        A = multiply(A, A, n);
        k >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, u, v;
    long long k;
    if (!(cin >> n >> m >> k >> u >> v)) return 0;
    --u; --v;
    Matrix adj(n, vector<long long>(n, 0));
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        --x; --y;
        adj[x][y] = (adj[x][y] + 1) % MOD;
        adj[y][x] = (adj[y][x] + 1) % MOD;
    }

    Matrix res = matPow(adj, k, n);
    cout << res[u][v] << "\n";
    return 0;
}
