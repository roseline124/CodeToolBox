#include <stdio.h>

int main(void) {

    int last = 1;  
    int degree = 1; 
    int first = 0;
    int dest;
    scanf("%d", &dest);

    while(dest != 1) {
        first = last + 1; 
        last = last + 6*degree; 
        degree = degree + 1; 

        if((first<=dest)&&(dest<=last)) {
            break;
        }
    } 
    printf("%d", degree);
    return 0;
}