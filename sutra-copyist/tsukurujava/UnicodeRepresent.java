//���3�|3
import java.io.*;

	public class UnicodeRepresent {
		public static void main (String[] args) {
			BufferedReader reader = new BufferedReader ( new InputStreamReader (System.in));
			
		System.out.println ("���������͂��Ă�������");
		
		try {
			String line = reader.readLine();
			int n = line.length();
		
			for ( int i = 0 ; i < n ; i++) {
				char name = line.charAt(i);
				int code = (int)name;
				System.out.println (  name  + "�̕����R�[�h��" + code + "�ł��B") ;
				
				}
			}	catch (IOException e) {
				System.out.println (e) ;
			}
		}
	}