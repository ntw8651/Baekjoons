#include <iostream>


using namespace std;

int main() {

  int N, MaxWeight;
  int MaxValue = 0;
  scanf("%d %d", &N, &MaxWeight);
  int Weight[N];
  int Value[N];//응...지금은 일단 벡터 미뤄두고 배열로도 다 되니까 뭐...
  for (int i = 0; i < N; i++) {
    cin >> Weight[i];
    cin >> Value[i];
  }
  int dp[N+1][100001];
  for (int i = 1; i <= N; i++) {
    for (int p = 1; p <= MaxWeight; p++) {
      if (p - Weight[i - 1] >= 0) {
        dp[i][p] =
            max(dp[i - 1][p], dp[i - 1][p - Weight[i - 1]] + Value[i - 1]);
      } else {
        dp[i][p] = dp[i - 1][p];
      }
    }
  }
  printf("%d", dp[N][MaxWeight]);
}