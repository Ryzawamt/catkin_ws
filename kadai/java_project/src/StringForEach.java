/* 第12回授業のサンプルプログラム(拡張for文) */

/* 標準ライブラリで定義されているクラス ArrayList をインポートする。 */ 
import java.util.ArrayList;

public class StringForEach {
    public static void main(String[] args){

        /* String のインスタンスを要素とするリストを生成する。 */ 
        /* 最初は要素なし。 */ 
        ArrayList<String> verbus;
        verbus = new ArrayList<String>();
        
        /* リスト verbus に文字列を追加する。 */ 
        verbus.add("VENI");
        verbus.add("VIDI");
        verbus.add("VICI");

        /* 拡張 for 文を用いて、
           リスト verbus の要素を順次表示する。 */ 
        for (String x : verbus) {
            System.out.println(x);
        }
    }   
}
