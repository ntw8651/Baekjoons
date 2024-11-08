#include <iostream>

int main() {
  int N = 5;
  int Numbers[6];
  for(int i =0; i<N; i++){
    scanf("%d", &Numbers[i]);
  }
  int currentNumber = 0;
  int count = 0;
  while(count < 3){
    count = 0;
    currentNumber += 1;
    for(int i = 0; i < N; i++){
      if(currentNumber%Numbers[i] == 0){
        count +=1;
      }
    }
    
    
  }
  printf("%d", currentNumber);
}