#include <stdio.h>
#include <string.h>

int recursion(const char *s, int l, int r, int *countP) {
  *countP += 1;
  if (l >= r)
    return 1;
  else if (s[l] != s[r])
    return 0;
  else
    return recursion(s, l + 1, r - 1, countP);
}

int isPalindrome(const char *s, int *countP) {
  return recursion(s, 0, strlen(s) - 1, countP);
}

int main() {
  int t = 0;
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    char stri[1001] = "";
    int count = 0;
    scanf("%s", stri);
    int q = isPalindrome(stri, &count);
    printf("%d %d\n", q, count);
  }
}