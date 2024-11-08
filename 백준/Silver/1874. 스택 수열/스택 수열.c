#include <stdio.h>

int main(void) {
  /*
  N정수개수


  만약 입력된 수가 현재 포인트 수보다 크다면 push계속
  같으면 push
  작으면 펑!

  왜지
  */
  int N;
  scanf("%d", &N);
  int isPass = 1;
  int numbers[100002] = {0};
  int commands[300002] = {0};
  numbers[0] = 0;

  int iptNum = 0;
  int point = 0;
  int pushNum = 1;

  int count = -1;
  for (int i = 0; i < N; i++) {
    scanf("%d", &iptNum);
    while (1 == 1) {
      count += 1;
      if (iptNum > numbers[point]) {
        point += 1;
        numbers[point] = pushNum;
        pushNum += 1;
        commands[count] = 1;
      } else if (iptNum == numbers[point]) {
        point -= 1;
        commands[count] = -1;
        break;
      } else {
        isPass = 0;
        break;
      }
    }
  }

  if (isPass == 1) {
    point = 0;
    while (1 == 1) {
      if (commands[point] != 0) {
        if (commands[point] == 1) {
          printf("+\n");
        } else if (commands[point] == -1) {
          printf("-\n");
        }
      } else {
        break;
      }
      point += 1;
    }
  }
  if (isPass == 0) {
    printf("NO");
  }

  return 0;
}//아 다 입력하기도 전에ㅋㅋㅋㅋㅋ출력해서ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ