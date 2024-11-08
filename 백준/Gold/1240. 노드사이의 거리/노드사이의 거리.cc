#include <iostream>
#include <vector>

using namespace std;
void dfs(int start, int end, int distance);
vector<bool> memori(1001, false);
vector<vector<int>> connectMap(1001, vector<int>(1001, 0));
vector<vector<int>> distanceMap(1001, vector<int>(1001, 0));
int endDistance;

int main() {
  int N;
  int M;
  int a;
  int b;
  scanf("%d %d", &N, &M);
  for (int i = 0; i < N - 1; i++) {
    int x;
    int y;
    int z;
    scanf("%d %d %d", &x, &y, &z);
    connectMap[y][connectMap[y][0] + 1] = x; // y축 개수+1칸에 연결 좌표
    distanceMap[y][connectMap[y][0] + 1] = z; //똑같이 거리
    connectMap[x][connectMap[x][0] + 1] = y;  //대칭으로 반복
    distanceMap[x][connectMap[x][0] + 1] = z;
    connectMap[x][0] += 1; //커넥트된 x축 개수?
    connectMap[y][0] += 1; //커넥트된 y축 개수?
  }
  for (int i = 0; i < M; i++) { //대충 초기화
    a = 1;
    b = 2;
    scanf("%d %d", &a, &b);
    dfs(a, b, 0);
    printf("%d\n", endDistance);
    vector<bool>(1001).swap(memori);
  }
}
//왜 시간 초과도 아니고 틀렸습니다일까
void dfs(int start, int end, int distance) {
  memori[start] = true; //어?
  if (start == end) {
    endDistance = distance;
  }
  for (int i = 1; i <= connectMap[start][0]; i++) {
    if (memori[connectMap[start][i]] == false) {
      dfs(connectMap[start][i], end, distance + distanceMap[start][i]);
    } //아니지 싹다 봐야하는 게 맞긴 하지 잠-깐... 설마 줄바꿈 안해서 오류가 났다거나-... 에이 설마
  }
}