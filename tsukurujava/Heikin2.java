public class Heikin2 {
	public static void main (String[] args) {
		int [] ten;
		double heikin;
		
		ten = new int[3];
		//一度ずつ定義する例
		ten [0] = 63;
		ten [1] = 53;
		ten [2] = 46;
		heikin = (ten [0] + ten [1] + ten [2] ) / 3;
		
		System.out.println ("平均の計算結果は" + ten[1] + "ではなくー" + heikin + "でしたー！");
	}
}