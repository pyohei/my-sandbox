import java.io.*;

public class Kuku {
	/** number of probulem representated */
	public static final int MAX_QESTION = 10;
	
	/** 
	   * This sets question of Kuku running until MAX_QUESTION times
	   *And displayed percentage of question answer
	   */
	   
	public static void main (String[] args) {
		int goodAnswers = 0;  			//number of collect answer
		System.out.println ("���ꂩ����̖���" + MAX_QESTION + "��o���܂��B");
		
		/*
		 *
		 *
		 */
		 
		 for (int i = 0; i  < MAX_QESTION; i++ ) {
		 	boolean ok = showQuestion (i + 1);
		 	if (ok) {
		 		goodAnswers++;
		 	}
		 }
		 double rate = goodAnswers * 100.0 / MAX_QESTION;
		 System.out.println("") ;
		 System.out.println("����" + MAX_QESTION + "�₠��܂���");
		 System.out.println("������������ꂽ�̂�" + goodAnswers + "��ŁA");
		 System.out.println("�Ԉ���Ă����̂�" + (MAX_QESTION - goodAnswers) + "��ł��B");
		 System.out.println("��������" + rate + "%�ł�");
		 System.out.println("�����ꁚ��");
		 }
		 
		 /**
		  *
		  *
		  *
		  */
		  
		  public static boolean showQuestion (int questno) {
		  	int x = (int)(Math.random() * 9) + 1;
		  	int y = (int)(Math.random() * 9) + 1;
		  	BufferedReader reader = new BufferedReader(new InputStreamReader (System.in));
		  	try {
		  		System.out.println (" [��" + questno + "��]   " + x + "X" + y + " = ? ");
		  		String line =reader.readLine();
		  		int result = Integer.parseInt(line);
		  		if (x * y == result) {
		  			System.out.println ("�͂��A�������ł��B");
		  			return true;
		  			} else {
		  				System.out.println ("����ˁ[�[�[�[��I");
		  				return false;
		  			}
		  		} catch (IOException e) {
		  			System.out.println (e) ;
		  		} catch (NumberFormatException e) {
					System.out.println ("���͂��������Ȃ��ł��B");
				}
				return false;
			}
		}