//問題3－2
import java.io.*;

public class AverageAge {
	public static void main (String[] args) {
		BufferedReader reader = new BufferedReader (new InputStreamReader (System.in));
	
		try{
		String line;
		//1人目
		System.out.println("Aさんの名前は？");
		String nameA = reader.readLine();
		System.out.println("Aさんの年齢は？");
		line = reader.readLine();
		int a = Integer.parseInt (line);
		//2人目
		System.out.println("Bさんの名前は？");
		String nameB = reader.readLine();
		System.out.println("Bさんの年齢は？");
		line = reader.readLine();
		int b = Integer.parseInt (line);
		
		double c;
		c = ( a + b ) / 2.0;
		
		System.out.println(nameA +"さん" + "と" + nameB +"さん" +"の2人の年齢の平均は" + c + "です");
		} catch (IOException e) {
			System.out.println(e);
		} catch (NumberFormatException e) {
			System.out.println(e);
		}
	}
}