/* **************************************************************** */

/* 標準ライブラリで定義されているクラス ArrayList をインポートする。 */ 
import java.util.ArrayList;

public class MizuSubclassTest {
    public static void main(String[] args){
        /* 課題では、ここに記述する。 */
        /* ソースコード末尾にてサブクラスを定義することも忘れずに。 */

        /* 今回は具入り水について考える */

        ArrayList<Mizu> suu;
        suu = new ArrayList<Mizu>();

        int kazu;  //具の個数は1から10までの乱数で生成
        
        Mizu data;
        /* リスト suu に文字列を追加する。 */ 
        kazu = (int)(Math.random()*(10)) + 1;
        data = new GuiriMizu(500, 80, kazu);
        suu.add(data);

        data = new Mizu(800, 90);
        suu.add(data);

        kazu = (int)(Math.random()*(10)) + 1;
        data = new GuiriMizu(500, 30, kazu);
        suu.add(data);

        kazu = (int)(Math.random()*(10)) + 1;
        data = new GuiriMizu(400, 50, kazu);
        suu.add(data);

        kazu = (int)(Math.random()*(10)) + 1;
        data = new GuiriMizu(600, 40, kazu);
        suu.add(data);


        /* 拡張 for 文を用いて、
           リストの要素を順次表示する。 */ 
        for (Mizu T : suu) {
            System.out.println(T);
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

/* 課題では、クラス Mizu を継承したサブクラスを新たに定義する。 */

/* 水溶液のクラス */
class GuiriMizu extends Mizu {
    
    protected int GuiriMizu_kosuu;

    public GuiriMizu(double s, double o, int P){
        /* まずクラスMizuのコンストラクタを呼び出し、質量がs、温度がoであるような水を生成 */
        super(s, o);
        
        /* そして、具の個数がP個であるような具入り水とする。 */
        GuiriMizu_kosuu = P;
    }

    /* メソッド toString は、自身の質量と温度と具の個数を返す。 */
    public String toString(){
        String str;

        str =
            "GuiriMizu: mizu_shitsuryou = " + String.valueOf(mizu_shitsuryou) +
            ", ondo = " + String.valueOf(ondo) +
            ", GuiriMizu_kosuu = " + String.valueOf(GuiriMizu_kosuu);

        return str;
    }
}