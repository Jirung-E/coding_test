#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int TESTCASE;
    scanf("%d", &TESTCASE);

    for(int _=0; _<TESTCASE; _++) {
        int N;
        scanf("%d", &N);

        char* curr = (char*)malloc(sizeof(char) * N + 1);
        char* goal = (char*)malloc(sizeof(char) * N + 1);
        scanf("%s", curr);
        scanf("%s", goal);

        int to_W = 0;
        int to_B = 0;

        for(int i=0; i<N; i++) {
            if(curr[i] != goal[i]) {
                if(goal[i] == 'W')  to_W++;
                else                to_B++;
            }
        }

        free(curr);
        free(goal);

        printf("%d\n", to_W > to_B ? to_W : to_B);
    }

    return 0;
}