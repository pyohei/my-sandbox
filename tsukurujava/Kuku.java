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
		System.out.println ("これから九九の問題を" + MAX_QESTION + "問出します。");
		
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
		 System.out.println("問題は" + MAX_QESTION + "問ありました");
		 System.out.println("正しく答えられたのは" + goodAnswers + "問で、");
		 System.out.println("間違っていたのは" + (MAX_QESTION - goodAnswers) + "問です。");
		 System.out.println("正答率は" + rate + "%です");
		 System.out.println("おつかれ★☆");
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
		  		System.out.println (" [第" + questno + "問]   " + x + "X" + y + " = ? ");
		  		String line =reader.readLine();
		  		int result = Integer.parseInt(line);
		  		if (x * y == result) {
		  			System.out.println ("はい、正しいです。");
		  			return true;
		  			} else {
		  				System.out.println ("ざんねーーーーん！");
		  				return false;
		  			}
		  		} catch (IOException e) {
		  			System.out.println (e) ;
		  		} catch (NumberFormatException e) {
					System.out.println ("入力が正しくないです。");
				}
				return false;
			}
		}