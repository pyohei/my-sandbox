import java.io.*;

public class Drink2 {
	public static void main (String[] args) {
		BufferedReader reader = new BufferedReader (new InputStreamReader (System.in));
		try {
			System.out.println ("���ݕ��͉����D���ł����H");
			System.out.println ("a �I�����W�W���[�X");
			System.out.println ("b �R�[�q�[");
			System.out.println ("c �ǂ�ł��Ȃ�");
			System.out.println ("a, b, c�̒�����I��ł�������");
			String line = reader.readLine( );
			char c = line.charAt(0);
			switch (c) {
			case 'a' :
				System.out.println ("�I�����W�W���[�X�ł��B");
				break;
			
			case 'b' :
				System.out.println ("�R�[�q�[�ł��B");
				break;
				
			default:
				System.out.println ("�ǂ���ł�����܂���");
				break;
			
			}
		} catch (IOException e) {
			System.out.println (e) ;
		}
	}
}