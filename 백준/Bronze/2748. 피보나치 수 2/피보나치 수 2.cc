#include <iostream>

int main() {
  long long int fabo[91] = {};
  fabo[0] = 0;
  fabo[1] = 1;
  int n;
  scanf("%d", &n);
  for(int i = 2; i <= n; i++){
    fabo[i] = fabo[i-2] + fabo[i-1];
  }
  printf("%lld", fabo[n]);
}