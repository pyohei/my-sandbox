// �f����������v���O���� 

import java.io.*;

class Sosufind {
	public static void main (String[] args) {
	System.out.println ("�`�F�b�N�����������́H");
		BufferedReader reader = new BufferedReader (new InputStreamReader (System.in));
		
	try {
		String line = reader.readLine();
		int m = Integer.parseInt (line);
		
		int n;
			for (int i = 2 ; i <= m -1 ; i++) {
				n = m % i ;
				
				if ( n == 0 ) {
					System.out.println ("�f���ł͂Ȃ��ł�");
					i = m -1;
			} else if (i < m -1) {
				
			} else {
				System.out.println ("�f���ł�");
			}
		}
		} catch (IOException e) {
			System.out.println (e);
		} catch (NumberFormatException e) {
			System.out.println ("���������Ă�������");
		}
	}
}