public class kadai13_4 {
    public static void main(String[] args){

        /* 計算方針 */
        /* 行列式を利用した固有値に関する2次関数を作成し、解の公式を用いて求める */

        double a = 3.0;
        double b = -1.0;
        double c = 3.0;

        /* 求める固有値をans1,ans2とおく */ 
        double ans1;
        double ans2;

        /* 2次関数をλ**2 + e*λ + fとしたとき、係数eと係数fについて求める */
        double e = -1 * (a + c);
        double f = (a*c - b*b);

        /* 解の公式を計算 */
        ans1 = ((-1*e) + Math.sqrt((e*e)-(4*f)))/2;
        ans2 = ((-1*e) - Math.sqrt((e*e)-(4*f)))/2;
        
        /* 計算結果の出力 */
        System.out.println(ans1);
        System.out.println(ans2);
    }   
}