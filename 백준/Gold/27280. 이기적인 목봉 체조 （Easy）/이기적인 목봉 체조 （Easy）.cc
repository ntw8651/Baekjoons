#include <iostream>
using namespace std;

int main() {
  int N;
  int M;

  cin >> N;
  cin >> M;
  long long Humans[N][2];
  long long Group[N][N];

  for (int i = 0; i < N; i++) {
    for (int p = 0; p < N; p++) {
      Group[i][p] = 0;
    }
  }

  // 0 height, 1 power
  //입력받기
  for (int i = 0; i < N; i++) {
    scanf("%lld %lld", &Humans[i][0], &Humans[i][1]);
  }
  long long maxHeight;
  long long sumWeight;
  for (int i = 0; i < N; ++i) {
    maxHeight = -1;
    sumWeight = 0;
    for (int p = i; p < N; ++p) { //앞번호부터 큰키를 찾을 때마다 키 갱신,
                                  //누적합 초기화, 동일 키 발견시 누적

      if (Humans[p][0] > maxHeight) {
        maxHeight = Humans[p][0];
        sumWeight = 0;
      }
      if (Humans[p][0] == maxHeight) {
        sumWeight += Humans[p][1];
      }

      Group[i][p] = sumWeight;
    }
  }
  long long dp[N];
  for (int i = 0; i < N; i++) {
    dp[i] = 0;
  }

  for (int i = 0; i < N; ++i) {
    dp[i] = Group[0][i];
  }
  for (int i = 1; i < M; ++i) {
    
    long long tempDp[N];
    for (int i = 0; i < N; i++) {
      tempDp[i] = 0;
    }
    
    for (int p = i; p < N; ++p) {
      for (int q = i - 1; q < p; ++q) {
        tempDp[p] = max(tempDp[p], dp[q] + Group[q + 1][p]);
      } //
    }  
    for (int r = 0; r < N; r++) {
      dp[r] = tempDp[r];

      tempDp[r] = 0;
    }

  }
  printf("%lld", dp[N - 1]);
}
