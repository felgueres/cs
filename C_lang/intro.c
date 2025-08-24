#include <stdio.h>
#define LOWER 0
#define UPPER 300
#define STEP 20

int main()
{
    float fahr;
    printf("=== Fahrenheit to Celsius ===\n");
    for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP){
        printf("%.1f\t%.1f\n", fahr, (fahr - 32)*(5/9.0) );
    }
    return 0;
}
