public class MizuSeisei {
    public static void main(String[] args){
        Mizu cup1;    //1つ目の水
        Mizu cup2;    //2つ目の水
        Mizu cup3;    //3つ目の水

        int num = 46;               //学籍番号の下2桁
        int mas3 = num*2 % 131;     //3つ目の水の質量: 学籍番号の下2桁を2倍して、それを131で割った余り
        int tem3 = num + 1;         //3つ目の水の温度: 学籍番号の下2桁に1を加えた値
       
        cup1 = new Mizu(100, 30);   //「水の質量が100、温度が30」の水を生成する。
        cup2 = new Mizu(50, 60);    //「水の質量が50、温度が60」の水を生成する。
        cup3 = new Mizu(mas3, tem3);      //7行目および8行目にて指定した質量、温度の水を生成する。

        /* 質量と温度を表示する。 */
        System.out.println(cup1.mizu_shitsuryou);    //1つ目の水の質量を表示
        System.out.println(cup1.ondo);               //1つ目の水の温度を表示

        System.out.println(cup2.mizu_shitsuryou);    //2つ目の水の質量を表示
        System.out.println(cup2.ondo);               //2つ目の水の温度を表示

        System.out.println(cup3.mizu_shitsuryou);    //3つ目の水の質量を表示
        System.out.println(cup3.ondo);               //3つ目の水の温度を表示
    }
}

/* ビーカーに入った水のクラス */
class Mizu {
    /* フィールド */
    /* 質量と温度を保持する。 */
    public double mizu_shitsuryou;
    public double ondo;

    /* コンストラクタ。
       double型 s とdouble型 o を引数にとる。
       質量が s で、温度が o であるような水を生成する。
    */
    public Mizu(double s, double o){
        mizu_shitsuryou = s;
        ondo = o;
    }
}