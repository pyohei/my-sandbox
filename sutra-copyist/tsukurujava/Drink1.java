// ���5�|4

import java.io.*;

public class Drink1 {
	public static void main (String[] args) {
		BufferedReader reader = new BufferedReader (new InputStreamReader ( System.in));
		
		try {
			System.out.println ("���ݕ��͍D���ł����H");
			System.out.println ("1�D�I�����W�W���[�X");
			System.out.println ("2�D�R�[�q�[");
			System.out.println ("3�@�~���N");
			System.out.println ("1�A2�A3�̂ǂꂩ����I��ł�������");
			
			String line = reader.readLine();
			int n = Integer.parseInt(line);
			
			switch (n) {
			case 1:
				System.out.println ("�I�����W�[�i");
				break;
				
			case 2:
				System.out.println ("�G���}��");
				break;
			
			case 3:
				System.out.println ("�~���N�ł�");
				break;
					
			default :
				System.out.println ("���Ⴀ���ł��c");
				break;
				
			}
			
		}catch (IOException e ) {
			System.out.println ( e );
		} catch (NumberFormatException e ) {
			System.out.println ("�`�����Ԉ���Ă���܂�");
		}
	}
}