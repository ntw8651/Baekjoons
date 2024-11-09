#include <math.h>
#include <stdio.h>
/*
기존 안정 정렬인 병합 정렬을 기반으로, 기준 위치를 잡아서 배열하기
*/
int rates[300001][2] = {0};
int sorted[300001][2] = {0};
int kind = 2;

void merge(int list[][2], int left, int mid, int right, int pivot) {
  int l = left;
  int r = mid + 1; // right start point, 같은 지점 중복되지 않도록 더하기1
  int p = left; //포인트. 말하자면 커서. sorted에 다음으로 적을 좌표 지정.
  int i = 0;
  // l이나 r이 한정범위를 나가기 전까지
  while (l <= mid && r <= right) {
    //더 큰거 순서대로 sorted에 넣어 정리하기
    if (list[l][pivot] <= list[r][pivot]) { //왼쪽 작으면 왼쪽거 먼저

      for (i = 0; i < kind; i++) {
        sorted[p][i] = list[l][i];
      }
      p++;
      l++;
    } else {

      for (i = 0; i < kind; i++) {
        sorted[p][i] = list[r][i];
      }
      p++;
      r++;
    }
  }

  //아 둘이 비교하고 남은 값 채워주기구나. 두 값이 고르게 들어갔다는 보장이
  //없으니까
  if (l > mid) {

    for (i = r; i <= right; i++) {

      for (int j = 0; j < kind; j++) {
        sorted[p][j] = list[i][j];
      }
      p++;
    }
  } else {
    for (i = l; i <= mid; i++) {

      for (int j = 0; j < kind; j++) {
        sorted[p][j] = list[i][j];
      }
      p++;
    }
  }

  //마지막으로 sorted된 값 다시 list로 업데이트 해주기
  for (i = left; i <= right; i++) {
    for (int j = 0; j < kind; j++) {
      list[i][j] = sorted[i][j];
    }
  }
}

void merge_sort(int list[][2], int left, int right, int pivot) {
  if (left < right) {
    int mid = (left + right) / 2; //무조건 내림

    merge_sort(list, left, mid, pivot);
    merge_sort(list, mid + 1, right, pivot);
    merge(list, left, mid, right, pivot);
  }
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d %d", &rates[i][0], &rates[i][1]);
  }
  merge_sort(rates, 0, n - 1, 0);

  merge_sort(rates, 0, n - 1, 1);

  for (int i = 0; i < n; i++) {
    printf("%d %d\n", rates[i][0], rates[i][1]);
  }
}