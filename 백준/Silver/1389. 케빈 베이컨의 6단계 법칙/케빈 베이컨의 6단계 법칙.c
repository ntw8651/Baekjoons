#include <stdio.h>

int main(void) {
  /*
  입력받고
  stack에따가 넣기
  -1마다 카운트업
  bfs
  for로 각각,
  나올때까지 또는 카운트 같거나 넘을 때까지 while


  */
  int n, m;
  int relations[102][102] = {0};
  scanf("%d %d", &n, &m);

  //관게 입력
  int s, e;
  for (int i = 0; i < m; i++) {
    scanf("%d %d", &s, &e);

    relations[s][e] = 1;
    relations[e][s] = 1;
  }

  int visited[105] = {0}; // = visited
  int baconCount = 0;

  int visitStack[10002] = {0};
  int chkPoint = 0;
  int iptPoint = 0;
  int cycle = 1;
  int visitCount = 0;

  int minBaconUser = 0;
  int minBaconValue = 9999999;
  //계속 하다보니까, 앞에서 빼는 걸 못하니
  // point를 잉ㅇ해서 하게 되네...
  //이게 맞나? 풀고 풀이 확인해자자

  // bacons를 통해 하지 말고, 그냥 실시간으로 더해서 올라갈까? 다만 새로운 길을
  // 갈 때마다 아직 못찾은 얘들만큼을 더하는거지..아니야 시간은 2초로 넉넉한데?
  // 그냥 리스트화 해서 하...면근데 음...으음... 마지막에 더하기로 하자
  // 리스트에서

  //모든 친구에 대해 해야 하므로,
  //친구 찾을 때마다 baconCount Up
  // baconCount가 사람수만큼 될 때까지
  //다 되면 baconCount 다 더하기?
  int startP;
  int nextVisitCount;
  int findVisitCount;
  for (int i = 1; i <= n; i++) {
    //printf("%d @@@@@@@@@@@@@@\n", i);
    // visited, baconCount초기화
    for (int t = 0; t <= n; t++) {
      visited[t] = 0;
    }
    for (int t = 0; t <= 10001; t++) {
      visitStack[t] = 0;
    }
    baconCount = 0;
    chkPoint = 0;
    iptPoint = 0;
    visitCount = 0;
    visitStack[0] = i;
    cycle = 0;
    nextVisitCount = 0;
    visited[i] = 1;
    findVisitCount = 1;
    while (visitCount < n - 1) {
      startP = visitStack[chkPoint];
      //nextVisitCount = 0;
      for (int endP = 1; endP <= n; endP++) {
        if (relations[startP][endP] == 1) {
          if (visited[endP] == 0) {
            //printf("\ncycle:%d\n", cycle);
            visited[endP] = 1;
            baconCount += cycle + 1;
            visitStack[++iptPoint] = endP;
            visitCount++;
            nextVisitCount++;
            /*
              printf("%d %d %d__", baconCount, startP, cycle + 1);
              for (int t = 0; t <= n + 5; t++) {
                printf("%d ", visitStack[t]);
              }
              printf("\n\n");
            */
          }
        }
      }
      //왜 cycle이 3밖에 안되
      if (--findVisitCount == 0) {
        findVisitCount = nextVisitCount;
        nextVisitCount = 0;
        cycle++;
        //printf("asd");
      }
      chkPoint++;
    }

    // printf("__:%d %d\n\n", baconCount, i);
    if (baconCount < minBaconValue) {

      minBaconValue = baconCount;
      minBaconUser = i;
    }
  }
  printf("%d", minBaconUser);
}