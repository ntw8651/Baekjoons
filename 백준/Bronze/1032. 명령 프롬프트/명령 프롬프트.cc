#include <iostream>

using namespace std;

int main(void) {
	int N;
	scanf("%d", &N);
	char originWord[51];
	scanf("%s", &originWord);
	char otherWord[51];
	int count = 0;
	while (originWord[count] != '\0') {
		count += 1;
	}
	for (int i = 0; i < N-1; i++) {
		scanf("%s", otherWord);
		for (int j = 0; j < count; j++) {
			if (originWord[j] != otherWord[j]) {
				originWord[j] = '?';
			}
		}
	}
	printf("%s", originWord);
	
	return 0;
}