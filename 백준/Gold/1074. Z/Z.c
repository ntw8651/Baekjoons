#include <math.h>
#include <stdio.h>
int ansX, ansY; //정답위치
int count = 0;
/* 배열 자체가 필요가 없네*/

void Z(int x, int y, int size) {
  /*
  size 가로(세로) 길이
  x, y 왼쪽맨위 좌표
  */
  if (size == 1) {
    if (x == ansX && y == ansY) {
      printf("%d", count);
    }
  } else {
    if (ansX >= x + size / 2 && ansY >= y + size / 2) {
      count += size * size / 4 * 3;
      Z(x + size / 2, y + size / 2, size / 2);

    } else if (ansX >= x + size / 2 && ansY >= y) {
      count+= size*size/4*2;
      Z(x + size / 2, y, size / 2);

    } else if (ansX >= x && ansY >= y + size / 2) {
      count+= size*size/4;
      Z(x, y + size / 2, size / 2);

    } else {
      Z(x, y, size / 2);
    }
  }
}

int main(void) {
  int N;
  scanf("%d %d %d", &N, &ansX, &ansY);
  Z(0, 0, pow(2, N));

  return 0;
}