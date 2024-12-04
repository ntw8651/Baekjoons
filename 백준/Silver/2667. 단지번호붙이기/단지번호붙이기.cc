#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<vector<int>> danji(25, vector<int>(25, 0));
int result = 0;
void checking(int x, int y);
int n;
vector<int> values;
int main()
{
    result = 0;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        for(int p=0; p<n; p++){
            scanf("%1d", &danji[i][p]);

        }
    }
    for(int i=0; i<n; i++){
        for(int p=0; p<n; p++){
            if(danji[i][p] == 1){
                result = 0;
                checking(i,p);
                values.push_back(result);
            }
        }
    }

    sort(values.begin(), values.end());

    printf("%d\n", values.size());
    for(int i = 0; i<values.size(); i++){
        printf("%d\n", values[i]);
    }
    return 0;
}
void checking(int x, int y)
{
    if(0<=x && x<n && 0<=y && y < n && danji[x][y] == 1){
        danji[x][y] = 0;
        result+=1;
        checking(x-1,y);
        checking(x,y-1);
        checking(x+1,y);
        checking(x,y+1);
    }

}
