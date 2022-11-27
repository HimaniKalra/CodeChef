#include <stdio.h>

int main(void) {
   float pa, x;
    int wa;
    scanf("%d %f", &wa, &pa);
    if (wa % 5 == 0)
    {
        if (pa>=(wa+0.5))
        {
            x = pa - wa - 0.5;
            printf("%.2f", x);
        }
        else
            printf("%.2f", pa);
    }
    else
        printf("%.2f", pa);
}
