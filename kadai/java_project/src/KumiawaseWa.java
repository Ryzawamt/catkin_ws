/* 課題13-6 異なるn個のものからr個取り出す組み合わせについて計算するプログラム */

public class KumiawaseWa {
    public static void main(String[] args){

        int wa;

        wa = 0;

        /* 12C0 + 12C1 + ... + 12C12 を計算する。 */
        for (int i = 0; i <= 12; i++) {
            wa = wa + kumiawase(12, i);
        }

        System.out.println(wa); 
    }   

    /* 関数 kumiawase は、
       整数 n と r を引数にとる。
       「異なる n 個のものから、r 個取り出す組み合わせの数」を返す。
    */
    public static int kumiawase(int n, int r){

        /* 課題では、ここを変更する。 */
        /* 計算方針 */
        /* nCr = n!/(n-r)!*r!  */
        int mark_c;
        int kaijo_r = 1;
        int kaijo_n = 1;
        int kaijo_sa = 1;
        int sa = n - r;

        while (sa >= 1){
            kaijo_sa = kaijo_sa * sa;
            sa = sa - 1;
        }
        while (n >= 1){
            kaijo_n = kaijo_n * n;
            n = n - 1;
        }
        while (r >= 1){
            kaijo_r = kaijo_r * r;
            r = r - 1;
        }

        mark_c = kaijo_n/(kaijo_sa*kaijo_r);

        return mark_c;
    }
}
