/* 課題8-1(1) "MizuMaze_before.java" の温度計算を正しく修正したプログラム */

public class MizuMaze_after {
    public static void main(String[] args){

        /* クラス Mizu の、
           要素を2つ持つ配列を宣言。 */
        Mizu[] cup;
        cup = new Mizu[2];

        Mizu bowl;

        /* 「水の質量が 100 で、温度が 30」
           「水の質量が 50  で、温度が 60」
           の水をそれぞれ生成する。
        */
        cup[0] = new Mizu(100, 30);
        cup[1] = new Mizu(50,  60);

        /* それぞれの水の情報を表示。 */
        System.out.println(cup[0].toString());
        System.out.println(cup[1].toString());

        /* bowl に cup[0] を代入。 */
        /* （オブジェクト変数なので、
           本来は「代入」より「指す」と理解すべき） */
        bowl = cup[0];

        /* bowl 自身に対し、
           cup[i] を混ぜたものを新たに bowl とする。 */
        /* 要するに「bowl に cup[0] を混ぜる」 */
        bowl = bowl.mazeru(cup[1]);

        /* 2つの水を混ぜた結果を表示。 */
        System.out.println(bowl.toString());
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

    /* メソッド mazeru は、
       クラス Mizu のオブジェクト変数 aite を引数にとる。
       自身と aite を混ぜて作られる、新しい水を生成して返す。
    */
    public Mizu mazeru(Mizu aite){
        Mizu m;
        
        double ondo_nume = (mizu_shitsuryou*ondo) + (aite.mizu_shitsuryou*aite.ondo);  //混ぜた水温の分子計算
        double ondo_deno = mizu_shitsuryou + aite.mizu_shitsuryou;                     //混ぜた水温の分母計算
        double ondo_calc = ondo_nume/ondo_deno;                                        //混ぜた水温を計算
        m = new Mizu(mizu_shitsuryou + aite.mizu_shitsuryou, ondo_calc);

        return m;
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

