//���5�|7

import java.io.*;
public class DayReader {
	public static void main (String[] args) {
		BufferedReader reader = new BufferedReader (new InputStreamReader(System.in));
		
		try {
			System.out.println ("0�|6�͈̔͂œ��͂��Ă��������B");
			String line = reader.readLine();
			int a = Integer.parseInt(line);
			
			switch (a) {
			case  0:
				System.out.println("Monday");
				break;
				
				case  1:
				System.out.println("Tuesday");
				break;
				
				case  2:
				System.out.println("Wednesday");
				break;
				
				case  3:
				System.out.println("Thursday");
				break;
				
				case  4:
				System.out.println("Friday");
				break;
				
				case  5:
				System.out.println("Saturday");
				break;
				
				case 6 :
				System.out.println("Sunday");
				break;
				
				default :
				System.out.println("�K��̐�������͂��Ă��������B");
				
				}
			} catch (IOException e) {
				System.out.println(e);
			} catch (NumberFormatException e) {
				System.out.println ("�����Ƒ�ڂ�ǂ�ł�");
			}
			
		}
	}