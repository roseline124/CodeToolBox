/*
Stone Game : 이기는 사람을 구하시오. 

1. 돌이 N개 있을 때 한 턴 마다 1 or 3개 가져갈 수 있다.
2. 마지막 돌을 가져가면 이김.
3. 상근이가 먼저 시작.

*/
#include <stdio.h>
#include <stdlib.h>
#define turn 1000 //turn은 최대 1000까지 가능 

int stoneGame(int number){ // 현재 돌의 수 

    // 턴(t)이 홀수면 상근이 win, 짝수면 창영이 win  
    // 가져갈 돌의 수 : rand % 2 -> 나머지가 0 또는 1 
    int t;

    // Turn
    for(t=1;t<=turn;t++){ 
        
        if(number>0){
            if((rand()%2)==1){ 
                number-=1; 
            } else{ 
                number-=3; 
            }

        //Game over
        } else { 
            break;
        } 
    }  

    return t; 
}


int main(void){

    int n, t; 

    scanf("%d", &n);
    t = stoneGame(n);
    printf("%s", (t-1)%2==1? "SK" : "CY");

    return 0; 
}

