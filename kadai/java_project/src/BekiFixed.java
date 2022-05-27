public class BekiFixed {
    /* 関数 main */
    public static void main(String[] args){

        int gaku;

        int kekka;

        /* 課題: 数値 99 を、
           自身の学籍番号の下2桁に 2 を加えた値に変更する。 */
        /* 例えば、学籍番号 15T5058Z なら 60 に変更する。 */
        gaku = 46 + 2;

        /* gaku を引数として関数 rokujuugojou を呼び出し、
           返り値を kekka に代入する。 */
        kekka = rokujuugojou(gaku);

        /* kekka の値を表示する。 */
        System.out.println(kekka);
    } 

    /* 関数 rokujuugojou */
    public static int rokujuugojou(int a){
      
        int x;
      
        /* x の初期値は 1 としておく。 */
        x = 1;

        /* 課題: 下の代入文を、 65 回だけ繰り返し実行するよう改造する。
           必要に応じて、変数を宣言する。 */
        for (int i = 0; i < 65; i++){
            x = (x * a) % 131;
        }

        /* x の値を返す。 */
        return x;
    }
}
