/* 授業のサンプルプログラム */

public class SatouMizuShuffle_before {
    public static void main(String[] args){

        Mizu[] card;
        card = new Mizu[14];
        int i;

        /* 「水の質量が 10、温度が 20」
           「水の質量が 11、温度が 20」
           ...
           「水の質量が 130、温度が 20」
           の水、および、
           「水の質量が 10 、温度が 20、砂糖の質量が 1」
           の砂糖水を（全部で14個ある）、
           card[0], card[1], ..., card[13]
           として生成する。
           ここで、クラス SatouMizu は、
           クラス Mizu のサブクラスであるから、
           クラス Mizu の配列に
           クラス SatouMizu のインスタンスを
           格納可能であることに注意。
        */
        for (i = 0; i < 13; i++) {
            card[i] = new Mizu(10 + 10 * i, 20);
        }

        card[13] = new SatouMizu(10, 20, 1);

        /* card[0], card[1], ..., card[13]
           を表示する。
        */
        for (i = 0; i < 14; i++) {
            System.out.println(card[i].toString());
        }

        System.out.println("##############################");

        Mizu[] temp;
        temp = new Mizu[14];

        /* 偶数番目を入れ替える */
        for (i = 0; i <= 12; i += 2) {
            temp[i] = card[i + 1];
        }

        /* 奇数番目を入れ替える */
        for (i = 1; i <= 13; i += 2) {
            temp[i] = card[i - 1];
        }

        /* temp を card にコピーする。 */
        for (i = 0; i < 14; i++) {
            card[i] = temp[i];
        }

        /* card[0], card[1], ..., card[13]
           を表示する。
        */
        for (i = 0; i < 14; i++) {
            System.out.println(card[i].toString());
        }
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
