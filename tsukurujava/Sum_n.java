import java.io.*;

public class Sum_n {

 /**
  * @param args
  */
 public static void main(String[] args) throws IOException {
  BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
  
  System.out.println("値を入力してください。");
  String str1 = br.readLine();
  double n = Integer.parseInt(str1);
  
  double i = 1;
  double total = 0;
  
  while(i<= n){
   total = total + 1 / (i * i * i);
   i++;
   
  }
  System.out.println("数列{1/n^3}の1から" + n + "までの和は、" + total + "です。"); 
  
 }

}