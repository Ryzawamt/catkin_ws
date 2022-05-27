public class BekiTest {
    public static void main(String[] args){

        int gaku;
        int i;

        /* 下の2文は、
           C言語における整数配列宣言 int kekka[130]; と同じ意味 */
        int[] kekka;
        kekka = new int[130];

        /* 課題: 数値 99 を、
       数値 99 を、
       自身の学籍番号の下2桁に 2 を加えた値に変更する。
       例えば、学籍番号 15T5058Z なら 60 に変更する。
       例えば、学籍番号 15T5098Z なら 100 に変更する。
       例えば、学籍番号 15T5099Z なら 101 に変更する。
       例えば、学籍番号 15T5100Z なら  2 に変更する。 */
        gaku = 46 + 2;

        /* kekka[0] = beki(gaku, 1), kekka[1] = beki(gaku, 2), ...,
       kekka[129] = beki(gaku, 130) とする。
           それぞれの値を表示する。 */
        for (i = 0; i < 130; i++){
            kekka[i] = beki(gaku, i + 1);

            System.out.println(kekka[i]);
        }

        System.out.println("##############################");

        /* 課題: kekka[0], kekka[1], ..., kekka[129] の値のうち、
           2 番目に大きな値を求め、
           その値を表示するようにプログラムを書く。
           必要に応じて、変数を宣言する。 */
        
        int big_1; //1番目に大きな値
        int big_2; //2番目に大きな値
        big_1 = 0;
        big_2 = 0;

        for (int count = 0; count < 130; count++){
            if (kekka[count] > big_1){
                big_2 = big_1;
                big_1 = kekka[count];
            }
            else if (kekka[count] > big_2 && big_1 > kekka[count]){
                big_2 = kekka[count];
            }
        }

        System.out.println(big_2);
    }  

    public static int beki(int a, int b){
       
        int x;
        int i;
       
        /* x の初期値は 1 としておく。 */
        x = 1;

        /* 代入文 x = (x * a) % 131; を、
           b 回だけ繰り返し実行する。 */
        for (i = 0; i < b; i++){
            /* x に a を掛けた結果を 131 で割った余りを、
               新しい x の値とする。 */
            x = (x * a) % 131;
        }

        /* x の値を返す。 */
        return x;
    }
}
