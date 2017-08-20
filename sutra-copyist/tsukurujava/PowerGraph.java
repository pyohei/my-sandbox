import java.io.*;

public class PowerGraph {
	public static void main (String[] args)  throws IOException {
	BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
	
	System.out.println("値は？？");
	String str1 = br.readLine();
	int a = Integer.parseInt(str1);
	
		for (int i = -8; i <= a; i++) {
			if ( i < 0) {
				printGraph ( getPower (i, 2) , '-' );
			} else {
				printGraph (getPower (i, 2) , '+' );
			}
		}
	}

	/*指定した文字でグラフを表示*/
	public static void printGraph (int x, char c) {
		for ( int i = 0; i < x; i++) {
			System.out.print ( c );
		}
		System.out.println ("");
	}
	
		/* xのn乗の計算 */
	public static int getPower (int x, int n) {
	// int getPowerとすることで戻り値を指定している。
		int y = 1;
		for (int i = 0; i < n; i++) {
			y  = y * x;
		}
		return y;
	}
}