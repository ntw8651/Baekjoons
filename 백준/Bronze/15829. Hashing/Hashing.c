#include <math.h>
#include <stdio.h>
int main(void) {
  int N;
  scanf("%d", &N);
  long long number = 0;
  char alp[1001];

  long long tempNum = 0;
  scanf("%s", alp);
  for (int i = 0; i < N; i++) {
    /*pow가 너무 커진다! for문으로 해서 계속 갈라주기*/

    tempNum = (alp[i] - 'a' + 1);
    for (int j = 0; j < i; j++) {
      tempNum *= 31;
      tempNum %= 1234567891;
    }
    number += tempNum;
    
  }
  printf("%lld", number % 1234567891);

  return 0;
}