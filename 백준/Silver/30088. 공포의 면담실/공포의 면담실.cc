#include <iostream>
#include<algorithm>
using namespace std;

long long int arr[3000] = { 0 };
int main(void)
{
	long long int n;
	long long int m;
	long long int t;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> m;
		for (int j = 0; j < m; j++) {
			cin >> t;
			arr[i] += t;
		}
	}
	long long int ans = 0;
	sort(arr, arr+n);
	for (int i = 0; i < n; i++) {
		ans += arr[i] * (n - i);
	}
	cout << ans;
	return 0;
}