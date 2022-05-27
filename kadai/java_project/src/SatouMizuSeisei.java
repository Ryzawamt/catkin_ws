/* 授業のサンプルプログラム */

public class SatouMizuSeisei {
    public static void main(String[] args){
        SatouMizu cup;
        
        /* 「水の質量が 80、温度が 30、砂糖の質量が 20」
           の砂糖水を生成する。
        */
        cup = new SatouMizu(80, 30, 20);

        /* 質量と温度と濃度を表示する。 */
        System.out.println(cup.toString());
    }   
}

/* ビーカーに入った水のクラス */
class Mizu {
    /* フィールド */
    /* 質量と温度を保持する。 */
    protected double mizu_shitsuryou;
    protected double ondo;

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
        
        m = new Mizu(mizu_shitsuryou + aite.mizu_shitsuryou,
                     (ondo * mizu_shitsuryou + aite.ondo * aite.mizu_shitsuryou)
                     / (mizu_shitsuryou + aite.mizu_shitsuryou));

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

/* ビーカーに入った砂糖水のクラス */
/* クラス Mizu を継承したサブクラス */
class SatouMizu extends Mizu {
    /* フィールド */
    /* 砂糖の質量を保持する。 */
    /* ここに記述がないが、
       スーパークラスであるクラス Mizu の質量と温度も、
       暗黙で存在することに注意。 */
    protected double satou_shitsuryou;

    /* コンストラクタ。
       double型 s とdouble型 o とdouble型 st を引数にとる。
       質量が s で、温度が o であるような水を生成し、
       そこに質量 st の砂糖を溶かした砂糖水とする。
    */
    public SatouMizu(double s, double o, double st){
        /* まず、クラス Mizu のコンストラクタを呼び出して、 */
        /* 質量が s で、温度が o であるような水を生成する。 */
        super(s, o);
        
        /* そして、砂糖の質量が st であるような砂糖水とする。 */
        satou_shitsuryou = st;
    }

    /* メソッド mazeru は、
       クラス SatouMizu のオブジェクト変数 aite を引数にとる。
       自身と aite を混ぜて作られる、新しい砂糖水を生成して返す。
    */
    public SatouMizu mazeru(SatouMizu aite){
        SatouMizu sm;
        
        sm = new SatouMizu(mizu_shitsuryou + aite.mizu_shitsuryou,
                           (ondo * mizu_shitsuryou + aite.ondo * aite.mizu_shitsuryou )
                           / (mizu_shitsuryou + aite.mizu_shitsuryou),
                           satou_shitsuryou + aite.satou_shitsuryou);

        return sm;
    }

    /* メソッド toString は、
       自身の質量と温度と砂糖の質量、
       および濃度を表す文字列を返す。
       クラス Mizu のメソッド toString をオーバーライドする。
    */
    public String toString(){
        String str;

        str =
            "satoumizu: mizu_shitsuryou = " + String.valueOf(mizu_shitsuryou) +
            ", ondo = " + String.valueOf(ondo) +
            ", satou_shitsuryou = " + String.valueOf(satou_shitsuryou) +
            ", noudo = " + String.valueOf(100.0 * satou_shitsuryou /
                                          (satou_shitsuryou + mizu_shitsuryou)) +
            "%";

        return str;
    }
}
