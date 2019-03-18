#include <stdio.h>
#include <string.h> // strtok 
#define _CRT_SECURE_NO_WARNINGS

void deque_func(char* statement){
    char *command;
    int x;
    int i = 0;
    char *sptr = strtok(statement, " ");

    while(sptr != NULL){
        printf("%s\n", sptr);

        if (i==0) {
            printf("%s\n", sptr);
            command = sptr;
        } else {
            x = (int)sptr;
            printf("%d\n", x);
        }
        i++;
        sptr = strtok(NULL, " ");
    }
    // printf("%s", command);
    // printf("%d", x);
}

void main(){
    int N, i;
    char stmnt[20];
    deque_func("push_back 1");
    // scanf("%d", &N);

    // for(i=0; i<N; i++){
    //     scanf("%s", &stmnt);
    // }
}