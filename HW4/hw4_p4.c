#include <stdio.h>

int main(void) {
    int rows;

    printf("Enter the number of rows: ");
    if (scanf("%d", &rows) != 1) {
        printf("Invalid input. Please enter an integer.\n");
        return 1;
    }

    if (rows <= 0) {
        printf("Please enter a positive integer.\n");
        return 1;
    }

    for (int i = 0; i < rows; i++) {
        // Print leading spaces so the triangle is centered
        for (int s = 0; s < rows - i - 1; s++) {
            printf("  ");
        }

        // build each row using the binmomal coefficient recursive definition- C(n, k+1) = C(n, k)*(n-k)/(k+1)
        int value = 1;
        for (int j = 0; j <= i; j++) {
            printf("%4d", value);
            value = value * (i - j) / (j + 1);
        }
        printf("\n");
    }

    return 0;
}
