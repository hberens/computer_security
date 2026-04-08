#include <stdio.h>

int f(int x) {
    int y = ~x; 
    if ((x+y)%2==1) {
        if(((x<<15)>>15)==0) {
            return 0; 
        }
        else {
            return 1; 
        }
    }
    else {
        if (((y<<31)>>31)==0) {
            return 0; 
        }
        else {
            return 1; 
        }
    }
}

int main() {
    int x;
    scanf("%d", &x);
    printf("%d\n", f(x));
    return 0;
}