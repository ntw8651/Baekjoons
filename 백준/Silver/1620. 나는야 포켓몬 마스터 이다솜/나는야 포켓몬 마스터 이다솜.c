#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char sortedDict[100002][22] = {0}; //배열용
char dictionary[100002][22] = {0}; //배열용
char originDict[100002][22] = {0}; //숫자용
int dictNum[100002] = {0};
int sortedDictNum[100002] = {0};

void inputString(char a[], char b[]) {
  /*
  input b to a, this function equal a = b;
  */
  for (int i = 0; i < 22; i++) {
    a[i] = b[i];
  }
}
void merge(char list[][22], int left, int right, int mid) {
  int l = left;
  int r = mid + 1;
  int p = left; //이거 왠지 값이 아니라 위치를 대입해버린 것 같지 않아?
                //주소말이야...

  while (l <= mid && r <= right) {
    if (strcmp(list[l], list[r]) <= 0) {
      sortedDictNum[p] = dictNum[l];
      inputString(sortedDict[p++], list[l++]);

    } else {
      sortedDictNum[p] = dictNum[r];
      inputString(sortedDict[p++], list[r++]);
    }
  }

  if (l <= mid) {
    for (int i = l; i <= mid; i++) {
      sortedDictNum[p] = dictNum[i];
      inputString(sortedDict[p++], list[i]);
    }
  } else {
    for (int i = r; i <= right; i++) {
      sortedDictNum[p] = dictNum[i];
      inputString(sortedDict[p++], list[i]);
    }
  }
  for (int i = left; i <= right; i++) {
    inputString(list[i], sortedDict[i]);
    dictNum[i] = sortedDictNum[i];
  }
}
void mergeSort(char list[][22], int left, int right) {
  if (left < right) {
    int mid = (left + right) / 2;
    mergeSort(list, left, mid);
    mergeSort(list, mid + 1, right);

    merge(list, left, right, mid);
  }
}

int main(void) {
  int n;
  int m;
  scanf("%d %d", &n, &m);

  for (int i = 1; i <= n; i++) {
    scanf("%s", dictionary[i]);
    inputString(originDict[i], dictionary[i]);
    dictNum[i] = i;
  }

  char answer[22] = {0};
  int number;

  mergeSort(dictionary, 1, n);

  int left;
  int right;
  int mid;
  int checkBool;
  for (int i = 0; i < m; i++) {
    scanf("%s", answer);
    if ('1' <= answer[0] && answer[0] <= '9') {
      number = atoi(answer);
      printf("%s\n", originDict[number]);
    } else {
      left = 1;
      right = n;
      while (left <= right) {
        mid = (left + right) / 2;
        checkBool = strcmp(sortedDict[mid], answer);
        if (checkBool == 0) {
          printf("%d\n", sortedDictNum[mid]);
          break;
        } else if (checkBool < 0) {
          left = mid+1;
        } else {
          right = mid-1;
        }
      }
      /*
      for (int j = 1; j <= n; j++) {
        int ans = strcmp(dictionary[j], answer);
        if (ans == 0) {
          printf("%d\n", j);
          break;
        }
      }
      */
    }
  }

  return 0;
}