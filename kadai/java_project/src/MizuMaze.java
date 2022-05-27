/* 課題8-2  70個の水を混ぜるプログラム */

public class MizuMaze {
    public static void main(String[] args){

        /* クラスMizuの、要素を2つ持つ配列を宣言。 */
        Mizu[] cup;
        cup = new Mizu[70];    //70個の水を生成

        Mizu bowl;    //これまでの水を混ぜたものについて、bowlとして定義

        cup[0] = new Mizu(100, 20);    //「水の質量が100、温度が20」の水を生成し、cup[0]とおく
        //cup[1] = new Mizu(50,  60);       //「水の質量が50、温度が60」の水を生成(sample)

        /* それぞれの水の情報を表示(sample) */
        //System.out.println(cup[0].toString());
        //System.out.println(cup[1].toString());

        bowl = cup[0];    //bowlへcup[0]を代入(bowlがcup[0]を指す)

        for (int i = 1; i < 70; i++){          //70個の水に対して処理を行う
            cup[i] = new Mizu(100-i, 20+i);    //新たに水を生成する
            bowl = bowl.mazeru(cup[i]);        //これまでに混ぜた水と生成した水を混ぜ、新たにbowlとする
        }

        /* 70個の水を混ぜた結果を表示。 */
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
            
    /* メソッド toString は、自身の質量と温度を表す文字列を返す。*/
    public String toString(){
        String str;

        /* 水の質量と温度を表す文字列(小数点以下を四捨五入して整数値とするため、"Math.round()"を追記) */
        str =
            "mizu: mizu_shitsuryou = " + String.valueOf(Math.round(mizu_shitsuryou)) +
            ", ondo = " + String.valueOf(Math.round(ondo));

        return str;
    }
}

