#include <bits/stdc++.h>
using namespace std;

struct Data{
    int idx, v;
}arr[10010];

int n, m, res;
int visited[10010];
stack <int> st;
vector <int> vt[10010], rvt[10010], scc[10010];

bool compare(Data d1, Data d2){
    return d1.v < d2.v;
}

void dfs(int a){
    int i, s;
    visited[a] = 1;
    for(i = 0; i < int(vt[a].size()); i++){
        s = vt[a][i];
        if(!visited[s]) dfs(s);
    }
    st.push(a);
}

void rdfs(int a){
    int i, s;
    visited[a] = 1;
    scc[res].push_back(a);
    for(i=0; i< int(rvt[a].size()); i++){
        s=rvt[a][i];
        if(!visited[s]) rdfs(s);
    }
}

int main()
{
    int i, j, a, s;
    scanf("%d %d", &n, &m);
    for(i = 0; i < m; i++){
        scanf("%d %d", &a, &s);
        vt[a].push_back(s);
        rvt[s].push_back(a);
    }
    for(i=1;i<=n;i++){
        if(!visited[i]) dfs(i);
    }
    memset(visited, 0, sizeof(visited));
    while(!st.empty()){
        a = st.top(); st.pop();
        if(!visited[a]) rdfs(a), res++;

    }
    printf("%d\n",res);
    for(i=0;i<res;i++){
        sort(scc[i].begin(), scc[i].end());
        arr[i] = (Data){i, scc[i][0]};

    }
    sort(arr, arr+res, compare);
    for(i =0; i< res; i++){
        a = arr[i].idx;
        for(j=0; j<scc[a].size();j++){
            printf("%d ", scc[a][j]);
        }
        printf("-1 \n");
    }
    return 0;
}
