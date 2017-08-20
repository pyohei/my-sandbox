// 素数を見つけるプログラム 

import java.io.*;

class Sosufind {
	public static void main (String[] args) {
	System.out.println ("チェックしたい数字は？");
		BufferedReader reader = new BufferedReader (new InputStreamReader (System.in));
		
	try {
		String line = reader.readLine();
		int m = Integer.parseInt (line);
		
		int n;
			for (int i = 2 ; i <= m -1 ; i++) {
				n = m % i ;
				
				if ( n == 0 ) {
					System.out.println ("素数ではないです");
					i = m -1;
			} else if (i < m -1) {
				
			} else {
				System.out.println ("素数です");
			}
		}
		} catch (IOException e) {
			System.out.println (e);
		} catch (NumberFormatException e) {
			System.out.println ("数字を入れてください");
		}
	}
}