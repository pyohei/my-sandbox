import java.io.*;

public class Sum_n {

 /**
  * @param args
  */
 public static void main(String[] args) throws IOException {
  BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
  
  System.out.println("�l����͂��Ă��������B");
  String str1 = br.readLine();
  double n = Integer.parseInt(str1);
  
  double i = 1;
  double total = 0;
  
  while(i<= n){
   total = total + 1 / (i * i * i);
   i++;
   
  }
  System.out.println("����{1/n^3}��1����" + n + "�܂ł̘a�́A" + total + "�ł��B"); 
  
 }

}