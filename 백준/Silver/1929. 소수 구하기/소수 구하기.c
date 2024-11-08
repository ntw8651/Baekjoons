#include <stdio.h>

int num_list[1000001];

int main(void){
    int start_num;
    
    int last_num;
    scanf("%d %d", &start_num, &last_num);
    if(start_num<=1){
        start_num = 2;
    }
    
    for(int i = 1;last_num>=i;i++){
        num_list[i] = 1;
    }
    for(int i = 2;last_num>=i;i++){
        for(int t = i*2;t<=last_num;t+=i){
            num_list[t] = 0;
        }
    }
    for(int i = start_num;last_num>=i;i++){
        if(num_list[i]==1){
            printf("%d\n", i);
        }
    }
   


    return 0;
}