import java.io.*;

public class Heikin3 {
	public static void main (String[] args) throws IOException {
	BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
	
	System.out.println("数学の点数を追加してください");
	String str1 =br.readLine();
	System.out.println("社会の点数を追加してください");
	String str2 =br.readLine();
	
	int a = Integer.parseInt(str1);
	int b = Integer.parseInt(str2);
	int [] ten;
	double sum1;
	double sum2;
	double heikin;
	
	ten = new int [2];
	ten [0] = 49;
	ten [1] = 89;
	sum1 = 0;
	sum2 = 0;
	
	for (int i = 0; i < 2; i++) {
		sum1 = sum1 + ten [i];
	}
	
	sum2 = sum1 + a +b;
	heikin = sum2 / 4;
	
	System.out.println ( "英語" + ten[0] + "点、国語" + ten[1] + "点");
	System.out.println ( "今日取った数学の点数は" + a + "点");
	System.out.println ( "今日取った社会の点数は" + b + "点");
	System.out.println ( "よって主要4科目の平均は" + heikin + "点");
	}
}