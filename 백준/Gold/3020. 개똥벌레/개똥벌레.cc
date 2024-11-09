#include <iostream>
#include <string>
using namespace std;

int nums[2000001] = { 0 };
int up[500001] = { 0 };
int down[500001] = { 0 };
int results[500001] = { 0 };
int main(void)
{
    /*
    엄 그냥 다 기록하고 마지막에 합 구하면 되는..문제 아닝가?
    */
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    int h;
    cin >> n;
    cin >> h;
    int inp;
    for (int i = 0; i < n; i++) {
        cin >> inp;
        if (i % 2 == 0) {
            down[inp] += 1;
        }
        else {
            up[inp] += 1;
        }
    }

    int count = 0;
    for (int i = h; i >= 0; i--) {
        count += up[i];
        results[h-i] += count;
    }
    count = 0;
    for (int i = h; i >= 0; i--) {
        count += down[i];
        results[i-1] += count;
    }

    int minValue = 300000;
    int answer = 0;
    for (int i = 0; i < h; i++) {
        if (minValue > results[i]) {
            minValue = results[i];
            answer = 1;
        }
        else if(minValue == results[i]) {
            answer += 1;
        }
    }




    cout << minValue << ' ' << answer;
    
	return 0;
}