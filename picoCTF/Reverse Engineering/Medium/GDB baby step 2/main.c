#include <stdio.h>
int main(void)

{
  int m;
  int n;
  
  n = 0x1e0da;
  for (m = 0; m < 0x25f; m = m + 1) {
    n = n + m;
  }
  printf("%i", n);
  printf("\n");
}

