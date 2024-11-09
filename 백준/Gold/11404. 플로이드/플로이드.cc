#include <bits/stdc++.h> 
#define INF 1e9

using namespace std;

int n, m;
int dp[110][110];


int main()
{
    int i, j, k, a, s, d;
    scanf("%d %d", &n, &m);
    for(i = 1; i <= n; i++) for(j=1;j<=n;j++) dp[i][j] = INF;
    for(i = 0; i <m; i++){
        scanf("%d %d %d", &a, &s, &d);
        dp[a][s] = min(dp[a][s], d);
    }
    for(k = 1; k<=n; k++){
        for(i = 1; i<=n; i++){
            for(j = 1; j<=n; j++){
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]);
            }
        }
    }

    for(i=1; i<=n; i++){
        for(j = 1; j <=n; j++){
            if(dp[i][j] == INF || i == j) printf("0 ");
            else printf("%d ", dp[i][j]);
        }
        printf("\n");
    }
    return 0;
}
