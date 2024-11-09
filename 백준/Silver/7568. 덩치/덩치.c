#include <stdio.h>

int main() {
  int N;
  int humans[51][2];
  int count;

  scanf("%d", &N);

  for (int i = 0; i < N; i++) {
    scanf("%d %d", &humans[i][0], &humans[i][1]);
  }

  for (int i = 0; i < N; i++) {
    count = 0;
    for (int j = 0; j < N; j++) {
      if (i != j && humans[i][0] < humans[j][0] &&
          humans[i][1] < humans[j][1]) {
        count += 1;
      }
    }
    printf("%d ", count+1);
  }
}