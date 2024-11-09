#include <stdio.h>
int main(void){
    int score = 0;
    int total_score = 0;
    for(int i=0;i<5;i++){
        scanf("%d", &score);
        if(score<40){
            score = 40;
        }
        total_score+=score;
    }
    printf("%d", total_score/5);
}