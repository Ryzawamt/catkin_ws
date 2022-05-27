/* 課題11-2  100個の砂糖水の濃度の最大値を表示するプログラム */

/* 標準ライブラリで定義されているクラス ArrayList をインポートする。 */ 
import java.util.ArrayList;

public class SatouMizuNoudo {
    public static void main(String[] args){

        /* SatouMizu のインスタンスを要素とするリストを生成する。 */ 
        /* 最初は要素なし。 */ 
        ArrayList<SatouMizu> cuplist;
        cuplist = new ArrayList<SatouMizu>();
        
        SatouMizu temp;
        int i;

        /* i = 0, 1, ..., 99 それぞれについて、
           「水の質量が 4900 - 131*i + i*i、温度が 20、砂糖の質量が i」
           である砂糖水を、リスト cuplist に追加する（全部で100個）。
        */
        for (i = 0; i < 100; i++) {
            temp = new SatouMizu(4900 - 131*i + i*i, 20, i);
            cuplist.add(temp);
        }

        /* 注意: 課題では、ここより上のソースコードは、変更しないこと。*/

        /* i = 2 においてリストに追加された砂糖水について、 */
        //temp = cuplist.get(2);
        /* メソッド getNoudo を呼び出すことにより、濃度を表示する。 */
        //System.out.println(temp.getNoudo());

        /* i = 20 においてリストに追加された砂糖水について、 */
        /* temp に代入することなく、 */
        /* メソッド getNoudo を呼び出すことにより、濃度を表示する。 */
        //System.out.println(cuplist.get(20).getNoudo());

        //以下のmain関数内が課題として作成した部分である
        double big = 0.0;                  //濃度の最大値を格納する変数

        for (i = 0; i < 100; i++) {        //100個の砂糖水に対して処理を行う
            temp = cuplist.get(i);         //i番目の砂糖水を考える
            if (temp.getNoudo() > big){    //これまでの砂糖水の最大濃度よりもi番目の砂糖水の濃度が大きい場合
                big = temp.getNoudo();     //濃度の最大値を更新する
            }
        }
        System.out.println("maximum concentration: " + Math.round(big));    //最大濃度の表示(四捨五入によって整数値を出力)
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
            ", noudo = " + String.valueOf(getNoudo()) +
            "%";

        return str;
    }

    /* メソッド getNoudo は、
       自身の濃度（単位はパーセント）を返す。
    */
    public double getNoudo(){
        return 100.0 * satou_shitsuryou / (satou_shitsuryou + mizu_shitsuryou);
    }
}
