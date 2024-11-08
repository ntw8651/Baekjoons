#include <iostream>

int main() {
  int count = 0;
  while(1==1){
    char Text;
    scanf("%c", &Text);
    if(Text == '#') break;
    if(Text == 'a' ||Text == 'e' || Text == 'i'||Text == 'o' || Text == 'u' || Text == 'A' ||Text == 'E' || Text == 'I'||Text == 'O' || Text == 'U'){
      count+=1;
    }
    else if(Text == '\n'){
      printf("%d\n", count);
      count = 0;
    }
  }
}