public class Sample1301 {
    public static void main(String[] args) {
        // パッケージ「package1」のクラス「Package1301」を使用するときは次のようになります。
        package1.Package1301 pk = new package1.Package1301();

        System.out.println("使用したクラスは");
        System.out.println(pk.getName());
    }
}