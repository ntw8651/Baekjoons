#include <stdio.h>
int main() {
	//엥?? 나니?
	long long int k = 0;
	long long int a, b, c, d = 0;
	scanf("%lld", &k);
	scanf("%lld %lld %lld %lld", &a, &b, &c, &d);
	if ((a * k + b) == (c * k + d)) {
		printf("Yes %lld", c * k + d);
	}
	else {
		printf("No");
	}
}