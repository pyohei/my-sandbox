//問題5－6

import java.io.*;
	
public class DrinkIf {
	public static void main (String[] args) {
		BufferedReader reader =new BufferedReader (new InputStreamReader ( System.in));
		
		try {
			System.out.println ("飲み物は何が好きですか？？");
			System.out.println ("あ＝オレンジジュース");
			System.out.println ("い＝コーヒー");
			System.out.println ("う＝どちらでもない");
			System.out.println ("あ、い、う、のいずれでもない");
			
			String line = reader.readLine();
			int n;
			
			if (line.equals("あ")) {
				n = 1;
			} else if ( line.equals("い")) {
				n = 2;
			} else if ( line.equals("う")) {
				n = 3;
			} else {
				n = 4;
			}
			
			switch (n) {
			case 1:
				System.out.println ("ファンタオレンジ");
				break;
				
			case 2:
				System.out.println ("ジョージア");
				break;
				
			case 3:
				System.out.println ("どっちでもない");
				break;
				
			default:
				System.out.println ("はっきりこたえや");
				break;
				
				}
			} catch (IOException e) {
				System.out.println (e);
			} catch (NumberFormatException e ) {
				System.out.println ("おいおい、間違えないでよ");
			}
		}
	}