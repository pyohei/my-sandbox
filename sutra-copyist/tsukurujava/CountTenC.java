import java.io.*;

public class CountTenC  extends Thread {
    public static void main (String[] args)	 {
        CountTenC ct = new CountTenC();
        ct.start();
        for (int i = 0 ; i < 50 ; i++) {
            String str = String.valueOf(i);
            int n = str.indexOf("3");
            if ( i % 3 == 0 && str.indexOf("3") != -1) {
                System.out.println ( "�A�z�ɂȂ�");
            } else if ( i % 3 == 0) {
                System.out.println ("�����A�z�ɂȂ�");
            } else if ( n != -1) { 
                System.out.println ("�l���̈�A�z�ɐ���");
            } else {
                 System.out.println ( i );
             }
         }
     }
         public void run() {
             for (int i = 0; i < 10; i ++) {
                 System.out.println ( i + "���W�Q�I");
             }
         }
     }