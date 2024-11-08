#include <stdio.h>
//시작 6시 10분 ~ 6시 40분
void goForward(int direction);
void checkMaxMin();
void turnRight();
void turnLeft();

int mazeMap[102][102] = {0}; // 0 안 가본 곳, 1 가본 곳
int direction = 3;           // 0 left 1 up 2 right 3 down

int nowX = 51;
int nowY = 51;

int maxX = 51;
int minX = 51;
int maxY = 51;
int minY = 51;

int main(void) {
  /*
   방향값 갖고,
   x,y 각 극값 저장하기
   그리고 배열 조금씩 바꾸기
   그리고 배열은 처음부터 100*100으로 선언하기
   forward 최대 50번, 좌우상하 50번씩 가도 괜찮도록 시작점 51로 설정
  */
  int n = 0;
  char action;
  mazeMap[51][51] = 1;
  scanf("%d", &n);

  //탐험 고고
  for (int i = 0; i <= n; i++) {
    scanf("%c", &action);
    if (action == 'F') {
      goForward(direction);
      mazeMap[nowX][nowY] = 1;
      checkMaxMin();
    } else if (action == 'L') {
      turnLeft();
    } else if (action == 'R') {
      turnRight();
    }
  }

  //범위로 출력

  for (int y = maxY; y >= minY; y--) {
    for (int x = minX; x <= maxX; x++) {
      if (mazeMap[x][y]) {
        printf(".");
      } else {
        printf("#");
      }
    }
    printf("\n");
  }

  return 0;
}
void goForward(int direction) {
  switch (direction) {
  case 0:
    nowX--;
    break;
  case 1:
    nowY++;
    break;
  case 2:
    nowX++;
    break;
  case 3:
    nowY--;
    break;
  }
}
void checkMaxMin() {
  if (maxX < nowX) {
    maxX = nowX;
  }
  if (maxY < nowY) {
    maxY = nowY;
  }
  if (minX > nowX) {
    minX = nowX;
  }
  if (minY > nowY) {
    minY = nowY;
  }
}
void turnRight() {
  if (++direction > 3) {
    direction = 0;
  }
}
void turnLeft() {
  if (--direction < 0) {
    direction = 3;
  }
}