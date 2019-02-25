#include <stdio.h>
#include <math.h>

int main(void) {
    int t=0; 
    int H=0 , W=0, N=0; 
    int f=0, num=0;

    scanf("%d", &t);

    while(t!=0) {
        t = t -1 ;
        scanf("%d %d %d", &H, &W, &N);

        if (N%H == 0) {
            f = H * 100;
        } else { 
            f = (N%H)*100;
        }

        num = ceil((double)N/H);
        printf("%d\n",f+num);

    }

    return 0;
}