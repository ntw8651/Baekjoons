#include <stdio.h>
#include <string.h>

int main() {
	int n = 0;
	int m = 0;
	int count = 0;
	int arr[2000] = {0};
	scanf("%d %d", &n, &m);
	for (int i = 1; i < 100;i++) {
		for (int j = 0; j < i; j++) {
			arr[count++] = i;
		}
		if (count > 1001) {
			break;
		}
	}
	int sum = 0;
	for (int i = 0; i < 0; i++) {
		printf("%d\n", arr[i]);
	}
	for (int i = n; i <= m; i++) {
		sum += arr[i-1];
	}
	printf("%d", sum);


	return 0;
}