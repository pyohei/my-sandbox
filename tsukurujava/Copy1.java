import java.io.*;

public class Copy1 {
	public static void main (String[] args) {
		System.out.println ("�����̓V�C�́H");
		BufferedReader reader = new BufferedReader (new InputStreamReader (System.in));
		System.out.println ("�����̋C���́H");
		BufferedReader reader1 = new BufferedReader (new InputStreamReader (System.in));
		try {
			String line = reader.readLine () ;
			String line1 = reader.readLine() ;
			while (line != null) {
				String s = line.replace ( "sunny", "rainy");
				String t = line1.toLowerCase() ;
				System.out.println("������" + s + "��" + t + "���Ƃ����ˁ�");
				line = reader.readLine ();
			}
		} catch (IOException e) {
			System.out.println (e) ;
		}
	}
}