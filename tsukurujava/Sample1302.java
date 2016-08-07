import package1.Package1301;

public class Sample1302 {
    public static void main(String[] args) {
        //「package1.Package1301」をインポートしているので次のようにクラス名のみで使用できます。
        Package1301 pk = new Package1301();

        System.out.println("使用したクラスは");
        System.out.println(pk.getName());
    }
}