#include <stdio.h>
#include <string.h>

int main(void) {
  int counter[26] = {0}; //등장 횟수 출력
  char word[1000002] = {
      0}; //범위를 초과하지 않도록 1,000,000보다 큰 크기의 배열을 할당
  scanf("%s", word);              //단어 입력받기
  int len = strlen(word);         // 단어 길이 체크
  for (int i = 0; i < len; i++) { //글자 하나하나 확인 시작
    if ('A' <= word[i] && word[i] <= 'Z') {
      //대문자일 경우 처리
      counter[word[i] - 'A']++; //몇번째 글자인지 알 수 있음.
      // ex)A = 65, D = 68이므로 68-65 = 3, 3번칸에 +1을 함
      //배열은 0번부터 시작하기 때문에 OK.
    } else {
      //소문자일 경우 처리, 동일함
      counter[word[i] - 'a']++;
    }
  }

  int flag = 0;     // 1 : 현재 max가 여러개, 0 : 현재 max는 유일함
  int maxCount = 0; //현재 최댓값
  int maxWord = -1; //현재 최댓값 글자
  for (int i = 0; i < 26; i++) {
    if (counter[i] > maxCount) { //최대값보다 크면
      maxCount = counter[i];
      maxWord = i;
      flag = 0; // flag초기화
    } else if (counter[i] == maxCount) {
      flag++;
    }
  }

  if (flag == 0) {
    printf("%c", 'A' + maxWord);
  } else {
    printf("?");
  }
  return 0;
}