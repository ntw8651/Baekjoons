#include <stdio.h>
#include <string.h>

int main() {
	int n = 0;
	char names[101] = "";
	int lensize = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", names);
		lensize = strlen(names);
		for (int j = 0; j < lensize; j++) { 
			if (names[j] == 'S') {
				printf("%s", names);
				break;
			}
		}
	}
	

	return 0;
}