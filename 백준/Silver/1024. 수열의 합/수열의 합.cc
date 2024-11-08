#include <iostream>

using namespace std;
int sumNum(int N);

int main() {
  int N;
  int L;
  int adder;
  scanf("%d %d", &N, &L);
  while(true){
    int sum = sumNum(L);
    if(N < sum){
      printf("-1");
      break;
    }
    if((N-sum)%L == 0){
      int Number = N-sum; 
      adder = Number/L; 
      for(int i = 0; i<L; i++){
        printf("%d ", i+adder);
     }
      break;
      }
    else if(L<=99){
      L+=1;
    }
    else{
      printf("-1");
      break;
    }
  }

}
int sumNum(int N){
  int number = 0;
  for(int i=0; i<N; i++){
    number+=i;
  }
  return number;
}