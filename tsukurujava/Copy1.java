import java.io.*;

public class Copy1 {
	public static void main (String[] args) {
		System.out.println ("今日の天気は？");
		BufferedReader reader = new BufferedReader (new InputStreamReader (System.in));
		System.out.println ("今日の気温は？");
		BufferedReader reader1 = new BufferedReader (new InputStreamReader (System.in));
		try {
			String line = reader.readLine () ;
			String line1 = reader.readLine() ;
			while (line != null) {
				String s = line.replace ( "sunny", "rainy");
				String t = line1.toLowerCase() ;
				System.out.println("明日も" + s + "で" + t + "だといいね★");
				line = reader.readLine ();
			}
		} catch (IOException e) {
			System.out.println (e) ;
		}
	}
}