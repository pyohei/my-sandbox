import java.io.*;

public class PowerGraph {
	public static void main (String[] args)  throws IOException {
	BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
	
	System.out.println("�l�́H�H");
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

	/*�w�肵�������ŃO���t��\��*/
	public static void printGraph (int x, char c) {
		for ( int i = 0; i < x; i++) {
			System.out.print ( c );
		}
		System.out.println ("");
	}
	
		/* x��n��̌v�Z */
	public static int getPower (int x, int n) {
	// int getPower�Ƃ��邱�ƂŖ߂�l���w�肵�Ă���B
		int y = 1;
		for (int i = 0; i < n; i++) {
			y  = y * x;
		}
		return y;
	}
}