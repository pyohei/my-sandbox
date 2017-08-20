import PackageA.ExPackage;  //(5)PackageA.ExPackageのインポート

public class ExPackage1 {
  public static void main(String[] args) {
    ExPackage ex = new ExPackage();  //(6)
    ex.showName();  //(7)
  }
}