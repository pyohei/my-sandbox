// 問題5－4

import java.io.*;

public class Drink1 {
	public static void main (String[] args) {
		BufferedReader reader = new BufferedReader (new InputStreamReader ( System.in));
		
		try {
			System.out.println ("飲み物は好きですか？");
			System.out.println ("1．オレンジジュース");
			System.out.println ("2．コーヒー");
			System.out.println ("3　ミルク");
			System.out.println ("1、2、3のどれかから選んでください");
			
			String line = reader.readLine();
			int n = Integer.parseInt(line);
			
			switch (n) {
			case 1:
				System.out.println ("オランジーナ");
				break;
				
			case 2:
				System.out.println ("エメマン");
				break;
			
			case 3:
				System.out.println ("ミルクです");
				break;
					
			default :
				System.out.println ("じゃあ水でも…");
				break;
				
			}
			
		}catch (IOException e ) {
			System.out.println ( e );
		} catch (NumberFormatException e ) {
			System.out.println ("形式が間違っております");
		}
	}
}