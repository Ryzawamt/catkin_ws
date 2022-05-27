/* 授業のサンプルプログラム */

public class MizuString {
    public static void main(String[] args){

        Mizu cup;
        String cupmojiretsu;

        /* 「水の質量が 100 で、温度が 30」
           の水を生成する。
        */
        cup = new Mizu(100, 30);

        /* メソッド呼び出しにより、
           質量と温度を表す文字列を取得する。 */
        cupmojiretsu = cup.toString();

        /* 文字列を表示。 */
        System.out.println(cupmojiretsu);
    }   
}

/* ビーカーに入った水のクラス */
class Mizu {
    /* フィールド */
    /* 質量と温度を保持する。 */
    private double mizu_shitsuryou;
    private double ondo;

    /* コンストラクタ。
       double型 s とdouble型 o を引数にとる。
       質量が s で、温度が o であるような水を生成する。
    */
    public Mizu(double s, double o){
        mizu_shitsuryou = s;
        ondo = o;
    }

    /* メソッド toString は、
       自身の質量と温度を表す文字列を返す。
    */
    public String toString(){
        String str;

        str =
            "mizu: mizu_shitsuryou = " + String.valueOf(mizu_shitsuryou) +
            ", ondo = " + String.valueOf(ondo);

        return str;
    }
}
