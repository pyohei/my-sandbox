//���4-3
import java.io.*;

public class NowTime {
	public static void main (String[] args) {
		BufferedReader reader = new BufferedReader (new InputStreamReader (System.in));
		
		System.out.println ("���݂̎�����(�Q�S���ԂŎ��̂ݕ\��)");

		
		try {
			String line = reader.readLine();
			int n = Integer.parseInt(line);
		
			if ( n >=0 && n<= 11 ) {
			System.out.println ("�����͂�");
			
			} else if ( n == 12 ) {
			System.out.println ("��������");
			
			} else if ( n >= 13 && n <=18 ) {
			System.out.println ("���񂿂�");
			
			} else if ( n >= 19 && n <=23 ) {
			System.out.println ("����΂��");
			}
			
			} catch (IOException e) {
				System.out.println ( e );
			} catch (NumberFormatException e) {
				System.out.println("�����͈̔͂𒴂��Ă��܂�");
			}
				
			}
		}
	