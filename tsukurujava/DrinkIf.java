//���5�|6

import java.io.*;
	
public class DrinkIf {
	public static void main (String[] args) {
		BufferedReader reader =new BufferedReader (new InputStreamReader ( System.in));
		
		try {
			System.out.println ("���ݕ��͉����D���ł����H�H");
			System.out.println ("�����I�����W�W���[�X");
			System.out.println ("�����R�[�q�[");
			System.out.println ("�����ǂ���ł��Ȃ�");
			System.out.println ("���A���A���A�̂�����ł��Ȃ�");
			
			String line = reader.readLine();
			int n;
			
			if (line.equals("��")) {
				n = 1;
			} else if ( line.equals("��")) {
				n = 2;
			} else if ( line.equals("��")) {
				n = 3;
			} else {
				n = 4;
			}
			
			switch (n) {
			case 1:
				System.out.println ("�t�@���^�I�����W");
				break;
				
			case 2:
				System.out.println ("�W���[�W�A");
				break;
				
			case 3:
				System.out.println ("�ǂ����ł��Ȃ�");
				break;
				
			default:
				System.out.println ("�͂����肱������");
				break;
				
				}
			} catch (IOException e) {
				System.out.println (e);
			} catch (NumberFormatException e ) {
				System.out.println ("���������A�ԈႦ�Ȃ��ł�");
			}
		}
	}