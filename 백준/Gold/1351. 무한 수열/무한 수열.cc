#include <cmath>
#include <iostream>
long long P;
long long Q;
long long dp[1000000][2] = {{}};
long long endPoint = 0;
/*
우선
1. 좌표에 따라 할당하는 건 불가능
2. Ai에 따라 할당도 불가능
3. I P 따로도 불가능
4. 근데 DP는 결국 메모이제이션인데
5. 아니면 그냥 숫자 큰 순서대로 메모할까?
6. 오?
7. 잠-깐만...왜 할당이 불가능하 아 그렇지 배열 안에 숫자는 되지만 배열 개수가
안되는구나
8. 아아아아니 잠깐만, 왜 할당이 불가능해?
2차원 배열로 100000000*100000000해버리면
10^16아닌가? 진짜 엄청난 용량 낭비인가?
아 P랑 Q 저거 값 같은 거 써서 그런가
아닌데 어차피 지역변순데
*/
long long Check(long long a);
int main() {

  long long N = 0;
  scanf("%lld %lld %lld", &N, &P, &Q);
  printf("%lld", Check(N));
  /*
  for(int i = 0; i<endPoint; i++){
    printf("\n%lld %lld", dp[i][0], dp[i][1]);
    
  }*/
  
}
long long Check(long long a) {
  //printf("%lld\n\n", a);
  if (a == 0) {
    return 1;
  }
  for (int i = 0; i < endPoint; i++) {
    if (dp[i][0] == 0) {
      break;
    } else if (dp[i][0] == a) {
      
      return dp[i][1];
    }
  }
  //printf("%f ㅁ끄끄아아아악", floor(a / P)); ?? 뭐임...
  long long m = Check(floor(a / P)); 
  long long n = Check(floor(a / Q));
  //왜 둘이 합친 갑을 할당하는거랑 할당하고 합치는 거랑 다르지...??
  
  dp[endPoint][0] = a;
  dp[endPoint][1] = m + n;
  endPoint+=1;
  
  //이런식으로 하려면 스택으로 쌓아야 하나?
  //큐인지 스택인지는 아직 안해봤는데 해봐야겠자너?
  //아니근데 이럴꺼면 그냥 스택 마지막 위치를 전역변수로 두고 하면 되잖아~
  return m+n;
}

