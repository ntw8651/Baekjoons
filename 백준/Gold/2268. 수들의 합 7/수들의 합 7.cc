#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n, m;
int arr[1000010];
ll bit[1000010];

void update(int a, int v){
    int i;//up and plus
    while(a<=n){
        bit[a] += v;
        a += a & -a;
    }
}

ll query(int a){
    ll sum = 0;
    while(a){
        sum += bit[a];
        a -= a& -a;
    }
    return sum;
}

int main()
{
    int i, a, s, d;
    scanf("%d %d", &n, &m);
    for(i=0; i<m; i++){
        scanf("%d %d %d", &a, &s, &d);
        if(a){
            update(s, -arr[s]);
            update(s, d);
            arr[s] = d;
        }
        else{
            if(s >d) swap(s, d);
            printf("%lld\n", query(d) - query(s-1));
        }
    }
    return 0;
}
