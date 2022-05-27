#include <stdio.h>

int main(void) {
    int x, y;
    
    for (y = 1 ; y < 10 ; y++) {
        for (x = 1 ; x <10 ; x++) {
            printf("%4d", x * y);
            if (y - x == 0){
                break;
            }
        }
        printf("\n");
    }
    
    return 0;
}

//実行方法
//コンパイル: make testing
//実行: ./testing