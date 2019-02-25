/*
python 

w, h = map(int, input().strip().split(' ')) #가장 느리다. 

i = 0

while i < h :
    print('*'*w)
    i += 1

*/

/*
C

#include <stdio.h>

int main(void) {
    
    int h, w = 0; 
    int n, m = 0;
    
    scanf("%d %d", &n, &m); 

    //height : h, width : w
    for (h=0; h<m ; h++ ) {
        for (w=0; w<n; w++) {
            printf("*");
        }
        printf("\n");
    }
    
    return 0;
}

*/

#include <stdio.h>

int main(void) {
    int a;
    int b;
    scanf("%d %d", &a, &b);
    for(int i=0; i<a*b;i++){
        printf("*");
        if((i+1)%a == 0){
            printf("\n");
        }
    }

    return 0;
}